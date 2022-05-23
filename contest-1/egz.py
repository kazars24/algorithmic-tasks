def mat_insert(n, matrix, index):
    letter = chr(ord('a') + i)
    next_letter = chr(ord('a') + i + 1)
    for x in range(n):
        for y in range(n):
            if matrix[x][y] == letter:
                if (y - 1 >= 0) and (matrix[x][y - 1] == ''):
                    matrix[x][y - 1] = next_letter
                if (y + 1 <= n - 1) and (matrix[x][y + 1] == ''):
                    matrix[x][y + 1] = next_letter
                if (x - 1 >= 0) and (matrix[x - 1][y] == ''):
                    matrix[x - 1][y] = next_letter
                if (x + 1 <= n - 1) and (matrix[x + 1][y] == ''):
                    matrix[x + 1][y] = next_letter


n = int(input())
matrix = [['' for x in range(n)] for y in range(n)]
left = [0, 0]
right = [0, n - 1]
for i in range(n):
    matrix[i][i] = 'a'
    matrix[i][-i - 1] = 'a'

for i in range(n):
    mat_insert(n, matrix, i)

for m in matrix:
    print(''.join(m))
