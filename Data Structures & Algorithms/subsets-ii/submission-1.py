class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        def backtrack(index, ans):

            result.append(ans[:])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]: continue

                ans.append(nums[i])
                backtrack(i+1, ans)
                ans.pop()

            return

        
        backtrack(0, [])
        return result
        
        