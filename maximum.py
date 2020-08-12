class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        pair = []
        for s,e in zip(speed,efficiency):
            pair.append((s,e))

        def cmpf(v1,v2):
            if v1[1] != v2[1]:
                return v1[1] - v2[1]
            return v2[0] - v1[0]
        pair.sort(cmp=cmpf)
        import bisect

        res = 0
        total = None
        speed.sort()
        for i in range(len(pair)):
            inx = bisect.bisect_left(speed,pair[i][0])
            flag = (inx + k - 1) >= len(speed)
            del speed[inx]
            if total == None:
                total = sum(speed[len(speed)-k + 1:len(speed)])
            elif i + k > len(pair):
                total -= pair[i][0]
            elif flag:
                total -= pair[i][0]
                total += speed[len(speed) - k + 1]

            res = max(res,(total+ pair[i][0]) * pair[i][1])

        return res % (10**9 + 7)
val=Solution()
n,k=map(int,input().split())
speed=list(map(int,input().split()))
efficiency=list(map(int,input().split()))
print(val.maxPerformance(n,speed,efficiency,k))
