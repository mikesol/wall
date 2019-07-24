
from ....wall.parser import parse
import pytest

def test_parse():
  parse(r'''
server=192
#fewfewfe efew
    w qqqwrs# = ff

q = #_-fwe!@$%^&*(")\/:;00E&<>? .,|~`,.';l[]{}#

str = "this is a \" string"
dangling  =  'ff4@
port    = (143)
file =   payroll
''')