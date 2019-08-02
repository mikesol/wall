from .data import W, SORT_TO_W
from z3 import *
from uuid import uuid4
from operator import iadd, isub, imul, truediv

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

def hoist(x, n):
  if n == 0:
    return x
  if n < 0:
    return hoist(SORT_TO_W[x.sort()].downa(x), n+1)
  return hoist(SORT_TO_W[x.sort()].next.down(x), n-1)

def wrap(lev, v):
  return v if lev.level == 0 else lev.down(wrap(lev.prev, v))

#########################
# Primitive constructors
#########################

_base = Const(str(uuid4()), P.sort)
def _wT(n, c0, c1, base):
  n = nize(n)
  return wrap(SORT_TO_W[base.sort()], c0 if c1 is None else c0(c1(n)))

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
  return P.bool(f(SORT_TO_W[v.sort()], v, c0))

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
  return Or(getattr(lev, c0)(v), If(lev.is_down(v), ___isC(lev.prev, lev.downa(v), c0), False))

def _isC(v, c0):
  return _is(___isC, v, c0)

def isFun(v):
  return _isC(v, 'is_fun')

def isSet(v):
  return _isC(v, 'is_set')

def isSeq(v):
  return _isC(v, 'is_seq')

def hasAllKeys(a, b):
  '''
  Returns P.bool(True) if all the keys that are not never in `a`
  are also not never in `b`. 
  '''
  l = SORT_TO_W[a.sort()]
  c = Const(str(uuid4()), l.funa(a).domain())
  # todo - widen to never at arbitrary level
  return P.bool(Not(Exists(c, And(Not(l.funa(a)[c] == P.never), l.funa(b)[c] == P.never))))

#########################
# Primitive get
#########################

def ___getT(lev, v, c0, weak):
  return ((v if weak else (getattr(lev.sort, c0)(v)))
    if lev.level == 0 else
    ___getT(lev.prev, lev.downa(v), c0, weak))

def _getT(v, c0, weak):
  return ___getT(SORT_TO_W[v.sort()], v, c0, weak)

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
# Application
######################

def apFun(f, x):
  if type(x) == type(0):
    x = P.int(x)
  elif type(x) == type(0.0):
    x = P.real(x)
  elif type(x) == type('s'):
    x = P.str(x)
  elif type(x) == type(True):
    x = P.bool(x)
  w = SORT_TO_W[f.sort()]
  asfun = w.funa(f)
  return asfun[hoist(x, (w.level - 1) - SORT_TO_W[x.sort()].level)]

######################
# Hoist
######################

def hoist2(v, tl = W.level):
  # drill down to hit the first thing we can elevate
  # once we hit this, emit a version of that at the current level
  # if we hit a primitive, emit a series of downs to the primitive
  l = SORT_TO_W[v.sort()]
  if l == P:
    return hoist(v, tl.level)
  # for functions, the problem is that if an unhoisted x produced
  # a non-never y, we will want to make that x produce never
  # but the hoisted version produce the desired y
  # this is an issue because hoisted to unhoisted is one to many
  # so there is no way to have Lambda(hoisted_x) and somehow get an
  # unhoisted x from that?
  # hoisted = Lambda(x,
  #   If(unhoisted(x), never,
  #   If(Exists(y, unhoisted(y) && old[y] != never && x == hoist(y)), <<<-problem old[y] ))
  # this illustrates the problem. there could be infinite old[y]'s that satisfy this constraint
  # how do we choose?
  #
  if l.is_fun(v):
    pass
  # problem here: we will just hit an infinite loop in compile
  # time because we will keep iterating the checks, meaning that
  # the checks themselves do not hit a stop condition, they
  # just emit a stop condition indefinitely
  # AFAIK, there is no procedure that can indicate "hoist on list"
  # or rather, we would have to have an array called hoist
  # hoist == Lambda(x, If(ll.is_nil(x), x, ll.cons(shoist(ll.car(x), hoist[ll.cdr(x)]))))
  elif l.is_list(v):
    pass
  # etc...
  

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
    return out, [constraint]

_ii = lambda x: isInt(x) == P.bool(True)
def _integer_binary_op_(dom2, op, s=None):
  return _binary_op(_ii, getInt, dom2, getInt, P.int, op, s)

def _integer_binary_op(op, s=None):
  return _integer_binary_op_(_ii, op, s)

def integer_addition(s=None):
  return _integer_binary_op(iadd, s)

def integer_subtraction(s=None):
  return _integer_binary_op(isub, s)

def integer_multiplication(s=None):
  return _integer_binary_op(imul, s)

def integer_division(s=None):
  return _integer_binary_op_(lambda x: xgetInt(x) != P.int(0), truediv, s)