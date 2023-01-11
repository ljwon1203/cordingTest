def solution(keyinput, board):
    
    column = board[0]
    row = board[1]
    result = [0, 0]
    
    for i in keyinput:
        if i == "left" and result[0]-1 >= -(column // 2):
            result[0] -= 1 #인덱스자릿값
        elif i == "right" and result[0]+1 <= (column // 2):
            result[0] += 1
        elif i == "up" and result[1]+1 <= (row // 2):
            result[1] += 1
        elif i == "down" and result[1]-1 >= -(row // 2):
            result[1] -= 1
    
    return result