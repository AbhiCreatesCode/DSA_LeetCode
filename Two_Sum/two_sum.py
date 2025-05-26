nums = [2,7,8,11,12,14]

# def two_sum(nums):
#     num_dict = {}
#     for i, num in enumerate(nums):
#         if num in num_dict:
#             return [num_dict[num], i]
#         else:
#             num_dict[num] = i
#             return [1 , 1]
        
def two_sum(nums, target):
    for i in nums:
        diff = target - i
        if diff in nums:
            return [nums.index(i), nums.index(diff)]
print(two_sum(nums=nums, target=13))  # Output: [0, 1]