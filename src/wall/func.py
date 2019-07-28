from .data import W
from z3 import *
from uuid import uuid4
from operator import add

_ALL = []

def nize(n):
  if n is None:
    n = str(uuid4())
  if n in _ALL: raise ValueError('There already exists a variable named %s' % n)
  _ALL.append(n)
  return n

def prim(x):
  return x if x.level == 0 else prim(x.prev)

P = prim(W)

def level(n, base=None):
  def down(x, base):
    return base if x == 0 else down(x+1, base.prev)
  def up(x, base):
    return base if x == 0 else up(x-1, base.next)
  return down(n, base if base != None else W) if n < 0 else up(n, base if base != None else P)

def clevel(n, name=None, base=None):
  name = nize(name)
  return Const(name, level(n, base).sort)

def wrap(lev, v):
  return v if lev.level == 0 else lev.down(wrap(lev.prev, v))

#########################
# Primitive constructors
#########################

_base = Const(str(uuid4()), P.sort)
def _wT(n, c0, c1, base):
  n = nize(n)
  def __wT(lev=W):
    return wrap(lev, c0 if c1 is None else c0(c1(n))) if (base.sort() == lev.sort) else __wT(lev.prev)
  return __wT()

def wInt(n=None, base=_base):
  return _wT(n, P.int, Int, base)

def wReal(n=None, base=_base):
  return _wT(n, P.real, Real, base)

def wStr(n=None, base=_base):
  return _wT(n, P.str, String, base)

def wBool(n=None, base=_base):
  return _wT(n, P.bool, Bool, base)

def wSym(n=None, base=_base):
  return _wT(n, P.sym, String, base)

def wNever(n=None, base=_base):
  return _wT(n, P.never, None, base)

#########################
# Primitive is?
#########################


def _is(f, v, c0):
  def __is(lev=W):
    return f(lev, v, c0) if (v.sort() == lev.sort) else __is(lev.prev)
  return __is()

def ___isT(lev, v, c0):
  return (getattr(lev.sort, c0)(v)
    if lev.level == 0 else
    If(lev.is_down(v),
      ___isT(lev.prev, lev.downa(v), c0),
      False))

def _isT(v, c0):
  return _is(___isT, v, c0)

def isInt(v):
  return _isT(v, 'is_int')

def isReal(v):
  return _isT(v, 'is_real')

def isBool(v):
  return _isT(v, 'is_bool')

def isSym(v):
  return _isT(v, 'is_sym')

def isStr(v):
  return _isT(v, 'is_str')

def ___isC(lev, v, c0):
  if lev.level == 0:
    return False
  #print(lev, c0)
  return Or(getattr(lev, c0)(v), If(lev.is_down(v), ___isC(lev.prev, lev.downa(v), c0), False))

def _isC(v, c0):
  return _is(___isC, v, c0)

def isFun(v):
  return _isC(v, 'is_fun')

def isSet(v):
  return _isC(v, 'is_set')

def isSeq(v):
  return _isC(v, 'is_seq')

#########################
# Primitive get
#########################

def ___getT(lev, v, c0, weak):
  return ((v if weak else (getattr(lev.sort, c0)(v)))
    if lev.level == 0 else
    ___getT(lev.prev, lev.downa(v), c0, weak))

def _getT(v, c0, weak):
  def __getT(lev=W):
    return ___getT(lev, v, c0, weak) if (v.sort() == lev.sort) else __getT(lev.prev)
  return __getT()

def getInt(v):
  return _getT(v, 'inta', False)

def getReal(v):
  return _getT(v, 'reala', False)

def getBool(v):
  return _getT(v, 'boola', False)

def getSym(v):
  return _getT(v, 'syma', False)

def getStr(v):
  return _getT(v, 'stra', False)

def _xgetT(v, n, m):
  base = _getT(v, n, True)
  return If(m(base), base, P.sort.never)

def xgetInt(v):
  return _xgetT(v, 'inta', P.sort.is_int)

def xgetReal(v):
  return _xgetT(v, 'reala', P.sort.is_real)

def xgetBool(v):
  return _xgetT(v, 'boola', P.sort.is_bool)

def xgetStr(v):
  return _xgetT(v, 'stra', P.sort.is_str)

def xgetSym(v):
  return _xgetT(v, 'syma', P.sort.is_sym)

######################
# Math
######################

def _binary_op(isArg0, accArg0, isArg1, accArg1, conRet, retF, s=None):
  l2 = level(2)
  l1 = level(1)
  out = clevel(2)
  arg0 = clevel(1)
  arg1 = clevel(0)
  constraint = out == l2.fun(
    Lambda([arg0],
      If(isArg0(arg0),
        l1.fun(Lambda([arg1],
          If(isArg1(arg1),
            conRet(retF(accArg0(arg0), accArg1(arg1))),
            wNever(base=arg1)))),
        wNever(base=arg0))))
  if s:
    s.add(constraint)
    return out
  else:
    return out, constraint

def integer_addition(s=None):
  return _binary_op(isInt, getInt, isInt, getInt, P.int, add, s)