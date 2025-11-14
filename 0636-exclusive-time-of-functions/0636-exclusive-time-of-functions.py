class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []               # holds function ids
        prev_time = 0

        for log in logs:
            fid_str, typ, time_str = log.split(':')
            fid = int(fid_str)
            t = int(time_str)

            if typ == "start":
                if stack:
                    # top function was running from prev_time to t-1
                    res[stack[-1]] += t - prev_time
                stack.append(fid)
                prev_time = t
            else:  # "end"
                # fid should equal stack[-1]
                stack.pop()
                # it has been running from prev_time to t (inclusive)
                res[fid] += t - prev_time + 1
                prev_time = t + 1

        return res


        
        