class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n=len(s)
        if n<2:
            return 0
        cut=[0]*(n+1)
        for i in range(0,n+1):
            cut[i]=i-1
        for i in range(0,n):
            j=0
            while(i-j>=0 and i+j<n and s[i-j]==s[i+j]):
                cut[i+j+1]=min(cut[i+j+1],cut[i-j]+1)
                j+=1
            j=0
            while(i-j>=0 and i+j+1<n and s[i-j]==s[i+j+1]):
                cut[i+j+2]=min(cut[i+j+2],cut[i-j]+1)
                j+=1
        return cut[n]
