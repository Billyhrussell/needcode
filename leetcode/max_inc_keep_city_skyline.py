# each block has a building
# grid[r][c] = height of building @ row r and col c

import collections

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        horizontal = collections.defaultdict(list)
        v_max = []

        # find the max vals for the vertical (west and east views)
        # also append building sizes to horizontal views {}
        for i, row in enumerate(grid):
            v_max.append(max(row))
            for j, col in enumerate(row):
                horizontal[j].append(row[j])


        h_max = []
        # Find the max values for the horizontal (north and south views)
        for row in horizontal.values():
            h_max.append(max(row))

        sum = 0

        # if horizontal max < vert max, sum = building - max
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if h_max[i] < v_max[j]:
                    sum += h_max[i] - col
                else:
                    sum += v_max[j] - col

        return sum