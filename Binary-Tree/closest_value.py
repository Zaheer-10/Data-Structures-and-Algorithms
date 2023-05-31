# create a binary search tree
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)


# define the closest_value function
def closest_value(root, target):
  if root is None:
    return float("inf")
  if root.val == target:
    return root.val
  closest = closest_value.closest
  
  if abs(root.val - target) < abs(closest - target):
    closest = root.val
  closest_value.closest = closest
  
  if target < root.val:
    return closest_value(root.left, target)
  else:
    return closest_value(root.right, target)

closest_value.closest = float("inf")

print(closest_value(root, 12))


