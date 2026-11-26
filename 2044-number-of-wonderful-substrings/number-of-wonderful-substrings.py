class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mySet = {
            'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
            'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9
        }

        # Earlier parity tuple -> number of occurrences
        myMap = {(0, 0, 0, 0, 0, 0, 0, 0, 0, 0): 1}
        prefix = [0] * 10
        count = 0

        for i in range(len(word)):
            index = mySet[word[i]]

            if (prefix[index] + 1) % 2 == 0:
                prefix[index] = 0
            else:
                prefix[index] = 1

            # Zero odd counts: earlier tuple matches exactly.
            key = tuple(prefix)
            count += myMap.get(key, 0)

            # One odd count: earlier tuple differs at one position.
            for j in range(len(prefix)):
                original = prefix[j]

                if prefix[j] == 0:
                    prefix[j] = 1
                else:
                    prefix[j] = 0

                prev = tuple(prefix)
                count += myMap.get(prev, 0)

                # Restore the current prefix.
                prefix[j] = original

            # Store the current prefix after counting its matches.
            myMap[key] = myMap.get(key, 0) + 1

        return count