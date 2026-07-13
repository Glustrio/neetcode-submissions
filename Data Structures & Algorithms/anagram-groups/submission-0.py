class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # specialized dictionary where 
        # any new key accessed will automatically be assigned an empty list 
        # as its default value, without raising a KeyError
        for s in strs: # for each string in strs
            count = [0] * 26 # Generates a list of 26 0's for a-z
            for c in s: # For character in string, increment the count for that character
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) # Adds s (the string) to the dictionary with specific count (the tuple/unchangeable list), the tuple is the key and adding s is the value
        return list(res.values())

