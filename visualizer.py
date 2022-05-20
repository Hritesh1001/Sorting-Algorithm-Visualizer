from turtle import update
import pygame
import random
pygame.init()

class GlobalVariable:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BG_COLOR = WHITE
    SIDE_PAD = 100
    TOP_PAD = 150
    GRADIENT = [
		(128, 128, 128),
		(160, 160, 160),
		(192, 192, 192)
	]
    
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)
    
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

def generate_lst(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst

def draw_lst(draw_info):
    lst = draw_info.lst
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        color = draw_info.GRADIENT[i % 3]
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
        
def draw(draw_info):
    draw_info.window.fill(draw_info.BG_COLOR)
    draw_lst(draw_info)
    pygame.display.update()