class Solution(object):
    def findCommonResponse(self, responses):
        counter=Counter()
        for day in responses:
            unique_responses=set(day)
            for response in unique_responses:
                counter[response]+=1
        max_count=max(counter.values())
        candidates = [resp for resp, count in counter.items() if count == max_count]
        return min(candidates) 

        
        