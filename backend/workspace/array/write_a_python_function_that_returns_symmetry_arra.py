# This code corresponds to repeated/similar prompt

def symmetry_array(arr):
  """
  Checks if an array is symmetric around its center.

  Args:
    arr: A list or tuple representing the array.

  Returns:
    A list of booleans indicating whether each element is symmetric
    with respect to the center of the array.  The array is symmetric if
    the element at index i is equal to the element at index len(arr) - 1 - i.
  """
  n = len(arr)
  symmetry = []
  for i in range(n):
    symmetry.append(arr[i] == arr[n - 1 - i])
  return symmetry