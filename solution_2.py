bcount=0 

size=input("Enter size of the NxN matrix: ") 
print()
size=int(size) 

game=[] 

k=0

h=0

global mid 

mid=int(size//2) 

def array(x): 

    for i in range(x): 

        game.append([]) 

        if i==0:  

            abc=game[0] 

            for h in range(x): 

                abc.append("W")   

        elif i==(x-1): 

            finalrow=game[x-1]     

            finalrow.append("W") 

            for i in range(x-2): 

                finalrow.append("G") 

            finalrow.append("W") 

            game[x-1][mid]="o" 

        else:

            asd=game[i] 

            asd.append("W") 

            for i in range(x-2): 

                asd.append(" ") 

            asd.append("W") 

array(size) 

def brick(abc): 

    n=int(abc[0]) 

    m=int(abc[2]) 

    weight=abc[4] 

    game[n][m]=weight 

  

def destroy(direction): 

    if direction=="LD": 

        global mid

        game[size-1][mid]="G" 

        mid=mid-1 

        game[size-1][mid]="o" 

    elif direction=="RD": 

        game[size-1][mid]="G" 

        mid=mid+1 

        game[size-1][mid]="o" 

    else: 

        print("ST") 

    

    for x in range(size-2,0,-1): 


        if game[x][mid]!=" ": 

            if game[x][mid]=="1": 

                game[x][mid]=" " 

                break 

            else: 

                game[x][mid]=str(int(game[x][mid])-1) 

                break    

    

while True:

    if(k==0):

        position=input("Enter the brick's position and the brick type : ") 

        brick(position)

        k=k+1 

    elif(k>0 and input('Do you want to continue(Y or N)? ') == 'N'): 

        break 

    else: 

        position=input("Enter the brick's position and the brick type : ") 

        brick(position) 

ballcount=input("Enter ball Count :  ") 

ballcount=int(ballcount) 

def printmat(): 

    for i in range(0,size): 

        row="" 

        for j in range(0,size): 

            chart=str(game[i][j]) 

            row=row+chart 

        print(row)     

printmat() 

print("Ball count is ",ballcount)

while True:

    if h==0:

        balldir=input("Enter the direction in which the ball need to traverse : ")     

        destroy(balldir)  

        ballcount=ballcount-1 

        printmat() 

        print("Ball count is ",ballcount)

        h=h+1

    elif (h>0 and input('Do you want to continue(Y or N)? ') == 'N'): 

        printmat() 

        break 

    else: 

        balldir=input("Enter the direction in which the ball need to traverse : ")     

        destroy(balldir)  

        ballcount=ballcount-1 

        printmat() 

        print("Ball count is ",ballcount)
