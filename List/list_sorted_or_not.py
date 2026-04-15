

nums = [2, 5, 7, 9, 11, 8]

for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
        print("List is not sorted")
        break
else:
    print("List is sorted")

