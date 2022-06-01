import tkinter as tk
import random

class Minesweeper:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1000x600")
        self.window.resizable(0,0)
        self.window.title("MineSweeper")
        
        # small test grid for starters > make size and bomb density a choice later
        self.grid = self.create_grid(5, 5)
        
        self.images = {
            "default": tk.PhotoImage(file = "images/default.png"),
            "empty": tk.PhotoImage(file = "images/empty.png"),
            "mine": tk.PhotoImage(file = "images/bomb.png"),
            "flagged": tk.PhotoImage(file = "images/flagged.png"),
            "numbers": []
        }
        for i in range[1,9]:
            self.images['numbers'].append(tk.PhotoImage(file = f"images/{str(i)}.png"))
            
    def button_press(self):
        # check for bomb > End game if bomb
        # check for number tile > uncover just the one tile
        # check for empty tile > run algorithm to clear empty space
        pass
    
    def clear_empty_spot(self):
        # recursive function to inspect adjacent tiles until number tiles are discovered
        pass
        
    def create_grid(self, rows, columns):
        grid = {}
        count = 0
        for col in columns:
            for row in rows:
                grid[count] = (row, col)
                count += 1
        return grid
    
    def create_board_tiles(self):
        for key, grid_value in self.grid.items():
            button = tk.Button()
            pass
        
    def check_area(self):
        # recursive function to uncover "islands"
        pass
        
    def create_bomb_list(self):
        # randomly select grid_values that are bombs
        # number of bombs scales by percentage of grid size
        pass
    
    def check_bomb(self):
        # check against the bomb list
        pass
    

    def run(self):
        self.window.mainloop()

ms = Minesweeper()
ms.run()