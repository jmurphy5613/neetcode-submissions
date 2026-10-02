class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            string = sorted(word)
            cur = ''.join(string)
            if cur in dic:
                dic[cur].append(word)
            else:
                dic[cur] = [word]
        bigList = []
        for key, value in dic.items():
            bigList.append(value)
        return bigList
