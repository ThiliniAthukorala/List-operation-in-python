#X = int(input("Enter a integer number")) 

#Y = X*4 + 14

#if Y>50:
    #Z=Y+4
    
#else :
    #Z=Y*2
    
#print(Z)

#List

list_1=[1,2,3,4]
print(list_1)

List_2=['a','c','d']
List_3=['apple','orange',12, 4.5,"hello",3,101,'f']
print(List_3)

print(List_3[2])
print(List_3[0:3])
print(List_3[2:5])

List_3.append("thilini")
print(List_3)

List_3[1]='v'
print(List_3)

List_3.remove(4.5)
del List_3[4]
print(List_3)

print(List_3[4:])

List_4=[[1,3,2],[1,1,3],[4,7,0]]
print(List_4)

print(List_4[2][1])

List_4[1][0]=100
print(List_4)

List_4[1].append('a')
print(List_4)
del List_4[2][2]
print(List_4)

print(len(List_4))

a=[1,2,3]
b=[4,5.7,7]
print(a+b)

print(['hi']*4)
print(['hi','s']*4)

print(3 in a)

for x in List_4:
    print(x)

L=[3,4,6,8,1,0,2]

my_list = [2, 4, 1, 5, 6]   
even_numbers = [num for num in my_list if num % 2 == 0]
print("Even numbers in the list:", even_numbers)

for x in L:
    print(x)
    print("**********")
    a=x%2    
        if a==0:
            print(a)
        
   