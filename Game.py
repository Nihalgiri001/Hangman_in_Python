import pygame
from pygame.locals import * import sys
import time import random

class Game:

def  init (self): self.w = 750
self.h = 500 self.reset = True self.active = False self.input_text = '' self.word = '' self.time_start = 0
self.total_time = 0
self.accuracy = '0%'
self.results = 'Time:0 Accuracy:0 % Wpm:0 ' self.wpm = 0
self.end = False
self.HEAD_C = (255, 213, 102)
self.TEXT_C = (240, 240, 240)
self.RESULT_C = (255, 70, 70)

pygame.init()
self.open_img = pygame.image.load('type-speed-open.png') self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))

self.bg = pygame.image.load('background.jpg') self.bg = pygame.transform.scale(self.bg, (500, 750))

self.screen = pygame.display.set_mode((self.w, self.h)) pygame.display.set_caption('Type Speed test')

self.easy_sentences = open('easy.txt').read().split('\n') self.medium_sentences = open('medium.txt').read().split('\n') self.hard_sentences = open('hard.txt').read().split('\n')

def draw_text(self, screen, msg, y, fsize, color): font = pygame.font.Font(None, fsize)
text = font.render(msg, 1, color)
text_rect = text.get_rect(center=(self.w / 2, y))
 
screen.blit(text, text_rect) pygame.display.update()

def get_sentence(self, level): if level == 'e':
return random.choice(self.easy_sentences) elif level == 'm':
return random.choice(self.medium_sentences) elif level == 'h':
return random.choice(self.hard_sentences) else:
return ''

def show_results(self, screen): if not self.end:
self.total_time = time.time() - self.time_start

count = 0
for i, c in enumerate(self.word): try:
if self.input_text[i] == c: count += 1
except:
pass
self.accuracy = count / len(self.word) * 100

self.wpm = len(self.input_text) * 60 / (5 * self.total_time) self.end = True
print(self.total_time)

self.results = 'Time:' + str(round(self.total_time)) + " secs Accuracy:" + str( round(self.accuracy)) + "%" + ' Wpm: ' + str(round(self.wpm))

self.time_img = pygame.image.load('icon.png')
self.time_img = pygame.transform.scale(self.time_img, (150, 150))
self.screen.blit(self.time_img, (self.w / 2 - 75, self.h - 140))
self.draw_text(self.screen, "Reset", self.h - 70, 26, (100, 100, 100))

print(self.results) pygame.display.update()

def run(self): while True:
level = input("Select level (e for easy, m for medium, h for hard): ").lower() if level in ['e', 'm', 'h']:
break
 
else:
print("Invalid input. Please try again.")

self.word = self.get_sentence(level) if not self.word:
print("No sentences available for the selected level.") return

self.reset_game(level) self.running = True while self.running:
clock = pygame.time.Clock() self.screen.fill((0, 0, 0), (50, 250, 650, 50))
pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)
self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250)) pygame.display.update()

for event in pygame.event.get(): if event.type == QUIT:
self.running = False

elif event.type == pygame.MOUSEBUTTONUP: x, y = pygame.mouse.get_pos()
if (x >= 50 and x <= 650 and y >= 250 and y <= 300): self.active = True
self.input_text = '' self.time_start = time.time()
if (x >= 310 and x <= 510 and y >= 390 and self.end): self.reset_game(level)
x, y = pygame.mouse.get_pos()

elif event.type == pygame.KEYDOWN: if event.key == pygame.K_ESCAPE:
self.running = False

if self.active and not self.end:
if event.key == pygame.K_RETURN: print(self.input_text) self.show_results(self.screen) print(self.results)
self.draw_text(self.screen, self.results, 350, 28, self.RESULT_C) self.end = True
elif event.key == pygame.K_BACKSPACE: self.input_text = self.input_text[:-1]
else:
try:
 
self.input_text += event.unicode except:
pass

pygame.display.update() clock.tick(60)

pygame.quit() sys.exit()

def reset_game(self, level): self.screen.blit(self.open_img, (0, 0))

pygame.display.update() time.sleep(1)

self.reset = False self.end = False

self.input_text = '' self.time_start = 0
self.total_time = 0
self.wpm = 0

self.word = self.get_sentence(level) if not self.word:
print("No sentences available for the selected level.") return

self.screen.fill((0, 0, 0))
self.screen.blit(self.bg, (0, 0)) msg = "Typing Speed Test"
self.draw_text(self.screen, msg, 80, 80, self.HEAD_C)
pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)
self.draw_text(self.screen, self.word, 200, 28, self.TEXT_C) pygame.display.update()


if  name	== ' main ': Game().run()
