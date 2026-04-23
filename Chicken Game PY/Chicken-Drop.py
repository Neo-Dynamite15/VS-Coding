import sys
import pygame
import random

pygame.init()

width = 800
height = 600
size = (width, height)
black = (0,0,0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Card Click Game")


clock = pygame.time.Clock()

card = pygame.image.load("Ace.png")
powerup = pygame.image.load("Jester.png")

numofchickens = 5
startX = []
startY = []
speed = []

# Power-up variables
powerup_X = None
powerup_Y = None
powerup_speed = 0.5
powerup_active = False
time_stopped = False
powerup_start_time = 0
time_stop_duration = 5000  # 5 seconds in milliseconds
powerup_spawn_chance = 0.005  # 0.5% chance per frame

for i in range(numofchickens):
  startX.append(random.randint(0, max(0, width - card.get_width())))
  startY.append(0 - random.randint(card.get_height(), card.get_height() * 2))
  speed.append(0.5)

# Spawn initial powerup
def spawn_powerup():
  global powerup_X, powerup_Y, powerup_active
  powerup_X = random.randint(-powerup.get_width() + 50, width - 50)
  powerup_Y = 0 - random.randint(powerup.get_height(), powerup.get_height() * 2)
  powerup_active = True

spawn_powerup()

replayscreen = False
#Set up game over stuff
bigfont = pygame.font.SysFont(None, 200)
playagaintext = bigfont.render("Play Again?", True, (0,200,0))
pax = width/2 - playagaintext.get_rect().width/2

smallfont = pygame.font.SysFont(None, 100)
yestext = smallfont.render("YES", True, (0, 200, 0))
yesx = width/4 - yestext.get_rect().width/2
notext = smallfont.render("NO", True, (0,200,0))
nox = width - width/4 - notext.get_rect().width/2

# Define powerup activation function before game loop
def activate_powerup():
  global time_stopped, powerup_start_time
  time_stopped = True
  powerup_start_time = pygame.time.get_ticks()

#Game Loop

gameover = False

while gameover == False:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameover = True

  #Clicking on the Cards
  if pygame.mouse.get_pressed()[0]:
    coords = pygame.mouse.get_pos()
    if replayscreen == False:
      # Check for powerup collision
      powerup_clicked = False
      if powerup_active:
        if coords[0] >= powerup_X and coords[0] <= powerup_X + powerup.get_width() and coords[1] >= powerup_Y and coords[1] <= powerup_Y + powerup.get_height():
          activate_powerup()
          powerup_active = False
          powerup_clicked = True
      
      # Check for card collision (independent of powerup)
      if not powerup_clicked:
        for i in range(numofchickens):
          if coords[0] >= startX[i] and coords[0] <= startX[i] + card.get_width() and coords[1] >= startY[i] and coords[1] <= startY[i] + card.get_height():
            startX[i] =  random.randint(0, max(0, width - card.get_width()))
            startY[i] = 0 - random.randint(card.get_height(), card.get_height() * 2)
            speed[i] = 0.5
            break
    else:
      if coords[0] >= yesx and coords[0] <= yesx + yestext.get_rect().width and coords[1] >= 450 and coords[1] <= 450 + yestext.get_rect().height:
        for i in range(numofchickens):
          startX[i] =  random.randint(0, max(0, width - card.get_width()))
          startY[i] = 0 - random.randint(card.get_height(), card.get_height() * 2)
          speed[i] = 0.5
        replayscreen = False

      if coords[0] >= nox and coords[0] <= nox + notext.get_rect().width and coords[1] >= 450 and coords[1] <= 450 + notext.get_rect().height:
        gameover = True


  #Updating
  if replayscreen == False:
    # Check if time-stop has expired
    if time_stopped:
      elapsed = pygame.time.get_ticks() - powerup_start_time
      if elapsed >= time_stop_duration:
        time_stopped = False
    
    # Spawn powerup randomly if not active
    if not powerup_active and random.random() < powerup_spawn_chance:
      spawn_powerup()
    
    # Move powerup
    if powerup_active:
      powerup_Y += powerup_speed
      if powerup_Y + powerup.get_height() > height:
        powerup_active = False
    
    # Move cards only if time is not stopped
    if not time_stopped:
      for i in range(numofchickens):
        if startY[i] + card.get_height() > height:
          replayscreen = True
          break
        startY[i] += speed[i]


  #Drawing

  if replayscreen == False:
    screen.fill(black)
    
    # Draw cards
    for i in range(numofchickens):
      screen.blit(card, (startX[i], startY[i]))
    
    # Draw powerup
    if powerup_active:
      screen.blit(powerup, (powerup_X, powerup_Y))
    
    # Draw time-stop indicator
    if time_stopped:
      elapsed = pygame.time.get_ticks() - powerup_start_time
      remaining = max(0, time_stop_duration - elapsed) / 1000
      time_text = pygame.font.SysFont(None, 50).render(f"TIME STOPPED: {remaining:.1f}s", True, (255, 255, 0))
      screen.blit(time_text, (width/2 - time_text.get_rect().width/2, 20))

  else:
    screen.fill((200,0,0))

    screen.blit(playagaintext, (pax, 150))
    screen.blit(yestext, (yesx, 450))
    screen.blit(notext, (nox, 450))

  pygame.display.flip()
  clock.tick(60)



pygame.quit()
sys.exit()