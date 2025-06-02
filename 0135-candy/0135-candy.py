class Solution:
    def candy(self, ratings: List[int]) -> int:
        res=0
        arr=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                arr[i]=arr[i-1]+1

        #skip last element reverse order til  reach the first 
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                arr[i]=max(arr[i+1]+1,arr[i]) #faza
                
        for i in range(len(ratings)):
            res+=arr[i]
        return res
            
        