def build_array(string1, string2):
    M = []
    for i in range(len(string1) + 1):
        for j in range(len(string2) + 1):
            if j == 0:
                M.append([i])
            elif i == 0:
                M[i].append(j)
            else:
                M[i].append(0)
    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i - 1] == string2[j - 1]:
                M[i][j] = M[i - 1][j - 1]
            else:
                M[i][j] = min(M[i - 1][j], M[i][j - 1], M[i - 1][j - 1]) + 1
    return M


def levenschtein_distance(string1, string2):
    return build_array(string1, string2)[len(string1)][len(string2)]
