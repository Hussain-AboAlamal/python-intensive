import cProfile
import random
import sys


class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
    

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)


if __name__ == "__main__":
    # get input from console
    n = input("Please enter the number of items: ")
    # check that user has inserted a valid integer
    try:
        n = int(n)
        if n < 1 :
            print("number should be gretaer than or equal 1.")
            sys.exit(1)
    except ValueError:
        print(f"{n} is not a valid integer. Please try again.")
        sys.exit(1)
    
    # generate items from user input
    nums = [random.uniform(0, 99) for _ in range(n + 1)]

    # print tree performance stats
    cp = cProfile.Profile()
    cp.enable()

    bst = BSTNode()
    for num in nums:
        bst.insert(num)
        
    cp.disable()
    cp.print_stats()
