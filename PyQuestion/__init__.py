import random #importing random module 

lst=["""Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints: 
Consider use range(#begin, #end) method""",""""Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.""",""""With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()""",""""Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple""",""""Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
Hints:
Use __init__ method to construct some parameters""",""""Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. 
""",""""Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.
""",""""Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.""",""""Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
""",""""Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.""",""""Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
""",""""Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.""",""""Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.""",""""Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.""",""""Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.""",""""Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
""",""""Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.""",""""A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
""",""""You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use itemgetter to enable multiple sort keys.
""",""""Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
Hints:
Consider use yield""",""""A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.""",""""Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
Hints
In case of input data being supplied to the question, it should be assumed to be a console input.""",""""Question:
    Write a method which can calculate square value of number
Hints:
    Using the ** operator""","""" Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function
    
Hints:
    The built-in document method is __doc__""",""""Question:
    Define a class, which have a class parameter and have a same instance parameter.
Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later""",""""Define a function which can compute the sum of two numbers.
Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.""",""""Define a function that can convert a integer into a string and print it in console.
Hints:
Use str() to convert a number to string.""",""""Define a function that can convert a integer into a string and print it in console.
Hints:
Use str() to convert a number to string.""",""""Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
Hints:
Use int() to convert a string to integer.""",""""Define a function that can accept two strings as input and concatenate them and then print it in console.
Hints:
Use + to concatenate the strings""",""""Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.
Hints:
Use len() function to get the length of a string""",""""Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
Hints:
Use % operator to check if a number is even or odd.""",""""Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.""",""""Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.""",""""Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.""",""""Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.""",""""Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
""","""Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list""",""""Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list""",""""Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list""",""""Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list
""",""""Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included). 
Hints:
Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use tuple() to get a tuple from a list.""",""""With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 
Hints:
Use [n1:n2] notation to get a slice from a tuple.""",""""Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
Hints:
Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.""",""""Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
Hints:
Use if statement to judge condition.
""",""""Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
Hints:
Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.""",""""Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
Hints:
Use map() to generate a list.
Use lambda to define anonymous functions.""",""""Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
Hints:
Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.""",""""Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
Hints:
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.""","""Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
Hints:
Use map() to generate a list.
Use lambda to define anonymous functions.
""",""""Define a class named American which has a static method called printNationality.
Hints:
Use @staticmethod decorator to define class static method.""",""""Define a class named American and its subclass NewYorker. 
Hints:
Use class Subclass(ParentClass) to define a subclass.""",""""Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 
Hints:
Use def methodName(self) to define a method.""",""""Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 
Hints:
Use def methodName(self) to define a method.
""",""""Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
Hints:
To override a method in super class, we can define a method with the same name in the super class.
""",""""Write a function to compute 5/0 and use try/except to catch the exceptions.
Hints:
Use try/except to catch exceptions.""",""""Define a custom exception class which takes a string message as attribute.
Hints:
To define a custom exception, we need to define a class inherited from Exception.""","""Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints:
Use \w to match letters.""",""""Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
google
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints:
Use \w to match letters.""","""Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
Example:
If the following words is given as input to the program:
2 cats and 3 dogs.
Then, the output of the program should be:
['2', '3']
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints:
Use re.findall() to find all substring using regex.""","""Print a unicode string "hello world".
Hints:
Use u'strings' format to define unicode string.
""","""Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
Hints:
Use unicode() function to convert.""","""Write a special comment to indicate a Python source code file is in unicode.
""","""Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints:
Use float() to convert an integer to a float
""","""Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1
with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
500
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints:
We can define recursive function in Python.""","""The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
13
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints:
We can define recursive function in Python.
""","""The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13
Hints:
We can define recursive function in Python.
Use list comprehension to generate a list from an existing list.
Use string.join() to join a list of strings.
In case of input data being supplied to the question, it should be assumed to be a console input.
""","""Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
Hints:
Use yield to produce the next value in generator.
In case of input data being supplied to the question, it should be assumed to be a console input.
""","""Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
Hints:
Use yield to produce the next value in generator.
In case of input data being supplied to the question, it should be assumed to be a console input.
""","""Please write assert statements to verify that every number in the list [2,4,6,8] is even.
Hints:
Use "assert expression" to make assertion.
""","""Please write a program which accepts basic mathematic expression from console and print the evaluation result.
Example:
If the following string is given as input to the program:
35+3
Then, the output of the program should be:
38
Hints:
Use eval() to evaluate an expression.""","""Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
Hints:
Use if/elif to deal with conditions.
""","""Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
Hints:
Use if/elif to deal with conditions.
""","""Please generate a random float where the value is between 10 and 100 using Python math module.
Hints:
Use random.random() to generate a random float in [0,1].
""","""Please generate a random float where the value is between 5 and 95 using Python math module.
Hints:
Use random.random() to generate a random float in [0,1].
""","""Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
Hints:
Use random.choice() to a random element from a list.
""","""Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.
Hints:
Use random.choice() to a random element from a list.""","""Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
Hints:
Use random.sample() to generate a list of random values.""","""Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
Hints:
Use random.sample() to generate a list of random values.""","""Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
Hints:
Use random.sample() to generate a list of random values.""","""Please write a program to randomly print a integer number between 7 and 15 inclusive.
Hints:
Use random.randrange() to a random integer in a given range.""","""Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
""","""Please write a program to print the running time of execution of "1+1" for 100 times.
Hints:
Use timeit() function to measure the running time.""","""Please write a program to shuffle and print the list [3,6,7,8].
Hints:
Use shuffle() function to shuffle a list.""","""Please write a program to shuffle and print the list [3,6,7,8].
Hints:
Use shuffle() function to shuffle a list.""","""Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
Hints:
Use list[index] notation to get a element from a list.""","""Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
Hints:
Use list comprehension to delete a bunch of element from a list.""","""By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
Hints:
Use list comprehension to delete a bunch of element from a list.
""","""By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.
""","""By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
Hints:
Use list comprehension to make an array.""","""By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.""","""By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
Hints:
Use list's remove method to delete a value.""","""With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
Hints:
Use set() and "&=" to do set intersection operation.""","""With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
Hints:
Use set() to store a number of values without duplicate.""","""Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
Hints:
Use Subclass(Parentclass) to define a child class.
""","""Please write a program which count and print the numbers of each character in a string input by console.
Example:
If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.
""","""Please write a program which accepts a string from console and print it in reverse order.
Example:
If the following string is given as input to the program:
rise to vote sir
Then, the output of the program should be:
ris etov ot esir
Hints:
Use list[::-1] to iterate a list in a reverse order.
""","""Please write a program which accepts a string from console and print the characters that have even indexes.
Example:
If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
Helloworld
Hints:
Use list[::2] to iterate a list by step 2.""","""Please write a program which prints all permutations of [1,2,3]
Hints:
Use itertools.permutations() to get permutations of list.""","""Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
Hint:
Use for loop to iterate all possible solutions.""","""You are given a positive integer .
Your task is to print a palindromic triangle of size .
For example, a palindromic triangle of size  is:
1
121
12321
1234321
123454321
You can't take more than two lines. The first line (a for-statement) is already written for you.
You have to complete the code using exactly one print statement.
Note:
Using anything related to strings will give a score of .
Using more than one for-statement will give a score of .
Input Format
A single line of input containing the integer N""","""You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format
A single line containing a string S.""","""In Python, a string can be split on a delimiter.
Example:
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
Joining a string is simple:
>>> a = "-".join(a)
>>> print a
this-is-a-string 
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
Input Format
The first line contains a string consisting of space separated words.""","""You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
Input Format
A single line containing a string S.""","""You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------""","""You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.
Input Format
A single line of input containing a string of Roman characters.""","""$ When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
  Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
  Day dd Mon yyyy hh:mm:ss +xxxx
  Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
  Input Format
  The first line contains T , the number of testcases.
  Each testcase contains 2 lines, representing time t1 and time t2 .
""",""" There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i∈A, you add 1 to your happiness. If i∈B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
  Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.
  
  Input Format
  The first line contains integers n and m separated by a space.
  The second line contains n integers, the elements of the array.
  The third and fourth lines contain m integers, A and B, respectively.
  Output Format
  Output a single integer, your total happiness.
""","""You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c) in the string.
  For a better understanding of the problem, check the explanation.
  Input Format
  A single line of input consisting of the string .
  Output Format
  A single line of output consisting of the modified string.
""","""A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
  Print the three most common characters along with their occurrence count.
  Sort in descending order of occurrence count.
  If the occurrence count is the same, sort the characters in alphabetical order.
  For example, according to the conditions described above,
  GOOGLE would have it's logo with the letters G,O,E.
  Input Format
  A single line of input containing the string S.
  Output Format
  Print the three most common characters along with their occurrence count each on a separate line.
  Sort output in descending order of occurrence count.
  If the occurrence count is the same, sort the characters in alphabetical order.
""","""The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools
  succinctly and efficiently in pure Python.
  To read more about the functions in this module, check out their documentation here.
  You are given a list N of lowercase English letters. For a given integer K, you can select any K indices
  (assume 1-based indexing) with a uniform probability from the list.
  Find the probability that at least one of the K indices selected will contain the letter: 'a'.
  Input Format
  The input consists of three lines. The first line contains the integer N, denoting the length of the list. The next line consists of N space-separated lowercase English letters, denoting the elements of the list.
  The third and the last line of input contains the integer K, denoting the number of indices to be selected.
"""]
def getQuestion():
    #return a problem statement from list
    x=random.randint(0,len(lst)) #using random module to get random number 
    if(lst[x][0]=='"'):
        return lst[x][1:]
    return lst[x] # returns a random index problem from list