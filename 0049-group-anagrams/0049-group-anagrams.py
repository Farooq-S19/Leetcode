class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        for word in strs:
            freq = [0]*26
            for letter in word:
                freq[ord(letter)-ord('a')]+=1
            anagrams[tuple(freq)].append(word)
        return list(anagrams.values())
        