class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        
        existing = {}
        for num in nums:

            if existing.get(str(num), None) == None:

                existing[str(num)] = 1

            else:
                return True

        return False
