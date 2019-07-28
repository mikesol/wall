
class Executable(object):
  slots = ['stmt']
  def __init__(self, stmt):
    self.stmt = stmt

class Assignment(object):
  slots = ['l', 'r']
  def __init__(self, l, r):
    self.l = l
    self.r = r

class PatternMatch(Assignment):
  def expand_to_assignments():
    pass

class SimpleAssignment(Assignment):
  pass
