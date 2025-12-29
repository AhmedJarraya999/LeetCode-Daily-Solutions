class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def count_neg_in_row(row: List[int])-> int:
            left,right=0,len(row)-1
            while left<=right:
                mid=(left+right)//2
                if row[mid]<0:
                    right=mid-1
                else:
                    left=mid+1
            return len(row)-left
        total_negatives = 0
        for row in grid:
            total_negatives+=count_neg_in_row(row)
        return total_negatives


        