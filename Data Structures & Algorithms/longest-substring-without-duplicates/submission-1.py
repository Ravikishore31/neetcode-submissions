class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        length = 0

        freq = defaultdict(int)
        for right in range(len(s)):
            freq[s[right]]+=1

            while freq[s[right]] > 1:
                freq[s[left]] -= 1

                if freq[s[left]] == 0:
                    del freq[s[left]]
                    
                left += 1

            length = max(length, right-left+1)

        return length
        