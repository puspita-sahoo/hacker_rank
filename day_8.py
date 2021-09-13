n = int(input())
phn_bk = {}
for i in range(n):
    nm, num= input().split(" ")
    phn_bk[nm] = int(num)


while True:
    name = str(input())
    
    if name not in phn_bk:
        print("Not found")
    else:
        print(f"{name}={phn_bk[name]}")











