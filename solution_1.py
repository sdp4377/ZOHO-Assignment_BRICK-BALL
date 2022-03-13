bcount=0 

size=input("Enter size of the NxN matrix: ") 

print()

size=int(size) 

game=[] 

k=0

def array(x): 

    for i in range(x): 

        game.append([]) 

        if i==0:  

          abc=game[0] 

          for h in range(x): 

              abc.append("W")   

        elif i==(x-1): 

            mid=size//2 

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

            chart=game[i][j] 

            row=row+chart 

        print(row)     

printmat() 

print("Ball count is ",ballcount)
