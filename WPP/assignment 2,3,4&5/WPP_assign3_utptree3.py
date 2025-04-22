'''Utopian Tree
The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the
monsoon, when it doubles in height. The second growth cycle occurs during the summer, when its height
increases by 1 meter.
Now, a new Utopian tree sapling is planted at the onset of the monsoon. Its height is 1 meter. Can you find
the height of the tree after N growth cycles?
Input Format
The first line contains an integer, T, the number of test cases.
T lines follow. Each line contains an integer, N, that denotes the number of cycles for that test case.
Constraints
1 <= T <= 10
0 <= N <= 60
Output Format
For each test case, print the height of the Utopian tree after N cycles.

Explanation #00:
There are 2 test cases. When N=0, the height of the tree remains unchanged. When N = 1, the tree doubles
its height as it's planted just before the onset of monsoon.
Explanation #01:
There are 2 test cases.
When N=0,
The height of the tree at the end of the 1st cycle = 1
The height of the tree at the end of the 2nd cycle = 2

The height of the tree at the end of the 3rd cycle = 6
When N = 1,
The height of the tree at the end of the 1st cycle = 2
The height of the tree at the end of the 2nd cycle = 3
The height of the tree at the end of the 3rd cycle = 6
the height of the tree at the end of the 4th cycle = 7
'''

def utopiantree(n):
    height=1
    for cycle in range(n):
        if cycle%2==0:
            height*=2
        else:
            height+=1
    return height

T=int(input("Enter the no of test cases: "))
for _ in range(T):
    N=int(input("Enter the no of cycles: "))
    print(utopiantree(N))
