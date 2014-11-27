class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        n=len(s)
        m=len(p)
        opt=[False]*(m+1)
        pre=[False]*(m+1)
        opt[0]=pre[0]=True
        for j in range(1,m+1):
            opt[j]=pre[j]=(j>=2 and p[j-1]=="*") and pre[j-2]

        for i in range(1,n+1):
            opt[0]=False
            for j in range(1,m+1):
                opt[j]=((s[i-1]==p[j-1] or p[j-1]=='.') and pre[j-1]) or\
                 ((p[j-1]=='*' and (p[j-2]==s[i-1] or p[j-2]=='.')) and pre[j]) or\
                  ((j>=2 and p[j-1]=='*') and opt[j-2]);
            for j in range(0,m+1):
                pre[j]=opt[j]
        return opt[m]
