class Person:
    def __init__(self, initial_age):
        if initial_age > 0:
            self.age = initial_age
        elif initial_age < 0:
            self.age = 0
            print("age is invalid, setting age to 0.")



    def am_i_old(self):
        if self.age >= 0 and self.age < 13:
            print("young")
        elif self.age >= 13 and self.age < 18:
            print("teenage")
        else:
            print("old")

    def year_passess(self):
        self.age += 3     
        if self.age >= 0 and self.age < 13:
            print("young")
        elif self.age >= 13 and self.age < 18:
            print("teenage")
        else:
            print("old")


t = int(input("enter number of time u want to test: "))
for i in range(0,t):
    age = int(input("enter your age: "))
    ob = Person(age)
    ob.am_i_old()
    ob.year_passess()
    print()




       
# Age is not valid, setting age to 0.
# You are young.
# You are young.

# You are young.
# You are a teenager

# You are a teenager.
# You are old.

# You are old
# You are old.       










# this is hacker rank ans=========================

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge > 0:
            self.age = initialAge
        else:
            self.age = 0
            print("Age is not valid, setting age to 0.")
            
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age >= 0 and self.age <= 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")        
                           
    def yearPasses(self):
        # he age of the person in here
        self.age += 1
        if self.age >= 0 and self.age <= 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")        
        
# Age is not valid, setting age to 0.
# You are young.
# You are young.

# You are young.
# You are a teenager

# You are a teenager.
# You are old.

# You are old
# You are old.       

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")










#     Your Output (stdout)

# Age is not valid, setting age to 0.
# You are young.
# You are young.
# You are young.
# You are young.
# You are young.

# You are young.
# You are young.
# You are a teenager.
# You are old.
# You are old.

# You are a teenager.
# You are old.
# You are old.
# You are old.
# You are old.

# You are old.
# You are old.
# You are old.
# You are old.
# You are old.


