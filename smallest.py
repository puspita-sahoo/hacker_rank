matrix = [[1, 5, 9], [-2, 0, 13], [7, 1, 5]]

# for i in range(3):
#     if i == 0:
#         sm_1 = min(m[i])
#     elif i == 1:
#         sm_2 = min(m[i])
#     else:
#         sm_3 = min(m[i])

# print(min(sm_1, sm_2, sm_3))


# ##########################
"""
temp_list =[]
m = None
n = None

for row in matrix:
    temp_min = min(row)
    temp_list.append(temp_min)
    m = temp_list.index(temp_min)


temp_min = min(temp_list)
n = temp_list.index(temp_min)

print(f"m*n: {m},{n} | smalest number is- {temp_min}")
"""
smallest = None
m, n = None, None
for m_ind, m_list in enumerate(matrix):
    print("H" ,m_ind, m_list)
    for n_ind, n_val in enumerate(m_list):

        if smallest == None:
            smallest = n_val
            m, n = m_ind, n_ind

        elif smallest > n_val:
            smallest = n_val
            m, n = m_ind, n_ind


print(smallest, m, n)
