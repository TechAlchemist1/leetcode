class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        '''
        Initial approach is to use prefix sum: Keep a sum of the count 
        of vowels, starting from 0...i our map will be numVowels:0..n 

        so with this at each point we can ask ourselves 

        Do i make key be: Valid even counts or total counts?

        question to ask: at index i, does a sub array exits that i can
        subtract to make this new sub array valid

        currPrefix - prev = even count

        '''
        myMap = {(0, 0, 0, 0, 0): -1}
        prefix = [0] * 5
        longest = 0
        vowels = {'a':0,'e':1,'i':2,'o':3,'u':4}

        for i in range(len(s)):
            if s[i] in vowels:
                prefix[vowels[s[i]]] += 1
            # if the sum of arr is even then we are good
            # otherwise can we subtract a different sum?
            # [1,1,1,] - [1,2,1]
            valid = tuple(count % 2 for count in prefix)
            if valid in myMap:
                length = i - myMap[valid]
                longest = max(length,longest)
            else:
                myMap[valid] = i
        
        return longest