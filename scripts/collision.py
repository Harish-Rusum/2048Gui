def collisionCalc(mat, dir):
    def merge(row, reverse=False):
        if reverse:
            row = row[::-1]
        
        new_row = [i for i in row if i != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        
        new_row = [i for i in new_row if i != 0]
        new_row += [0] * (len(row) - len(new_row))
        
        if reverse:
            new_row = new_row[::-1]
        
        return new_row
    
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
        
        mat = [[transposed[j][i] for j in range(len(transposed))] for i in range(len(transposed[0]))]
    
    return mat

