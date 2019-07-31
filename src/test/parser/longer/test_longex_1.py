
from ....wall.parser import parse
import pytest

def test_parse():
  parse(r'''
a = + 1 2
b = - 3 4
c = + + 1 2 - 3 4
z = { 1.+ 2 3 }
{ 'a b 'c d } = { 'a 1.+ 1 'c (+ 3 4 ) }

q = <<! _? >> @{ 'foobar a0 } foobar
q
''')