  
# print("geeks", end =" ")
# print("geeksforgeeks")
    
# print("geeks", end ="")
# print("geeksforgeeks")
  


#   2
# Hacker
# Rank
# Sample Output

# Hce akr
# Rn ak


# s = input("enter the string: ")
# for i in range(len(s)):
#     if i % 2 == 0:
#         print(s[i], end="")
# for i in range(len(s)):
#     if i % 2 != 0:
#         print(s[i])


    # else:
    #     print(s[i])






# s = input("enter the string: ")
# # var = ' '
# for i in range(len(s)):
#     if i % 2 == 0:
#         print(s[i])
#         var ="".join(s[i]),
#         print(var)
# for i in range(len(s)):
#     if i % 2 != 0:
#         var ="".join(s[i])
#         print(var)


# t= int(input("enter: "))

# for i in t:
#     s = input("enter the string: ")












# s = input("enter the string: ")
# var ="".join(s[::2])
# print(var, end=" ")
# var ="".join(s[1::2])
# print(var)

# s = input("enter the string: ")
# print("".join(s[::2]),"".join(s[1::2]))


s = input("enter the string: ")
even = ""
odd = ""
for i,j in enumerate(s):
    if i % 2 == 0:
        even += j
    else:
        odd += j
res = f'{even} {odd}'
print(res)














# #hacker rank soltn
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# T = int(input())

# for i in range(T):
#     S = input()
#     odd_indexed_characters = ''
#     even_indexed_characters = ''
#     for i,j in enumerate(S):
        
#         if i % 2 == 0:
#             odd_indexed_characters += j
#         else:    
#             even_indexed_characters += j
#     print(f"{odd_indexed_characters} {even_indexed_characters}")

