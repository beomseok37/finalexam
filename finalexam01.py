def findpi(i):
    result=0
    for a in range(1,2*i):
        if a%4==1:
            result+=1/a
        elif a%4==3:
            result-=1/a
    result*=4
    return result

print("i\t\tm(i)")
for i in range(10):
    print(str(i*100+1)+"\t\t{0:.4f}".format(findpi(i*100+1)))
