import pygame 
import random


#Set the screen 
screen_size = [360, 600 ]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()


background = pygame.image.load('img/backgroound1.png') #set the screen running motion but we are converting to game loop mode
user = pygame.image.load('img/user1.png')
chicken = pygame.image.load('img/chicken.png')

def display_score(score):
    
    font = pygame.font.SysFont('Comic Sans MS', 30)
    score_text = 'score: ' + str(score)
    text_img = font.render(score_text, True, (0, 255, 0))
    screen.blit(text_img, [20, 10])

def random_offset():
    return -1*random.randint(100, 1500) #this func will return a random CHICKEN position

chicken_y = [random_offset(), random_offset(), random_offset()]
user_x = 150
score = 0


def crashed(index):
    global score
    global keep_alive
    score = score - 5
    chicken_y[index] = random_offset()
    if score < -0:
        print("Game Over")
        keep_alive = False
        


def update_chicken_position(index):
    global score
    if chicken_y[index] > 600:      #we told the chicken to repeat and come from above
        chicken_y[index] = random_offset()
        score = score + 5
        print("Your Score", score)    
    else:
        chicken_y[index] = chicken_y[index] + 5

keep_alive = True
clock = pygame.time.Clock() # we control the chicken how smoothly she run
while keep_alive:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_x < 290:
        
        user_x = user_x + 10    #move the user left right 
        
    elif keys[pygame.K_LEFT] and user_x > 0:
        user_x = user_x - 10
            
        
    
    update_chicken_position(0)
    update_chicken_position(1)
    update_chicken_position(2)
    

    
    screen.blit(background, [0, 0]) #hey when screen is running PLEASE transfer this background img
    screen.blit(user, [user_x, 520]) 
    screen.blit(chicken, [0, chicken_y[0]])
    screen.blit(chicken, [140, chicken_y[1]])
    screen.blit(chicken, [270, chicken_y[2]])
    
    if chicken_y[0] > 500 and user_x < 70:  #crash on chicken 1,2,3
        keep_alive = False
        crashed(0)
        
    if chicken_y[1] > 500 and user_x > 80 and user_x < 200:
        keep_alive = False
        crashed(1)    
          
    if chicken_y[2] > 500 and user_x > 220:
        keep_alive = False
        crashed(2)
    display_score(score)    

        
      
        
        
    
    
    pygame.display.update() # keep update the screen when game loop is running
    clock.tick(60) # we control the chicken how smoothly she run
    


