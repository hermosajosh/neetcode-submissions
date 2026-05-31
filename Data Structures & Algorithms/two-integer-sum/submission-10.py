class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        differences = {}

        for i in range(len(nums)):

            difference = target - nums[i]

            if differences.get(difference) != None:

                return [differences[difference], i]

            else:

                differences[nums[i]] = i

