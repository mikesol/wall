from z3 import *
from abc import ABC, abstractmethod

# cf = constraint function
class Contribution(object):
  slots = ['base', 'cf']
  def __init__(self, base, cf)
  self.base = base
  self.cf = cf

class WallObj(ABC):
  @abstractmethod
  def contribution(self, world):
    pass

class WallInt(WallObj):
  def contribution(self, world):
    return (IntSort(),)

class WallReal(WallObj):
  def contribution(self, world):
    return (RealSort(),)

class WallBool(WallObj):
  def contribution(self, world):
    return (BoolSort(),)