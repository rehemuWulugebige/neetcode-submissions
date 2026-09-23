class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy = nums1[:]
        i, j, k = 0, 0, 0
        while (i < n and j < m):
            if (nums2[i] <= copy[j]):
                nums1[k] = nums2[i]
                i += 1
            else:
                nums1[k] = copy[j]
                j += 1
            k += 1
        while (i < n):
            nums1[k] = nums2[i]
            i += 1
            k += 1
        while (j < m):
            nums1[k] = copy[j]
            j += 1
            k += 1
