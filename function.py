# -*- coding: utf-8 -*-


p1=[]
p2=[]
for i in range(6):
    p1.append(4)
    p2.append(4)
p1.append(0)
p2.append(0)
p=[p1,p2] #초기 게임 상황을 2차원리스트로 나타냄

def move(game,seat): #게임 상황과 돌옮기는 위치대입 -> 다음 게임상황이 리턴되는 함수
    t=seat[0] #t=0: 1P, t=1: 2P
    if seat[1] in range(6):
        a=seat[1]

        if game[t][a]==0: #옮길 위치에 돌이 없을때
            return '옮길 돌이 없는 자리입니다'
        elif game[t][a]<49:
            
            if game[t][a]+a<7:
                g=game[t][a]
                game[t][a]=0 #돌을 옮기는자리는 우선 돌이 0개가됨
                for i in range(a+1,g+a+1): #돌을 1개씩 놓아둠
                    game[t][i]+=1
                
                if g+a<6 and game[t][g+a]==1: #마지막돌이 나의 빈자리에 놓일때
                    l=game[t][g+a]
                    m=game[1-t][5-g-a]
                    game[t][g+a]=0
                    game[1-t][5-g-a]=0
                    game[t][6]+=l+m
                
            elif 6<game[t][a]+a<13:
                g=game[t][a]
                game[t][a]=0 #돌을 옮기는자리는 우선 돌이 0개가됨
                for i in range(a+1,7): #돌을 1개씩 놓아둠
                    game[t][i]+=1
                for i in range(0,g+a-6):
                    game[1-t][i]+=1
                
            elif 12<game[t][a]+a<20:
                g=game[t][a]
                game[t][a]=0 #돌을 옮기는자리는 우선 돌이 0개가됨
                for i in range(a+1,7): #돌을 1개씩 놓아둠
                    game[t][i]+=1
                for i in range(0,6):
                    game[1-t][i]+=1
                for i in range(0,g+a-12):
                    game[t][i]+=1
                
                if g+a<19 and game[t][g+a-13]==1: #마지막돌이 나의 빈자리에 놓일때
                    l=game[t][g+a-13]
                    m=game[1-t][18-g-a]
                    game[t][g+a-13]=0
                    game[1-t][18-g-a]=0
                    game[t][6]+=l+m
                                 
            elif 19<game[t][a]+a<26:
                g=game[t][a]
                game[t][a]=0 #돌을 옮기는자리는 우선 돌이 0개가됨
                for i in range(a+1,7): #돌을 1개씩 놓아둠
                    game[t][i]+=1
                for i in range(0,6):
                    game[1-t][i]+=1
                for i in range(0,7):
                    game[t][i]+=1
                for i in range(0,g+a-19):
                    game[1-t][i]+=1
                
            elif 25<game[t][a]+a<33:
                g=game[t][a]
                game[t][a]=0 #돌을 옮기는자리는 우선 돌이 0개가됨
                for i in range(a+1,7): #돌을 1개씩 놓아둠
                    game[t][i]+=1
                for i in range(0,6):
                    game[1-t][i]+=1
                for i in range(0,7):
                    game[t][i]+=1
                for i in range(0,6):
                    game[1-t][i]+=1
                for i in range(0,g+a-25):
                    game[t][i]+=1
                
            elif 32<game[t][a]+a<39:
                g=game[t][a]
                game[t][a]=0 #돌을 옮기는자리는 우선 돌이 0개가됨
                for i in range(a+1,7): #돌을 1개씩 놓아둠
                    game[t][i]+=1
                for i in range(0,6):
                    game[1-t][i]+=1
                for i in range(0,7):
                    game[t][i]+=1
                for i in range(0,6):
                    game[1-t][i]+=1
                for i in range(0,7):
                    game[t][i]+=1
                for i in range(0,g+a-32):
                    game[1-t][i]+=1
                
            elif 38<game[t][a]+a<46:
                g=game[t][a]
                game[t][a]=0 #돌을 옮기는자리는 우선 돌이 0개가됨
                for i in range(a+1,7): #돌을 1개씩 놓아둠
                    game[t][i]+=1
                for i in range(0,6):
                    game[1-t][i]+=1
                for i in range(0,7):
                    game[t][i]+=1
                for i in range(0,6):
                    game[1-t][i]+=1
                for i in range(0,7):
                    game[t][i]+=1
                for i in range(0,6):
                    game[1-t][i]+=1
                for i in range(0,g+a-38):
                    game[t][i]+=1
                    
            elif 45<game[t][a]+a<52:
                g=game[t][a]
                game[t][a]=0 #돌을 옮기는자리는 우선 돌이 0개가됨
                for i in range(a+1,7): #돌을 1개씩 놓아둠
                    game[t][i]+=1
                for i in range(0,6):
                    game[1-t][i]+=1
                for i in range(0,7):
                    game[t][i]+=1
                for i in range(0,6):
                    game[1-t][i]+=1
                for i in range(0,7):
                    game[t][i]+=1
                for i in range(0,6):
                    game[1-t][i]+=1
                for i in range(0,7):
                    game[t][i]+=1
                for i in range(0,g+a-45):
                    game[1-t][i]+=1
            
            return game #옮긴후 게임상황을 리턴

        else: #한칸에 돌이 40개 정도 넘게 모일때(발생하지 않는경우)
            return 0