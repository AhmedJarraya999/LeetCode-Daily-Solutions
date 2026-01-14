from bisect import bisect_left

class SegTree:
    def __init__(self, xs):
        self.xs = xs
        self.n = len(xs)
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)

    def update(self, node, start, end, L, R, val):
        if L <= start and end <= R:
            self.count[node] += val
        else:
            mid = (start + end) // 2
            if L <= mid:
                self.update(node*2, start, mid, L, R, val)
            if R > mid:
                self.update(node*2+1, mid+1, end, L, R, val)

        if self.count[node] > 0:
            self.covered[node] = self.xs[end+1] - self.xs[start]
        else:
            if start == end:
                self.covered[node] = 0
            else:
                self.covered[node] = self.covered[node*2] + self.covered[node*2+1]

class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        events = []
        xset = set()
        for x, y, l in squares:
            events.append((y, 1, x, x+l))
            events.append((y+l, -1, x, x+l))
            xset.add(x)
            xset.add(x+l)

        events.sort(key=lambda e: e[0])
        xs = sorted(xset)

        # Build segment tree (nodes represent intervals between unique xs)
        st = SegTree(xs)

        # Compute total union area
        total_area = 0
        prev_y = events[0][0]
        for y, typ, xl, xr in events:
            covered_width = st.covered[1]
            total_area += covered_width * (y - prev_y)
            L = bisect_left(xs, xl)
            R = bisect_left(xs, xr) - 1
            st.update(1, 0, len(xs)-2, L, R, typ)
            prev_y = y

        half = total_area / 2

        # Sweep again to find y that reaches half area
        st = SegTree(xs)
        area_so_far = 0
        prev_y = events[0][0]

        for y, typ, xl, xr in events:
            covered_width = st.covered[1]
            dy = y - prev_y
            seg_area = covered_width * dy
            if area_so_far + seg_area >= half:
                if covered_width == 0:
                    return prev_y
                remain = half - area_so_far
                return prev_y + remain / covered_width

            area_so_far += seg_area

            L = bisect_left(xs, xl)
            R = bisect_left(xs, xr) - 1
            st.update(1, 0, len(xs)-2, L, R, typ)
            prev_y = y

        return prev_y
