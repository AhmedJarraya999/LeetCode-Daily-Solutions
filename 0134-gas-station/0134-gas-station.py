class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        start=0
        fuel=0
        for i in range(len(gas)):
            fuel+=gas[i]-cost[i]
            #wakteli f position fuel wala akal najmouch neebdew mel index heeka
            if fuel<0:
                start+=1
                fuel=0
        return start

        
