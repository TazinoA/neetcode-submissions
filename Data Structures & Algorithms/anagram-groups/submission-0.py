class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = {}
        idx_count = 0

        for i in range(len(strs)):
            result.append([])
        
        for word in strs:
            anagram = "".join(sorted(word))

            if anagram in anagrams:
                result[anagrams[anagram]].append(word)
            else:
                anagrams[anagram] = idx_count
                result[idx_count].append(word)
                idx_count += 1
        
        return [res for res in result if len(res) != 0]
            
        