# numbers = [10, 5, 9, 18, 24, 6, 90, 100, 78]
# list_size = len(numbers)

def do_reverse (array):
  reversed_numbers = numbers[::-1]
  return reversed_numbers

# # 1. Bubble Sort
# def do_sorting (array, list_size):
#   for index in range(0, list_size):
#     for ind in range(index+1, list_size):
#       if numbers[index] >= numbers[ind]:
#         numbers[index], numbers[ind] = numbers[ind],numbers[index]

#   return do_reverse(numbers)

# buble_sorted_reversed_numbers  = do_sorting(numbers, list_size)
# print(buble_sorted_reversed_numbers)




numbers = [10, 8, 15, 4, 5, 9]

# 2. Selection Sort
def selectionSort(array):  
  list_size = len(numbers)
  for index in range(list_size):
      min_index = index
      for j in range(index + 1, list_size):
           # select the minimum element in every iteration
          if array[j] < array[min_index]:
              min_index = j
      array[index], array[min_index] = array[min_index], array[index]
    
  return do_reverse(array)

selection_sorted_reversed_numbers  = selectionSort(numbers)
print(selection_sorted_reversed_numbers)






# # 3. Insertion Sort
# def insertionSort(numbers):
#     size = len(numbers)  
#     if size <= 1:
#         return 

#     for i in range(1, size):  
#         key = numbers[i]  
#         j = i-1
#         while j >= 0 and key < numbers[j]:  
#             numbers[j+1] = numbers[j]  
#             j -= 1
#         numbers[j+1] = key  
    
#     return do_reverse(numbers)

# insertion_sorted_reversed_numbers  = insertionSort(numbers)
# print(insertion_sorted_reversed_numbers)






