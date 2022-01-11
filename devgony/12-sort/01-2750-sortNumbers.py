n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

done = None
while not done:
    done = True
    for i, num in enumerate(nums[1:]):
        if nums[i+1] < nums[i]:
            tmp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = tmp
            done = None
for num in nums:
    print(num)