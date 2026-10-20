n=int(input("enter the total marks of the subject"))
a=int(input("enter the marks of maths"))
b=int(input("enter the marks of physics"))
c=int(input("enter the marks of chemestry"))
d=int(input("enter the marks of english"))
e=int(input("enter the marks of biology"))
avg=((a+b+c+d+e)/5)
percentage=((avg/n)*100)
print("the total percentage is" ,((avg/n)*100))
if(percentage>=75):
 print("distinction class")
elif (percentage>=65):
 print("first class")
elif("percentage>=40"):
 print("second class")
else:
 print("student is failed")