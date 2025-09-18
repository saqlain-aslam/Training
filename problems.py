 # 1  swap first element with second last element of an array

arr1 = [10, 20, 30, 40, 50]

temp = arr1[0]
arr1[0] = arr1[-2]  
arr1[-2] = temp

print("after swap:", arr1)


# 2 dynamic array 

length = int(input("enter length of array: "))
arr2 = []

for i in range(length):
    num = int(input(f"Enter element {i+1}: "))
    arr2.append(num)

if length >= 2: 
    temp = arr2[0]
    arr2[0] = arr2[-2]
    arr2[-2] = temp

print("after swap first and second last:", arr2)



# 3 swapuser-selected indexes in array

arr3 = [5, 10, 15, 20, 25]

print("original aray:", arr3)
i = int(input("Enter first index to swap: "))
j = int(input("Enter second index to swap: "))

# check if indexes are valid
if i <= 0 < len(arr3) and j <= 0 < len(arr3):
    temp = arr3[i]
    arr3[i] = arr3[j]
    arr3[j] = temp
    print("array after swapping:", arr3)
else:
    print("invalid indexes")


# 4: count vowels and consonants

text = input("enter string: ").lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha():  # check if character is a letter
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("total vowels:", vowel_count)
print("total consonants:", consonant_count)


# 5 sum of matching elements in an array

arr = [1, 2, 3, 2, 4, 1, 2]
num = int(input("Enter number to find sum of all matches: "))

total = 0
for x in arr:
    if x == num:
        total += x

print(f"total of all {num}'s in array:", total)


