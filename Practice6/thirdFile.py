from firstFile import GLOBAL_VAR
from secondFile import print1
import firstFile


def print2():
    print("PRINT2")
    print(GLOBAL_VAR)
    print(firstFile.GLOBAL_VAR)
    print()


GLOBAL_VAR = 1
print1()
print2()

firstFile.GLOBAL_VAR = 1
print1()
print2()
