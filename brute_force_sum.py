#  brute force for sum
def two_sum_brute_force(nums, target):

    #  selects the first number
    for i in range(len(nums)):

        #  selects the second number
        for j in range(i + 1, len(nums)):
            #  if the two numbers sum is equal  to the target
            if nums[i] + nums[j] == target:
                return [i, j]  
    return []
# array
nums = [2, 6, 8, 1]

target = 9

# Call 
result = two_sum_brute_force(nums, target)
print(result)
# brute force is used to check all possible pairs when the value is not found 
# when the loop finds the pair it returns the index of the two numbers that sum to the target