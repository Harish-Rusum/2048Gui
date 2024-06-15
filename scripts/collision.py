def collisionCalc(mat, dir):
    def merge(row, reverse=False):
        if reverse:
            row = row[::-1]

        newRow = [i for i in row if i != 0]
        for i in range(len(newRow) - 1):
            if newRow[i] == newRow[i + 1]:
                newRow[i] *= 2
                newRow[i + 1] = 0

        newRow = [i for i in newRow if i != 0]
        newRow += [0] * (len(row) - len(newRow))

        if reverse:
            newRow = newRow[::-1]

        return newRow

    if dir == "r":
        for j in range(len(mat)):
            mat[j] = merge(mat[j], reverse=True)

    elif dir == "l":
        for j in range(len(mat)):
            mat[j] = merge(mat[j])

    elif dir in ["d", "u"]:
        transposed = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

        if dir == "d":
            for j in range(len(transposed)):
                transposed[j] = merge(transposed[j], reverse=True)

        elif dir == "u":
            for j in range(len(transposed)):
                transposed[j] = merge(transposed[j])

        mat = [
            [transposed[j][i] for j in range(len(transposed))]
            for i in range(len(transposed[0]))
        ]

    return mat
