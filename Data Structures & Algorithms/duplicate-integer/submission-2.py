class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        
        existing = []
        for num in nums:
            if num in existing:
                return True
            else:
                existing.append(num)

        return False
