#Question 1
def Towerofhanoi(n , from_rod, to_rod, middle_rod):
	if n == 0:
		return
	Towerofhanoi(n-1, from_rod, middle_rod, to_rod)
	print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
	Towerofhanoi(n-1, middle_rod, to_rod, from_rod)
n = 3
Towerofhanoi(n, 'A', 'C', 'B')   
print("")



#Question 2
from math import factorial, remainder 
from tracemalloc import start
n=int(input('Enter a value for pascal triangle : ')) 

print("By Loops")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ") 

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!) , this is the formula.
	print()	
print("\n\n")

print("By Reccursions")

def Pascal_Triangle(n,originalength=n):
    if n == 0:
        return
    Pascal_Triangle(n-1,originalength)
    
    print('  '*(originalength-n), end='')

    
    start = 1  
    for i in range(1, n+1):

        print(start, end ='   ')
        
        start = start * (n - i) // i 
    print()
Pascal_Triangle(n)
print("\n")



#Question 3
int1, int2 = map(int,input("Enter 2 numbers: ").split())
Quotient = int1 // int2 
Remainder = int1 % int2

#A)
print(callable(Quotient)) 
print(callable(Remainder))

#B)
if (Quotient == 0):
    print("The quotient value is zero")
if (Remainder == 0):
    print("The reminder value is zero")
if (Quotient != 0 and Remainder != 0):
    print("All the values are non zero")

#C)
Required_list = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(Required_list)):
    if Required_list[i] > 4:
        result.append(Required_list[i])
print(f"Filtered out numbers that are greater than 4 are : {result}")

#D)
setresult = set(result)
print("Set:",setresult)

#E)
immutableSet = frozenset(setresult) 
print("Immutable set:",immutableSet)

#F)
print("Hash value of the max value from the above set:", hash(max(immutableSet)))
print("")



#Question 4
class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object destroyed")

student_Required = Student("SANCHITA GOEL", 21103011) 
print("Object has been created")

print(f"The name of the student is {student_Required.name} and SID is {student_Required.roll_no}.")
del student_Required 
print("")



#Question 5
class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
#Record of employees.         
employee1 = Employees("Mehak", 40000)
employee2 = Employees("Ashok", 50000)
employee3 = Employees("Viren", 60000)

#A)
employee1.salary = 70000
print(f"The Updated Salary Of {employee1.name} is going to be {employee1.salary} ")

#B)
print("Record Of Viren Has been deleted.", end='')
del employee3
print("")



#Question 6
word1 = input("Enter The Word Please: ")
word1 = word1.lower() 
word2 = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
word2 = word2.lower()
def count_in_dict(word):
    count = {}
    Required_list = list(word)
    
    n = len(Required_list) 
    for i in range(n):
        if Required_list[i] in count:
            count[Required_list[i]] += 1 
        else:
            count[Required_list[i]] = 1
    return count

def userinput():
    if count_in_dict(word1) != count_in_dict(word2):
        print("Your words did not match , Your friendship is fake.")
        return
    answer = input("Does The Word Makes Any Sense?(Y/y Or N/n) ")
    if answer == 'y' or answer=='Y':
        print("You both have passed the friendship test.")
    elif answer == 'n' or answer=='N':
        print("This is a meanningless word , your friendship is fake")
    else:
        print("Please Try again! , your input word is wrong")
        userinput()
userinput()






