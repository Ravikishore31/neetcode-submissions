class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(ind, ans):

            if ind == len(nums):
                result.append(ans[:])
                return

            ans.append(nums[ind])
            backtrack(ind+1, ans)
            ans.pop()

            backtrack(ind+1, ans)

        backtrack(0, [])
        return result

        
        