class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        myMap = {(0, 0, 0, 0, 0): -1}
        prefix = [0] * 5
        longest = 0
        lookUp = {'a':0,'e':1,'i':2,'o':3,'u':4}

        for i in range(len(s)):
            if s[i] in lookUp:
                index = lookUp[s[i]]
                prefix[index] += 1

            # determine if we can find valid state in map
            # so we know this CurrPRefix - prevPRefix = Even meaning both need to have same
            # parity
            # so currPrefix - prevPrefix is valid iff (currPrefix % 2 == prevPrefix % 2)
            # so maybe represent the currPrefix in a way that we can look up?

            key = tuple(p%2 for p in prefix)
            if key in myMap:
                # get the length of it and compare
                length = i - myMap[key]
                # keep the longest
                longest = max(longest,length)
            else:
                myMap[key] = i
        
        return longest
