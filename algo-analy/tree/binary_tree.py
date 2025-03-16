class BinaryTree:
  
    def left(self, p):
      raise NotImplementedError('must be implemented by subclass')
    
    def right(self, p):
      raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
      """返回p的兄弟节点"""
      parent = self.parent(p)
      if parent is None:
        return None
      else:
        if p == self.left(parent):
          return self.right(parent)
        
    def children(self, p):
      """返回p的孩子节点"""
      if self.left(p) is not None:
        yield self.left(p)
      if self.right(p) is not None:
        yield self.right(p)
        
        
    # R8.10:二叉树计算子节点数量
    def num_children(self, p):
        count = 0
        if self.left(p) is not None:
          count += 1
        if self.right(p) is not None:
          count += 1
          
        return count
      
      

      
       
