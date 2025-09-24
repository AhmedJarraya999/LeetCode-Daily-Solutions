class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res=[]
        if  numerator==0:
            return "0"
        #sign checker
        if (numerator<0) !=(denominator<0):
            res.append("-")
        num,den=abs(numerator),abs(denominator)
        res.append(str(num//den))
        rem=num%den
        if rem==0:
            return "".join(res)
        res.append(".")
        rem_map={}
        while rem!=0:
            if rem in rem_map:
                pos=rem_map[rem]
                res.insert(pos,"(")
                res.append(")")
                return "".join(res)
            rem_map[rem]=len(res)
            rem*=10
            res.append(str(rem//den))
            rem%=den
        return "".join(res)

        