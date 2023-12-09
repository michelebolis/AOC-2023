nums = [[int(newline) for newline in line.strip().split()] for line in open("input.txt")]

def resolve(nums):
    diffs = [nums[index] - nums[index-1] for index in range(1, len(nums))]
    return nums[-1] + resolve(diffs) if len(diffs) != 0 else nums[-1]

print('part 1:', sum([resolve(num) for num in nums]))
print('part 2:', sum([resolve(num[::-1]) for num in nums]))