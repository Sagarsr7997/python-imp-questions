#nth term of Fibonacci Series
def fib(n):
    if n <= 1:
        return n 
    return fib(n-1) + fib(n-2)

n = int(input())
result = fib(n)
print(result)

#n term of Fibonacci Series
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def get_fibonacci_series(n):
    list_a = []
    for i in range(n):
        term = fibonacci(i)
        list_a.append(term)
    return list_a

n = int(input())
final_list = get_fibonacci_series(n)
print(final_list)

#Max Contagious Subarray
a=list(map(int,input().split()))
if not a:
    print(0)
else:
    sum_dict={} 
    for i in range(len(a)):
        for j in range(i+1,len(a)+1):
            sum_dict[tuple(a[i:j])]=sum(a[i:j])
    keys=list(sum_dict.keys())
    values=list(sum_dict.values())
    max_sum=values.index(max(values))
    print(*keys[max_sum])

#Perimeter of a Matrix#

m,n = list(map(int,input().split()))
matrix = []
total = 0
for i in range(m):
    numbers = list(map(int,input().split()))
    matrix.append(numbers)
    
for i in range(m):
    for j in range(n):
        if i == 0 or i == m-1:
            total += matrix[i][j]
        else:
            if j == 0 or j == n-1:
                total += matrix[i][j]
print(total)

#Swap Characters#

wordOne = list(input())
wordTwo = list(input())
n = len(wordOne)
for i in range(n-1):
    if (wordOne[i] != wordTwo[i]):
        k = wordOne[i]
        r = wordOne[i+1]
        wordOne[i] = r 
        wordOne[i+1] = k 
        
if wordOne == wordTwo:
    print("Yes")
else:
    print("No")
        

#Swap Competition #

def swap_comp(word):
    word_one = word[0]
    word_two = word[1]
    wordOne_Op = sorted(word_one)
    wordTwo_Op = sorted(word_two)
    
    if (wordOne_Op == wordTwo_Op):
        return ("YES")
    else:
        return ("NO")
        
n = int(input())
output = ""
for i in range(n):
    word = input().lower()
    word = word.split()
    outPut_func = swap_comp(word)
    output += outPut_func + " "

print(output)
    
    
#Sum of Powers

num_list = input().split()

output = 0

for num in num_list:
    length = len(num)
    if length == 1:
        output += 0
    else:
        last_number = num[-1]
        rem_nums = num[:length - 1]
        powers = int(rem_nums) ** int(last_number)
        output += powers
print(output)
    
    
#nth Number Sum

n,m = list(map(int,input().split()))

number_list = list(map(int,input().split()))
number_list_positions = []

for i in range(1,(m+1)):
    number_list_positions.append(i)

count = 0

for j in number_list_positions:
    if (j%n == 0):
        k = number_list[j-1]
        count += k 

print(count)
    
    
    