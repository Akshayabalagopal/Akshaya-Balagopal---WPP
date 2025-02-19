'''Bigger is Greater
Given a word w, rearrange the letters of w to construct another word s in such a way that s is
lexicographically greater than w.
Input Format:
The first line of inputs contains t, number of test cases. Each of the next t lines contains w.
Constraints:
1 <= t <= 105
1 <= |w| <= 100
w will contain only lower-case English letters and its length will not exceed 100.
Output Format:
For each test case, output a string lexicographically bigger than w in a separate line. In case of
multiple possible answers print the lexicographically smallest one and if no answer exists, print
no answer.
Sample Input:
3
ab
bb
hefg
Sample Output:
ba
no answer
hegf

Explanation:
Testcase 1: There exists only one string greater than ab which can be built by rearranging ab. That
is ba.
Testcase 2: Not possible to rearrange bb and get a lexicographically greater string.
Testcase 3: hegt is the next string (lexicographically greater) to hefg.
'''

T=int(input("Enter the no of test cases: ").strip())
result=[]
for i in range(T):
    W=list(input("Enter the word: ").strip())
    n=len(W)

    i=n-2
    while i>=0 and W[i]>=W[i+1]:
        i-=1

    if i==-1:
        result.append("No Answer")
        continue

    j=n-1
    while W[j]<=W[i]:
        j-=1
    
    W[i], W[j]= W[j], W[i]

    W=W[:i+1]+sorted(W[i+1:])

    result.append("".join(W))

for _ in result:
    print(_)


