import pygame
import os
import random

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
        self.IsAtttacking = False
        

    def Attack(self):
        
        attacknumber = random.randint(0, 3)
        print(attacknumber)
        if attacknumber == 0:
            Attack_0()
        elif attacknumber == 1:
            Attack_1()
        elif attacknumber == 2:
            Attack_2()
        elif attacknumber == 3:
            Attack_3()
        elif attacknumber == 4:
            Attack_4()
        
        
        

    def ChangeFace(self):
        if self.activeimage == Enemy_image:
            self.activeimage = Enemy_image2
        else:
            self.activeimage = Enemy_image

        self.image = pygame.transform.rotate(pygame.transform.scale(self.activeimage, (self.length, self.height)), 0)

    def Lose_Health(self, damage_value):
        self.health -= damage_value

    def Die(self, timepassed):
        GameOverWin(timepassed)

     
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
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        

    def Move(self):
        pass


class Ball(Projectile):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.xvelocity = 10
        self.yvelocity = .7
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)
        self.IsFinished = False
        

    def Move(self):
        if self.x + self.width > WindowLength or self.x < 0:
            newxvelocity = self.xvelocity * -1
            self.xvelocity = newxvelocity
        self.x += self.xvelocity
        self.y += self.yvelocity
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.y > WindowHeight:
            IsFinished = True

        
class Randomball(Projectile):
    def __init__(self, x, y, width, height, color, xvelocity, yvelocity):
        super().__init__(x, y, width, height, color)
        self.xvelocity = xvelocity
        self.yvelocity = yvelocity
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)
        self.IsFinished = False

    def Move(self):
        self.x += self.xvelocity
        self.y += self.yvelocity
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)


class Laser:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


class Sweep(Laser):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.velocity = 2
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)
        self.attacktimepassed = 0
        self.IsActive = True

    def Move(self):
        self.x += self.velocity
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)

    def SwapActiveState(self):
        if self.IsActive == True:
            self.IsActive = False
        elif self.IsActive == False:
            self.IsActive = True
        

class Bar(Laser):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)
        self.attacktimepassed = 0

    def PopOut(self):
        self.y -= 330
        self.image = pygame.Rect(self.x, self.y, self.width, self.height)


class Tracking(Laser):
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
        self.rectangle = pygame.Rect(self.x, self.y, self.length, self.height)
        self.IsInvincible = False
        
    def Move(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velocity
        if keys_pressed[pygame.K_RIGHT] and self.x + self.length <= WindowLength:
            self.x += self.velocity
        if keys_pressed[pygame.K_DOWN] and self.y + self.height <= self.downlimit:
            self.y += self.velocity
        if keys_pressed[pygame.K_UP] and self.y >= self.uplimit:
            self.y -= self.velocity
        
        self.rectangle = pygame.Rect(self.x, self.y, self.length, self.height)

    def Shoot(self, keys_pressed):
        pass

    def Take_Damage(self):
        if self.IsInvincible == False:
            self.hitpoints -= 1
            self.IsInvincible = True

    def Die(self):
        GameOverLose()


#ATTACKS

def Attack_0():
    attackball = Ball(100, 100, 50, 50, White)
    projectile_list.append(attackball)

number_of_randomballs = 4
def Attack_1():
    #from the top
    for ii in range(0, number_of_randomballs):
        xvelocity = random.randint(-3, 3) 
        yvelocity = random.randint(1, 3)
        xstartingposition = ii * (WindowLength / number_of_randomballs)
        projectile_list.append(Randomball(xstartingposition, 75, 5, 5, White, xvelocity, yvelocity))
    #from the right
    for ii in range(0, number_of_randomballs):
        xvelocity = random.randint(-3, -1) 
        yvelocity = random.randint(-3, 3)
        ystartingposition = ii * (WindowHeight / number_of_randomballs)
        projectile_list.append(Randomball(WindowLength, ystartingposition, 5, 5, White, xvelocity, yvelocity))
    #from the bottom
    for ii in range(0, number_of_randomballs):
        xvelocity = random.randint(-3, 3) 
        yvelocity = random.randint(-3, -1)
        xstartingposition = ii * (WindowLength / number_of_randomballs)
        projectile_list.append(Randomball(xstartingposition, WindowHeight - 70, 5, 5, White, xvelocity, yvelocity))
    #from the left
    for ii in range(0, number_of_randomballs):
        xvelocity = random.randint(1, 3) 
        yvelocity = random.randint(-3, 3)
        ystartingposition = ii * (WindowHeight / number_of_randomballs)
        projectile_list.append(Randomball(0, ystartingposition, 5, 5, White, xvelocity, yvelocity))


def Attack_2():
    sweepinglaser = Sweep(0, 75, 25, WindowHeight - 145, White)
    laser_list.append(sweepinglaser)
    sweep_list.append(sweepinglaser)
    

def Attack_3():
    barlaser1 = Bar(random.randint(0, 450), WindowHeight - 90, 50, 400, White)
    barlaser2 = Bar(random.randint(0, 450), WindowHeight - 90, 50, 400, White)
    laser_list.append(barlaser1)
    laser_list.append(barlaser2)

def Attack_4():
    pass



#better way to draw stuff [make sure every object in object_list has an image, x, and y, property, or else this goes to shit]
def Drawing_Function(object_list, timetextsurface):
    
    for ii in object_list:
        Window.blit(ii.image, (ii.x, ii.y))
    Window.blit(timetextsurface, (100, 450))
    
    pygame.display.update()

def Drawing_Enemy(enemy): 
    
    Window.blit(enemy.image, (enemy.x, enemy.y))
    
    pygame.display.update()

def Drawing_Player(player):
    Window.blit(player.image, (player.x, player.y))
    pygame.display.update()

def Drawing_Rectangles(shape_list, bullet_list, shield_list):
    for ii in shape_list:
        pygame.draw.rect(Window, ii.color, ii.image)
    for ii in bullet_list:
        pygame.draw.rect(Window, ii.color, ii.image)
    for ii in shield_list:
        pygame.draw.rect(Window, ii.color, ii.image)
    pygame.display.update()
    

def Drawing_Projectiles(projectile_list):
    for ii in projectile_list:
        pygame.draw.rect(Window, ii.color, ii.image)
    pygame.display.update()

def Drawing_Lasers(laser_list):
    for ii in laser_list:
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

  
#Loading in the images and sounds
Spaceship_image = pygame.image.load("./BulletHellAssets/pixilart-drawing (1).png")
Enemy_image = pygame.image.load(r"./BulletHellAssets/froggyboss.png")
Enemy_image2 = pygame.image.load(r"./BulletHellAssets/froggyboss2.png")
Heart_image = pygame.image.load(r"./BulletHellAssets/rainbowheart.png")
pygame.mixer.init(44100, -16, 2, 2048)
Song = pygame.mixer.music.load("./BulletHellSounds/vvvvvvv.version2.wav")
warningsound = pygame.mixer.Sound("./BulletHellSounds/warningsound.wav")
pygame.mixer.music.play(-1) 

def PlayWarningSound():
    pygame.mixer.Sound.play(warningsound)


#this is list of every object that needs to get drawn to the screen
object_list = []
rect_list = []
bullet_list = []
shield_list = []
projectile_list = []
laser_list = []
sweep_list = []

#main function. runs when the program starts
def main():

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
    invincibility_timer = 0
    Attackcounter = 0
    object_list.append(Heart1)
    object_list.append(Heart2)
    object_list.append(Heart3)
    rect_list.append(EnemyHealthBar)
    rect_list.append(HUD)

    

    #initial drawing functions
    '''
    Reset_Screen()
    Drawing_Function(object_list, UpdatedTime(TimePassed))
    Drawing_Rectangles(rect_list, bullet_list, shield_list)
    Drawing_Projectiles(projectile_list)
    Drawing_Lasers(laser_list)
    Drawing_Player(Player)
    Drawing_Enemy(MainEnemy)
    '''
 
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
            MainEnemy.Die(TimePassed)
            run = False

        #Handles the player dying  
        if Player.hitpoints == 0:
            Player.Die()
            run = False
        
        
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
            

        #Handles projectile movement and collision
        for ii in projectile_list:
            ii.Move()
            if Player.rectangle.colliderect(ii.image):
                Player.Take_Damage()
            if ii.x > WindowLength + 50 or ii.x < -50:
                projectile_list.remove(ii)
            elif ii.y > WindowHeight + 50 or ii.y < -50:
                projectile_list.remove(ii)
                


        #Handles laser collision
        for ii in laser_list:
            if Player.rectangle.colliderect(ii.image):
                Player.Take_Damage()
        
        #Handles sweep laser movement
        for ii in sweep_list:
            ii.Move()
            ii.attacktimepassed += 1
            if ii.attacktimepassed == 40:
                ii.SwapActiveState()
                ii.attacktimepassed = 0
                if ii.IsActive == True:
                    laser_list.append(ii)
                else:
                    laser_list.remove(ii)
            if ii.x > WindowLength + 50:
                sweep_list.remove(ii)
                laser_list.remove(ii)

        #Handles bar laser pop up 
        for ii in laser_list:
            if type(ii) is Bar:
                ii.attacktimepassed += 1
                if ii.attacktimepassed == 60:
                    ii.PopOut()
                if ii.attacktimepassed == 180:
                    laser_list.remove(ii)
                    

        
        #Handles invincibility
        if Player.IsInvincible == True:
            invincibility_timer += 1
            if invincibility_timer == 180:
                Player.IsInvincible = False
                invincibility_timer = 0


        #this is the way i wanted to do attacks but its being fickle right now, so instead ill just have it attack every 4 seconds or so
        '''
        if len(projectile_list) == 0 and len(laser_list) == 0 and len(sweep_list) == 0:
            MainEnemy.IsAtttacking == False

        print(len(projectile_list))
        print(len(laser_list))
        print(MainEnemy.IsAtttacking)
        
        #Starts an attack
        if MainEnemy.IsAtttacking == False:
            MainEnemy.IsAtttacking = True
            MainEnemy.Attack()
        '''
        Attackcounter += 1
        if Attackcounter == 120:
            PlayWarningSound()
        if Attackcounter == 180:
            MainEnemy.Attack()
            Attackcounter = 0


        #Graphics
        Reset_Screen()
        Drawing_Rectangles(rect_list, bullet_list, shield_list)
        Drawing_Projectiles(projectile_list)
        Drawing_Player(Player)
        Drawing_Lasers(laser_list)
        Drawing_Function(object_list, UpdatedTime(TimePassed))
        Drawing_Enemy(MainEnemy)
        
        


    pygame.quit()


def GameOverWin(timepassed):
    print("You Win!!!")
    print(f"It took you {timepassed} seconds to beat the dude!") 

def GameOverLose():
    print("You Lose!!!")
    

 

#this line of code makes it stay open. not really sure what the condition is, but it calls the main(), so its whatever
if __name__ == "__main__":
    #write main() here
    main()
