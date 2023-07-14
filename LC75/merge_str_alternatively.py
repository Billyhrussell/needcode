def mergeAlternately(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        extra = ""
        if len(word1) > len(word2):
            extra = word1[len(word2):len(word1)]
            word1 = word1[0:len(word2)]
        elif len(word2) > len(word1):
            extra = word2[len(word1):len(word2)]
            word2 = word2[0:len(word1)]

        word = ""
        for i in range(len(word1)):
             word += word1[i] + word2[i]

        if extra:
             word += extra

        return word





w1 = "abcde"
w2 = "pqr"
print(mergeAlternately(w1,w2))


# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: str
#         """

#         extra = ""
#         if len(word1) > len(word2):
#             extra = word1[len(word2):len(word1)]
#             word1 = word1[0:len(word2)]
#         elif len(word2) > len(word1):
#             extra = word2[len(word1):len(word2)]
#             word2 = word2[0:len(word1)]

#         word = ""
#         for i in range(len(word1)):
#              word += word1[i] + word2[i]

#         if extra:
#              word += extra

#         return word