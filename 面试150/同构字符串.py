class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapping_st={}
        mapping_ts={}
        for st,ts in zip(s,t):
            if st in mapping_st:
                if mapping_st[st]!=ts:
                    return False
            else:
                mapping_st[st]=ts
            if ts in mapping_ts:
                if mapping_ts[ts]!=st:
                    return False
            else:
                mapping_ts[ts]=st 
        return True
        
