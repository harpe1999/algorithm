
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        n=len(ratings)
        if n==0:
            return 0
        sum1=1
        precan=1
        top=0
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                precan+=1
                sum1+=precan
                top=i
            elif ratings[i]==ratings[i-1]:
                precan=1
                sum1+=precan
                top=i
            else:
                precan-=1
                sum1+=precan
                if precan<1:
                    sum1+=(i-top+1)
                    precan=1
                else:
                    if i==n-1 or ratings[i]<=ratings[i+1]:
                        precan-=1
                        sum1-=(i-top)*precan
                        precan=1
        return sum1
        
