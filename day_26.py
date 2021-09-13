# d1, m1, y1 = map(int,(input()).split(" "))   #d1 = actual reurn dt
# d2, m2, y2 = map(int,input().split(" "))   #d2 = expected reurn dt

# if d1 <= d2 and m1 == m2 and y1 == y2:
#     fine = 0
#     print(fine)
# elif d1 > d2:
#     if m1 == m2 and y1 == y2:
#         fine = 15 * (d1-d2)
#         print(fine)
# elif m1 > m2:
#     if y1 == y2:
#         fine = 500 * (m1-m2)
#         print(fine)
# else:
#     if y1 > y2:
#         fine = 10000
#         print(fine)

        




# Enter your code here. Read input from STDIN. Print output to STDOUT

d1, m1, y1 = map(int,(input()).split()) #actual retn
d2, m2, y2 = map(int,(input()).split()) #expect rtn
# if y1 <= y2:
#     fine = 0
#     print(fine)
#     if m1 <= m2:
#         fine = 0
#         print(fine)
#         if d1 <= d2:
#             fine = 0
#             print(fine)
# elif y1 > y2:
#     fine = 10000
#     print(fine)
# elif m1 > m2:
#     if y1 == y2:
#         fine = 500 * (m1-m2)
#         print(fine)    
# elif d1 > d2:
#     if m1 == m2 and y1 == y2:
#         fine = 15 * (d1-d2)
#         print(fine)
        

    
    






 
# if y1 <= y2 and m1<= m2:
#     if d1 > d2:
#         fine = 15 * (d1 - d2)
#         print(fine)
# if y1 <= y2:
#     if m1 > m2:
#         fine = 500 * (m1 - m2)
#         print(fine)
#     # elif m1 < m2:
#     #     fine = 0
#     #     print(fine)
# if y1 > y2:
#     fine = 10000
#     print(fine)

# if y1 == y2 :
#     if m1 <= m2 and d1 <= d2 :
#         fine = 0
#         print(fine)
#     elif m1 < m2:
#         fine = 0
#         print(fine)
#         fine = 0
#     print(fine)


if y1 > y2:
    fine = 10000

if y1 == y2:
    if m1 > m2:
        fine = 500 * (m1 - m2)
        print(fine)  
    elif  d1 > d2:
        fine = 15 * (d1 - d2)
else:
    fine = 0
print(fine)



# if y1 == y2 :
#     if m1 <= m2 and d1 <= d2 :
#         fine = 0
#         print(fine)
#     elif m1 < m2:
#         fine = 0
#         print(fine)
#         fine = 0
#     print(fine)














   
