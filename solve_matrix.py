import os

diff = 1e-7

dim = int(input('Input number of unknowns: '))
mat = []
ans = [0] * dim

print('Input the matrix (separated with spaces):')
for i in range(dim):
    mat.append(([float(x) for x in input().split()]))
    if len(mat[len(mat) - 1]) != dim + 1:
        print('ERROR')
        exit()

print()

def print_mat():
    for line in mat:
        s = str(round(float(line[0]), 2))
        for i in range(1, len(line)):
            num = line[i]
            s += '%7s' % round(float(num), 2)
            s += ' '
        print(s)
    print()

# print_mat()

for i in range(dim - 1):
    if abs(mat[i][i]) <= diff:
        for j in range(i, dim):
            if abs(mat[j][i]) > diff:
                mat[i], mat[j] = mat[j], mat[i]
                print('R%d <-> R%d' % (i + 1, j + 1))
                print_mat()
                break

    if abs(mat[i][i]) <= diff:
        continue

    for j in range(i + 1, dim):
        c = -1.0 * mat[j][i] / mat[i][i]
        if abs(c) <= diff:
            continue
        mat[j][i] = 0
        for k in range(i + 1, dim + 1):
            mat[j][k] += c * mat[i][k]
        print('%.2f * R%d + R%d -> R%d' % (c, i + 1, j + 1, j + 1))

    print_mat()

# print(mat)

# pdb.set_trace()

INF = 0

for i in range(0, dim)[::-1]:
    tot = 0
    for j in range(i + 1, dim):
        tot += ans[j] * mat[i][j]
    mat[i][dim] -= tot
    if abs(mat[i][i]) <= diff:
        INF = 1
        if abs(mat[i][dim]) > diff:
            print('INCONSISTENT\n')
            exit()
        continue
    ans[i] = 1.0 * mat[i][dim] / mat[i][i]

if INF == 1:
    print('DEPENDENT\n')
    exit()

# print(mat)
print('Answer: ' + str(ans) + '\n')

