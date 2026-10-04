num=int(input("Enter number:"))
if num < 2:
    print("Not Prime")
else:
    for i in range(2,num):
        if num % i == 0:
            print("Not prime")    
            break
        else:
            print("prime")