from ...wall.func import integer_addition, level, P
from z3 import *

def test_get_int():
  s = Solver()
  l2 = level(2)
  l1 = level(1)
  add = integer_addition(s)
  s.add(l2.sort.is_fun2(add))
  s.push()
  s.add(l1.funa(l2.funa(add)[l1.down(P.int(4))])[P.int(5)] == P.int(9))
  assert s.check() == sat
  s.pop()
  s.push()
  s.add(l1.funa(l2.funa(add)[l1.down(P.int(4))])[P.int(5)] == P.int(10))
  assert s.check() == unsat
  s.pop()
  s.push()
  # we need to add this constraint because otherwise the accessor will work
  # meaning that it returns never, but the accessor just returns a function anyway
  # so we need to prove that this is not a function
  # the reason that working with sets is better is that this would return False
  s.add(l1.sort.is_fun1(l2.funa(add)[l1.down(P.bool(True))]))
  s.add(l1.funa(l2.funa(add)[l1.down(P.bool(True))])[P.int(5)] == P.int(10))
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(l1.funa(l2.funa(add)[l1.down(P.int(5))])[P.bool(True)] == P.int(10))
  assert s.check() == unsat
  s.pop()
  s.push()
  s.add(l1.funa(l2.funa(add)[l1.down(P.int(5))])[P.bool(True)] == P.never)
  assert s.check() == sat
  s.pop()
  s.push()
  s.add(l1.funa(l2.funa(add)[l1.down(P.bool(True))])[P.int(5)] == P.never)
  assert s.check() == sat