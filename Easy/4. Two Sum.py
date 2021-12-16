nums = [2, 7, 11, 15]
target = 9

diff = input()
i = input()

prevMap = {}  # value : index
for i, n in enumerate(nums):
    diff = target - n
    if diff in prevMap:
        print([prevMap[diff], i])
    prevMap[n] = i
print([prevMap[diff], i])
