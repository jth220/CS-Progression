class TreeNode:
  def __init__(self, key):
   self.key = key
   self.left = None
   self.right = None
   self.parent = None

class BinaryTree:
  def __init__(self):
    self.root = None


  def insert(self, root, key):
    newNode = TreeNode(key)
    if self.root is None:
      self.root = newNode
      newNode.parent = None
      return
    
    parentNode = None
    currentNode = root
    while currentNode != None:
      parentNode = currentNode
      if currentNode.key >= newNode.key:
        currentNode = currentNode.left
      else:
        currentNode = currentNode.right
    
    if key > parentNode.key:
      parentNode.right = newNode
    else:
      parentNode.left = newNode

    newNode.parent = parentNode

    return

    
    






  
  
