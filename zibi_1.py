def sum_3(a,b):
    for i in range(a,b):
        if i%2==0 and i%2!=0:
            return i
    else:
        print("Число неудачное")
a=int(input())
b=int(input())
print(sum_3(a,b))
