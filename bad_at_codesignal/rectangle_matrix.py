# input:
# [[. , . , . ],
#  [F , F , . ],
#  [. , F , F ],
#  [# , F , F ],
#  [. , F , . ],
#  [. , . , . ],
#  [. , . , # ],
#  [. , . , . ]]

# output:
# [[. , . , . ],
#  [. , . , . ],
#  [F , F , . ],
#  [# , F , F ],
#  [. , F , F ],
#  [. , F , . ],
#  [. , . , # ],
#  [. , . , . ]]



# . = free space
# F = formation
# # = blocked

# formation is falling,
# return where the formation STOPS

def falling(matrix):

    length = len(matrix)