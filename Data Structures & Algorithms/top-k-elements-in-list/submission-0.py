from collections import Counter
from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)

        sorted_frequency = dict(sorted(frequency.items(), key=itemgetter(1), reverse=True))

        results = []

        for i,key in zip(range(k),sorted_frequency):
            results.append(key)

        return results
        
        
        

        
        