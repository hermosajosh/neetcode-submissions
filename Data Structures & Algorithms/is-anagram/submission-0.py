class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        word1_map = {}
        word2_map = {}

        for letter in s:

            if(word1_map.get(letter, None) == None):
                word1_map[letter] = 1
            else:
                word1_map[letter] += 1

        for letter in t:

            if(word2_map.get(letter, None) == None):
                word2_map[letter] = 1
            else:
                word2_map[letter] += 1
        
        return word1_map == word2_map