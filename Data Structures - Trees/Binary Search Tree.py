class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:

  def __init__(self):
    self.root = None

  def insert(self,data):
    new_node = Node(data)
    if self.root is None:
      self.root = new_node
      return
    else:
      curr_node = self.root
      while True:
        if data < curr_node.data:
          #Left
          if curr_node.left is None:
            curr_node.left = new_node
            return
          else:
            curr_node = curr_node.left
        elif data > curr_node.data:
            #Right
          if curr_node.right is None:
            curr_node.right = new_node
            return
          else:
            curr_node = curr_node.right

  def lookup(self,data):
    curr_node = self.root
    while True:
      if curr_node is None:
        return False
      if curr_node.data == data:
        return True
      elif data < curr_node.data:
        curr_node = curr_node.left
      else:
        curr_node = curr_node.right
    
  def print_tree(self):
    if self.root != None:
      self.printt(self.root)
#Inorder Traversal (We get sorted order of elements in tree)

  def printt(self,curr_node):
    if curr_node != None:
      self.printt(curr_node.left)
      print(curr_node.data)
      self.printt(curr_node.right)
    
  #If Intrested
  #code for remove
  
  def remove(self,data):
    if self.root is None:
      return False

    currentNode = self.root
    parentNode = None

    while currentNode:
      if data < currentNode.data:
        parentNode = currentNode
        currentNode = currentNode.left
      elif data > currentNode.data:
          parentNode = currentNode
          currentNode = currentNode.right
      elif data == currentNode.data:
              # We have a match, get to work!

              # Option 1: No right child:
        if currentNode.right is None:
          if parentNode is None:
            self.root = currentNode.left
          elif currentNode.data < parentNode.data:
            parentNode.left = currentNode.left
          elif currentNode.data > parentNode.data:
              parentNode.right = currentNode.left

        elif currentNode.right.left is None:
          currentNode.right.left = currentNode.left
          if parentNode is None:
            self.root = currentNode.right
          elif currentNode.data < parentNode.data:
            parentNode.left = currentNode.right
          elif currentNode.data > parentNode.data:
              parentNode.right = currentNode.right


        else:
          #find the Right child's left most child
          leftmost = currentNode.right.left
          leftmostParent = currentNode.right
          while leftmost.left != None:
              leftmostParent = leftmost
              leftmost = leftmost.left

          #Parent's left subtree is now leftmost's right subtree
          leftmostParent.left = leftmost.right
          leftmost.left = currentNode.left
          leftmost.right = currentNode.right

          if parentNode is None:
            self.root = leftmost
          elif currentNode.data < parentNode.data:
            parentNode.left = leftmost
          elif currentNode.data > parentNode.data:
              parentNode.right = leftmost
      return True

        

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)
x = bst.lookup(6)
print(x)
y = bst.lookup(99)
print(y)
bst.print_tree()
