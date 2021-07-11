m = int(input("Enter the number of equation : "))
n = int(input("Enter the number of variable : "))
n = n+1

li = [[0 for i in range(n)]for j in range(m)]


for i in range(m):
    for j in range(n):
        #enter only coeficients
        li[i][j] = float(input("Enter the value of a({}{}) : ".format(i+1,j+1) if j != n-1 else "Enter the value of b({}) : ".format(i+1)))
        

print("\n\n\n\n You have entered this matrix : \n" + "-"*32)

#print the array
for i in range(m):
    for j in range(n):
        print("{}".format(round(li[i][j],2)) if j != n-2 else "{}\t=".format(round(li[i][j],2)) , end="\t")
    print("")
    
    
for k in range(m-1):      
    for i in range(k+1,m):
        temp = li[i][k]
        for j in range(k,n):
            
            li[i][j] = li[i][j] - (( temp * li[k][j]) / li[k][k]) 
        



    print("\n\n\n\n after elemination the {}th variable we have : \n".format(k+1) + "-"*48)
    
    
    #print the array
    for i in range(m):
        for j in range(n):
            print("{}".format(round(li[i][j],2)) if j != n-2 else "{}\t=".format(round(li[i][j],2)) , end="\t")
        print("")
        