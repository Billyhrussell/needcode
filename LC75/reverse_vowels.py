# def reverseVowels( s):
#     """
#     :type s: str
#     :rtype: str
#     """

#     sp = list(s)

#     vowels = ["a", "e", "i", "o", "u"]

#     i = 0
#     right = len(s) -1

#     while i != right:
#         if sp[i] in vowels and sp[right] in vowels:
#             temp = sp[i]
#             sp[i] = sp[right]
#             sp[right] = temp
#             right -= 1
#             i += 1



#     return sp.join("")

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """

    sp = list(s)
    print(sp)
    vowels = ["a", "e", "i", "o", "u"]

    left = 0
    right = len(s) -1

    while left < right:
        # breakpoint()
        print(left, "left")
        print(right, "right")
        if sp[left] in vowels and sp[right] in vowels:
            temp = sp[left]
            sp[left] = sp[right]
            sp[right] = temp
            left += 1
            right -= 1
            continue
        if sp[left] not in vowels:
            left += 1
        if sp[right] not in vowels:
            right -= 1

    return "".join(sp)

print(reverseVowels("hello"))