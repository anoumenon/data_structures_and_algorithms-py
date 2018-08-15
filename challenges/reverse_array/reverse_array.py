def reverse_array(arr):

  if type(arr) is not list:
    raise TypeError('type error, argument is not a list')

  mid = len(arr) // 2
  p1, p2, = 0, -1

  for _ in range(mid):
    arr[p1], arr[p2] = arr[p2], arr[p1]
    p1 += 1
    p2 -= 1
  
  return arr