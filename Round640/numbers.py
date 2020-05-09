#Result: Accepted
#Solution: Break number up into numbers of 10 starting from the largest power of 10
#smaller than n
#and add how many of these powers of 10 fit into the current n
for tc in range(int(input())):
    n = int(input())
    count = 0
    ans = []
    while(n):
        digit = (10**(len(str(n))-1))
        ans.append(digit*(n//digit))
        count+=1
        n -= digit * (n // digit)
    print(count)
    print(*ans)