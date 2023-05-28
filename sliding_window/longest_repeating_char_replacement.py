import collections


def characterReplacement(s, k):
    maxlen, largestCount = 0, 0

    # dict subclass for counting hashable objects
    counter = collections.Counter()


    for idx in range(len(s)):
        counter[s[idx]] += 1

        #            = max(1, counter[2]] = a (2))
        largestCount = max(largestCount, counter[s[idx]])
        # lc = 2

        # if   2 - 2 >= 2
        if maxlen - largestCount >= k:
            counter[s[idx - maxlen]] -= 1
        else:
            maxlen += 1
    return maxlen

s = "ABAB"
k = 2
print(characterReplacement(s,k))