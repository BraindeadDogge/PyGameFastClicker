import pygame
from random import randint
from time import time
class Area():
    def __init__(self, x = 0, y = 0, width = 10, height = 10, color=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)

class Label(Area):
    def __init__(self, x = 0, y = 0, width = 10, height = 10, color=None):
        super().__init__(x, y, width, height, color)
        self.x = x
        self.y = y
    def set_text(self, text = "CLICK", fsize = 50, text_color = "BLACK"):
        self.text = text
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x = 0, shift_y = 0):
        self.fill()
        mw.blit(self.image, (self.x + shift_x, self.y + shift_y))
    

pygame.init()
mw = pygame.display.set_mode((500,500))
mw.fill((200,255,255))
clock = pygame.time.Clock()

cards = list()
l1 = Label(5,50,115,200,(255,255,0))
l2 = Label(130,50,115,200,(255,255,0))
l3 = Label(255,50,115,200,(255,255,0))
l4 = Label(380,50,115,200,(255,255,0))
cards.append(l1)
cards.append(l2)
cards.append(l3)
cards.append(l4)

for i in range(4):
    cards[i].set_text()

start_time = time()
cur_time = start_time
new_time = start_time

time_text = Label(0,0,50,50,(200,255,255))
score_text = Label(450,0,50,50,(200,255,255))


wait = 0
score = 0

while True:
    if new_time - start_time >= 2:
        win = Label(0,0,500,500,(255,0,0))
        win.set_text("Время вышло!", 60, "DARK_BLUE")
        win.draw(110,180)
        pygame.display.update()
        clock.tick(1)
        continue

    new_time = time()
    if new_time - cur_time >= 1:
        time_text.set_text(str(int(new_time - start_time)),40, "DARK_BLUE")
        time_text.draw(0,0)
        cur_time = new_time
    if wait == 0:
        wait = 60
        click = randint(1, len(cards))
        for i in range(len(cards)):
            cards[i].color((255,255,0))
            if (i+1) == click:
                cards[i].draw(10,70)
            else:
                cards[i].fill()
    else:
        wait -= 1

    x = 0 
    y = 0
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos

    for i in range(len(cards)):
        if cards[i].collidepoint(x,y):
            if i + 1 == click:
                cards[i].color((0,255,0))
                cards[i].draw(10,70)
                score += 1
                score_text.set_text(str(score),40, "DARK_BLUE")
                score_text.draw(0,0)
            else:
                cards[i].color((255,0,0))
                cards[i].fill()
                score -= 1
                score_text.set_text(str(score),40, "DARK_BLUE")
                score_text.draw(0,0)

    pygame.display.update()
    clock.tick(60)
