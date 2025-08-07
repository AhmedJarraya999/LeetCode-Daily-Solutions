class NumArray:

    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.tree=[0]*(4*self.n)
        self.nums=nums
        self.build(0, 0, self.n - 1)
        
    def build(self, node: int, l: int, r: int):
        if l == r:
            self.tree[node] = self.nums[l]
        else:
            mid = (l + r) // 2
            self.build(2 * node + 1, l, mid)
            self.build(2 * node + 2, mid + 1, r)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
        

    def update(self, index: int, val: int) -> None:
        self._update(0, 0, self.n - 1, index, val)
    def _update(self, node: int, l: int, r: int, index: int, val: int):
        if l == r:
            self.tree[node] = val
        else:
            mid = (l + r) // 2
            if index <= mid:
                self._update(2 * node + 1, l, mid, index, val)
            else:
                self._update(2 * node + 2, mid + 1, r, index, val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
        

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
    def _sumRange(self, node: int, l: int, r: int, left: int, right: int) -> int:
        if right < l or r < left:
            return 0
        if left <= l and r <= right:
            return self.tree[node]
        mid = (l + r) // 2
        return self._sumRange(2 * node + 1, l, mid, left, right) + \
               self._sumRange(2 * node + 2, mid + 1, r, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)