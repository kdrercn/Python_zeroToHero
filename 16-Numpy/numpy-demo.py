import numpy as np

numbers = np.array([10,15,30,45,60])
numbers = np.arange(5,15)
numbers = np.arange(50,100,5)
numbers = np.zeros(10)
numbers = np.ones(10)
numbers = np.linspace(0,100,5)
numbers = np.random.randint(10,30,5)
numbers = np.random.randn(10)

nums = np.random.randint(-50,50,15).reshape(3,5)
print(nums)
# x = nums.sum(axis=1)
# y = nums.sum(axis=0)
# print(x,y)
# print(nums.max(),nums.min(),nums.mean())
# print(nums.argmax())

# numbers = np.arange(10,20)
# result = numbers[:3]
# result = numbers[::-1]

# result = nums[0]
result = nums[1,2]
result = nums[:,0]
result = nums*nums

ciftler = nums[nums % 2 == 0]
result = ciftler[ciftler>0]



print(result)
