class Solution:
    def longestPalindrome(self, s):
        
        if len(s) > 1000:
            return -1

        largest_palindrome = ""
        if len(s) != 0:
            largest_palindrome += s[0]
        
        # Running over every possible first position of the palindrome
        for i in range(len(s)):
            
            # We will temporarily store the substring generated from the ith
            # element in substring
            substring = ""

            # We won't bother beginning a collection processes if the number
            # characters, s[i], is not over 1.
            if s.count(s[i]) > 1:
                
                # We will run a while loop until we have found the end of the
                # substring, which occurs if we've found another character 
                # s[i]
                end_of_string = False

                # We immediately add the first character to the string
                substring += s[i]

                # We use j to loop over the next elements in s
                j=i+1

                # While we do not encounter an end to our palindromic 
                # substring, we loop over the elements
                while not end_of_string:
                    
                    # If our j iterator is out of bounds, we set 
                    # end_of_string to True
                    if j > len(s) - 1:
                        end_of_string = True

                    # If we encounter another character like s[i], we set 
                    # end_of_string to True
                    elif s[j] == s[i]:
                        substring += s[j]
                        end_of_string = True
                    
                    # Otherwise we accumulate the characters into the 
                    # substring
                    else:
                        substring += s[j]
                    
                    j+=1
            
            # We must now analyze the substring accumulated
            if palindrome_check(substring) and len(substring) > len(largest_palindrome):
                
                largest_palindrome = substring
                    
            
            
        return largest_palindrome

def palindrome_check(s):


    if len(s) == 1:
        return True

    if len(s) % 2 == 0:
                
        is_palindrome = True

        j = 0
        while is_palindrome and j < (len(s) / 2):

            if s[j] != s[len(s) - 1 - j]:
                is_palindrome = False


            j += 1
    else:

        is_palindrome = True

        j = 0
        while is_palindrome and j < (len(s) - 1 / 2):

            if s[j] != s[len(s) - 1 - j]:
                is_palindrome = False


            j += 1

    return is_palindrome


#print(palindrome_check("abcddcba"))
#print(palindrome_check("abcba"))
#print(palindrome_check("abca"))
#print(palindrome_check("a"))


s = Solution()

print(s.longestPalindrome("abcba"))
print(s.longestPalindrome("a"))
print(s.longestPalindrome("ac"))
print(s.longestPalindrome("bbbb"))
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
