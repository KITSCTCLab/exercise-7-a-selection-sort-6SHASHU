from typing import List

def selectionSort(array, size) -> List[int]:
  for i in range(len(arr)):
    maximum = i
    for j in range(i+1,len(arr)):
      if arr[j] > arr[maximum]:
        maximum = j
    temp = arr[i]
    arr[i] = arr[maximum]
    arr[maximum] = temp
  return arr

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
