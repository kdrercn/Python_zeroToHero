numbers = [1,10,5,16,4,9,10]
letters = ["a","g","s","b","y","a","s"]

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]

numbers[4] = 40

numbers.append(49)
numbers.insert(3,78)
numbers.pop()
numbers.remove(78)
numbers.sort()
numbers.reverse()
letters.sort()
letters.reverse()


print(len(numbers))
print(len(letters))

print(numbers.count(10))
print(letters.count("a"))

numbers.clear()
print(numbers)

#https://www.w3schools.com/python/python_ref_list.asp