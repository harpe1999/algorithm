class Solution:
    # @param num, a list of integer
    # @return an integer
    def find(self, b, e, num):
        while b<e-1:
            m=(e+b)>>1
            if num[m]>num[e]:
                b=m+1
            elif num[m]<num[e]:
                e=m
            else:
                min1=self.find(b,m,num)
                min2=self.find(m,e,num)
                if min1<min2:
                    return min1
                else:
                    return min2

        if num[e]<num[b]:
            return num[e]
        else:
            return num[b]


    def findMin(self, num):
        n=len(num)
        if n==0:
            return -1
        if n==1:
            return num[0]
        return self.find(0,n-1,num)
