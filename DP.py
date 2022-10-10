from numpy import true_divide


class DP:
    def canSum(total, numbers):
        if(total == 0): return True
        if(total < 0): return False

        for num in numbers:
            remainder = total - num
            if (DP.canSum(remainder, numbers)):
                return True
        return False

    def fib(location, memo={}):
        if(location <= 1): return 1
        if(memo.)
        return DP.fib(location - 1) + DP.fib(location - 2)

import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(2000000)
#print(DP.canSum(30000001, [2, 3, 5, 4,6,7,9,1]))
print(DP.fib(50))
