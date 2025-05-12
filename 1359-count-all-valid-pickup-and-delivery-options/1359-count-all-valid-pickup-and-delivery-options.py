class Solution(object):
    def countOrders(self, n):
        slots=2*n
        output=1
        while slots>0:
            valid_choices=slots*(slots-1)//2
            output*=valid_choices
            slots-=2
        return output%(10**9+7)
         
        