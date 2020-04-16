import pygame
import random
from sys import exit

#početni setup

pygame.init()

screen=pygame.display.set_mode((800,800))

pygame.display.set_caption("Snek")
icon=pygame.image.load('snake.png')
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 32)

green=(0,255,0)
red=(255,0,0)

clock=pygame.time.Clock()

#kako bi se igram mogla ponavljati s Y/N

a=1
while a==1:

    #početna točka i duljina zmije, vraćanje scorea na 0, inicijalna pozicija hrane
    
    movedir=0

    x=400
    y=400
    score=0

    length=0
    curX=0
    curY=0
    trail=[]
    trail2=[]

    xfood=(random.randrange(0, 32))*25
    yfood=(random.randrange(0, 32))*25
    
    running=True
    while running:

        #kretanje i izlazak iz igre
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()
                exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and prevmovedir!=3:
                    movedir=1
                elif event.key==pygame.K_RIGHT and prevmovedir!=4:
                    movedir=2
                elif event.key==pygame.K_DOWN and prevmovedir!=1:
                    movedir=3
                elif event.key==pygame.K_LEFT and prevmovedir!=2:
                    movedir=4

        #provjeravanje je li se zmija zabila u zid
    
        if x<0 or x>775 or y<0 or y>775:
            print("U died lmao. Ur score is", str(score)+'.', "Retry? [Y/N]")
            e=input()
            if e=='n' or e=='N':
                a=0
                pygame.quit()
                exit()
            break
            running=False
            pygame.quit()
            
        curX=x
        curY=y

        #zapravo ovdje se provodi kretanje
        
        if movedir==1:
            y=y-25
        elif movedir==2:
            x=x+25
        elif movedir==3:
            y=y+25
        elif movedir==4:
            x=x-25
        prevmovedir=movedir

        #random bojanje ekrana iz nekog razloga
        
        screen.fill((0, 15, 0))

        #provjera je li zmija pojela hranu
        
        if x==xfood and y==yfood:

            #regeneracija hrane, while loop je da se ne generira u zmiji
            
            xfood=(random.randrange(0, 32))*25
            yfood=(random.randrange(0, 32))*25
            while [xfood, yfood]==[x, y] or [xfood, yfood] in trail:
                xfood=(random.randrange(0, 32))*25
                yfood=(random.randrange(0, 32))*25

            #produljivanje zmije i povećavanje scorea
            
            length=length+1
            score=score+1

        #kako mi radi 'rep' zmije je da se sprema svaka točka u kojoj je zmija bila, a ako premaši broj pojedene hrane, smaji se za 1
        
        trail.append([curX, curY])
        if len(trail)>length:
            del trail[0]

        #crtanje repa i glave zmije
        
        pygame.draw.rect(screen, green, [curX, curY, 25, 25])
        for i in range(len(trail)):
            pygame.draw.rect(screen, green, [trail[i][0], trail[i][1], 25, 25])
        pygame.draw.rect(screen, red, [xfood, yfood, 25, 25])
        pygame.draw.rect(screen,green,[x,y,25,25])

        #provjera je li se zmija zabila sama u sebe
    
        h=[x,y]
        if h in trail:
            print("U died lmao. Ur score is", str(score)+'.', "Retry? [Y/N]")
            e=input()
            if e=='n' or e=='N':
                a=0
                pygame.quit()
                exit()
            break
            running=False
            pygame.quit()

        #score

        text = font.render(str(score), True, (200,200,200))
        textRect = text.get_rect()
        textRect.center = (50, 50)
        screen.blit(text, textRect)
        pygame.display.update()
        clock.tick(15)

