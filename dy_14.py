class Difference:
    def __init__(self, a):
        self.__elements = a
    
    def computeDifference(self):
        # self.max_diff = max(self.__elements) - min(self.__elements) 
        self.maximumDifference = max(self.__elements) - min(self.__elements) 
        # maximumDifference = self.max_diff
        # return 
    
        
    # def maximumDifference(self):
        # return self.max_diff
    
	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)