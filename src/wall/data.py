from z3 import *
from abc import ABC

class WallDatatype(ABC): pass

class WallDatatype(ABC): pass

class PrimitiveWallDatatype(WallDatatype):
  slots = ['int','inta','str','stra','bool','boola','real','reala','sym','syma','never','level','sort','con_to_acc','con_to_sort','next']
  def __init__(self):
    data = Datatype('w0')
    cons = [
      ('int', ('inta', IntSort())),
      ('str', ('stra', StringSort())),
      ('bool', ('boola', BoolSort())),
      ('real', ('reala', RealSort())),
      ('sym', ('syma', StringSort()))
    ]
    for x in cons:
      data.declare(x[0], x[1])
    data.declare('never')
    data = data.create()
    self.level = 0
    self.sort = data
    for x in cons:
      setattr(self, x[0], getattr(data, x[0]))
      setattr(self, x[1][0], getattr(data, x[1][0]))
    self.never = data.never
    self.con_to_acc = {
      getattr(data, x[0]): getattr(data, x[1][0]) for x in cons
    }
    self.con_to_acc[self.never] = None
    self.con_to_sort = {
      getattr(data, x[0]): x[1][1] for x in cons
    }
    self.con_to_sort[self.never] = data
    self.prev = None

class ComposedWallDatatype(WallDatatype):
  slots = ['set','seta','is_set','fun','funa','is_fun','seq','seqa','is_seq','down','downa','is_down','level','sort','prev','con_to_acc','con_to_sort','next']
  def __init__(self, prev):
    self.level = prev.level + 1
    self.prev = prev
    self.prev.next = self
    data = Datatype('w%d' % self.level)
    cons = [
      ('set', ('seta', SetSort(prev.sort))),
      ('fun', ('funa', ArraySort(prev.sort, prev.sort))),
      ('seq', ('seqa', SeqSort(prev.sort))),
      ('down', ('downa', prev.sort)),
    ]
    l = lambda x: x+str(self.level)
    for x in cons:
      data.declare(l(x[0]), (l(x[1][0]), x[1][1]))
    data = data.create()
    self.sort = data
    for x in cons:
      setattr(self, x[0], getattr(data, l(x[0])))
      setattr(self, 'is_'+x[0], getattr(data, l('is_'+x[0])))
      setattr(self, x[1][0], getattr(data, l(x[1][0])))
    self.con_to_acc = {
      getattr(self, x[0]): getattr(self, x[1][0]) for x in cons
    }
    self.con_to_sort = {
      getattr(self, x[0]): x[1][1] for x in cons
    }

_P = PrimitiveWallDatatype()
def _W(n):
  def _(d, x):
    return d if x == n else _(ComposedWallDatatype(d), x+1)
  return _(PrimitiveWallDatatype(), 0)

DEPTH = 256
W = _W(DEPTH)
W_TO_SORT = dict()
SORT_TO_W = dict()
_x = W
while hasattr(_x, 'prev'):
  W_TO_SORT[_x] = _x.sort
  SORT_TO_W[_x.sort] = _x
  _x = _x.prev
