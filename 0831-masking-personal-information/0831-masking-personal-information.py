class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s=s.lower()
            name,domain=s.split("@")
            return name[0] + "*****" + name[-1] + "@" + domain
        digits = [c for c in s if c.isdigit()]
        local = "***-***-" + "".join(digits[-4:])
        
        country_len = len(digits) - 10
        
        if country_len <= 0:
            return local
        
        return "+" + ("*" * country_len) + "-" + local
        