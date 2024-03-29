def quicksort(start, end, nums):
    if start >= end:
        return

    pivot, left, right = start, start + 1, end

    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]
    quicksort(start, right - 1, nums)
    quicksort(left, end, nums)


nums = [int(x) for x in input().split()]

quicksort(0, len(nums) - 1, nums)

print(*nums, sep=' ')
