# -*- coding: utf-8 -*-
#리스트를 만들어서 게임판과 같은 상태를 만듦, 인덱스에는 이미지&좌표가 들어있음.

import pygame
import time
import random
import function as func
WHITE = (255,255,255)
BLACK = (0,0,0)
pad_width=1366 #디스플레이 가로 길이
pad_height=768 #디스플레이 세로 길이
bag_image=pygame.image.load('./image/mancala_board.png') 
pearl=pygame.image.load('./image/pearl1.png')
p1_win=pygame.image.load('./image/p1_win.png')
p2_win=pygame.image.load('./image/p2_win.png')
draw=pygame.image.load('./image/draw.png')
def runGame():
    global gamepad, clock, BLACK
    point=[956,830,705,582,459,336] #구슬이 놓이는 자리의 x좌표
    crashed = False
    gamepad.fill(WHITE)
    gamepad.blit(bag_image,(180,200))
    pearl_list1=[] #이미지가 들어간 리스트
    pearl_list2=[] #이미지가 출력될 좌표가 들어간 리스트
    check=0
    font_obj=pygame.font.Font('Font.ttf',28)
    text_obj=font_obj.render('4',True,BLACK)
    text_rectobj=text_obj.get_rect();
    game=[[4,4,4,4,4,4,0],[4,4,4,4,4,4,0]] #게임판 상황
    for i in range(len(game)): #구슬을 놓을 위치를 랜덤하게 설정해 리스트에 추가하는 반복문
        for j in range(len(game[0])-1):
            for k in range(game[i][j]):
                if i==0:
                    y=random.randrange(258,288)
                else:
                    y=random.randrange(371,401)
                x=point[j]+random.randrange(0,35)
                pearl_list1.append(pearl)
                pearl_list2.append((x,y))
    for i in range(len(game)): #구슬 개수를 출력하는 반복문
        for j in range(len(game[0])-1):
            if i==0:
                text_rectobj.center=(point[j]+20,220)
                gamepad.blit(text_obj,text_rectobj)
            else:
                text_rectobj.center=(point[-(j+1)]+20,500)
                gamepad.blit(text_obj,text_rectobj)
    for i in range(48):#구슬을 출력하는 반복문
        gamepad.blit(pearl_list1[i],pearl_list2[i])
    pearl1=0
    pearl2=0
    check=0
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed = True
        LEFT = 1  
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == LEFT: #마우스 우클릭 시 좌표에 따라 구슬을 움직이는 조건문
          if 259<event.pos[1]<323:
              if point[0]<event.pos[0]<point[0]+70:
                  func.move(game,[0,0])
                  check=1
                  time.sleep(0.5) #0.5초 딜레이
              elif point[1]<event.pos[0]<point[1]+70:
                  func.move(game,[0,1])
                  check=1
                  time.sleep(0.5)
              elif point[2]<event.pos[0]<point[2]+70:
                  func.move(game,[0,2])
                  check=1
                  time.sleep(0.5)
              elif point[3]<event.pos[0]<point[3]+70:
                  func.move(game,[0,3])
                  check=1
                  time.sleep(0.5)
              elif point[4]<event.pos[0]<point[4]+70:
                  func.move(game,[0,4])
                  check=1
                  time.sleep(0.5)
              elif point[5]<event.pos[0]<point[5]+70:
                  func.move(game,[0,5])
                  check=1
                  time.sleep(0.5)
          elif 372<event.pos[1]<434:
              if point[0]<event.pos[0]<point[0]+70:
                  func.move(game,[1,5])
                  check=1
                  time.sleep(0.5)
              elif point[1]<event.pos[0]<point[1]+70:
                  func.move(game,[1,4])
                  check=1
                  time.sleep(0.5)
              elif point[2]<event.pos[0]<point[2]+70:
                  func.move(game,[1,3])
                  check=1
                  time.sleep(0.5)
              elif point[3]<event.pos[0]<point[3]+70:
                  func.move(game,[1,2])
                  check=1
                  time.sleep(0.5)
              elif point[4]<event.pos[0]<point[4]+70:
                  func.move(game,[1,1])
                  check=1
                  time.sleep(0.5)
              elif point[5]<event.pos[0]<point[5]+70:
                  func.move(game,[1,0])
                  check=1
                  time.sleep(0.5)
        if check==1: #구슬의 이동이 있었을 경우 실행되는 함수
            gamepad.fill(WHITE)
            gamepad.blit(bag_image,(180,200))
            pearl_list1=[]
            pearl_list2=[]
            for i in range(len(game)): #구슬의 위치를 리스트에 넣고, 구슬의 개수를 화면에 출력하는 반복문
                for j in range(len(game[0])):
                    for k in range(game[i][j]):
                        if j!=6:
                            if i==0:
                                x=point[j]+random.randrange(0,35)
                                y=random.randrange(258,288)
                                text_obj=font_obj.render('%d'%game[i][j],True,BLACK)
                                text_rectobj=text_obj.get_rect();
                                text_rectobj.center=(point[j]+20,220)
                                gamepad.blit(text_obj,text_rectobj)
                            else:
                                x=point[-(j+1)]+random.randrange(0,35)
                                y=random.randrange(371,401)
                                text_obj=font_obj.render('%d'%game[i][j],True,BLACK)
                                text_rectobj=text_obj.get_rect();
                                text_rectobj.center=(point[-(j+1)]+20,500)
                                gamepad.blit(text_obj,text_rectobj)
                        else:
                            y=random.randrange(301,370)
                            if i==0:
                                x=random.randrange(240,248)
                                text_obj=font_obj.render('%d'%game[i][j],True,BLACK)
                                text_rectobj=text_obj.get_rect();
                                text_rectobj.center=(150,335)
                                gamepad.blit(text_obj,text_rectobj)
                            else:
                                x=random.randrange(1072,1080)
                                text_obj=font_obj.render('%d'%game[i][j],True,BLACK)
                                text_rectobj=text_obj.get_rect();
                                text_rectobj.center=(1200,335)
                                gamepad.blit(text_obj,text_rectobj)
                        pearl_list1.append(pearl)
                        pearl_list2.append((x,y))
            check=0
        for i in range(48):#위치와 개수에 맞게 구슬 출력
            gamepad.blit(pearl_list1[i],pearl_list2[i])
        for i in range(len(game)): #구슬을 놓는 자리가 모두 비어있는지 판별
            times=0
            for j in range(len(game[0])-1):
                if game[i][j]==0:
                    times+=1
            if times==6:
                break
        if times==6: #구슬을 놓는 자리가 모두 비어있다면 각 플레이어의 구슬 개수를 종합하는 조건문
            for i in range(len(game)):
                for j in range(len(game[0])):
                    if i==0:
                        pearl1+=game[i][j]
                    else:
                        pearl2+=game[i][j]
        if times==6: #구슬의 총 개수에 따라 승패를 판별하고 이를 출력하는 조건문
            if pearl1<pearl2:
                gamepad.blit(p2_win,(400,300))
                pygame.display.update()
                time.sleep(3)
            elif pearl1>pearl2:
                gamepad.blit(p1_win,(400,300))
                pygame.display.update()
                time.sleep(3)#3초 딜레이
            else:
                gamepad.blit(draw,(400,300))
                pygame.display.update()
                time.sleep(3)
            break
        pygame.display.update() #디스플레이를 업데이트
        clock.tick(30) #초당 30회 수행
    pygame.quit()
    
def initGame(): #게임 실행 환경 구축 함수
    global gamepad, clock
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('mancala')
    clock = pygame.time.Clock()
    runGame() #실제 게임 실행 함수
    
initGame()