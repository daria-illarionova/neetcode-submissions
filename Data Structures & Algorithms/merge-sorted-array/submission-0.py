class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        SOLUTION: Three Pointers Without Extra Space - I
        
        Intuition
        The key insight is that nums1 has empty space at the end. If we fill
        from the back instead of the front, we never overwrite elements we
        still need. By comparing the largest remaining elements from both
        arrays and placing the larger one at the current end position, we can
        merge in place without extra space.
        """
        # Pointer <last> refers to index of current end position where larger value is inserted  
        last = (m+n) -1 

        while m > 0 and n > 0:
            n1 = nums1[m-1]
            n2 = nums2[n-1]
            
            if n1 > n2:
                nums1[last] = n1
                m -= 1
            else:
                nums1[last] = n2
                n -= 1
            last -= 1

        # Case: Loop terminated and untransferred values remain in nums2 (n != 0)
        while n > 0: 
            nums1[last] = nums2[n-1]
            n -=1 
            last -= 1
            


        