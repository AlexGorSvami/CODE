class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Проверяем, отсортирована ли левая половина
            if nums[left] <= nums[mid]:
                # Проверяем, находится ли target в диапазоне левой половины
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            # Иначе отсортирована правая половина
            else:
                # Проверяем, находится ли target в диапазоне правой половины
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1    
