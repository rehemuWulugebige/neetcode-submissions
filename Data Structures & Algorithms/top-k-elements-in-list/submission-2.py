class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums)

        heap = []

        for key, value in dict.items(): 
            heapq.heappush(heap, (value, key))
            if (len(heap) > k): 
                heapq.heappop(heap)

        res = []

        for i in range(k): 
            pop = heapq.heappop(heap)
            res.append(pop[1])

        return res



