from ...wall.parser import parse
import pytest
from parsimonious import IncompleteParseError

def test_func():
  parse('''a = { 1 2 }
''')
