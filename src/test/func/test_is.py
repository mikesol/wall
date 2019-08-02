from ...wall.func import *
from z3 import *

def test_is_int():
  s = Solver()
  i = wInt()
  s.push()
  s.add(isInt(i) == P.bool(True))
  assert s.check() == sat
  s.pop()
  s.add(isReal(i) == P.bool(True))
  assert s.check() == unsat

def test_is_real():
  s = Solver()
  i = wReal()
  s.push()
  s.add(isReal(i)  == P.bool(True))
  assert s.check() == sat
  s.pop()
  s.add(isBool(i)  == P.bool(True))
  assert s.check() == unsat

def test_is_bool():
  s = Solver()
  i = wBool()
  s.push()
  s.add(isBool(i) == P.bool(True))
  assert s.check() == sat
  s.pop()
  s.add(isReal(i)  == P.bool(True))
  assert s.check() == unsat

def test_is_str():
  s = Solver()
  i = wStr()
  s.push()
  s.add(isStr(i) == P.bool(True))
  assert s.check() == sat
  s.pop()
  s.add(isReal(i) == P.bool(True))
  assert s.check() == unsat

def test_is_sym():
  s = Solver()
  i = wSym()
  s.push()
  s.add(isSym(i) == P.bool(True))
  assert s.check() == sat
  s.pop()
  s.add(isReal(i) == P.bool(True))
  assert s.check() == unsat

def test_is_fun():
  s = Solver()
  l = clevel(W.level-1)
  i = W.fun(Lambda([l], l))
  s.push()
  s.add(isFun(i) == P.bool(True))
  assert s.check() == sat
  s.pop()
  s.push()
  s.add(isSeq(i) == P.bool(True))
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(isReal(i) == P.bool(True))
  assert s.check() == unsat

def test_is_seq():
  s = Solver()
  i = W.seq(Const(str(uuid4()), W.seqsort))
  s.push()
  s.add(isSeq(i) == P.bool(True))
  assert s.check() == sat
  s.pop()
  s.push()
  s.add(isFun(i) == P.bool(True))
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(isReal(i) == P.bool(True))
  assert s.check() == unsat

def test_is_set():
  s = Solver()
  i = W.set(Const(str(uuid4()), SetSort(level(-1).sort)))
  s.push()
  s.add(isSet(i) == P.bool(True))
  assert s.check() == sat
  s.pop()
  s.push()
  s.add(isFun(i) == P.bool(True))
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(isReal(i) == P.bool(True))
  assert s.check() == unsat

def test_is_subtype():
  s = Solver()
  a = Array(str(uuid4()), level(0).sort, level(0).sort)
  b = Array(str(uuid4()), level(0).sort, level(0).sort)
  a = Store(a, P.int(5), P.bool(True))
  aa = level(1).fun(a)
  bb = level(1).fun(b)
  s = Solver()
  s.push()
  s.add(isSubtype(bb, aa) == P.bool(True))
  assert s.check() == sat
  s.pop()
  s.push()
  s.add(isSubtype(aa, bb) == P.bool(False))
  assert s.check() == sat