from ...wall.func import *
from z3 import *

def test_is_int():
  s = Solver()
  i = wInt()
  s.push()
  s.add(isInt(i))
  assert s.check() == sat
  s.pop()
  s.add(isReal(i))
  assert s.check() == unsat

def test_is_real():
  s = Solver()
  i = wReal()
  s.push()
  s.add(isReal(i))
  assert s.check() == sat
  s.pop()
  s.add(isBool(i))
  assert s.check() == unsat

def test_is_bool():
  s = Solver()
  i = wBool()
  s.push()
  s.add(isBool(i))
  assert s.check() == sat
  s.pop()
  s.add(isReal(i))
  assert s.check() == unsat

def test_is_str():
  s = Solver()
  i = wStr()
  s.push()
  s.add(isStr(i))
  assert s.check() == sat
  s.pop()
  s.add(isReal(i))
  assert s.check() == unsat

def test_is_sym():
  s = Solver()
  i = wSym()
  s.push()
  s.add(isSym(i))
  assert s.check() == sat
  s.pop()
  s.add(isReal(i))
  assert s.check() == unsat

def test_is_fun():
  s = Solver()
  l = clevel(W.level-1)
  i = W.fun(Lambda([l], l))
  s.push()
  s.add(isFun(i))
  assert s.check() == sat
  s.pop()
  s.push()
  s.add(isSeq(i))
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(isReal(i))
  assert s.check() == unsat

def test_is_seq():
  s = Solver()
  i = W.seq(Const(str(uuid4()), W.seqsort))
  s.push()
  s.add(isSeq(i))
  assert s.check() == sat
  s.pop()
  s.push()
  s.add(isFun(i))
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(isReal(i))
  assert s.check() == unsat

def test_is_set():
  s = Solver()
  i = W.set(Const(str(uuid4()), SetSort(level(-1).sort)))
  s.push()
  s.add(isSet(i))
  assert s.check() == sat
  s.pop()
  s.push()
  s.add(isFun(i))
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(isReal(i))
  assert s.check() == unsat