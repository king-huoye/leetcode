class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #建立映射
        t=s.split(' ')
        if len(pattern)!=len(t):
            return False
        mapping_p={}
        mapping_t={}
        for p,t in zip(pattern,t):
            if p in mapping_p:
                if mapping_p[p]!=t:
                    return False
            else:
                mapping_p[p]=t 
            
            if t in mapping_t:
                if mapping_t[t]!=p:
                    return False
            else:
                mapping_t[t]=p 
        return True

