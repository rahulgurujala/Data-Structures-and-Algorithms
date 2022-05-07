def insertionsort(arr):
  end = arr[0]
  length = len(arr)
  for i in range(1, length):
    if arr[i] < end:
      x = arr.pop(i)
      for j in range(i):
        if x < arr[j]:
          arr.insert(j,x)
          break
    end = arr[i]
  return arr

arr = [6,5,3,1,8,7,2,4]
print(insertionsort(arr))




