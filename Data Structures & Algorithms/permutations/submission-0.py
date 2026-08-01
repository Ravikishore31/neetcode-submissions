class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def backtrack(ans):

            if len(ans) == len(nums):
                result.append(ans[:])
                return


            for num in nums:

                if num in ans:
                    continue

                ans.append(num)
                backtrack(ans)
                ans.pop()

        backtrack([])
        return result
            