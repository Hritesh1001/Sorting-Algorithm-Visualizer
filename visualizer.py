from turtle import update
import pygame
import random
import math
import time

pygame.init()

# Necessary Global variables necessary for data representation and visualization
class GlobalVariable:
    # Some color codes for data representation
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BG_COLOR = WHITE
    GRADIENT = [
		(128, 128, 128),
		(160, 160, 160),
		(192, 192, 192)
	]
    
    # Gap to be from top and side corners left for central display
    SIDE_PAD = 100
    TOP_PAD = 150
    
    # Font size
    FONT = pygame.font.SysFont('Visualizer', 30)
    L_FONT = pygame.font.SysFont('Visualizer', 40)
    
    # Math required for customizing the size of window
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        
        # Heading of the Application
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)
    
    # Configuring the drawing width and height of the data in the form of rectangles
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

# Generating the list for visualization with random data
def generate_lst(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst

"""
SORTING ALGORITHMS :
Bubble Sort
Insertion Sort
Merge Sort
Quick Sort
Selection Sort
"""

# BUBBLE SORT
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

# INSERTION SORT
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

# MERGE SORT
def merge_sort(draw_info, ascending = True):
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

# MERGE Function is also a part of MERGE SORT
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

# QUICK SORT         
def quick_sort(draw_info, ascending = True):
    lst = draw_info.lst
    l = 0
    h = len(lst) - 1
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    
    top = top + 1
    stack[top] = l
    
    top = top + 1
    stack[top] = h
    
    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        draw_lst(draw_info, {l : draw_info.RED, h : draw_info.GREEN}, True)
        yield True
        draw_lst(draw_info, {l : draw_info.RED, h : draw_info.GREEN}, True)
        yield True
        p = partition(draw_info, l, h, ascending)
        draw_lst(draw_info, {l : draw_info.RED, h : draw_info.GREEN}, True)
        yield True
        draw_lst(draw_info, {l : draw_info.RED, h : draw_info.GREEN}, True)
        yield True
        
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
            
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
            
# PARTITION Function is also a part of QUICK SORT
def partition(draw_info, l, h, ascending):
    lst = draw_info.lst
    i = (l - 1)
    x = lst[h]
    
    if ascending:
        for j in range(l, h):
            if lst[j] <= x:
                i = i + 1
                draw_lst(draw_info, {i : draw_info.RED, j : draw_info.GREEN}, True)
                time.sleep(0.02)
                lst[i], lst[j] = lst[j], lst[i]
        draw_lst(draw_info, {i + 1 : draw_info.RED, h : draw_info.GREEN}, True)
        time.sleep(0.02)
        lst[i + 1], lst[h] = lst[h], lst[i + 1]
        return (i + 1)
    else:
        for j in range(l, h):
            if lst[j] >= x:
                i = i + 1
                draw_lst(draw_info, {i : draw_info.RED, j : draw_info.GREEN}, True)
                time.sleep(0.02)
                lst[i], lst[j] = lst[j], lst[i]
        draw_lst(draw_info, {i + 1 : draw_info.RED, h : draw_info.GREEN}, True)
        time.sleep(0.02)
        lst[i + 1], lst[h] = lst[h], lst[i + 1]
        return (i + 1)

# SELECTION SORT
def selection_sort(draw_info, ascending = True):
    lst = draw_info.lst
    
    if ascending:
        for i in range(len(lst)):
            min_idx = i
            for j in range(i+1, len(lst)):
                draw_lst(draw_info, {i : draw_info.RED, min_idx : draw_info.GREEN}, True)
                time.sleep(0.009)
                if lst[min_idx] > lst[j]:
                    min_idx = j
            draw_lst(draw_info, {i : draw_info.RED, min_idx : draw_info.GREEN}, True)
            yield True
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
    else:
        for i in range(len(lst)):
            max_idx = i
            for j in range(i+1, len(lst)):
                draw_lst(draw_info, {i : draw_info.RED, max_idx : draw_info.GREEN}, True)
                time.sleep(0.009)
                if lst[max_idx] < lst[j]:
                    max_idx = j
            draw_lst(draw_info, {i : draw_info.RED, max_idx : draw_info.GREEN}, True)
            yield True
            lst[i], lst[max_idx] = lst[max_idx], lst[i]
            
    return lst

# Drawing rectangular bars ont the basis of data present list and math done in the GlobalVariable Class
def draw_lst(draw_info, cur_block = {}, clear_bg = False):
    lst = draw_info.lst
    
    # Clear the entire background if needed
    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BG_COLOR, clear_rect)
    
    # Drawing mechanism of the entire list in the form of rectangles
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width # Logical width of a rectangle
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height # Logical height of a rectangle
        color = draw_info.GRADIENT[i % 3] # Color decision 
        if i in cur_block:
            color = cur_block[i]
        # Draw the rectangle
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
        
    if clear_bg:
        pygame.display.update()

# Drawing the basic text part on the window for better and simple understanding of any random user
def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BG_COLOR)
    
    # Display the Sorting Algorithm and Order of Sorting that is currently set
    cur = draw_info.L_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.RED)
    draw_info.window.blit(cur, (draw_info.width / 2 - cur.get_width() / 2, 5))
    
    # Kind of User Guide
    controls = draw_info.FONT.render("R - Reset | SPACE - Start | A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 40))
    
    sort = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | M - Merge Sort | Q - Quick Sort | S - Selection Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sort, (draw_info.width / 2 - sort.get_width() / 2, 65))
    
    # Display the current list
    draw_lst(draw_info)
    pygame.display.update()
    
def main():
    run = True
    clock = pygame.time.Clock()
    
    lst = generate_lst(60, 1, 100) # List size = 60 , Minimum Value = 1 , Maximum Value = 100
    draw_info = GlobalVariable(900, 600, lst) # Window Size : Wide -> 900px  Height -> 600px
    
    sorting = False
    ascending = True
    
    # By default application set to Bubble Sort / Ascending Order
    sorting_algo = bubble_sort
    sorting_algo_name = "Bubble Sort"
    
    sorting_algo_generator = None # For displaying the current algorithm that is set
    
    while run:
        clock.tick(60) # Higher the clock tick, faster is the visualization
        
        if sorting == True:
            # If further sorting is left then continue otherwise set sorting as False and terminate the current sorting algo
            try:
                next(sorting_algo_generator)
            except StopIteration:
                sorting = False
        else:
            # After the sorting is completed, display the final result
            draw(draw_info, sorting_algo_name, ascending)
        
        for event in pygame.event.get():
            # If Cross (X) button is pressed, then close the application
            if event.type == pygame.QUIT:
                run = False
            
            # If not Key is pressed then continue to run the application
            if event.type != pygame.KEYDOWN:
                continue
            
            # If R button is pressed, reset the data of list
            if event.key == pygame.K_r:
                lst = generate_lst(60, 1, 100)
                draw_info.set_list(lst)
                
            # If SPACE is pressed, Run the Sorting Algorithm
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                # Pass the entire data to its respective sorting function
                sorting_algo_generator = sorting_algo(draw_info, ascending)
                
            # If A is pressed, then sorting in ascending order will be done
            elif event.key == pygame.K_a and not sorting:
                ascending = True
                
            # If A is pressed, then sorting in descending order will be done
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            
            # If I is pressed, then INSERTION SORT will be implemented
            elif event.key == pygame.K_i and not sorting:
                sorting_algo = insertion_sort
                sorting_algo_name = "Insertion Sort"
            
            # If B is pressed, then BUBBLE SORT will be implemented
            elif event.key == pygame.K_b and not sorting:
                sorting_algo = bubble_sort
                sorting_algo_name = "Bubble Sort"
            
            # If M is pressed, then MERGE SORT will be implemented
            elif event.key == pygame.K_m and not sorting:
                sorting_algo = merge_sort
                sorting_algo_name = "Merge Sort"
            
            # If Q is pressed, then QUICK SORT will be implemented
            elif event.key == pygame.K_q and not sorting:
                sorting_algo = quick_sort
                sorting_algo_name = "Quick Sort"
            
            # If S is pressed, then SELECTION SORT will be implemented
            elif event.key == pygame.K_s and not sorting:
                sorting_algo = selection_sort
                sorting_algo_name = "Selection Sort"
                
    pygame.quit()
    
if __name__ == "__main__":
    main()