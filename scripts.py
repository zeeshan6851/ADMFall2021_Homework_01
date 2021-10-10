# Say Hellow World with python
print("Hello, World!")

#Python If-Else
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    else :
        if(n>=2 and n<=5):
            print("Not Weird")
        elif(n>=6 and n<=20):
            print("Weird")
        elif(n>20):
            print("Not Weird")
            
#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    add = a + b
    diff = a - b
    mul = a * b
    print (add)
    print (diff)
    print (mul)

#Python:Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    floordiv = a // b
    div = a / b
    print(floordiv)
    print(div)
    
#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)
    
#Write a Function
def is_leap(year):
    leap = False
    
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap=True
            else:
                leap=False
        else:
             leap=True
    else:
        leap=False
    
    return leap

#Print Function
if __name__ == '__main__':
    n = int(input())
    for j in range(n):
        print(j+1,end="")

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k==n:
                    continue
                else:
                    output.append([i,j,k])
    
    print(output)

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])

#Nested Lists
if __name__ == '__main__':
    score_list = [];
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append([name, score])
second_highest = sorted(set([score for name, score in score_list]))[1]
print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))

#Find the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        x = ((float(student_marks[query_name][0]) + float(student_marks[query_name][1]) + float(student_marks[query_name][2])) / 3)
    
    print('%.2f' % x)

#Lists
if __name__ == '__main__':
    N = int(input())
    # Lists in Python - Hacker Rank Solution START
    Output = [];
    for i in range(0,N):
        ip = input().split();
        if ip[0] == "print":
            print(Output)
        elif ip[0] == "insert":
            Output.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            Output.remove(int(ip[1]))
        elif ip[0] == "pop":
            Output.pop();
        elif ip[0] == "append":
            Output.append(int(ip[1]))
        elif ip[0] == "sort":
            Output.sort();
        else:
            Output.reverse();

#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t=tuple(integer_list)
print(hash(t))

#Swap Case
def swap_case(s):
    return s.swapcase()

#String Split and Join
def split_and_join(line):
    a = line.split(" ")
    a = "-".join(a)
    return a

#What's your name

def print_full_name(a, b):
    b = b+"!"
    print("Hello",a, b,"You just delved into python.");
    
#Mutations
def mutate_string(string, position, character):
    lis=list(string)
    lis[position]=character
    return ''.join(lis)

#Find a String
def count_substring(string, sub_string):
    count=0
    for i in range(0, len(string)-len(sub_string)+1):
        if string[i] == sub_string[0]:
            flag=1
            for j in range (0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag=0
                    break
            if flag==1:
                count += 1
    return count

#String Validators
if __name__ == '__main__':
    s = input()
    res = ["False", "False", "False", "False", "False"]
    for i in s:
        if i.isalnum():
            res[0] = "True"
        if i.isalpha():
            res[1] = "True"
        if i.isdigit():
            res[2] = "True"
        if i.islower():
            res[3] = "True"
        if i.isupper():
            res[4] = "True"
    print(*res, sep="\n")

#Text Alignment

thickness = int(input()) 
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


#Text Wrap


def wrap(string, max_width):
    return textwrap.fill(string,max_width)

#Designer Door mat
N, M = map(int, input().split())
for i in range(1, N, 2):
    print(str('.|.' * i).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N-2, -1, -2):
    print(str('.|.' * i).center(M, '-'))
    
#String Formatting
def print_formatted(number):
    l1 = len(bin(number)[2:])
   
    for i in range(1,number+1):
        print(str(i).rjust(l1,' '),end=" ")
        print(oct(i)[2:].rjust(l1,' '),end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1,' '),end=" ")
        print(bin(i)[2:].rjust(l1,' '),end=" ")
        print("")


#Alphabet Rangoli
def print_rangoli(size):
    # your code goes here
    width  = size*4-3
    string = ''

    for i in range(1,size+1):
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
        for k in range(i-1,0,-1):    
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
        print(string.center(width,'-'))
        string = ''

    for i in range(size-1,0,-1):
        string = ''
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < width :
                string += '-'
        for k in range(i-1,0,-1):
            string += chr(97+size-k)
            if len(string) < width :
                string += '-'
        print(string.center(width,'-'))


#Capitalize


# Complete the solve function below.
def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s

#The Minion game
def minion_game(string):
    vowels = 'AEIOU'
    str_lenght = len(string)
    kevin_score, stuart_score = 0, 0

    for i in range(str_lenght):
        if s[i] in vowels:
            kevin_score += (str_lenght - i)
        else:
            stuart_score += (str_lenght - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


#Merge The Tools
from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    strlen = len(string)
    for i in range(0,strlen,k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))

#Introduction to sets
def average(array):
    # your code goes here
    sum_array = sum(set(array))
    len_array = len(set(array))
    output = sum_array/len_array
    return output;

#No Idea
# Enter your code here. Read input from STDIN. Print output to STDOUT
io = input().split()
m = int(io[0])
n = int(io[1])

storage = list()
count = 0

storage = list(map(int, input().strip().split()))

A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

for i in storage:
    if i in A:
        count = count+1
    if i in B:
        count = count-1

print(count)

#Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
mset = set(map(int, input().split()))
N = int(input())
nset = set(map(int, input().split()))

mdef = mset.difference(nset)
ndef = nset.difference(mset)

output = mdef.union(ndef)

for i in sorted(list(output)):
    print(i)

#Set.add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

countries = set()

for i in range(N):
    countries.add(input())

print(len(countries))

#Set.Discard, Remove and Pop
n = int(input())
s = set(map(int,input().split()))
num = int(input())
for i in range(num):
    ip = input().split()
    if ip[0]=="remove":
        s.remove(int(ip[1]))
    elif ip[0]=="discard":
        s.discard(int(ip[1]))
    else :
        s.pop()
print(sum(list(s)))

#Set.union()
# Enter your code here. Read input from STDIN. Print output to STDOUT
N1 = int(input())
storage1 = set(input().split());

N2 = int(input())
storage2 = set(input().split());

storage3 = storage1.union(storage2)

print(len(storage3))

#Set.Intersection()
# Enter your code here. Read input from STDIN. Print output to STDOUT
N1 = int(input())
storage1 = set(input().split())

N2 = int(input())
storage2 = set(input().split())

storage3 = storage2.intersection(storage1)

print(len(storage3))

#Set.difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
N1 = int(input())
storage1 = set(input().split())

N2 = int(input())
storage2 = set(input().split())

storage3 = storage1.difference(storage2)

print(len(storage3))

#Set.symmetric_difference operation
e = int(input())
eng = set(map(int,input().split())) 
f = int(input())
fre = set(map(int,input().split()))
print(len(eng ^ fre))

#Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
len_set = int(input())

storage = set(map(int, input().split()))

op_len = int(input())

for i in range(op_len):
    operation = input().split()
    if operation[0] == 'intersection_update':
        temp_storage = set(map(int, input().split()))
        storage.intersection_update(temp_storage)
    elif operation[0] == 'update':
        temp_storage = set(map(int, input().split()))
        storage.update(temp_storage)
    elif operation[0] == 'symmetric_difference_update':
        temp_storage = set(map(int, input().split()))
        storage.symmetric_difference_update(temp_storage)
    elif operation[0] == 'difference_update':
        temp_storage = set(map(int, input().split()))
        storage.difference_update(temp_storage)
    else :
        assert False

print(sum(storage))

#The Captions Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

storage = map(int, input().split())
storage = sorted(storage)

for i in range(len(storage)):
    if(i != len(storage)-1):
        if(storage[i]!=storage[i-1] and storage[i]!=storage[i+1]):
            print(storage[i])
            break;
    else:
        print(storage[i])

 #Check Subset
 # Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for _ in range(T):
    a = input()
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    print(A.issubset(B))

#Check Strict Super Set
# Enter your code here. Read input from STDIN. Print output to STDOUT
storage = set(input().split())
N = int(input())
output = True

for i in range(N):
    storage2 = set(input().split())
    if not storage2.issubset(storage):
        output = False
    if len(storage2) >= len(storage):
        output = False

print(output)

#Collections.counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = input()
S = Counter(map(int,input().split()))
n = input()
N = int(n) 
earnings = 0
for customer in range(N):
    size, x_i = map(int,input().split())
    if size in S and S[size] > 0:
        S[size] -= 1
        earnings += x_i
            
print(earnings)

#DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int,input().split())

a = defaultdict(list)
for i in range(1, n + 1):
    a[input()].append(i)

for i in range(1, m + 1):
    key = input()
    if len(a[key]) > 0:
        print(" ".join(str(c) for c in a[key]))
    else:
        print(-1)

#Collections.namedtouple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
N, headers, total = int(input()), list(input().split()), 0
for _ in range(N):
    total += int(list(input().split())[headers.index('MARKS')])
print(total/N)

#Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import*;
N = int(input());
d = OrderedDict();
for i in range(N):
    item = input().split()
    itemPrice = int(item[-1])
    itemName = " ".join(item[:-1])
    if(d.get(itemName)):
        d[itemName] += itemPrice
    else:
        d[itemName] = itemPrice
for i in d.keys():
    print(i, d[i])

#Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
n_ish = int(input())
counter_dict = {}
words_list = []

for i in range(n_ish):
  word = input()
  words_list.append(word)
  if word in counter_dict:
    counter_dict[word] += 1
  else:
    counter_dict[word] = 1
    
print(len(counter_dict))
print(' '.join([str(counter_dict[word]) for word in counter_dict]))

#Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
d = deque()
for _ in range(n):
    lst = list(input().split())
    if lst[0]=='append':
        d.append(int(lst[1]))
    elif lst[0]=='appendleft':
        d.appendleft(int(lst[1]))
    elif lst[0]=='popleft':
        d.popleft()
    elif lst[0]=='pop':
        d.pop()
for i in d:
    print(i,end=" ")
                    
#Company Logo
import math
import os
import random
import re
import sys
import collections

if __name__ == '__main__':
    s = sorted(input().strip())
    s_counter = collections.Counter(s).most_common()
    s_counter = sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))
    for i in range(0, 3):
        print(s_counter[i][0], s_counter[i][1])

#Pilling Up
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def test_cubes(cubes):
    t_cube = 0
    
    if cubes[0] > cubes[len(cubes)-1]:
        t_cube = cubes[0]
        cubes.pop(0)
    else:
        t_cube = cubes[len(cubes)-1]
        cubes.pop(len(cubes)-1)
    
    while len(cubes) > 0:
        if t_cube == cubes[0]:
            t_cube = cubes.pop(0)
        elif t_cube == cubes[len(cubes)-1]:
            t_cube = cubes.pop(len(cubes)-1)
        elif (cubes[0] > cubes[len(cubes)-1]) and (t_cube >= cubes[0]):
            t_cube = cubes.pop(0)
        elif (cubes[0] < cubes[len(cubes)-1]) and (t_cube >= cubes[len(cubes)-1]):
            t_cube = cubes.pop(len(cubes)-1)
        elif (cubes[0] == cubes[len(cubes)-1]):
            t_cube = cubes.pop(0)
        else:
            return "No"
    return "Yes"

num_of_tests = sys.stdin.readline().strip()
num_of_tests = int(num_of_tests)

for i in range(0, num_of_tests):
    sys.stdin.readline()
    cubes = list(map(int, sys.stdin.readline().strip().split(' ')))
    print(test_cubes(cubes))
                    
#Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
m,d,y = map(int,input().split())
days = {0:'MONDAY',1:'TUESDAY',2:'WEDNESDAY',3:'THURSDAY',4:'FRIDAY',5:'SATURDAY',6:'SUNDAY'}
print(days[calendar.weekday(y,m,d)])

#Time_Delta
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
from datetime import datetime
def time_delta(t1, t2):
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((t1-t2).total_seconds())))
# Time Delta in Python - Hacker Rank Solution END

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

#Exceptions
x = int(input());
for i in range(x):
    try:
        a, b = input().split()
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e);
    except ValueError as v:
        print("Error Code:",v);

#Zipped
# Enter your code here. Read input from STDIN. Print output to STDOUT
N, X = input().split()

io = list()

for _ in range(int(X)):
    ip = map(float, input().split())
    io.append(ip)

for i in zip(*io): 
    print( sum(i)/len(i) )

#Athlete Sort
#!/bin/python3

import math
import os
import random
import re
import sys



N, M = map(int, input().split())
rows = [input() for _ in range(N)]
K = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)

#ginorts
def sort_String(s):
    lower_case = []
    upper_case = []
    odd_digits = []
    even_digits = []
    for char in s:
        if char.islower():
            lower_case.append(char)
        elif char.isupper():
            upper_case.append(char)
        elif char.isdigit():
            if int(char)%2==0:
                even_digits.append(char)
            else:
                odd_digits.append(char)
    return (''.join(sorted(lower_case)+sorted(upper_case)+sorted(odd_digits)+sorted(even_digits)))
    
if __name__=='__main__':
    
    S = input()
    print (sort_String(S))

#Map and Lambda Function
cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    storage = [0, 1]
    for i in range(2, n):
        storage.append(storage[i-1] + storage[i-2])
    return(storage[0:n])
   
    
#Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

class Main():
    def __init__(self):
        self.n = int(input())
        
        for i in range(self.n):
            self.s = input()
            print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.s)))
                    
if __name__ == '__main__':
    obj = Main()

#Re. Split()
regex_pattern = r"[,.]" # Do not delete 'r'.

#Group, Groups and GroupDict
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

expression=r"([a-zA-Z0-9])\1+"

m = re.search(expression,input())

if m:
    print(m.group(1))
else:
    print(-1)

#Refindall,Refinditer
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

Storage = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)

if Storage:
    for i in Storage:
        print(i)
else:
    print(-1)
    
#Restart and Re end
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S, k = input(), input()
matches = re.finditer(r'(?=(' + k + '))', S)

anymatch = False
for match in matches:
    anymatch = True
    print((match.start(1), match.end(1) - 1))

if anymatch == False:
    print((-1, -1))

#Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def change(match):
    if match.group(1) == '&&':
        return 'and'
    else:
        return 'or'

for _ in range(int(input())):
    print(re.sub(r"(?<= )(\|\||&&)(?= )", change,input()))

#Validating Roman Numerals
thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'
regex_pattern = r"%s%s%s%s$" % (thousand, hundred, ten, digit)    

#Validating Phone Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

for i in range(N):
    number = input()
    if(len(number)==10 and number.isdigit()):
        output = re.findall(r"^[789]\d{9}$",number)
        if(len(output)==1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

#Validating and Parsing Email Address
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

for i in range(N):
    name, email = input().split()
    pattern="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(pattern, email)):
        print(name,email)

#Hex Color Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input())
in_css = False
for _ in range(T):
    s = input()
    if '{' in s:
        in_css = True
    elif '}' in s:
        in_css = False
    elif in_css:
        for color in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(color)

#HTML Parser Part 01
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ('Start :', tag)
        for ele in attrs:
            print ('->', ele[0], '>', ele[1])

    def handle_endtag(self, tag):
        print ('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print ('Empty :', tag)
        for ele in attrs:
            print ('->', ele[0], '>', ele[1])


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())

#HTML Parser Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' not in data:
            print('>>> Single-line Comment')
            print(data)
        elif '\n' in data:
            print('>>> Multi-line Comment')
            print(data)
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Detect HTML Tages, Attributes and Attribute Values
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print("->", attr, ">", value)

html = ''
for _ in range(int(input())):
    html += input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for i in range(int(input())):
    N = input().strip()
    if N.isalnum() and len(N) == 10:
        if bool(re.search(r'(.*[A-Z]){2,}',N)) and bool(re.search(r'(.*[0-9]){3,}',N)):
            if re.search(r'.*(.).*\1+.*',N):
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')

#Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    S = input().strip()
    pre_match = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',S)
    if pre_match:
        processed_string = "".join(pre_match.group(0).split('-'))
        final_match = re.search(r'(\d)\1{3,}',processed_string)
        if final_match:
            print('Invalid')
        else :
            print('Valid')
    else:
        print('Invalid')

#Validating Postal Codes
regex_integer_in_range = r'^[1-9][\d]{5}$'  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'  # Do not delete 'r'.

#Matrix Script
#!/bin/python3

import math
import os
import random
import re
import sys



first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# start   
matrix = list(zip(*matrix))

sample = str()

for words in matrix:
    for char in words:
        sample += char
       
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', sample))

#XML1-Find the score

def get_attr_number(node):
    return len(node.attrib) + sum(get_attr_number(child) for child in node);

#XML2 - Find the maximum depth


maxdepth = 0
def depth(elem, level):
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1

    for child in elem:
        depth(child, level + 1)
        
#Standardize mobile number using decorators
def wrapper(f):
    def fun(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return fun

#Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

#Arrays


def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    numpy_arr = numpy.array(arr,float)
    return numpy_arr

    
#Shape and Reshape
import numpy
# Shape and Reshape in Python - Hacker Rank Solution START
print(numpy.array(input().split(), int).reshape(3, 3))

#Transpose and Flatten
import numpy
n, m = map(int, input().split())

storage = numpy.array([input().strip().split() for _ in range(n)], int)
print (storage.transpose())
print (storage.flatten())

#Concatenate
import numpy

n,m,p=map(int,input().split())

lista1=[list(map(int,input().split())) for i in range(n)]
lista2=[list(map(int,input().split())) for i in range(m)]
a1=numpy.array(lista1)
a2=numpy.array(lista2)

print(numpy.concatenate((a1,a2),axis=0))

#Zeros and Ones
import numpy

size = tuple(map(int,input().strip().split()))
print( numpy.zeros(size, int) )
print( numpy.ones(size, int) )

#Eye and Identity
import numpy

numpy.set_printoptions(sign=' ')
print(numpy.eye(*map(int, input().split())))

#Array Mathematics
import numpy

N, M = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for n in range(N)])
B = numpy.array([list(map(int, input().split())) for n in range(N)])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)

#Floor, Ceila and Rent
import numpy

numpy.set_printoptions(sign=' ')

array = numpy.array(input().split(),float)

print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))

#Sum and Proad
import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))

#Min and Max
import numpy

N, M = map(int, input().split())
storage = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(storage, axis=1), axis=0))

#Mean, Var and Std
import numpy
N,M = map(int, input().split(" "))
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.mean(A, axis = 1))
print(numpy.var(A, axis = 0))
print(round(numpy.std(A, axis = None),11))

#Dot and Cross
import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))

#Inner and Outer
import numpy

A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(numpy.inner(A, B), numpy.outer(A, B), sep='\n')

#Polynomials
import numpy

coefs=list(map(float,input().split()))
x=float(input())

print(numpy.polyval(coefs,x))
                    
#Linear Algebra
import numpy
print(round(numpy.linalg.det(numpy.array([input().split() for _ in range(int(input()))],float)),2))

#Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_cand = max(candles)
    total = 0
    for i in range(len(candles)):
        if candles[i] == max_cand:
            total+=1
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if (v1>v2) and (x1-x2)%(v2-v1) == 0:    
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    p = 5                   #total people as on day 1
    s = 0
    for _ in range(n):
        l = p//2            #minimum people who like
        s += l              #people who likes
        p = l*3             #each share to 3 people
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    return 1 + (k * sum(int(x) for x in n) - 1) % 9

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#Insertion Sort - Part 01
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    target = arr[-1]
    idx = n-2

    while (target < arr[idx]) and (idx >= 0):
        arr[idx+1] = arr[idx]
        print(*arr)
        idx -= 1

    arr[idx+1] = target
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#Insertion Sort - Part 02
#!/bin/python3
import sys

def insertionSort1(start, arr):
    probe = arr[start]
    
    for ind in range(start-1, -1, -1):
        if arr[ind] > probe:
            arr[ind+1] = arr[ind]
        else:
            arr[ind+1] = probe
            break
    if arr[0] > probe:
        arr[0] = probe

def insertionSort2(n, arr):
    for ind in range(1, len(arr)):
        insertionSort1(ind, arr)
        print(" ".join(map(str, arr)))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)










