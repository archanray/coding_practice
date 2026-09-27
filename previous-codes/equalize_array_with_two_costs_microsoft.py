def t(maxA, nums, c1, c2): # optimzal cost when all numbers= maxA
    A1, n = sorted([maxA-i for i in nums]),2
    su=tot=sum(A1)
    while A1 and A1[-1]>su//n: 
        n-=1
        su-=A1.pop()
    su//=n
    return tot, su, tot-2*su, (tot-2*su)*c1+su*c2
    
def solution(nums, c1, c2):
    maxA,l,n = max(nums),t(max(nums),nums,c1,c2)[2],len(nums)
    while l>=n-1>1: # new maxA if we have raised all numbers to maxA but one number<maxA, e.g. [5,12,12,12,12], we want to get maxA=14
        maxA+=l//(n-1)
        l+=(2-n)*(l//(n-1))
    return min([c1*(max(nums)*n-sum(nums)),t(max(nums), nums, c1, c2)[3], t(maxA, nums, c1, c2)[3], t(maxA+1, nums, c1, c2)[3]]) 

def wrapper(nums, c1, c2):
    return int(solution(nums, c1, c2) % (1e+9))

A=[2, 11, 11, 11, 12]
c1=10
c2=4

print(wrapper(A, c1, c2))