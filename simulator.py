import matplotlib.pyplot as plt
import numpy as np
import time
from typing import List, Tuple, Dict

Coord = Tuple[int, int]

def draw_grid(grid, robot: Coord = None, objects: Dict[str, Coord] = None):
    plt.clf()
    plt.title("Robot Path Simulation")

    rows, cols = len(grid), len(grid[0])

    # Set background white
    plt.gca().set_facecolor("white")

    # Draw obstacles in yellow
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                plt.gca().add_patch(plt.Rectangle((c-0.5, r-0.5), 1, 1, color="yellow"))

    # Draw robot (black dot)
    if robot is not None:
        plt.plot(robot[1], robot[0], "ko", markersize=8, label="Robot")

    # Draw objects
    if objects:
        for name, pos in objects.items():
            if name == "red box":
                plt.plot(pos[1], pos[0], "rx", markersize=12, label="Red Box")
            elif name == "blue box":
                plt.plot(pos[1], pos[0], "bx", markersize=12, label="Blue Box")
            elif name == "charging station":
                plt.plot(pos[1], pos[0], "gx", markersize=12, label="Charging Station")

    # Formatting
    plt.xlim(-0.5, cols-0.5)
    plt.ylim(rows-0.5, -0.5)  # Flip y-axis so (0,0) is top-left
    plt.grid(True, which="both", color="lightgray", linewidth=0.5)
    plt.gca().set_aspect("equal", adjustable="box")

    # Show legend without duplicates
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), loc="upper right")

    plt.pause(0.001)


def simulate(grid, full_path: List[Coord], start: Coord, objects: Dict[str, Coord] = None, delay: float = 0.2):
    plt.ion()
    pos = start
    draw_grid(grid, pos, objects)
    for step in full_path:
        pos = step
        draw_grid(grid, pos, objects)
        time.sleep(delay)
    plt.ioff()
    plt.show()

    
