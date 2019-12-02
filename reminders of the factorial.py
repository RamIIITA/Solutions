#Fac Function results facotrial for a particular number
def fact(n):
    Sum = 1
    if n<3:
        return n
    for i in range(2,n+1):
        Sum*=i
    return Sum

#solution part
def sol(n):
    temp = 1
    fac = [0,1]
    dic_fac = {1:1,2:2,0:0}
    for i in range(2,n):
        factor = fact(i)
        temp+=(factor*i)
        dic_fac[i] = factor
        fac.append(i)
        if n<temp:
            break
    
    ans=dict()
    for i in fac:
        ans[i]=0
    
    while(n):
        for i in reversed(fac):
            for j in range(i,-1,-1):
                if (j*dic_fac[i]) <=  n:
                    n-=(j*dic_fac[i])
                    ans[i] = j
                    break
                if n<1:
                    break
                
            if n<1:
                break
    result = ""
    for i in sorted(ans.keys(), reverse = True):
        result=result+str(ans[i])+" "
    return result
    
#checking the base conndition    
def fun(n):
    if n<1:
        return 0
    if n<2:
        return str(1)+" "+str(0)
    return sol(n)

if __name__=='__main__':
    n = int(input("Enter the number: "))
    print(fun(n))
