class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)

        heap = []

        for key in map: 
            heapq.heappush_max(heap, (map[key], key))

        res = []

        for i in range(k): 
            pop = heapq.heappop_max(heap)
            n = pop[1]
            res.append(n)

        return res




