class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]
        result = []

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for n, cnt in counts.items():
            freq[cnt].append(n)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        