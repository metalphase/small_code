class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string input, s, the function returns the length of the 
        longest substring within s.
        """

        # Check for constraints
        if len(s) > 5e4:
            return -1

        # We will store the largest length substring with distinct
        # characters in this variable and return it in the end
        largest_substring_length = 0

        # We loop over the length of the string
        for i in range(len(s)):

            # The length will denote the length of the current substring 
            # being counted. 
            length = 0

            # The distinct characters will be stored and checked with the 
            # list, distinct_chars. We will use the boolean distinct to help 
            # us loop over each of the substrings until we detect a duplicate
            # character
            distinct_chars = []
            distinct = True

            # We loop over each substring with help of the variable, j, which
            # starts at the ith position
            j = i

            # While the characters being encountered are still distinct and
            # we are not going past the end of the string, s, we check if the
            # current character has been seen and append it to
            # distinct_chars if not. We increase the size of length by one. 
            while distinct and j <= len(s)-1:
                
                if s[j] not in distinct_chars:
                    
                    distinct_chars.append(s[j])
                    length += 1

                # If we encounter a duplicate character, then if the size of 
                # length is larger than the global largest_substring_length 
                # variable, then we redefine largest_substring_length to length.
                else:
                    
                    if length > largest_substring_length:
                        largest_substring_length = length
                    
                    distinct = False

                j+=1
               
            # If it has reached the end without encountering a duplicate,
            # we must set largest_substring_length to length
            if length > largest_substring_length:
                largest_substring_length = length

                    
        return largest_substring_length

sol = Solution()
print(sol.lengthOfLongestSubstring('abcabcbb'))
print(sol.lengthOfLongestSubstring('bbbbb'))
print(sol.lengthOfLongestSubstring('pwwkew'))
print(sol.lengthOfLongestSubstring('au'))
print(sol.lengthOfLongestSubstring(''))
print(sol.lengthOfLongestSubstring(' '))