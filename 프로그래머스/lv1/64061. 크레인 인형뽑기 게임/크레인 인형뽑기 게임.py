def solution(board, moves):
    answer = []
    count=0
    if len(moves)==0:
        count=0
    else:
        for i in moves:
            for j in range(len(board)):
                if board[j][i-1]!=0:
                    answer.append(board[j][i-1])
                    board[j][i-1]=0
                    break
    i=1
    while i<=len(answer)-1:
        if answer[i]==answer[i-1]:
            del answer[i-1]
            del answer[i-1]
            count+=2
            i-=1
        else:
            i+=1
        if len(answer)==1:
            break
    return count