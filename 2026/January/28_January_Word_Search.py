#POD: Word Search
#Timestamp: 2026-01-28 17:54:51.592101
class Solution:
    def isWordExist(self, mat, word):
        n = len(mat)
        m = len(mat[0])
        
        def backtrack(row, col, index):
            if index == len(word):
                return True
            
            if row < 0 or row >= n or col < 0 or col >= m or mat[row][col] != word[index]:
                return False
            
            temp = mat[row][col]
            mat[row][col] = '#'
            
            found = (backtrack(row + 1, col, index + 1) or
                     backtrack(row - 1, col, index + 1) or
                     backtrack(row, col + 1, index + 1) or
                     backtrack(row, col - 1, index + 1))
            
            mat[row][col] = temp
            return found

        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True
                        
        return False

if __name__ == "__main__":
    obj = Solution()
    mat = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']]
    word = "GEEK"
    print(obj.isWordExist(mat, word))