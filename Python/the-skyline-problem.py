# Time:  O(nlogn)
# Space: O(n)
#
# A city's skyline is the outer contour of the silhouette formed 
# by all the buildings in that city when viewed from a distance. 
# Now suppose you are given the locations and height of all the 
# buildings as shown on a cityscape photo (Figure A), write a
# program to output the skyline formed by these buildings 
# collectively (Figure B).
# 
# The geometric information of each building is represented by a 
# triplet of integers [Li, Ri, Hi], where Li and Ri are the x 
# coordinates of the left and right edge of the ith building, 
# respectively, and Hi is its height. It is guaranteed that 0 <= Li, 
# Ri <= INT_MAX, 0 < Hi <= INT_MAX, and Ri - Li > 0. You may assume 
# all buildings are perfect rectangles grounded on an absolutely 
# flat surface at height 0.
# 
# Notes:
# 
# The number of buildings in any input list is guaranteed to be 
# in the range [0, 10000].
# The input list is already sorted in ascending order by the 
# left x position Li.
# The output list must be sorted by the x position.
# There must be no consecutive horizontal lines of equal height 
# in the output skyline. 
# For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is 
# not acceptable; 
# the three lines of height 5 should be merged into one 
# in the final output as such: [...[2 3], [4 5], [12 7], ...]
#

# Divide and conquer solution.
start, end, height = 0, 1, 2
class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        intervals = self.ComputeSkylineInInterval(buildings, 0, len(buildings))
        
        res = []
        last_end = -1
        for interval in intervals:
            if last_end != -1 and last_end < interval[start]:
                res.append([last_end, 0])
            res.append([interval[start], interval[height]])
            last_end = interval[end]
        if last_end != -1:
            res.append([last_end, 0])
            
        return res
    
    # Divide and Conquer.
    def ComputeSkylineInInterval(self, buildings, left_endpoint, right_endpoint):
        if right_endpoint - left_endpoint <= 1:
            return buildings[left_endpoint:right_endpoint]
        mid = left_endpoint + ((right_endpoint - left_endpoint) / 2)
        left_skyline = self.ComputeSkylineInInterval(buildings, left_endpoint, mid)
        right_skyline = self.ComputeSkylineInInterval(buildings, mid, right_endpoint)
        return self.MergeSkylines(left_skyline, right_skyline)
    
    # Merge Sort.
    def MergeSkylines(self, left_skyline, right_skyline):
        i, j = 0, 0
        merged = []
        
        while i < len(left_skyline) and j < len(right_skyline):
            if left_skyline[i][end] < right_skyline[j][start]:
                merged.append(left_skyline[i])
                i += 1
            elif right_skyline[j][end] < left_skyline[i][start]:
                merged.append(right_skyline[j])
                j += 1
            elif left_skyline[i][start] <= right_skyline[j][start]:
                i, j = self.MergeIntersectSkylines(merged, left_skyline[i], i,\
                                                   right_skyline[j], j)
            else: # left_skyline[i][start] > right_skyline[j][start].
                j, i = self.MergeIntersectSkylines(merged, right_skyline[j], j, \
                                                   left_skyline[i], i)
        
        # Insert the remaining skylines.
        merged += left_skyline[i:]
        merged += right_skyline[j:]
        return merged
    
    # a[start] <= b[start]
    def MergeIntersectSkylines(self, merged, a, a_idx, b, b_idx):
        if a[end] <= b[end]:
            if a[height] > b[height]:   # |aaa|
                if b[end] != a[end]:    # |abb|b
                    b[start] = a[end]
                    merged.append(a)
                    a_idx += 1
                else:             # aaa
                    b_idx += 1    # abb
            elif a[height] == b[height]:  # abb
                b[start] = a[start]       # abb
                a_idx += 1
            else:  # a[height] < b[height].
                if a[start] != b[start]:                            #    bb
                    merged.append([a[start], b[start], a[height]])  # |a|bb
                a_idx += 1
        else:  # a[end] > b[end].
            if a[height] >= b[height]:  # aaaa
                b_idx += 1              # abba
            else:
                #    |bb|
                # |a||bb|a
                if a[start] != b[start]:
                    merged.append([a[start], b[start], a[height]])
                a[start] = b[end]
                merged.append(b)
                b_idx += 1
        return a_idx, b_idx
