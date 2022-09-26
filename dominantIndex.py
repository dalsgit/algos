def dominant(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        if sorted_nums[-1] > 2*sorted_nums[-2]:
            return sorted_nums[-1]
        return -1

def dominantIndex(nums):
        d_idx = -1
        for idx, num in enumerate(nums):
            
        sorted_nums = sorted(nums)
        if sorted_nums[-1] > 2*sorted_nums[-2]:
            return sorted_nums[-1]
        return -1

l=[1,2,9,3,4]
print(dominantIndex(l))