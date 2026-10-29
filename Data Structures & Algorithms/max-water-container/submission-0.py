class Solution:
    def maxArea(self, heights: List[int]) -> int:
        indx1 = 0
        indx2 = len(heights) - 1
        max_area = 0

        while indx1 < indx2:
            curr_area = (indx2 - indx1) * (min(heights[indx1], heights[indx2]))

            if curr_area > max_area:
                max_area = curr_area
            
            # update pointers to check next container
            # height determined by min height of bars => maximize container area by maximizing bar heights, update the pointer with the lower height
            if heights[indx1] > heights[indx2]:
                indx2 -= 1
            else:
                indx1 += 1
        return max_area
    