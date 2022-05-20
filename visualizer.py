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
    FONT = pygame.font.SysFont('Visualizer', 30)
    L_FONT = pygame.font.SysFont('Visualizer', 40)
    
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

def bubble_sort(draw_info, ascending = True):
    lst = draw_info.lst
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            num1 = lst[j]
            num2 = lst[j + 1]
            if (num1 > num2 and ascending == True) or (num1 < num2 and ascending == False):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_lst(draw_info, {j : draw_info.GREEN, j + 1 : draw_info.RED}, True)
                yield True
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
    controls = draw_info.FONT.render("R - Reset | SPACE - Start | A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 5))
    sort = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sort, (draw_info.width / 2 - sort.get_width() / 2, 35))
    draw_lst(draw_info)
    pygame.display.update()
    
def main():
    run = True
    clock = pygame.time.Clock()
    
    lst = generate_lst(50, 0, 100)
    draw_info = GlobalVariable(800, 600, lst)
    sorting = False
    ascending = True
    
    while run:
        clock.tick(60)
        draw(draw_info)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type != pygame.KEYDOWN:
                continue
            
            if event.key == pygame.K_r:
                lst = generate_lst(50, 0, 100)
                draw_info.set_list(lst)
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
                
    pygame.quit()
    
if __name__ == "__main__":
    main()