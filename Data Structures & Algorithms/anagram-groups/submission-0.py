class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =  defaultdict(list) # mapping charcount to list of anagrams 
        for s in strs:
            count=[0]*26 #a to z
            for c in s: # every single character in each string 
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()



        