class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        allmax=0
        for i in range(0,len(points)):
            count={}
            max1=0
            same=0
            for j in range(i,len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    same+=1
                elif points[i].x == points[j].x:
                    if count.get(float("inf")) is None:
                        count[float("inf")]=1
                    else:
                        count[float("inf")]+=1
                    if count[float("inf")]>max1:
                        max1=count[float("inf")]
                else:
                    k=(points[i].y - points[j].y)*1.0/(points[i].x - points[j].x)
                    if count.get(k) is None:
                        count[k]=1
                    else:
                        count[k]+=1
                    if count[k]>max1:
                        max1=count[k]
            max1+=same
            if max1>allmax:
                allmax=max1
        return allmax