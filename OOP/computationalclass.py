class Computational:

    def __init__(self):
        pass

    def Factorial(self,n):
        product=1
        for i in range(1,n+1):
            product=product*i
        print('the factorial of',n,'is',product)

    def naturalsum(self,n):
        sum=(n*(n+1))//2
        print('the sum of',n,'is',sum)

    def testprime(self,n):
        flag = True
        for i in range(2,n):
            if n%i==0:
                flag = False
        if flag == True:
            print('the integer is prime')
        else:
            print('the integer is not prime')

    def testprims(self,n1,n2):
        for i in range(min(n1,n2),0,-1):
            if n1%i==0 and n2%i==0:
                if i==1:
                  print('it is co-prime')
                else:
                  print('it is not co-prime')
                break

    def tableMult(self,n):
        for i in range(1,11):
            print(n*i)
        print()

    def listDiv(self,n):
        L=[]
        for i in range(1,n+1):
            if n%i==0:
                L.append(i)
        print(L)

    def listprimeDiv(self,n):
        L=[]
        M=[]
        for i in range(1,n+1):
            if n%i==0:
                L.append(i)

        for j in L:
            if j>1:
             flag = True
             for k in range(2,j):
                if j%k==0:
                 flag = False
                 break
             if flag:
               M.append(j)
        print(M)
                    


test1 = Computational()
test1.listprimeDiv(9)