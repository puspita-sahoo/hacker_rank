def pallindrome_creator(str):
    if str == str[::-1]:
        print("Pallindrome")
    elif len(str) < 4 and str != str[::-1]:
        print("Not possible")
    elif len(str) > 3 :#and str != str[::-1]
        for i in range(len(str)):
            lst = list(str)
            ch = lst.pop(i)
            temp = "".join(lst)
            if len(lst) > 3:
                for i in range(len(lst)):
                    lst1 = lst.copy()
                    ch = lst1.pop(i)
                    temp = "".join(lst1)
                    if temp == temp[::-1]:
                        print("CH",ch)
                        print(temp)
                        break
            if temp == temp[::-1]:
                print("C",ch)
                break
            if i == (len(str)-1) and temp != temp[::-1]:
                print("Not possible")


s = input("enter the word: ")
pallindrome_creator(s)















# def pallindrome_creator(str):
#     if str == str[::-1]:
#         print("Pallindrome")
#     elif len(str) <= 3 and str != str[::-1]:
#         print("Not possible")
#     elif len(str) >= 3 and str != str[::-1]:
#         for i in range(len(str)-2):
#             print(i)
#             lst = str.split()
#             print('lst: ',lst)
#             ch = lst.pop(i)
#             print('ch:',ch)
#             str.replace(ch, '')
#             print('str: ',str)
#             print("possible")
#     elif len(str) >= 3 and str != str[::-1]:
#         pass


# s = input("enter the word: ")
# pallindrome_creator(s)
