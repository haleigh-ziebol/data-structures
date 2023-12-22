from array import array
import statistics

## learning python

arr = array('i', [1, 2, 3, 4, 5])
## 1st argument = type code; i = integer
## 2nd argument = elements

print(arr[0]) # output: 1
print(arr[2]) # output: 3

## O= 1, same speed no matter size of array

arr.append(4) # adds 4 to the end
arr.extend([5, 6]) # adds 5 and 6 to end
# extend has O of n, time to do it depends on number of elements
# to add
arr.pop() # removes late element, which is 6

# result: [1, 2, 3, 4, 5]


# for loop

for element in arr:
        print(element)


# while loop

counter = 0  # don't have to declare var to initiate like in JS
condition = True
while condition:
        print(arr[counter])
        counter += 1
        if counter >= len(arr):
                condition = False


# array to store ages of family members

arr1 = array('i', [2, 27, 29, 33])

print(statistics.mean(arr1))