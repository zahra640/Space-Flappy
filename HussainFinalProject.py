#Zahra Hussain
#Nov 10, 2021
#Final Project
#------ SPACE FLAPPY --------
#GAME IDEA - - - - character is controlled with the space key - jumping up preventing the ufo from falling -  there are space aestroids/meteors and satellites flying around the air that your character has to avoid - collect coins to add to your score. 
#add in planets in the background that pass by at random time and spots and there are white circles as stars

import pygame
import random
pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
#INPUT COLORS
SPACE_BACKGROUND = (0, 0, 40)
GREY = (150, 150, 150)
BLUE = (0, 0, 255)
GREEN = (0, 150, 0)
GREEN1 = (100, 230, 20)
REDISH = (200, 170, 150)
SATELITE = (235, 78, 187)
COINS = (240, 170, 120)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (225, 0, 0)
GAME_OVER_BACKGROUND = (50, 50, 50)
DARK_BLUE = (0, 0, 40)
STARS = (255, 246, 224)

#Screen mode will dictate which screen is drawn
#1 - Intro Screen, 2 - Main Screen, etc.
#Start with intro screen
screen_mode = 1

#Some text for visualizing the different screens
#text set up for screen mode 1 - intro screen
font = pygame.font.SysFont('Calibri', 30, True, False)
titlefont = pygame.font.SysFont('Calibri', 40, True, False)
gameTitle = titlefont.render("WELCOME TO SPACE FLAP!", True, WHITE)
introText = font.render("Control the rocket ship by pressing the space key.", True, WHITE)
introTextTwo = font.render("Try to avoid the Meteorites and satellites!", True, WHITE)
instructionText = font.render("Press 'i' for more instructions!", True, WHITE)
startText = font.render("Click the screen to play!", True, WHITE)

#text set up for screen mode 2 - still start screen
playText = font.render("press space to start!", True, WHITE)
#text set up for screen mode 4 - game over screen
gameoverText = font.render("Game Over!", True, BLACK)
#text set up for screen 5 - instruction screen
instructionfont = pygame.font.SysFont('Calibri', 20, True, False)
howtoplayOne = font.render("Press the space key to prevent the UFO from falling!", True, BLACK)
howtoplayTwo = font.render("Try to collect coins to boost your score!", True, BLACK)
howtoplayThree = font.render("Avoid hitting the asteroids/meteorites, and satellites!", True, BLACK)
howtoplayFour = font.render("The game will speed up once your score reaches 200!", True, BLACK)
howtoplayFive = font.render("Press the down key to go back to the main screen!", True, BLACK)

#score variable
high_score = 0
score = 0

#UFO variables
x = 300
y = 200
sy = 1

#VARIBLES FOR METEORITES - METEOR 1
m_x1_move = random.randrange(1, 5)
m_y1_move = random.randrange(1, 5)
m_r1 = random.randrange(5, 10)
m_x1 = random.randrange(1, 700)
m_y1 = 0
#VARIBLES FOR METEORITES - METEOR 2
m_x2_move = random.randrange(1, 5)
m_y2_move = random.randrange(1, 5)
m_r2 = random.randrange(5, 10)
m_x2 = random.randrange(1, 700)
m_y2 = 0
m_x2 = random.randrange(1, 5)

#set up for stars
#Star variable
star_list_x = []
star_list_y = []
for i in range(50):
  numx = random.randrange(0, 700)
  numy = random.randrange(0, 500)
  star_list_x.append(numx)
  star_list_y.append(numy)
  
star_x = 100
star_y2 = random.randrange(1, 500)
star_move = 1
star_radius = random.randrange(1, 5)


#IMPORTING PHOTOS and setting up variables for the photos
#Satellite
satelliteImg = pygame.image.load('satellite1.png')
satelliteImg = pygame.transform.scale(satelliteImg, (178, 100))
satx = 450
satx_move = random.randrange(1,5)
saty = random.randrange(0, 500)
#COIn
#COIN VARIABLE
x_coin = 700
y_coin = random.randrange(10, 480)
x_coin2 = random.randrange(700)
y_coin2 = random.randrange(10, 480)
coin_move = satx_move
coin_move2 = satx_move
#IMPORT COIN PHOTO
coinImg = pygame.image.load('gold_coin.png')
coinImg = pygame.transform.scale(coinImg, (20, 20))
#IMPORT METEORITE PHOTO - for now meterites are yellow circles
meteorImg = pygame.image.load('meteor8.png')
meteorImg = pygame.transform.scale(meteorImg, (60, 60))
#import spaceship
ufoImg = pygame.image.load('ufo1.png')
ufoImg = pygame.transform.scale(ufoImg, (70, 27))
#import game over
gameoverImg = pygame.image.load('gameover13.png')
#import play again
playagainImg = pygame.image.load('play again.png')
playagainImg = pygame.transform.scale(playagainImg, (200, 64))
#background Image for intro screen
backgroundIntroImg = pygame.image.load('planet.jpg')
backgroundIntroImg = pygame.transform.scale(backgroundIntroImg, (700, 500))
#PRINT PLANETS
#earth
earthplanet = pygame.image.load('Planet_earthlike.png')
earthplanet = pygame.transform.scale(earthplanet, (40, 40))
#jupiter
jupiter = pygame.image.load('jupiter.png')
jupiter = pygame.transform.scale(jupiter, (50, 50))

#Variable for planet
PLANET = earthplanet
planet_move = star_move + 1
planetx = 700
planety = random.randrange(1, 499)


done = False
while not done:
  
  #INTRO SCREEN 
  if screen_mode == 1:
    
    #screen with info and click screen to play
    screen.blit(backgroundIntroImg, [0, 0])
    screen.blit(gameTitle, [130, 80])
    pygame.draw.line(screen, WHITE, [128, 125], [580, 125], 5)
    screen.blit(introText, [50, 150])
    screen.blit(introTextTwo, [90, 200])
    screen.blit(instructionText, [50, 450])
    if pygame.time.get_ticks() > 2000:
      screen.blit(startText, [210, 300])
    
    
  #print still start image - BEFORE START GAME
  elif screen_mode == 2:
    #reset variables for when someone presses "play again"
    score = 0
    y = 200
    m_y1 = 0
    m_y2 = 0
    satx = 450
    star_move = 1
    #draw background 
    screen.fill(SPACE_BACKGROUND)
    #draw stars
    for i in range(50):
      pygame.draw.circle(screen, WHITE, [(star_list_x[i]), (star_list_y[i])], 2) 
    #draw ufo, satellite, and writing
    screen.blit(ufoImg, [x, int(y)])
    screen.blit(satelliteImg, [satx, saty])
    screen.blit(playText, [220, 300])
   
  #SCREEN MODE 3 
  #START GAME  
  elif screen_mode == 3:
    #===============DRAW HERE====================
    screen.fill(SPACE_BACKGROUND)
    
    #PLANETS
    #display planet
    screen.blit(PLANET, [planetx, planety])
    planet_move = star_move + 1
    planetx = planetx - planet_move
    #if the planet is out of screen then - put planet in different spot and maybe chnage the planet
    if planetx <= -100:
      planetx = 1000
      planety = random.randrange(1, 499)
      num = random.randrange(1, 10)
      if num <= 3:
        PLANET = earthplanet
      if num > 3 and num <= 5:
        PLANET = jupiter           
      
    #STARS  - print the stars
    for i in range(50):
      pygame.draw.circle(screen, WHITE, [(star_list_x[i]), (star_list_y[i])], 2)
      star_list_x[i] = star_list_x[i] - star_move
      if star_list_x[i] < 0:
        star_list_x[i] = 700
        numy = random.randrange(0, 500)
        star_list_y.append(numy)        
      if score > 150:
        star_move = 3
           
    #Drawing a falling mechanic
    screen.blit(ufoImg, [x, y])
    sy = sy + 1
    #make it hit the ground
    if y >= 490 or y < 0:
      screen_mode = 4
      y = y
    else:
      y = y + sy
    
    
    #DRAW METEROTITES  

    #Metorite 1
    screen.blit(meteorImg, [m_x1, m_y1])
    m_x1 = m_x1 + m_x1_move
    m_y1 = m_y1 + m_y1_move
    if m_y1 >= 500:
      m_x1 = m_x1 + random.randrange(5, 10) * -1
      m_y1_move = random.randrange(1, 5) * -1
    #if m_y1 < (-m_r1 * 2):
    if m_y1 <= -100:
      m_x1 = m_x1 + random.randrange(5, 10)
      m_y1_move = random.randrange(1, 5)
    if m_x1 >= 700:
      m_y1 = m_y1 + random.randrange(5, 10)
      m_x1_move = random.randrange(1, 5) * -1
    #if m_x1 < (-m_r1 * 2):
    if m_x1 <= -100:
      m_y1 = m_y1 + random.randrange(5, 10)
      m_x1_move = random.randrange(1, 5)
      
    
    #SECOND METEROITE
    screen.blit(meteorImg, [m_x2, m_y2])
    m_x2 = m_x2 + m_x2_move
    m_y2 = m_y2 + m_y2_move
    if m_y2 >= 500:
      m_x2 = m_x2 + random.randrange(5, 10) * -1
      m_y2_move = random.randrange(1, 5) * -1
    #if m_y2 < (-m_r2 * 2):
    if m_y2 <= -100:
      m_x2 = m_x2 + random.randrange(5, 10)
      m_y2_move = random.randrange(1, 5)
    if m_x2 >= 700:
      m_y2 = m_y2 + random.randrange(5, 10)
      m_x2_move = random.randrange(1, 5) * -1
    #if m_x2 < (-m_r2 * 2):
    if m_x2 <= -100:
      m_y2 = m_y2 + random.randrange(5, 10)
      m_x2_move = random.randrange(1, 5)

    #SATELITE
    #sraw satellite and make it move - if it leaves screen make it come back into frame
    screen.blit(satelliteImg, [satx, saty])
    satx = satx - satx_move
    if satx < -200:
      satx = 700
      satx_move = random.randrange(2, 5)
      saty = random.randrange(1, 500)
    if score > 150:
      satx_move = random.randrange(4, 7)
  
    #COINS for points 
    #first coin
    screen.blit(coinImg, [x_coin, y_coin])
    x_coin = x_coin - coin_move
    if x_coin < -10:
      x_coin = 700
      coin_move = random.randrange(2, 5)
      y_coin = random.randrange(1, 480)
    if star_move >= 3:
      coin_move2 = random.randrange(4, 7)    
    #second coin
    screen.blit(coinImg, [x_coin2, y_coin2])
    x_coin2 = x_coin2 - coin_move2  
    if x_coin2 < -10:
      x_coin2 = 700
      coin_move2 = random.randrange(2, 5)
      y_coin2 = random.randrange(1, 480)   
    if star_move >= 3:
      coin_move2 = random.randrange(4, 7)
      
    #If UFO hits satellite - change screen to game over
    if abs((satx + 89) - (x + 35)) < 89:
      if abs((saty + 50) - (y + 13.5)) < 40:
        screen_mode = 4
        
    #If UFO hits a meteor - change screen to game over
    #meteor 1
    if abs((m_x1 + 30) - (x + 35)) < 30:
      if abs((m_y1 + 30) - (y + 13.5)) < 30:  
        screen_mode = 4
    #meteor 2
    if abs((m_x2 + 30) - (x + 35)) < 30:
      if abs((m_y2 + 30) - (y + 13.5)) < 30:  
        screen_mode = 4  
        
      
    #if character and coin touch then the user gets 50 points
    #first coin
    if abs((x_coin + 10) - (x + 35)) < 15:
      if abs((y_coin + 10) - (y + 13.5)) < 15:
        y_coin = 1000
        score = score + 50   
    #second coin
    if abs((x_coin2 + 10) - (x + 35)) < 15:
      if abs((y_coin2 + 10) - (y + 13.5)) < 15:
        y_coin2 = 1000
        score = score + 50    
        
        
    #keep track of score and high score   
    highscoreText = font.render("High Score:" + str(high_score), True, WHITE)
    scoreText = font.render("Your Score:" + str(score), True, WHITE)
    #print the score and highscore
    screen.blit(scoreText, [10, 10])
    if score > high_score:
      high_score = score
    else:
      high_score = high_score
    screen.blit(highscoreText, [10, 50])    
       
    
    #GAME OVER SCREEN
    if screen_mode == 4:
      screen.fill(GAME_OVER_BACKGROUND)
      #PRINT A GAME OVER PICTURE - PRINT HIGHSCORE AND SCORE - PRINT "CLICK HERE TO PLAY AGAIN"
      screen.blit(backgroundIntroImg, [0, 0])
      screen.blit(gameoverImg, [200, 100])
      screen.blit(playagainImg, [250, 350])
      
      screen.blit(scoreText, [500, 10])
      screen.blit(highscoreText, [500, 50])      
      
  if screen_mode == 5:
    screen.fill(WHITE)
    #press space to keep the ufo from falling - print a photo of the ufo
    screen.blit(howtoplayOne, [30, 10])
    screen.blit(ufoImg, [300, 50])
    
    #Try to collect coins to boost your score - print a photo of a coin
    screen.blit(howtoplayTwo, [80, 100])
    screen.blit(coinImg, [320, 135])
    
    #Avoid hitton the astroids/meteroites and satelites - print a photo of both satelite and meteor
    screen.blit(howtoplayThree, [20, 175])
    #screen.blit(meteorImg, [260, 195])
    screen.blit(meteorImg, [200, 215])
    screen.blit(satelliteImg, [360, 215])
    
    #Game will speed up one score is 200
    screen.blit(howtoplayFour, [20, 350])  
    
    #press the down arrow to go back to main screen
    screen.blit(howtoplayFive, [40, 430])
    
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

    if event.type == pygame.KEYDOWN:
      #change screen from still start to actual game play screen 
      if screen_mode == 2 and event.key == pygame.K_SPACE:
        screen_mode = 3  
      #jumping mechanic
      if screen_mode == 3 and event.key == pygame.K_SPACE:
        y = y - 4
        sy = -10
      #instructions screen
      if screen_mode == 1 and event.key == pygame.K_i:
        screen_mode = 5
      #exit instruction screen
      if screen_mode == 5 and event.key == pygame.K_DOWN:
        screen_mode = 1
        
    #if mouse is clicked    
    if event.type == pygame.MOUSEBUTTONDOWN:
      #change screen from intro to still start
      if screen_mode == 1:
        screen_mode = 2  
      #change screen from game over to still start to play again
      if screen_mode == 4:
        screen_mode = 2

  pygame.display.flip()
  clock.tick(60)
        
  
pygame.quit()