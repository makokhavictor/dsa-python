class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
def preorder(root):
  if root is None:
    return

  print(root.data)
  inorder(root.left)
  inorder(root.right)

def inorder(root):
  if root is None:
    return

  inorder(root.left)
  print(root.data)
  inorder(root.right)

def postorder(root):
  if root is None:
    return

  postorder(root.left)
  postorder(root.right)
  print(root.data)


def main():
  root = Node(10)
  root.left = Node(5)
  root.right = Node(15)
  root.left.left = Node(2)
  root.left.right = Node(7)
  root.right.left = Node(12)
  root.right.right = Node(17)

  inorder(root)


if __name__ == "__main__":
  main()