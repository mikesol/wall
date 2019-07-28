from ...wall.func import wInt, getInt, getBool
from z3 import *

def test_get_int():
  s = Solver()
  i = wInt()
  j = wInt()
  s.add(getInt(i) == 5)
  s.add(getInt(j) == 6)
  s.push()
  s.add(getInt(i) + getInt(j) == 11)
  assert s.check() == sat
  s.pop()
  s.push()
  s.add(getInt(i) + getInt(j) == 12)
  assert s.check() == unsat

# in z3, it is perfectly ok to create one type and get another
def test_get_does_not_automatically_raise_error():
  s = Solver()
  i = wInt()
  j = wInt()
  s.add(getInt(i) == 5)
  s.add(getBool(j) == True)
  assert s.check() == sat