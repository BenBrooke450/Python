

## copy.deepcopy()


"""In Python, a deep copy creates a new object and recursively
 copies all objects found in the original. This is useful when
  you need to ensure that changes to the new object do not
   affect the original object. Here's an example using the
    copy module:
"""

import copy
# Original list containing nested lists
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Perform a deep copy of the original list
deep_copied_list = copy.deepcopy(original_list)

# Modify the deep copied list
deep_copied_list[0][0] = 'a'

# Print both lists to show they are independent
print("Original List:", original_list)
#Original List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Deep Copied List:", deep_copied_list)
#Deep Copied List: [['a', 2, 3], [4, 5, 6], [7, 8, 9]]