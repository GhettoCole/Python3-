# Self defined module test

import sum

print("Sum: ", sum.getSum(1,2,3,4,5,7))

from sum import getSum

print("Another Sum: ", getSum(12,12,12,1,2,12))

print("5 * 6 + 6 = ", sum.multiply(5, 6))