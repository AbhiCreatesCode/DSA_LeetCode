# here we are going to find the issing numbers in the array ranging from 0 to n

nums = [0, 1, 3]


# if single value is missing then we can use this solution
def find_missing_number(nums):
    n = len(nums) + 1
    for i in range(n):
        if i not in nums:
            return i
print(find_missing_number(nums))

# if multiple values are missing then we can use this solution
nums = [0,3,4]
def find_missing_numbers(nums):
    n = len(nums) + 1
    missing_numbers = []
    for i in range(n):
        if i not in nums:
            missing_numbers.append(i)
    return missing_numbers
print(find_missing_numbers(nums))
# here we are going to find the issing numbers in the array ranging from 0 to
# n