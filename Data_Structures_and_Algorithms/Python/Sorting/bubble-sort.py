# Bubble sort - compares two adjacent elements and swaps them until they are in the intended order

def bubbleSort(data):
  # loop to access each array element
  for i in range(len(data)):

    # loop to compare array elements
    for j in range(len(data) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if data[j] > data[j+1]:
        temp = data[j]
        data[j] = data[j+1]
        data[j+1] = temp

data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)