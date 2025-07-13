def is_serpertine(mat):
    # col == rows

    if mat[0][0] != 1:
        return False

    if len(mat) != len(mat[0]):
        return False

    for row in mat:
        check_row()

def check_row(row,start_num):
    for num in row:
        if num >