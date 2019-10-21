
def TicTacDraw(board):
    for i in range(int(len(board))):
        lst=[]
        for l in board[i]:
            if l==1:
                lst.append(' O ')
            elif l==2:
                lst.append(' X ')
            else:
                lst.append('   ')
        res=''
        for a in lst:
            res=res+a
            res=res+'|'
        print(res[:-1])
        if i<int(len(board)-1):
            print('-'*(4*int(len(board))-1))
        else:
            pass
