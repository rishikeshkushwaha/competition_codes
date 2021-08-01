class Solution:
    def searchRange(self, nums, target: int):
        def searchLeft(A, x):
            left , right = 0,len(A)-1
            while left <= right:
                mid = int((left+right) / 2)
                if A[mid] < x:
                    left = mid+1
                else:
                    right = mid-1
            return left
        def searchRight(A, x):
            left , right = 0,len(nums)-1
            while left <= right:
                mid = int((left+right) / 2)
                if A[mid] <= x:
                    left = mid+1
                else:
                    right = mid-1
            return right
        left, right = searchLeft(nums, target), searchRight(nums, target)
        return [left, right] if left <= right else [-1, -1]

if __name__ =="__main__":
    nums= [5,7,7,8,8,10]
    target = 7
    print(Solution().searchRange(nums,target))
            