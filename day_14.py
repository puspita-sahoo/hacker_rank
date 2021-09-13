class Difference:
    def __init__(self, a):
        self.__elements = a
    
    def computeDifference(self):
        # for i in range(_):
        #     self.__elements[i] - self.__elements[i+1]
        self.max_diff = max(self.__elements) - min(self.__elements)


    def maximumDifference(self):
        return self.max_diff
   
_ = int(input())
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print("K:", d.maximumDifference())