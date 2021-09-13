# bnry = list(map(int,format(125, 'b')))
# # print(bnry)

# count = 0
# for i in bnry:
#     # print('i', i)
#     if i == 1:
#         # print(bnry)
#         # print('C:', count)
#         count += 1
#         print("N:", count)
#     else:
#         count = 0
#         break
# print("H:",count)











n = int(input().strip())
bnry = list(map(int,format(n, 'b')))
print(bnry)
maximum = 0
count = 0
for i in bnry:
    print('i', i)
    if i == 1:
        # print(bnry)
        # print('C:', count)
        count += 1
        print("N:", count)
    else:
        maximum= max(count, maximum)
        count = 0
print("H:",count)
print(max(maximum,count))
