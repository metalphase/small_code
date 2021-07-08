class Solution:
    def getBiggestThree(self, grid):
        
        # We will store our rhombus sums here
        biggest_rhombus_sums = [0, 0, 0]

        # We get our length and width values from the length of the grid
        # list and the length of the zeroeth list
        m = len(grid)
        n = len(grid[0])

        # We store the top three largest sums in this list
        largest_sums = []


        # We cycle through each x and y and see how many rhombus sums can 
        # be calculated at x and y and insert them into our list
        for x in range(m):

            for y in range(n):
                
                rhombus_size = 0
                # We calculate the rhombus sums at (x,y) while a rhombus 
                # of size rhombus_size can fit at (x,y)
                while self.can_fit_rhombus(grid, x, y, rhombus_size):
                    
                    # Sort the list of largest sums, the smallest sum will be 
                    # last
                    largest_sums.sort(reverse=True)

                    # Calculate the next sum
                    rhombus_sum = self.rhombus_sum(grid, x, y, rhombus_size)

                    # If we have an empty list to begin with, we only add to it
                    # if the current sum is larger than the smallest one in the 
                    # list, and if the sum isn't already in the list. We limit
                    # our list size to 3
                    if len(largest_sums) < 3 and rhombus_sum not in largest_sums:
                        largest_sums.append(rhombus_sum)
                    elif (rhombus_sum not in largest_sums) and (rhombus_sum > largest_sums[-1]):

                        largest_sums[-1] = rhombus_sum

                    rhombus_size += 1

        # We do a final reverse sort and then return our list
        largest_sums.sort(reverse=True)
        return largest_sums
    

    # Helper function that allows us to determine if a rhombus of size 
    # rhombus_size can be calculated at (x,y)
    def can_fit_rhombus(self, grid, x, y, rhombus_size):
        
        m = len(grid)
        n = len(grid[0])
        
        # If the bounds for the top, bottom, left, and right vertices 
        # exceed the boundary of the grid, we return False. Otherwise, we return
        # true.
        if (y - rhombus_size < 0) or (y + rhombus_size > n-1) or \
            (x + rhombus_size > m-1) or (x - rhombus_size < 0):
            return False
        else:
            #print('x: ', x, 'y: ', y, 'rhombus size: ', rhombus_size)
            return True

    # Helper function that calculates the rhombus sum at (x,y) with size
    # rhombus_size
    def rhombus_sum(self, grid, x, y, rhombus_size):
        
        # Define the top and bottom vertices of the rhombus
        b_y = y + rhombus_size
        b_x = x
        
        t_y = y - rhombus_size
        t_x = x

        # We store our sum into a variable
        sum = 0

        # If the rhombus size is zero, we just return the number at [i,j]
        if rhombus_size == 0:
            return grid[x][y]

        # Otherwise, we want to sum up the perimeter points
        for i in range(rhombus_size + 1):
        
            # In the beginning of the loop we only add two points
            if i == 0:
                sum += grid[t_x][t_y] + grid[b_x][b_y]
            # At the same time at the end of the loop we only add 
            # two points
            elif i == rhombus_size:
                sum += grid[t_x - i][t_y + i] + grid[t_x + i][t_y + i]
            #  Otherwise we need to add up 4 separate points
            else:
                
                
                sum += (grid[t_x - i][t_y + i] + grid[t_x + i][t_y + i] 
                        + grid[b_x - i][b_y - i] + grid[b_x + i][b_y - i])

        return sum



# Testing regimen


grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]

sol = Solution()


print(sol.rhombus_sum(grid, 2, 2, 0))
print(sol.rhombus_sum(grid, 2, 2, 1))
print(sol.rhombus_sum(grid, 2, 2, 2))
print(sol.can_fit_rhombus(grid, 2, 2, 3))

print(sol.can_fit_rhombus(grid, 0, 0, 3))
print(sol.can_fit_rhombus(grid, 0, 0, 2))
print(sol.can_fit_rhombus(grid, 0, 0, 1))
print(sol.can_fit_rhombus(grid, 0, 0, 0))

print(sol.can_fit_rhombus(grid, 4, 4, 0))
print(sol.can_fit_rhombus(grid, 4, 4, 1))
print(sol.can_fit_rhombus(grid, 4, 4, 2))
print(sol.can_fit_rhombus(grid, 4, 4, 3))

print(sol.getBiggestThree(grid))
print('_______________________________________________________________________')

# 3x3 Grid
grid = [[1,2,3],[4,5,6],[7,8,9]]
print(grid[0][1])
print(sol.getBiggestThree(grid))

grid = [[7,7,7]]
print(sol.getBiggestThree(grid))

print('_______________________________________________________________________')

grid =[[20,17,9,13,5,2,9,1,5],[14,9,9,9,16,18,3,4,12],\
    [18,15,10,20,19,20,15,12,11],[19,16,19,18,8,13,15,14,11],\
    [4,19,5,2,19,17,7,2,2]]
print(sol.getBiggestThree(grid))