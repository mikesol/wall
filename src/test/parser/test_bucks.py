from ...wall.parser import parse
import pytest
from parsimonious import IncompleteParseError

def test_bucks():
  parse('''a = 5 $ 3
''')

def test_bucks_no_space():
  parse('''a = 5 $3
''')

def test_func_error():
  with pytest.raises(IncompleteParseError):
    parse('''foo = $5
''')
