
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        
        self.iterator = iterator
        self.index = -1

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        

    def next(self):
        """
        :rtype: int
        """
       
        

    def hasNext(self):
        """
        :rtype: bool
        """
        


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


peek_iter = PeekingIterator(iter([1, 2, 3]))
print(peek_iter.peek())