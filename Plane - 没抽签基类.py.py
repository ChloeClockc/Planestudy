import pygame
from pygame.locals import *
import time
import random


class HeroPlane(object):
    # 飞机的类
    def __init__(self, screen_tmp):
        self.x = 210
        self.y = 700
        self.screen = screen_tmp
        self.image = pygame.image.load("./feiji/hero1.png")
        # 存储发射的子弹对象引用
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        # 显示所有发射子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge(): #判断子弹是否越界
                self.bullet_list.remove(bullet)
    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class EnemyPlane(object):
    # 敌人飞机的类
    def __init__(self, screen_tmp):
        self.x = 0
        self.y = 0
        self.screen = screen_tmp
        self.image = pygame.image.load("./feiji/enemy0.png")
        # 存储发射的子弹对象引用
        self.bullet_list = []
        #用来存储飞机移动方向
        self.direction = "right"


    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        # 显示所有发射子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge(): #判断子弹是否越界
                self.bullet_list.remove(bullet)
    def move(self):

        if self.direction=="right":
            self.x += 5
        elif self.direction=="left":
            self.x -= 5
        if self.x>480-50: #窗口宽度减去飞机宽度
            self.direction = "left"
        elif self.x<0:
            self.direction = "right"



    def fire(self):
        random_num =random.randint(1, 100)#1到100随机产生数字 为8或0时候发射子弹
        if random_num==8 or  random_num==20:
                self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class Bullet(object):
    def __init__(self, screen_tmp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_tmp
        self.image = pygame.image.load("./feiji/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -=5

    def judge(self):
        if self.y<0:
            return True
        else:
            return False

class EnemyBullet(object):
    def __init__(self, screen_tmp, x, y):
        self.x = x+25
        self.y = y+40
        self.screen = screen_tmp
        self.image = pygame.image.load("./feiji/bullet1.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 5

    def judge(self):
        if self.y>852:
            return True
        else:
            return False
def key_control(hero_tmp):
    #   控制键盘输入的函数 接受hero_tmp 参数

    # 获取事件，比如按键等
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_tmp.move_left()
                # x -= 5
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_tmp.move_right()
                # x += 5
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_tmp.fire()


def main():
    # 1.创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2. 创建一个背景
    background = pygame.image.load("./feiji/background.png")

    # 3. 创建一个飞机对象
    hero = HeroPlane(screen)

    # 4. 创建一个敌人飞机对象
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background, (0, 0))

        hero.display()

        enemy.display()

        enemy.move()

        enemy.fire()

        pygame.display.update()

        key_control(hero)

        time.sleep(0.01)


if __name__ == "__main__":
    main()
