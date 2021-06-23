import math


class Solution:
    def numSquares(self, n: int) -> int:
        
        if math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n)):
            return 1
        
        num_perfect_squares = 0

        largest_square = int(math.sqrt(n))
        new_n = n - (largest_square**2)

        num_perfect_squares += self.numSquares(new_n)

        return num_perfect_squares


sol = Solution()
print(sol.numSquares(12))
print(sol.numSquares(100))

