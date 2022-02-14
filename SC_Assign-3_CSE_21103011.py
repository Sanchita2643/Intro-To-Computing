#Ques1

string1=input("Give a string-")
list1=[]
list2=string1.split()
y=len(list2)
d=dict()
t=dict()
if len(list2)==1:          
    for i in string1:      
        list1.append(i) 
    for j in list1:        
        if j in d:         
            d[j]=d[j]+1    
        else:
            d[j]=1
    print(d)        

else:
    for i in list2:        
        if i in t:
            t[i]=t[i]+1
        else:
            t[i]=1
    print(t)

    
#Ques 2

month=int(input("Give month-"))


if(month in[1,3,5,7,8,10,12]):
    day=int(input("Give day-"))
    if(1<=day<=31):
        year=int(input("Give year-"))
        if(1800<=year<=2025):
            print("Date-",day,"/",month,"/",year)
            if(month==12 and day==31):
                print("Next Date-","1/1/",year+1)
            elif(day==31):
                print("Next Date-","1/",month+1,"/",year)
            else:
                print("Next Date-",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date")
elif(month in[4,6,9,11]):
    day=int(input("Give day-"))
    if(1<=day<=30):
        year=int(input("Give year-"))
        if(1800<=year<=2025):
            print("Date-",day,"/",month,"/",year)
            if(day==30):
                print("Next Date-","1/",month+1,"/",year)
            else:
                print("Next Date-",day+1,"/",month,"/",year)
        else:
            print("invalid year")
    else:
         print("invalid date")
elif(month==2):
    year=int(input("Give year-"))
    if(1800<=year<=2025):
        day=int(input("Give day-"))
        if(year%4==0):
            if(1<=day<=29):
                print("Date-",day,"/",month,"/",year)
                if(day==29):
                    print("Next Date-","1/",month+1,"/",year)
                else:
                    print("Next Date-",day+1,"/",month,"/",year)              
            else:
                print("invalid day")
        else:
            if(1<=day<=28):
                print("Date-",day,"/",month,"/",year)
                if(day==28):
                    print("Next Date-","1/",month+1,"/",year)
                else:
                    print("Next Date-",day+1,"/",month,"/",year)       
            else:
                print("invalid day")     
    else:
        print("invalid year")
else:
    print("invalid month")


    
#Ques 3

alist=[1,2,3,4,5,6,7,8,9,10]
list_with_tuples=[]
for i in alist:
    list_with_tuples.append((i,i**2))
print(list_with_tuples)



#Ques 4


#if else statements

Grade_points=int(input("Give a number between 4 and 10 including them-"))
if(Grade_points==4):
    print("Performance=Poor")
    print("Letter Grade=D")
elif(Grade_points==5):
    print("Performance=Below Average")
    print("Letter Grade=C")
elif(Grade_points==6):
    print("Performance=Average")
    print("Letter Grade=C+")
elif(Grade_points==7):
    print("Performance=Good")
    print("Letter Grade=B")
elif(Grade_points==8):
    print("Performance=Very Good")
    print("Letter Grade=B+")
elif(Grade_points==9):
    print("Performance=Excellent")
    print("Letter Grade=A")
elif(Grade_points==10):
    print("Performance==Outstanding")
    print("Letter Grade=A+")
else:
    print("error")



#Ques 5

Word="ABCDEFGHIJK"

counter=1

while(counter<7):
    print(" "*(counter-1),Word[0:11-((counter-1)*2)])
    counter=counter+1


#Ques 6

student_info=dict()
n="y"
alistsid=[]

#(a)
print("----------------(a)-------------------")
while(n=="y"):
    sid=int(input("Give the sid (a number):"))
    name=input("Enter your name:")
    student_info[sid]=name
    n=input("give a letter y or n:")
    alistsid.append((sid,name))
print("The required dictionary--",student_info)
print("The list will be used in further parts--")
print("The required list--",alistsid)


#(b)
print("----------------(b)------------------------")
print("The dictionary we had-")
print(student_info)

newdict=dict()
alistname=[]

for (k,v) in student_info.items():
    newdict[v]=k
    alistname.append((v,k))
print("now we have exchanged the key value pair but its not sorted-")

print(newdict)
print("The unsorted list--")
print(alistname)
alistname.sort()

print("The sorted list--")
print(alistname)

print("The sorted dictionary-")
sorted_dict=dict(alistname)
print(sorted_dict)


required_dict_name=dict()
for (k,v) in sorted_dict.items():
    required_dict_name[v]=k
print("This is the dictionary sorted on the basis of name-")
print(required_dict_name)


#(c)
print("-----------------(c)-----------------")
print("The list we made before will be used now-")
print(alistsid)
alistsid.sort()
print("now the list is sorted-")
print(alistsid)
sorted_student_info_sid=dict(alistsid)
print("sorted dictionary based on sid-",sorted_student_info_sid)


#(d)
print("-----------------(d)-----------------")    
entered_sid=int(input("Please enter one of the sids you entered before-"))
print("The name of the student with the entered sid is-")    
print(student_info[entered_sid])


#Ques 7

#fibonacci sequence
first_term=int(input("Give a number-"))
second_term=int(input("Give a number-"))

sum=first_term+second_term
series=[first_term,second_term]
n="y"
while(n=="y"):
    series.append(series[len(series)-1]+series[len(series)-2])
    print(series)
    n=input("Give y to contnue and n to stop going further-")
print("Now we got a list having a fibonacci series-")
print(series)


sum=0
for i in series:
    sum=sum+i
print("Average of the sequence-")
print(sum/len(series))


#Ques 8

Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

#(a)
print("-------------(a)------------")
required_Set=Set1^Set2
print(required_Set)

#(b)
print("-------------(b)------------")
required_Set=Set1^(Set2^Set3)
print(required_Set)


#(c)
print("-------------(c)------------")
required_Set=(Set1&Set2)|(Set2&Set3)|(Set1&Set3)
print(required_Set)


#(d)
print("-------------(d)------------")
new_Set={1,2,3,4,5,6,7,8,9,10}
required_Set=new_Set-Set1
print(required_Set)


#(e)
print("-------------(e)------------")
required_Set=new_Set-(Set1|Set2|Set3)
print(required_Set)




