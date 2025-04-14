class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums.sort()
        longest=1
        current_streak=1

        for i in range(1, len(nums)):
           if nums[i] == nums[i - 1]:
               continue  # skip duplicates
           elif nums[i] == nums[i - 1] + 1:
               current_streak += 1
           else:
            longest = max(longest, current_streak)
            current_streak = 1

        return max(longest, current_streak)
