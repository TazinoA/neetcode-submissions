class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            anagram = "".join(sorted(word))

            anagrams[anagram].append(word)
        
        return list(anagrams.values())
            
        