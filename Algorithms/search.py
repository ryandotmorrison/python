import random

def create_list():
    list = []
    for i in range(8):
        list.append(random.randint(1,1000))
    return list

nums = create_list()
#print(nums)

def switch_nums(num, num1):
    temp = nums[num]
    nums[num]= nums[num1]
    nums[num1] = temp

def bubble_sort():
    for i in range(1, len(nums)):
        for j in range(0, len(nums) - i):
             if nums[j] > nums[j+1]:
                switch_nums(j, j+1)

def selection_sort():
    for i in range(9):
        biggest_num = 0
        for j in range(len(nums)-(1+i)):
            if nums[j+1] > nums[biggest_num]:
                biggest_num = j+1
        switch_nums(biggest_num, 9-i)
        #print(nums)

#selection_sort()

def split_lists(a):
    if len(a) <= 1:
        return a
    half = len(a) // 2
    left = a[:half]
    right = a[half:]
    splitLeft = split_lists(left)
    splitRight = split_lists(right)
    return merge_sort(splitLeft, splitRight)

test = [1, 2, 3, 4]
testRight = test[1:]
testLeft = test[:1]
testSorted = []

def merge_sort(left, right):
    number1 = 0
    number2 = 0
    merged = []
    while number1 < len(left) and number2 < len(right):
        if left[number1] < right[number2]:
            merged.append(left[number1])
            number1 += 1
        else:
            merged.append(right[number2])
            number2 += 1
    merged.extend(left[number1:])
    merged.extend(right[number2:])
    return merged

print(nums)
newNums = split_lists(nums)
print(newNums)