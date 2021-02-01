list1=[]
list2=[]

l=int(input("Enter the length of the list\n"))

i=0

while i<l:
     list1.append(int(input("Enter the elements of the list\n")))
     i+=1



for n in list1:
     if(n>0):
          list2.append(n)


print("Output:",list2)
          
