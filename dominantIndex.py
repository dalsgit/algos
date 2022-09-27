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
        d_idx = 0
        highest = 0
        second_highest = 0
        if(nums[0] >= nums[1]):
            highest = nums[0]
            second_highest = nums[1]
        else:
            highest = nums[1]
            second_highest = nums[0]
            d_idx = 1
        for idx in range(2, len(nums)):
            current = nums[idx]
            if current > highest:
                second_highest = highest
                highest = current
                d_idx = idx
            elif current > second_highest:
                second_highest = current
        if 2*second_highest <= highest:
            return d_idx
        return -1

def plusOne(digits):
    if len(digits) == 0:
        return [1]
    if digits[-1] == 9:
        digits = plusOne(digits[:-1])
        digits.append(0)
    else:
        digits[-1] = digits[-1]+1
    return digits


l=[9,9,9]
print(plusOne(l))