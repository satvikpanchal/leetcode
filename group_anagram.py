class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for chars in word:
                count[ord(chars) - ord("a")] += 1

            result[tuple(count)].append(word)

        return list(result.values())