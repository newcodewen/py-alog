# R8.15
from linked_binary_tree import LinkedBinaryTree
class MutableLinkedBinaryTree(LinkedBinaryTree):

  def add_root(self, e):
    return self._add_root(e)

  def add_left(self, p, e):
    return self._add_left(p, e)

  def add_right(self, p, e):
    return self._add_right(p, e)
  def replace(self, p, e):
    return self._replace(p, e)
  
  def delete(self, p):
    return self._delete(p)
  
  def attach(self, p, t1, t2):
    self._attach(p, t1, t2)
    
    
