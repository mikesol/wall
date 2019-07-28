from .parser import parse
from parsimonious.grammar import NodeVisitor

class WallVisitor(NodeVisitor):
  '''
  def visit_expr(self, node, visited_children):
    return visited_children or node

  def visit_assignment(self, node, visited_children):
    print('assignment here', type(visited_children))
    for i, vc in enumerate(visited_children[0]):
      print('   ', i, vc)
    return visited_children or node

  def visit_stmt(self, node, visited_children):
    return visited_children or node

  def visit_symbol_asgn(self, node, visited_children):
    return visited_children or node

  def visit_other_asgn(self, node, visited_children):
    return visited_children or node

  def visit_value(self, node, visited_children):
    return visited_children or node

  def visit_evil(self, node, visited_children):
    return visited_children or node

  def visit_flipper(self, node, visited_children):
    return visited_children or node

  def visit_bucks(self, node, visited_children):
    return visited_children or node

  def visit_dotbucks(self, node, visited_children):
    return visited_children or node

  def visit_valueseq(self, node, visited_children):
    return visited_children or node

  def visit_word(self, node, visited_children):
    return visited_children or node

  def visit_tickquote(self, node, visited_children):
    return visited_children or node

  def visit_symword(self, node, visited_children):
    return visited_children or node

  def visit_quoted(self, node, visited_children):
    return visited_children or node

  def visit_backticked(self, node, visited_children):
    return visited_children or node

  def visit_equal(self, node, visited_children):
    return visited_children or node

  def visit_dot(self, node, visited_children):
    return visited_children or node

  def visit_number(self, node, visited_children):
    return visited_children or node

  def visit_int(self, node, visited_children):
    return visited_children or node

  def visit_float(self, node, visited_children):
    return visited_children or node

  def visit_paren(self, node, visited_children):
    return visited_children or node

  def visit_set(self, node, visited_children):
    return visited_children or node

  def visit_func(self, node, visited_children):
    return visited_children or node

  def visit_let(self, node, visited_children):
    return visited_children or node

  def visit_emptyset(self, node, visited_children):
    return visited_children or node

  def visit_lp(self, node, visited_children):
    return visited_children or node

  def visit_rp(self, node, visited_children):
    return visited_children or node

  def visit_letlb(self, node, visited_children):
    return visited_children or node

  def visit_lb(self, node, visited_children):
    return visited_children or node

  def visit_rb(self, node, visited_children):
    return visited_children or node

  def visit_ls(self, node, visited_children):
    return visited_children or node

  def visit_rs(self, node, visited_children):
    return visited_children or node

  def visit_dollar(self, node, visited_children):
    return visited_children or node

  def visit_allws(self, node, visited_children):
    return visited_children or node

  def visit_newline(self, node, visited_children):
    return visited_children or node

  def visit_space(self, node, visited_children):
    return visited_children or node

  def visit_forcespace(self, node, visited_children):
    return visited_children or node

  def visit_emptyline(self, node, visited_children):
    return visited_children or node
  '''
  def generic_visit(self, node, visited_children):
      """ The generic visit method. """
      return visited_children or node

def visit(parsed):
  return WallVisitor().visit(parsed)

def visit_parsed(str):
  return WallVisitor().visit(parse(str))