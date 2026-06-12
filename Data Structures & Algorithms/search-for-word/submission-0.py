class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row = len(board)
        col = len(board[0])

        def find(r,c,index):
            if index == len(word):
                return True
            if r<0 or r>row-1 or c<0 or c>col-1 or board[r][c] != word[index]:
                return False
            
            temp = board[r][c]      # 先把原本的字母記下來
            board[r][c] = '#'       # 標記為已訪問，防止同一次路徑中重複踩到

            result = (find(r-1,c,index+1) or find(r+1,c,index+1) or \
            find(r,c-1,index+1) or find(r,c+1,index+1))

            board[r][c]=temp

            return result

        for i in range(row):
            for j in range(col):
                    if find(i,j,0):
                        return True
        return False
                        


            
        
                
