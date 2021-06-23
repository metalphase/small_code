# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def list_repr(self):

        # Here we will list the numbers in the ListNode in a list 
        # representation
        list_integer = []

        # We store our current node's value in a variable
        current_node = self

        # If the ListNode doesn't link to another ListNode, we append its 
        # value into the list
        if self.next == None:
            list_integer.append(current_node.val)
        # Otherwise, we will loop over the ListNodes and append their values
        else:
            while current_node != None:
                list_integer.append(current_node.val)
                current_node = current_node.next
        
        return list_integer

'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
'''
def list_to_integer(nums):
    """Creates ListNode representation of an integer given by a list"""

    # Store the length of the list
    length = len(nums)

    # Check for invalid leading zeros unless the size of nums is zero
    if nums[0] == 0 and length != 1:
        return -1

    # Set up our first node and create a variable for the value of the next
    # node
    initial_node = ListNode(nums[0])

    temp_node = initial_node

    # For each element in nums, we want to link it to the initial node
    for i in (range(length - 1)):

        initial_node.next = ListNode(nums[i+1])
        initial_node = initial_node.next

    
    return temp_node

def add_list_node_integers(l1, l2):
    """
    Returns a ListNode representing the result of the addition of ListNode 
    integers, l1 and l2.
    """

    # We want to add up the integers only up to the maximum length of the 
    # smaller integer.
    length = min(len(l1), len(l2))

    # Reverse the lists since the lists l1 and l2 represent the reverse of the
    # numbers we want to add up
    l1_reverse = l1[::-1] 
    l2_reverse = l2[::-1] 

    # We will store the summation in here
    sum = []

    if len(l1) < len(l2):
        sum = l2.copy()
    elif len(l1) > len(l2):
        sum = l1.copy()

    print(sum)
    # We loop over the length of the smaller integer and add up the integers
    # by their individual digits
    for i in range(length):

        sum[i] = (l1_reverse[i] + l2_reverse[i])

    # Next we loop over the length of the sum list.
    # First we define the carryover 
    carryover = 0
    
    print(sum)
    
    for i in range(len(sum)):
        
        # We add the carryover to the element
        sum[i] += carryover
        carryover = 0

        # If the element is larger than or equal to 10, we set it to 0 and distribute the 
        # remainder into carryover
        if sum[i] >= 10:
            
            sum_to_str = str(sum[i])
            # We add the carryover from sum[i] and set sum[i] to 9
            carryover += int(sum_to_str[0])
            sum[i] = int(sum_to_str[1])


    # If we still have carryover leftover, we must add it to the fron of sum
    if carryover != 0:
        
        carryover_to_str = str(carryover)

        for i in range(len(carryover_to_str)):

            sum.append(int(carryover_to_str[i]))

        
    return sum

        

# testing ListNode.list_repr()

print("Testing ListNode.list_repr()")
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)

node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

print(node_1.list_repr())
print(node_2.list_repr())
print('---------------------------------------------------------------------')
print('\n')

# Testing list_to_integer

print("Testing list_to_integer")

integer_invalid = [0, 1, 2, 3]
integer_1 = [1, 2, 3, 4]
integer_2 = [12, 23, 43, 111]
integer_3 = [1,2,3,4,5,6,7,8,9,10]

integer_1_node = list_to_integer(integer_1)
print(integer_1_node.list_repr())

integer_2_node = list_to_integer(integer_2)
print(integer_2_node.list_repr())

integer_3_node = list_to_integer(integer_3)
print(integer_3_node.list_repr())

print('---------------------------------------------------------------------')
print('\n')

# Testing with example input

print("Testing with example input l1, l2")
# 2 -> 4 -> 3
l1 = [2, 4, 3]

# 5 -> 6 -> 4
l2 = [5, 6, 4]

# Convert the list into ListNode representation 
l1_int = list_to_integer(l1)
l2_int = list_to_integer(l2)

# Express it back in the list form, which should be equivalent to the input
print(l1_int.list_repr())
print(l2_int.list_repr())

print('---------------------------------------------------------------------')
print('\n')


# Testing with example input

print("Testing addition with l1 and l2")

# Add together using add_list_node_integers
print(add_list_node_integers(l1, l2))

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

print(add_list_node_integers(l1, l2))