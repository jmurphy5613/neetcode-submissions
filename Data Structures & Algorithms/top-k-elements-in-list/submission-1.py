class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
            
        freq = []
        for key, item in dic.items():
            freq.append([item, key])
        freq.sort()
        freq.reverse()
        sortedList = [item[1] for item in freq]
        return sortedList[0:k]