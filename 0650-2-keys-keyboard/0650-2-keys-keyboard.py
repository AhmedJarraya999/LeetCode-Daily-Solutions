class Solution:
    def minSteps(self, n: int) -> int:
        cache={}
         #paste how many a can we pase
        #count current number of a 
        def helper(count,paste):
            if count==n:
                return 0
            if count>n:
                return 1000
            if (count,paste) in cache:
                return cache[(count,paste)]
            #paste
            res1=1+helper(count+paste,paste)

            #copy & paste
            res2=2+helper(count*2,count)
            cache[(count,paste)]=min(res1,res2)
            return cache[(count,paste)]
        if n==1:
            return 0
        return 1+helper(1,1)

       

        