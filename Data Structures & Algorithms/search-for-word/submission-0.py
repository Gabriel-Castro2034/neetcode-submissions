class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        linha, coluna = len(board), len(board[0])
        path = set()

        def dfs(l, c, i):
            if i == len(word):
                return True
            
            if (l < 0 or c < 0 or 
                l >= linha or c >= coluna or 
                word[i] != board[l][c] or 
                (l, c) in path):
                return False
            path.add((l, c))
            res = (dfs(l + 1, c, i + 1) or 
                   dfs(l - 1, c, i + 1) or 
                   dfs(l, c + 1, i + 1) or 
                   dfs(l, c - 1, i + 1))
            path.remove((l, c))
            
            return res

        for l in range(linha):
            for c in range(coluna):
                if dfs(l, c, 0):
                    return True            
        return False