class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        res=[]
        n=len(s)
        if n==0:
            return res
        m={}
        for i in range(n-1,-1,-1):
            vs=[]
            for j in range(i,n):
                str=s[i:j+1]
                if str in dict:
                    if m.get(j+1) is None:
                        vs.append(str)
                    else:
                        for ss in m[j+1]:
                            vs.append(str+" "+ss)
            m[i]=vs
        return m[0]
        
