import pygame
import os
from PIL import Image

#The variables and such
FPS = 60
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
HealthColor = (199, 26, 26)

#Making the window
WindowHeight = 500
WindowLength = 500
Window = pygame.display.set_mode((WindowLength, WindowHeight))
pygame.display.set_caption("Bullet Hell")


#classes
class Enemy:
    def __init__(self, health, x, y, length, height, imported_image):
        self.health = health
        self.x = x
        self.y = y
        self. length = length
        self.height = height
        self.activeimage = imported_image 
        self.image = pygame.transform.rotate(pygame.transform.scale(self.activeimage, (self.length, self.height)), 0)
        self.imagelistvalue = None
        self.enemy_rectangle = pygame.Rect(self.x, self.y, self.length, self.height)
        

    def Attack(self):
        pass

    def ChangeFace(self):
        if self.activeimage == Enemy_image:
            self.activeimage = Enemy_image2
        else:
            self.activeimage = Enemy_image

        self.image = pygame.transform.rotate(pygame.transform.scale(self.activeimage, (self.length, self.height)), 0)

    def Lose_Health(self, damage_value):
        self.health -= damage_value

    def Die(self):
        GameOverWin()

    
        


class Shield:
    def __init__(self, x, y):
        self.x = x
        self.initialx = x
        self.y = y
        self.length = 35
        self.height = 3
        self.movevalue = 0
        self.velocity = .5
        self.image = pygame.Rect(self.x, self.y, self.length, self.height)
        self.color = White
        self.MoveLimit = 30
        self.IsMovingLeft = True

    def MoveLeft(self):
        if self.initialx - self.x == self.MoveLimit:
            self.IsMovingLeft = False
            self.MoveRight()
        elif self.IsMovingLeft == False:
            self.MoveRight()
        else:
            self.x -= self.velocity
            self.image = pygame.Rect(self.x, self.y, self.length, self.height)

    def MoveRight(self):
        if self.x - self.initialx == self.MoveLimit:
            self.IsMovingLeft = True
            self.MoveLeft()
        else:
            self.x += self.velocity
            self.image = pygame.Rect(self.x, self.y, self.length, self.height)
        


class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Damage(self):
        pass

    def Move(self):
        pass


class Laser:
    def __init__(self):
        pass

    def Damage(self):
        pass


class Bullet:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.width = 3
        self.height = 10
        self.velocity = 4
        self.color = Red
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)
        self.damage_value = 1


    def Move(self):
        self.y -= self.velocity
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)



class HealthBar:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        self.imagelistvalue = None


    def RemoveHealth(self, totalhealth):
        self.width = WindowLength * (totalhealth / 100)
        self.image = pygame.rect.Rect(self.x, self.y, self.width, self.height)


class HUDBackground:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)
        self.imagelistvalue = None


class Heart:
    def __init__(self, x, y, width, height, image, healthvalue):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.rotate(pygame.transform.scale(image, (self.width, self.height)), 0)
        self.healthvalue =  healthvalue
        self.imagelistvalue = None


class Spaceship:
    def __init__(self, x, y, length, height, velocity, image):
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.velocity = velocity
        self.image = pygame.transform.rotate(pygame.transform.scale(image, (self.length, self.height)), 0)
        #uplimit is the y point that the character cannot move above. same with downlimit
        self.uplimit = 80
        self.downlimit = WindowHeight - 70
        self.hitpoints = 3
        self.imagelistvalue = None
        self.bulletlimit = 3
        
    def Move(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velocity
        if keys_pressed[pygame.K_RIGHT] and self.x + self.length <= WindowLength:
            self.x += self.velocity
        if keys_pressed[pygame.K_DOWN] and self.y + self.height <= self.downlimit:
            self.y += self.velocity
        if keys_pressed[pygame.K_UP] and self.y >= self.uplimit:
            self.y -= self.velocity

    def Shoot(self, keys_pressed):
        pass

    def Take_Damage(self):
        self.hitpoints -= 1

    def Die(self):
        pass








#draws stuff
'''
def Draw_Window():
    Window.fill(Black)
    Window.blit(Player.image, (200, 200))
    pygame.display.update()
'''

#better way to draw stuff [make sure every object in object_list has an image, x, and y, property, or else this goes to shit]
def Drawing_Function(object_list, timetextsurface):   
    for ii in object_list:
        Window.blit(ii.image, (ii.x, ii.y))
    Window.blit(timetextsurface, (100, 450))
    pygame.display.update()

def Drawing_Rectangles(shape_list, bullet_list, shield_list):
    for ii in shape_list:
        pygame.draw.rect(Window, ii.color, ii.image)
    for ii in bullet_list:
        pygame.draw.rect(Window, ii.color, ii.image)
    for ii in shield_list:
        pygame.draw.rect(Window, ii.color, ii.image)
    pygame.display.update()
    
def Reset_Screen():
    Window.fill(Black)

#handles the timer thingy at the bottom of the screen
pygame.font.init()
myfont = pygame.font.SysFont('Sans Serif MS', 30)
def UpdatedTime(time):
    timetextsurface = myfont.render(f"Time: {time}", False, (0, 0, 0))
    return timetextsurface



    
#Loading in the images
Spaceship_image = pygame.image.load("../BulletHellAssets/pixilart-drawing (1).png")
Enemy_image = pygame.image.load(r"../BulletHellAssets/froggyboss.png")
Enemy_image2 = pygame.image.load(r"../BulletHellAssets/froggyboss2.png")
Heart_image = pygame.image.load(r"../BulletHellAssets/rainbowheart.png")





#main function. runs when the program starts
def main():
    
    #this is list of every object that needs to get drawn to the screen
    object_list = []
    rect_list = []
    bullet_list = []
    shield_list = []

    #initial objects getting created
    Player = Spaceship(200, 200, 50, 25, 6, Spaceship_image)
    MainEnemy = Enemy(100, 0, 10, 500, 50, Enemy_image)
    EnemyHealthBar = HealthBar(0, 0, 500, 10, HealthColor)
    HUD = HUDBackground(0, WindowHeight - 70, WindowLength, 70, White)
    Heart1 = Heart(300, WindowHeight - 50, 25, 25, Heart_image, 1)
    Heart2 = Heart(350, WindowHeight - 50, 25, 25, Heart_image, 2)
    Heart3 = Heart(400, WindowHeight - 50, 25, 25, Heart_image, 3)
    
    number_of_shields = 7
    length_between_shields = 10
    for ii in range(number_of_shields):
        shield = Shield((ii * (WindowLength // number_of_shields)) + (ii * length_between_shields), 75)
        shield_list.append(shield)


    #initial objects getting drawn [make sure the right object gets added to the right list]
    EnemyGraphicsCounter = 0
    TimePassed = 0
    TimeCounter = 0
    object_list.append(Player)
    object_list.append(MainEnemy)
    object_list.append(Heart1)
    object_list.append(Heart2)
    object_list.append(Heart3)
    rect_list.append(EnemyHealthBar)
    rect_list.append(HUD)

    

    #initial drawing functions
    Reset_Screen()
    Drawing_Function(object_list, UpdatedTime(TimePassed))
    Drawing_Rectangles(rect_list, bullet_list, shield_list)


    #function that handles heart removal
    def HeartRemoval(Player):
        if Player.hitpoints < Heart3.healthvalue:
            if Heart3 in object_list:
                object_list.remove(Heart3)
        if Player.hitpoints < Heart2.healthvalue:
            if Heart2 in object_list:
                object_list.remove(Heart2)
        if Player.hitpoints < Heart1.healthvalue:
            if Heart1 in object_list:
                object_list.remove(Heart1)


    clock = pygame.time.Clock()
    run = True
    while run == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and len(bullet_list) <= Player.bulletlimit:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(Player.x + Player.length//2, Player.y)
                    bullet_list.append(bullet)
                    

        #everything here happens every time loop
        
        #handles player movement
        keys_pressed = pygame.key.get_pressed()
        Player.Move(keys_pressed)
        Player.Shoot(keys_pressed)

        

        #handles enemy graphics change
        EnemyGraphicsCounter += 1
        if EnemyGraphicsCounter == 40:
            MainEnemy.ChangeFace()
            EnemyGraphicsCounter = 0
            
        #Handles the removal of enemy health
        EnemyHealthBar.RemoveHealth(MainEnemy.health)
        if MainEnemy.health <= 0:
            MainEnemy.Die()
            run = False

        #Handles the player dying  
        if Player.hitpoints == 0:
            Player.Die()
        
        
        #Handles the removal of player health hearts
        HeartRemoval(Player)
        
        #Handles the unstoppable passing of time that will eventually kill us all 
        TimeCounter += 1
        if TimeCounter == FPS:
            TimePassed += 1
            TimeCounter = 0

        #Handles bullet movement and collision
        for bullets in bullet_list:
            bullets.Move()
            if MainEnemy.enemy_rectangle.colliderect(bullets.image):
                MainEnemy.Lose_Health(bullets.damage_value)
                bullet_list.remove(bullets)
            for ii in shield_list:
                if ii.image.colliderect(bullets.image):
                    bullet_list.remove(bullets)
        
        #Handles sheild movement
        for ii in shield_list:
            ii.MoveLeft()
            




        #running the graphics functions
        Reset_Screen()
        Drawing_Rectangles(rect_list, bullet_list, shield_list)
        Drawing_Function(object_list, UpdatedTime(TimePassed))


        


    pygame.quit()


def GameOverWin():
    print("You Win!!!")

def GameOverLose():
    print("You Lose!!!")




#this line of code makes it stay open. not really sure what the condition is, but it calls the main(), so its whatever
if __name__ == "__main__":
    #write main() here
    main()
