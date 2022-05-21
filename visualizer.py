from turtle import update
import pygame
import random
import math
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
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
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

def insertion_sort(draw_info, ascending = True):
    lst = draw_info.lst
    for i in range(1, len(lst)):
        cur = lst[i]
        while True:
            ascending_sort = i > 0 and lst[i - 1] > cur and ascending
            descending_sort = i > 0 and lst[i - 1] < cur and not ascending
            if not ascending_sort and not descending_sort:
                break
            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = cur
            draw_lst(draw_info, {i : draw_info.RED, i - 1 : draw_info.GREEN}, True)
            yield True
    return lst

def mergeSort(draw_info, ascending = True):
    lst = draw_info.lst
    width = 1
    n = len(lst)
    while (width < n):
        l=0;
        while (l < n):
            r = min(l + (width * 2 - 1), n - 1)
            m = min(l + width - 1, n - 1) 
            draw_lst(draw_info, {l : draw_info.RED, r : draw_info.GREEN}, True)
            yield True
            draw_lst(draw_info, {l : draw_info.RED, r : draw_info.GREEN}, True)
            yield True
            merge(lst, l, m, r, ascending)
            draw_lst(draw_info, {l : draw_info.RED, r : draw_info.GREEN}, True)
            yield True
            draw_lst(draw_info, {l : draw_info.RED, r : draw_info.GREEN}, True)
            yield True
            l += width * 2
        width *= 2
    return lst

def merge(lst, l, m, r, ascending = True):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = lst[l + i]
    for i in range(0, n2):
        R[i] = lst[m + i + 1]
        
    i, j, k = 0, 0, l
    if ascending:
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
    
        while i < n1:
            lst[k] = L[i]
            i += 1
            k += 1
    
        while j < n2:
            lst[k] = R[j]
            j += 1
            k += 1
    else:
        while i < n1 and j < n2:
            if L[i] >= R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1
    
        while i < n1:
            lst[k] = L[i]
            i += 1
            k += 1
    
        while j < n2:
            lst[k] = R[j]
            j += 1
            k += 1

def draw_lst(draw_info, cur_block = {}, clear_bg = False):
    lst = draw_info.lst
    
    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BG_COLOR, clear_rect)
        
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        color = draw_info.GRADIENT[i % 3]
        if i in cur_block:
            color = cur_block[i]
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
        
    if clear_bg:
        pygame.display.update()
        
def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BG_COLOR)
    cur = draw_info.L_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.RED)
    draw_info.window.blit(cur, (draw_info.width / 2 - cur.get_width() / 2, 5))
    
    controls = draw_info.FONT.render("R - Reset | SPACE - Start | A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 40))
    
    sort = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sort, (draw_info.width / 2 - sort.get_width() / 2, 65))
    
    draw_lst(draw_info)
    pygame.display.update()
    
def main():
    run = True
    clock = pygame.time.Clock()
    
    lst = generate_lst(50, 0, 100)
    draw_info = GlobalVariable(800, 600, lst)
    sorting = False
    ascending = True
    
    sorting_algo = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algo_generator = None
    
    while run:
        clock.tick(60)
        if sorting == True:
            try:
                next(sorting_algo_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)
        
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
                sorting_algo_generator = sorting_algo(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algo = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algo = bubble_sort
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_m and not sorting:
                sorting_algo = mergeSort
                sorting_algo_name = "Merge Sort"
                
    pygame.quit()
    
if __name__ == "__main__":
    main()