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
  s.add(apFun(apFun(add, 4), 5) == P.int(10))
  assert s.check() == unsat
  s.pop()
  s.push()
  # we need to add this constraint because otherwise the accessor will work
  # meaning that it returns never, but the accessor just returns a function anyway
  # so we need to prove that this is not a function
  # the reason that working with sets is better is that this would return False
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