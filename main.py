import argparse
from typing import List, Tuple
from nlp_parser import parse_command
from path_planner import astar
from simulator import simulate

Coord = Tuple[int, int]

GRID = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0],
    [0,0,1,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0],
]

OBJECTS = {
    "red box": (2, 5),
    "blue box": (5, 4),
    "charging station": (7, 1),
}

START: Coord = (0, 0)

def run_single_command(command: str) -> None:
    print(f"[INFO] Command: {command}")
    waypoints = parse_command(command, OBJECTS, START)
    if not waypoints:
        print("[WARN] No valid waypoints found.")
        return

    print(f"[INFO] Waypoints: {waypoints}")
    current = START
    full_path: List[Coord] = []

    for goal in waypoints:
        segment = astar(GRID, current, goal)
        full_path.extend(segment)
        current = goal

    # ✅ pass all objects for visualization
    simulate(GRID, full_path, START, objects=OBJECTS)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--command", type=str)
    parser.add_argument("--commands_file", type=str)
    args = parser.parse_args()

    if args.command:
        run_single_command(args.command)
    elif args.commands_file:
        with open(args.commands_file, "r", encoding="utf-8") as f:
            for line in f:
                cmd = line.strip()
                if cmd:
                    run_single_command(cmd)
    else:
        print("Provide --command or --commands_file")

if __name__ == "__main__":
    main()
