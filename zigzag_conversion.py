class Solution:
    def convert(self, s, numRows):
        

        if numRows == 1:
            print(s)


        # We store the position of each character and their row number in the
        # following dictionary
        ordered_chars = {}

        # We use j to iterate over the string
        j = 0

        # We itereate while we are still within the bounds of the string
        while j <= len(s) - 1:
            
            # We iterate over i in ascending order but we exit if we are
            # still within the string and the number i is beyond numRows+1.
            # We assign the j'th index the value of i.
            i = 1
            while i < numRows + 1 and j <= len(s) - 1:

                ordered_chars[j] = i
                i+=1
                j+=1
            
            # We likewise iterate over k in descending order from numRows-1 
            # to 1 and exit if we go below that or if j is beyond the string
            # length. We assign the j'th index the value of k.
            k = numRows - 1
            while k > 1 and j <= len(s) - 1:

                ordered_chars[j] = k
                k -= 1
                j+= 1
        

        s_zigzag = ""
        for i in range(1, numRows+1):
            for index in ordered_chars.keys():

                if ordered_chars[index] == i:
                    s_zigzag += s[index]
            
        return s_zigzag

sol = Solution()
print(sol.convert("PAYPALISHIRING", 2))
print(sol.convert("PAYPALISHIRING", 3))
print(sol.convert("PAYPALISHIRING", 4))
print(sol.convert("PAYPALISHIRING", 5))