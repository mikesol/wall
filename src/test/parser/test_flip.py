from ...wall.parser import parse
import pytest
from parsimonious import IncompleteParseError

def test_flip():
  parse('''a = 5.+ 3
''')

def test_func_error():
  with pytest.raises(IncompleteParseError):
    parse('''foo = .5
''')
