class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count=0
        for i in range(low, high+1):
            s=str(i)
            if len(s)%2 != 0:
                continue  
            half=len(s)//2

            left_sum=0
            right_sum=0
  
            for j in s[:half]:
             left_sum+=int(j)
            for k in s[half:]: 
             right_sum+=int(k)

            if right_sum==left_sum:
                count+=1
        return count 
     
       
        
        