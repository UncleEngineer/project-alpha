import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.width = 400
        self.height = 400
        self.cell_size = 20
        self.direction = 'Right'
        self.running = True
        self.score = 0
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.place_food()
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg='black')
        self.canvas.pack()
        self.root.bind('<Up>', lambda e: self.change_direction('Up'))
        self.root.bind('<Down>', lambda e: self.change_direction('Down'))
        self.root.bind('<Left>', lambda e: self.change_direction('Left'))
        self.root.bind('<Right>', lambda e: self.change_direction('Right'))
        self.update()

    def place_food(self):
        while True:
            x = random.randint(0, (self.width - self.cell_size) // self.cell_size) * self.cell_size
            y = random.randint(0, (self.height - self.cell_size) // self.cell_size) * self.cell_size
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, new_direction):
        opposites = {'Up':'Down', 'Down':'Up', 'Left':'Right', 'Right':'Left'}
        if self.direction != opposites.get(new_direction):
            self.direction = new_direction

    def move(self):
        x, y = self.snake[0]
        if self.direction == 'Up':
            y -= self.cell_size
        elif self.direction == 'Down':
            y += self.cell_size
        elif self.direction == 'Left':
            x -= self.cell_size
        elif self.direction == 'Right':
            x += self.cell_size
        new_head = (x, y)
        if (
            x < 0 or x >= self.width or
            y < 0 or y >= self.height or
            new_head in self.snake
        ):
            self.running = False
            return
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.food = self.place_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete('all')
        # Draw snake (green)
        for segment in self.snake:
            self.canvas.create_rectangle(
                segment[0], segment[1],
                segment[0]+self.cell_size, segment[1]+self.cell_size,
                fill='green', outline='')
        # Draw food (red)
        x, y = self.food
        self.canvas.create_oval(
            x, y, x+self.cell_size, y+self.cell_size,
            fill='red', outline='')
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill='white', font=('Arial', 14))

    def update(self):
        if self.running:
            self.move()
            self.draw()
            self.root.after(100, self.update)
        else:
            self.canvas.create_text(
                self.width//2, self.height//2,
                text=f"Game Over!\nScore: {self.score}", fill='white', font=('Arial', 20))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
