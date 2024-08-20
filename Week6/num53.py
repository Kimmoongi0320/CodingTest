moves = [[1,0],[-1,0],[0,1],[0,-1]]

def can_move(board,next_x,next_y):
    if 0 <= next_x < len(board) and 0 <= next_y < len(board) and board[next_x][next_y] != 0:
        return True
    else:
        return False

def solution(board,aloc,bloc):
    movements = []
    def backtracking(a,b,a_move,b_move):
        for move in moves:
            dx,dy = move[0],move[1]
            #둘의 위치가 같고 a가 움직일 곳이 있을경우
            if a[0] == b[0] and a[1] == b[1] and can_move(board,a[0]+dx,a[1]+dy):
                movements.append(min(a_move+1,b_move))
                return
            #둘의 위치가 같고 a가 움직일 곳이 없을경우
            elif a[0] == b[0] and a[1] == b[1] and not can_move(board,a[0]+dx,a[1]+dy):
                movements.append(min(a_move,b_move))
                return
        for a_way in moves:
            for b_way in moves:
                # 둘다 움직일 곳이 있다면
                if can_move(board,a[0]+a_way[0],a[1]+a_way[1]) and can_move(board,b[0]+b_way[0],b[1]+b_way[1]):
                    board[a[0]+a_way[0],a[1]+a_way[1]] = 0
                    board[b[0]+b_way[0],b[1]+b_way[1]] = 0
                    backtracking([a[0]+a_way[0],a[1]+a_way[1]],b[0]+b_way[0],b[1]+b_way[1],a_move+1,b_move+1)
                    board[a[0]+a_way[0],a[1]+a_way[1]] = 1
                    board[b[0]+b_way[0],b[1]+b_way[1]] = 1
            movements.append(min(a_move,b_move))

