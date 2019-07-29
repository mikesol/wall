from ...wall.func import *
from z3 import *

def test_addition():
  s = Solver()
  l2 = level(2)
  l1 = level(1)
  add = integer_addition(s)
  s.add(isFun(add))
  s.push()
  s.add(apFun(apFun(add, 4), 5) == P.int(9))
  assert s.check() == sat
  s.pop()
  s.push()
  c = wInt()
  s.add(isInt(apFun(apFun(add, 4), c)))
  assert s.check() == sat
  s.pop()
  s.push()
  c = wInt()
  s.add(P.inta(c) <= 0)
  s.add(P.inta(apFun(apFun(add, 4), c)) > 3)
  assert s.check() == sat
  s.pop()
  s.push()
  c = wInt()
  s.add(P.inta(c) <= 0)
  s.add(P.inta(apFun(apFun(add, 4), c)) > 4)
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(apFun(apFun(add, 4), 5) == P.int(10))
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(isFun(apFun(add, True)))
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(apFun(apFun(add, 4), True) == P.int(10))
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(apFun(apFun(add, 4), True) == P.never)
  assert s.check() == sat

def test_division():
  s = Solver()
  l2 = level(2)
  l1 = level(1)
  div = integer_division(s)
  s.add(isFun(div))
  s.push()
  s.add(apFun(apFun(div, 4), 5) == P.int(0))
  assert s.check() == sat
  s.pop()
  s.push()
  c = Int(str(uuid4()))
  s.add(ForAll([c], isInt(apFun(apFun(div, 4), P.int(c)))))
  assert s.check() == unsat
  s.pop()
  s.push()
  c = Const(str(uuid4()), P.sort)
  # sat because c could be 0, so div by 0 could happen, meaning not int
  s.add(Exists(c, And(isInt(c), Not(isInt(apFun(apFun(div, 4), c))))))
  assert s.check() == sat
  s.pop()
  s.push()
  c = Const(str(uuid4()), P.sort)
  d = wInt()
  s.add(P.inta(d) >= 1)
  # unsat because c could not be 0, so must be int
  s.add(Exists(c, And(c==d, Not(isInt(apFun(apFun(div, 4), c))))))
  assert s.check() == unsat
  s.pop()
  s.push()
  c = Const(str(uuid4()), P.sort)
  # sat because 0 in num is ok
  s.add(ForAll([c], If(P.sort.is_int(c), isInt(apFun(apFun(div, c), 4)), True)))
  assert s.check() == sat
  s.pop()
  s.push()
  s.add(isFun(apFun(div, True)))
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(apFun(apFun(div, 4), 0) == P.int(10))
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(apFun(apFun(div, 4), 1) == P.int(4))
  assert s.check() == sat
  s.pop()
  s.push()
  s.add(apFun(apFun(div, 4), 0) == P.never)
  assert s.check() == sat