# input: numRows
# return: first numRows of pascals triangle

# pascals triangle: each num is the sum of two nums directly above it
    #         1
    #       1   1
    #     1   2    1
    #   1   3    3    1
    #    (n[0] + n[1]), (n[1] +n[2]), (n[2] + n[3])
    # 1   4    6    4   1


# numRows = 3
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        output = []

        for i in range(numRows):
            if(i == 0):
                prev = [1]
                output.append(prev)
            else:
                curr = [1]
                j = 1

                while(j < i):
                    curr.append(prev[j-1] + prev[j])
                    j += 1

                curr.append(1)

                output.append(curr)

                prev = curr

        return output


# numRows = 3
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        output = []
        # [[1], [1,1], [1,2,1]]

        for i in range(numRows):
            # [0, 1, 2]

            if(i == 0):
                prev = [1]
                output.append(prev)
                # output = [[1]]
            else:
                curr = [1]
                j = 1

                while(j < i):
                    # 1 < 2
                    curr.append(prev[j-1] + prev[j])
                    # [1, prev[1-1] + prev[1]]
                    # [1, 2]
                    j += 1

                curr.append(1)

                output.append(curr)

                # [1,1]
                prev = curr

        return output