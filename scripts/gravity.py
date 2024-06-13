def gravCalc(mat, dir):
    if dir in ["r", "l"]:
        for i in range(len(mat)):
            row = mat[i]
            if dir == "l":
                row = sorted(row, key=lambda x: x == 0)
            else:
                row = sorted(row, key=lambda x: x == 0, reverse=True)
            mat[i] = row
    elif dir in ["d", "u"]:
        transposed = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
        for i in range(len(transposed)):
            row = transposed[i]
            if dir == "u":
                row = sorted(row, key=lambda x: x == 0)
            else:
                row = sorted(row, key=lambda x: x == 0, reverse=True)
            transposed[i] = row
        mat = [[transposed[j][i] for j in range(len(transposed))] for i in range(len(transposed[0]))]
    return mat
