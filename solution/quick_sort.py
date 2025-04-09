
'''
Create a simple quick sort algorithm
'''


def quick_sort(arr):
  if len(arr)<=1:
    return arr

  pivot = arr[len(arr)//2]
  left = [i for i in arr if i<pivot]
  right = [i for i in arr if i>pivot]
  return quick_sort(left) + [pivot] + quick_sort(right)

arr = [15,24,9,49,12,23]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)