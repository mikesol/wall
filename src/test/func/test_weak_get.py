from ...wall.func import wInt, xgetInt, wBool, P
from z3 import *

def test_get_int():
  s = Solver()
  i = wInt()
  j = wInt()
  s.add(xgetInt(i) == P.int(5))
  s.add(xgetInt(j) == P.int(6))
  assert s.check() == sat

def test_get_error():
  s = Solver()
  i = wInt()
  j = wBool()
  s.add(xgetInt(i) == P.int(5))
  s.add(xgetInt(j) == P.int(6))
  assert s.check() == unsat
