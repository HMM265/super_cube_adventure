# Cool game v.13 RICK WAS HERE


import pygame
import random
import winsound
pygame.init()


clock = pygame.time.Clock()
fps = 60


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 430


scroll = 500


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('3-D Background')


ground_image = pygame.image.load('images/ground.png').convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()




me = pygame.image.load("sprites/sprite 1-2.png.png")
mex = screen.get_width()/2 - me.get_width()
mey = screen.get_height() - 130
mexh =270
meyh =320
mesw, mesh = 50, 60
move = 0
moveu = 0
orient = 1
air = False
start = False
go = False
helps = 0
boost = 400
hitbox = False
ht = "Press e to enable hit boxes"
red = 255
level = 1
stage = 1
win = False




dead = pygame.image.load("death/death 1.png")
deadani = 0


font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 50)


rans = 42
ranx = screen.get_width() + 10
rany = random.randint(0, screen.get_height() - rans - 130)
eme = pygame.image.load("sprites/evil cube 1.png")
ani = 0


rans = 42
ranx2 = screen.get_width() + 50
rany2 = random.randint(0, screen.get_height() - rans - 130)
eme2 = pygame.image.load("sprites/evil cube 1.png")
wait = 0


score = 0
subscore = 0
highscore = 0
speeds = 1
slow = 0
back = 0
slide = False
timeout = False
death = False








bg_images = []
for i in range(1, 5):
   bg_image = pygame.image.load(f'images/plx-{i}.png').convert_alpha()
   bg_images.append(bg_image)
   bg_width = bg_images[0].get_width()
   bg_height = bg_images[0].get_height()






def draw_bg():
   for x in range(100):
       speed = 1
       for i in bg_images:
           screen.blit(i, ((x * bg_width) - scroll * speed, 0))
           speed += 0.2


def draw_bg2():
   for x in range(100):
       speed = 1
       for i in bg_images2:
           screen.blit(i, ((x * bg_width) - scroll * speed, 0))
           speed += 0.2


def draw_bg3():
   for x in range(100):
       speed = 1
       for i in bg_images3:
           screen.blit(i, ((x * bg_width) - scroll * speed, 0))
           speed += 0.2


def draw_ground():
   for x in range(260):
       screen.blit(ground_image, ((x * ground_width) - scroll * 2.4, SCREEN_HEIGHT - ground_height))


def draw_ground2():
   for x in range(260):
       screen.blit(ground_image2, ((x * ground_width) - scroll * 2.4, SCREEN_HEIGHT - ground_height))


def draw_ground3():
   for x in range(260):
       screen.blit(ground_image3, ((x * ground_width) - scroll * 2.4, SCREEN_HEIGHT - ground_height))


def dhitbox():
   pygame.draw.rect(screen, (0, 100, 0), (ranx, rany, rans, rans))
   pygame.draw.rect(screen, (0, 100, 0), (ranx2, rany2, rans, rans))
   pygame.draw.rect(screen, (100, 0, 0), (mexh, meyh, mesw, mesh))


def make():
   if start and level > 0:
       if hitbox:
           dhitbox()
       pygame.draw.rect(screen, (50,50,50), (40, 15, 420, 30))
       pygame.draw.rect(screen, (232, 126, 5), (50, 20, boost,20))


       score_text = font.render("Score: " + str(score), True, (255, 255, 255))
       screen.blit(score_text,
                   (screen.get_width() - score_text.get_width() - 20, 20))
       if win:
           highscore_text = font.render("Highscore: " + str(highscore), True, (240, 183, 29))
           screen.blit(highscore_text,
                       (screen.get_width() - highscore_text.get_width() - 150, 20))








       screen.blit(me,(mex,mey))


       screen.blit(eme,(ranx - 27,rany-28))
       screen.blit(eme2, (ranx2 - 27, rany2 - 28))


run = True


while run:
   key = pygame.key.get_pressed()
   clock.tick(fps)
   screen.fill((100,100,100))
   if level == 2:
       ground_image2 = pygame.image.load('images2/ground1.png').convert_alpha()
       ground_width2 = ground_image2.get_width()
       ground_height2 = ground_image2.get_height()


       bg_images2 = []
       for i in range(1,2):
           bg_image2 = pygame.image.load(f'images2/background.png').convert_alpha()
           bg_images2.append(bg_image2)
           bg_width = bg_images2[0].get_width()
           bg_height = bg_images2[0].get_height()


   if level == 3:
       ground_image3 = pygame.image.load('images3/purple guy.png').convert_alpha()
       ground_width3 = ground_image3.get_width()
       ground_height3 = ground_image3.get_height()


       bg_images3 = []
       for i in range(1,2):
           bg_image3 = pygame.image.load(f'images3/low quality webb.png').convert_alpha()
           bg_images3.append(bg_image3)
           bg_width = bg_images3[0].get_width()
           bg_height = bg_images3[0].get_height()






   if start:
       if death:
           level = 0
           ani = 0
       if level == 0:
           deadani += 20
           if deadani == 0:
               dead = pygame.image.load("death/death 1.png")
           if deadani == 100:
               dead = pygame.image.load("death/death 2.png")
           if deadani == 200:
               dead = pygame.image.load("death/death 3.png")
           if deadani == 300:
               dead = pygame.image.load("death/death 4.png")
           if deadani == 400:
               dead = pygame.image.load("death/death 5.png")
           if deadani == 500:
               dead = pygame.image.load("death/death 6.png")
           if deadani == 600:
               dead = pygame.image.load("death/death 7.png")
           if deadani == 700:
               dead = pygame.image.load("death/death 8.png")
           if deadani == 800:
               dead = pygame.image.load("death/death 9.png")
           if deadani == 900:
               dead = pygame.image.load("death/death 10.png")
           if deadani == 1000:
               dead = pygame.image.load("death/death 11.png")
           if deadani == 1100:
               dead = pygame.image.load("death/death 12.png")
           if deadani == 1200:
               dead = pygame.image.load("death/death 13.png")
           if deadani == 1300:
               dead = pygame.image.load("death/death 14.png")
           if deadani == 1400:
               dead = pygame.image.load("death/death 15.png")
           if deadani == 1500:
               dead = pygame.image.load("death/death 16.png")
           if deadani == 1600:
               dead = pygame.image.load("death/death 17.png")
           if deadani == 1700:
               dead = pygame.image.load("death/death 18.png")
           if deadani == 1800:
               dead = pygame.image.load("death/death 19.png")
           if deadani == 1900:
               dead = pygame.image.load("death/death 20.png")
           if deadani == 2000:
               dead = pygame.image.load("death/death 21.png")
           if deadani == 2100:
               dead = pygame.image.load("death/death 22.png")
           if deadani == 2200:
               dead = pygame.image.load("death/death 23.png")
           if deadani == 2300:
               dead = pygame.image.load("death/death 24.png")
           if deadani == 2400:
               dead = pygame.image.load("death/death 25.png")
           if deadani == 2500:
               dead = pygame.image.load("death/death 26.png")
           if deadani == 2600:
               dead = pygame.image.load("death/death 27.png")
           if deadani == 2700:
               dead = pygame.image.load("death/death 28.png")
           if deadani == 2800:
               dead = pygame.image.load("death/death 28.png")
           if deadani > 3200:
               start5_text = font.render("Press r to restart, x to return to menu", True, (255, 255, 255))
               screen.blit(start5_text,
                           (screen.get_width() / 2 - start5_text.get_width() + 150, screen.get_height() / 2 + 80))
               if key[pygame.K_r]:
                   if win == False:
                       death = False
                       deadani = 0
                       level = stage
                       score = 0
                       subscore = 0
                   if win:
                       death = False
                       deadani = 0
                       score = 0
                       subscore = 100
                       level = 1
               if key[pygame.K_x]:
                   death = False
                   deadani = 0
                   start = False
                   level = 1
                   score = 0
                   subscore = 0
                   stage = 1


       screen.blit(dead,(screen.get_width()/2-dead.get_width()+300,screen.get_height()/2-dead.get_height()+100))


       if level == 1:
           draw_bg()
           draw_ground()
           make()
       if level == 2:
           draw_bg2()
           draw_ground2()
           make()
           stage = 2
       if level == 3:
           draw_bg3()
           draw_ground3()
           make()
           stage = 3
       if level == 4:
           screen.fill((191, 167, 98))
           subscore = 1
           win_text = font2.render("You Win!", True, (255, 255, 255))
           screen.blit(win_text,
                       (screen.get_width() / 2 - win_text.get_width()+60, 20))
           win2_text = font.render("You have escaped the evil influence of mike webb", True,
                                     (255, 255, 255))
           screen.blit(win2_text,
                       (screen.get_width() / 2 - win2_text.get_width() + 300, screen.get_height() / 2))
           win3_text = font.render("Now you can finally be happy and stare at this yellow screen", True,
                                   (255, 255, 255))
           screen.blit(win3_text,
                       (screen.get_width() / 2 - win3_text.get_width() + 330, screen.get_height() /2 +30))
           win4_text = font.render("Press x to return to menu ... for your prize", True,
                                   (255, 255, 255))
           screen.blit(win4_text,
                       (screen.get_width() / 2 - win4_text.get_width() + 220, screen.get_height() / 2 + 60))
           win5_text = font.render("If you press start the game will reset", True,
                                   (255, 255, 255))
           screen.blit(win5_text,
                       (screen.get_width() / 2 - win5_text.get_width() + 190, screen.get_height() / 2 + 90))
           if key[pygame.K_x]:
               death = False
               deadani = 0
               start = False
               level = 1
               score = 0
               subscore = 0
               ani = 0
               win = True




   stop = True
   go = False


   if key[pygame.K_0]:
       level = 0
       subscore = 1
   if key[pygame.K_1]:
       level = 1
   if key[pygame.K_2]:
       level = 2
   if key[pygame.K_3]:
       level = 3
   if key[pygame.K_4] and subscore < 99:
       level = 4
   if key[pygame.K_LEFT] and back < 2000 and timeout == False:
       scroll -= 5
       move += 20
       back += 20
       ranx += 4
       ranx2 += 4
       stop = False
       go = True
       orient = 2
       if move == 0:
           me = pygame.image.load("sprites/sprite 1-2f.png")
       if move == 100:
           me = pygame.image.load("sprites/sprite 2f.png")
       if move == 200:
           me = pygame.image.load("sprites/sprite 3f.png")
       if move == 300:
           me = pygame.image.load("sprites/sprite 4f.png")
       if move == 400:
           me = pygame.image.load("sprites/sprite 5f.png")
       if move == 500:
           me = pygame.image.load("sprites/sprite 6f.png")
       if move == 600:
           me = pygame.image.load("sprites/sprite 7f.png")
       if move == 700:
           me = pygame.image.load("sprites/sprite 8f.png")
       if move == 800:
           me = pygame.image.load("sprites/sprite 9f.png")
           move = 0
       if slide:
           mey -= 20


   if key[pygame.K_RIGHT] and timeout == False:
       scroll += 5
       move += 20
       back -= 50
       ranx -= 5
       ranx2 -= 5
       stop = False
       go = True
       orient = 1
       if move == 0:
           me = pygame.image.load("sprites/sprite 1-2.png.png")
       if move == 100:
           me = pygame.image.load("sprites/sprite 2.png")
       if move == 200:
           me = pygame.image.load("sprites/sprite 3.png")
       if move == 300:
           me = pygame.image.load("sprites/sprite 4.png")
       if move == 400:
           me = pygame.image.load("sprites/sprite 5.png")
       if move == 500:
           me = pygame.image.load("sprites/sprite 6.png")
       if move == 600:
           me = pygame.image.load("sprites/sprite 7.png")
       if move == 700:
           me = pygame.image.load("sprites/sprite 8.png")
       if move == 800:
           me = pygame.image.load("sprites/sprite 9.png")
           move = 0
       if slide:
           mey -= 20


   if key[pygame.K_UP] and mey > 0 and timeout == False and boost > 0:
       mey -= 5
       meyh -= 5
       stop = False
       go = True
       if slide:
           mey -= 20
   if key[pygame.K_DOWN] and mey < screen.get_height() -130 and timeout == False and slide == False:
       stop = False
       mey += 5
       meyh += 5
       go = True


   if stop and air == False:
       if orient == 1:
           me = pygame.image.load("sprites/sprite 1-2.png.png")
       if orient ==2:
           me = pygame.image.load("sprites/sprite 1-2f.png")






   if mey < screen.get_height() - 130:
       air = True
       if orient == 1:
           move = 0
           moveu += 20
           if moveu == 0:
               me = pygame.image.load("sprites/fly 1.png")
           if moveu == 100:
               me = pygame.image.load("sprites/fly 2.png")
           if moveu == 200:
               moveu = 0
       if orient == 2:
           move = 0
           moveu += 20
           if moveu == 0:
               me = pygame.image.load("sprites/fly 1f.png")
           if moveu == 100:
               me = pygame.image.load("sprites/fly 2f.png")
           if moveu == 200:
               moveu = 0


   if mey == screen.get_height() - 130 and stop == True:
       if orient == 1:
           me = pygame.image.load("sprites/sprite 1-2.png.png")
       if orient ==2:
           me = pygame.image.load("sprites/sprite 1-2f.png")
       air = False


   if air == True:
       boost -= 5
   if boost < 395 and mey + mesh >= screen.get_height() -90:
       boost += 5
       air = False
   if boost < 5 and mey < screen.get_height() -130:
       mey += 1




   if subscore == 0 and start:
       speeds = 3
       scroll = 500
       mey = screen.get_height() - 130
       meyh = 320
       ranx2 = ranx
       timeout = True
       s_text = font.render("Get ready to dodge cubes get to 50", True, (255, 255, 255))
       screen.blit(s_text,
                   (screen.get_width() / 2 - s_text.get_width()+50, screen.get_height() / 2))
   if subscore == 1:
       speeds = 1




   if subscore == 10:
       speeds = 2
       scroll = 500
       mey = screen.get_height() - 130
       meyh = 320
       ranx2 = ranx
       timeout = True
       s2_text = font.render("Speed Up!", True, (255, 255, 255))
       screen.blit(s2_text,
                   (screen.get_width()/2 - s2_text.get_width(), screen.get_height()/2))


   if subscore == 20:
       speeds = 3
       scroll = 500
       mey = screen.get_height() - 130
       meyh = 320
       ranx2 = ranx
       timeout = True
       s3_text = font.render("Speed Up!", True, (255, 255, 255))
       screen.blit(s3_text,
                   (screen.get_width() / 2 - s3_text.get_width(), screen.get_height() / 2))
   if subscore == 30:
       speeds = 5
       scroll = 500
       mey = screen.get_height() - 130
       meyh = 320
       ranx2 = ranx
       timeout = True
       s4_text = font.render("Speed Up!", True, (255, 255, 255))
       screen.blit(s4_text,
                   (screen.get_width() / 2 - s4_text.get_width(), screen.get_height() / 2))
   if subscore == 50 and level == 1:
       speeds = 5
       scroll = 500
       mey = screen.get_height() - 130
       meyh = 320
       timeout = True
       level = 2
       score = 0
       subscore = 0


   if subscore == 50 and level == 2:
       speeds = 5
       scroll = 500
       mey = screen.get_height() - 130
       meyh = 320
       timeout = True
       level = 3
       score = 0
       subscore = 0


   if subscore == 50 and level == 3:
       speeds = 5
       scroll = 500
       mey = screen.get_height() - 130
       meyh = 320
       timeout = True
       level = 4
       score = 0
       subscore = 0


   if subscore == 100:
       speeds = 1
       scroll = 500
       mey = screen.get_height() - 130
       meyh = 320
       ranx2 = ranx
       timeout = True
       score = 0
       s_text = font.render("Welcome to Endless mode, use number keys to change theme", True, (255, 255, 255))
       screen.blit(s_text,
                   (screen.get_width() / 2 - s_text.get_width() + 350, screen.get_height() / 2))
       s_text = font.render("Use zero to end the run ...", True, (255, 255, 255))
       screen.blit(s_text,
                   (screen.get_width() / 2 - s_text.get_width() + 50, screen.get_height() / 2+20))
   if subscore == 110:
       speeds = 2
       scroll = 500
       mey = screen.get_height() - 130
       meyh = 320
       ranx2 = ranx
       timeout = True
       s4_text = font.render("Speed Up!", True, (255, 255, 255))
       screen.blit(s4_text,(screen.get_width() / 2 - s4_text.get_width(), screen.get_height() / 2))
   if subscore == 120:
       speeds = 3
       scroll = 500
       mey = screen.get_height() - 130
       meyh = 320
       ranx2 = ranx
       timeout = True
       s4_text = font.render("Speed Up!", True, (255, 255, 255))
       screen.blit(s4_text,(screen.get_width() / 2 - s4_text.get_width(), screen.get_height() / 2))
   if subscore == 130:
       speeds = 5
       scroll = 500
       mey = screen.get_height() - 130
       meyh = 320
       ranx2 = ranx
       timeout = True
       s4_text = font.render("Speed Up!", True, (255, 255, 255))
       screen.blit(s4_text,(screen.get_width() / 2 - s4_text.get_width(), screen.get_height() / 2))
   if subscore == 180:
       speeds = 10
       scroll = 500
       mey = screen.get_height() - 130
       meyh = 320
       ranx2 = ranx
       timeout = True
       s4_text = font.render("Speed Up!", True, (255, 255, 255))
       screen.blit(s4_text,(screen.get_width() / 2 - s4_text.get_width(), screen.get_height() / 2))


   if ranx + rans < 0:
       ranx = screen.get_width() + 10
       rany = random.randint(0, screen.get_height() - rans)
       score += 1
       subscore += 1
       timeout = False
   if ranx2 + rans < 0 and wait > 500:
       ranx2 = screen.get_width() + 50
       rany2 = random.randint(0, screen.get_height() - rans)
       score += 1
       subscore += 1
       timeout = False
       wait = 0
   if start:
       scroll += speeds
       ranx -= speeds
       ranx2 -= speeds
       ani += 5
       wait += 5






   if start and timeout == False and go == False and air == False:
       me = pygame.image.load("sprites/slide.png")
       mex = screen.get_width() / 2 - me.get_width()
       mey = screen.get_height() - 110
       mesw, mesh = 60, 20
       mexh = mex + 70
       meyh = mey + 40
       slide = True
   else:
       mesw, mesh = me.get_width()-150, me.get_height()-40
       mexh = mex +70
       meyh = mey +20
       slide = False






   if ani == 0 and level == 1 or level == 2:
       eme = pygame.image.load("sprites/evil cube 1.png")
       eme2 = pygame.image.load("sprites/evil cube 1.png")
   if ani == 100 and level == 1 or level == 2:
       eme = pygame.image.load("sprites/evil cube 2.png")
       eme2 = pygame.image.load("sprites/evil cube 2.png")
   if ani == 200 and level == 1 or level == 2:
       eme = pygame.image.load("sprites/evil cube 3.png")
       eme2 = pygame.image.load("sprites/evil cube 3.png")
   if ani == 300 and level == 1 or level == 2:
       eme = pygame.image.load("sprites/evil cube 4.png")
       eme2 = pygame.image.load("sprites/evil cube 4.png")
   if ani == 400 and level == 1 or level == 2:
       eme = pygame.image.load("sprites/evil cube 5.png")
       eme2 = pygame.image.load("sprites/evil cube 5.png")
       ani = 0


   if ani == 0 and level == 3:
       eme = pygame.image.load("sprites/evil webb 1.png")
       eme2 = pygame.image.load("sprites/evil webb 1.png")
   if ani == 100 and level == 3:
       eme = pygame.image.load("sprites/evil webb 2.png")
       eme2 = pygame.image.load("sprites/evil webb 2.png")
   if ani == 200 and level == 3:
       eme = pygame.image.load("sprites/evil webb 3.png")
       eme2 = pygame.image.load("sprites/evil webb 3.png")
   if ani == 300 and level == 3:
       eme = pygame.image.load("sprites/evil webb 4.png")
       eme2 = pygame.image.load("sprites/evil webb 4.png")
   if ani == 400 and level == 3:
       eme = pygame.image.load("sprites/evil webb 5.png")
       eme2 = pygame.image.load("sprites/evil webb 5.png")
   if ani == 500 and level == 3:
       eme = pygame.image.load("sprites/evil webb 6.png")
       eme2 = pygame.image.load("sprites/evil webb 6.png")
       ani = 0








   if ranx < mexh + mesw and rany < meyh + mesh and rany + rans > meyh and ranx + rans > mexh and timeout == False:
       score = 0
       subscore = 1
       scroll = 500
       death = True
       mey = screen.get_height() - 130
       meyh = 320
       ranx = screen.get_width() + rans




   if (ranx2 < mexh + mesw and rany2 < meyh + mesh and rany2 + rans > meyh and ranx2 + rans > mexh and timeout ==
           False and wait > 100):
       score = 0
       subscore = 1
       scroll = 500
       death = True
       mey = screen.get_height() - 130
       meyh = 320
       ranx2 = screen.get_width() + rans
       wait = 0


   if score > highscore:
       highscore = score








       screen.blit(me,(mex,mey))


       screen.blit(eme,(ranx - 27,rany-28))
       screen.blit(eme2, (ranx2 - 27, rany2 - 28))




   if start == False and helps == 0:
       start_text = font2.render("Super cube Adventure", True, (255, 255, 255))
       screen.blit(start_text,
                   (screen.get_width()/2 - start_text.get_width(), 20))
       start2_text = font.render("Press Space to start", True, (255, 255, 255))
       screen.blit(start2_text,
                   (screen.get_width()/2 - start2_text.get_width()+100, screen.get_height()/2))
       start3_text = font.render("Press h for controls and help", True, (255, 255, 255))
       screen.blit(start3_text,
                   (screen.get_width() / 2 - start3_text.get_width() + 150, screen.get_height() / 2 + 40))
       start4_text = font.render(f"{ht}", True, (red, 255, 255))
       screen.blit(start4_text,
                   (screen.get_width() / 2 - start4_text.get_width() + 125, screen.get_height() / 2 + 70))
       if win:
           start3_text = font.render("Press w for endless mode", True, (255, 255, 255))
           screen.blit(start3_text,
                       (screen.get_width() / 2 - start3_text.get_width() + 105, screen.get_height() / 2 + 100))
           if key[pygame.K_w]:
               level = 1
               subscore = 100
               ranx = screen.get_width()+rans
               start = True
       if key[pygame.K_SPACE]:
           start = True
           subscore = 0
           win = False
           winsound.Beep(640,500)
       if key[pygame.K_h]:
           winsound.Beep(640, 500)
           helps = 1


       if key[pygame.K_e]:
           winsound.Beep(640, 500)
           hitbox = True
           red = 200
           ht = "Press w to disable hit boxes"
       if key[pygame.K_w]:
           winsound.Beep(640, 500)
           hitbox = False
           red = 255
           ht = "Press e to enable hit boxes"




   if helps == 1:
       screen.fill((200,100,100))
       start2_text = font2.render("Super cube Adventure", True, (255, 255, 255))
       screen.blit(start2_text,
                   (screen.get_width() / 2 - start2_text.get_width(), 20))
       start3_text = font.render("Use arrow keys to move, Right speeds up and Left slows down", True, (255, 255, 255))
       screen.blit(start3_text,
                   (screen.get_width() / 2 - start3_text.get_width() + 350, screen.get_height() / 2))
       start4_text = font.render("Use up and down to dodge objects", True, (255, 255, 255))
       screen.blit(start4_text,
                   (screen.get_width() / 2 - start4_text.get_width() + 150, screen.get_height() / 2 + 40))
       start5_text = font.render("Press x to return to the menu", True, (255, 255, 255))
       screen.blit(start5_text,
                   (screen.get_width() / 2 - start5_text.get_width() + 150, screen.get_height() / 2 + 80))
       if key[pygame.K_x]:
           helps = 0
           winsound.Beep(640, 500)




   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
   pygame.display.update()


pygame.quit()

