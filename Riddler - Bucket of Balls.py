from random import *
file = open('Riddler - Bucket of Balls.txt', 'w')
file.write('Bucket1,Bucket1Blue,Bucket1Red,Bucket2,Bucket2Blue,Bucket2Red,wins\n')

maxWins = 0
#Set up the 50 Bucket Sizes
for Bucket1 in range(1,51):
    Bucket2 = 100-Bucket1

    #Set up Ball Distrubutions per Bucket Size
    for Bucket1Blue in range(0,Bucket1+1):
        Bucket1Red = Bucket1 - Bucket1Blue
        Bucket2Blue = 50 - Bucket1Blue
        Bucket2Red = 50 - Bucket1Red
        
        #Pick a bucket and a ball 10000 Times
        wins = 0
        for game in range(1,1000001):        
            SelectedBucket = randint(1,2)
            if SelectedBucket == 1:
                BallPick = randint(1,Bucket1)
                if BallPick > Bucket1Blue:
                    wins += 1
            else:
                BallPick = randint(1,Bucket2)
                if BallPick > Bucket2Blue:
                    wins += 1
          
        print str(Bucket1)+','+str(Bucket1Blue)+','+str(Bucket1Red)+','+str(Bucket2)+','+str(Bucket2Blue)+','+str(Bucket2Red)+','+str(wins)

        file.write(str(Bucket1)+','+str(Bucket1Blue)+','+str(Bucket1Red)+','+str(Bucket2)+','+str(Bucket2Blue)+','+str(Bucket2Red)+','+str(wins)+'\n')

file.close


