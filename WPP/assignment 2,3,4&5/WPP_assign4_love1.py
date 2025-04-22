'''The Love-Letter Mystery
James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he
decides to meddle with the letter. He changes all the words in the letter into palindromes.
To do this, he follow 2 rules:
(a) He can reduce the value of a letter. E.g. He can change ‘d’ to ‘c’ but he cannot change ‘c’ to
‘d’.
(b) In order to form a palindrome, if he has to repeatedly reduce the value of a letters, he can do it
until the letters becomes ‘a’. Once a letters has been changed to ‘a’, it can no longer be changed.
Each reduction in the value of any letter is counted as a single operation. Find the minimum number
of operations required to convert a given string into a palindrome.
Input Format:
The first line contains an integer T, i.e., the number of the test cases.
The next T lines will contain a string each.
Output Format:
A single line containing the number of minimum operations corresponding to each test case.
Constraints:
1 <= T <= 10
1 <= length of string <= 104
All character are lower case English letters.
Sample Input #00
3
abc
abcba
abcd
Sample Output #01
2
0
4

Explanation:
For the first test case, ab*c* -> ab*b* -> aba.
For the second test case, abcba is a palindromic string.
For the third test case, abc*d* -> abc*c* -> abc*b* -> ab*c*a -> abba.
'''
def palindrome(s):
    n=len(s)
    operations=0
    for i in range(n//2):
        operations+=abs(ord(s[i])-ord(s[n-i-1]))
    return operations 

T=int(input("Enter the no of test cases: ").strip())
for _ in range(T):
    s=input("Enter the string: ").strip()
    print(palindrome(s))
