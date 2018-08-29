#!/usr/bin/env python3

# input
n = int( input() )
a = [ int(x) for x in input().split() ]

# EOF
while True:
    try:
        solve()
    except:
        break;

# output
print( x, sep=' ')
print( ''.join( str(x)+' ' for x in a ) )
print( '{:5d}'.format(x) ) 

# sort
a.sort()
sorted(a)

# list
a = [ x for x in range(n) ]
a.append(x)

# Basic operator 
a, b = 10, 20
a/b  # 0.5
a//b # 0
a%b  # 10
a**b # 10^20

# if, else if, else
if a==0:
    print('zero')
elif a>0:
    print('postive')
else:
    print('negative')

# loop
while a==b and b==c:
for i in LIST:

# stack	        # C++
stack = [3,4,5] 
stack.append(6)	# push()
stack.pop()     # pop()
stack[-1]       # top()
len(stack)      # size() O(1)

# queue         # C++
from collections import deque
queue = deque([3,4,5])
queue.append(6) # push()
queue.popleft() # pop()
queue[0]        # front()
len(queue)      # size() O(1)
