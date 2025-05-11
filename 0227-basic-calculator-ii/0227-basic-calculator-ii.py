class Solution(object):
    def calculate(self, s):
        s = s.replace(" ", "")  # remove spaces
        cur = 0
        prev = 0
        res = 0
        cur_op = "+"
        i = 0

        while i < len(s):
            if s[i].isdigit():
                cur = 0
                while i < len(s) and s[i].isdigit():
                    #parse full number
                    cur = cur * 10 + int(s[i])
                    i += 1
                # After the number is parsed, apply the previous operator
                if cur_op == "+":
                    res += cur
                    prev = cur
                elif cur_op == "-":
                    res -= cur
                    prev = -cur
                elif cur_op == "*":
                    res -= prev
                    prev = prev * cur
                    res += prev
                elif cur_op == "/":
                    res -= prev
                    prev = int(float(prev) / cur)# truncate toward zero
                    print("sssss",prev)
                    res += prev
                continue  # skip i+=1 since we already moved i during number parsing
            else:
                cur_op = s[i]
            i += 1

        return res
