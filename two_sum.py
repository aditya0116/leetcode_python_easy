class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        while i < len(nums) :
            x = target -nums[i]
            rem = nums[i+1:]
            if x in rem :
                return [i , i + rem.index(x) + 1]
            i+=1


if __name__=="__main__":
    obj = Solution()
    z = obj.twoSum([3,2,4],6)
    print(z)
