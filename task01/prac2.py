from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i >= j:
                continue
            else:
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    continue


if __name__ == "__main__":
    get: List[int] = twoSum([2, 7, 11, 15], 9)
    print(get)
    get: List[int] = twoSum([3, 2, 4], 6)
    print(get)
    get: List[int] = twoSum([3, 3], 6)
    print(get)