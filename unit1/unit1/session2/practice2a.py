def goldilocks_approved(nums):
    minumum = 0 
    maximum = 0
    if len(nums) <= 2:
        return -1
    for i in range(len(nums)):
        if i!=min(nums) and i!=max(nums):
            print(i)                

nums = [3, 2, 1, 4]
x = goldilocks_approved(nums)
print(x)
nums = [1, 2]
x = goldilocks_approved(nums)
print(x)
nums = [2, 1, 3]
x = goldilocks_approved(nums)
print(x)