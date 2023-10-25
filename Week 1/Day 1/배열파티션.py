nums = [6,2,6,5,1,2]

# nums.sort()
# result = 0
# print(nums)
# for i, n in enumerate(nums):
#     if i % 2 ==0:
#         result += n
#
# print(result)

print(sum(sorted(nums)[::2]))