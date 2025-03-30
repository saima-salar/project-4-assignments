import tkinter as tk

# Constants for canvas size and grid
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 20  # Each square size
ERASER_SIZE = 40  # Eraser dimensions

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eraser Tool")

        # Create canvas
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        # Draw grid of blue cells
        self.cells = {}
        for x in range(0, CANVAS_WIDTH, CELL_SIZE):
            for y in range(0, CANVAS_HEIGHT, CELL_SIZE):
                cell = self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="blue", outline="white")
                self.cells[(x, y)] = cell  # Store cell references

        # Create eraser (white rectangle)
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="white", outline="black")

        # Bind mouse movements to eraser actions
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def move_eraser(self, event):
        """Moves eraser and erases blue cells by turning them white."""
        x1, y1 = event.x, event.y
        x2, y2 = x1 + ERASER_SIZE, y1 + ERASER_SIZE

        # Move eraser
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Check overlapping cells and erase them
        for (cx, cy), cell_id in self.cells.items():
            if cx < x2 and cx + CELL_SIZE > x1 and cy < y2 and cy + CELL_SIZE > y1:
                self.canvas.itemconfig(cell_id, fill="white")

def main():
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
