import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()
        self.cells = []

        # Draw grid of blue cells
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(
                    col, row, col + CELL_SIZE, row + CELL_SIZE,
                    fill="blue", outline="white"
                )
                self.cells.append(cell)

        # Create eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")
        self.canvas.bind("<Motion>", self.move_eraser)

    def move_eraser(self, event):
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)

        # Check for overlapping cells
        overlapping = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        for item in overlapping:
            if item != self.eraser:
                self.canvas.itemconfig(item, fill="white")

def main():
    root = tk.Tk()
    root.title("Eraser Canvas")
    app = EraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
