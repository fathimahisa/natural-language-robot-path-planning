from typing import List, Tuple, Dict

Coord = Tuple[int, int]

def _normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())

ALIASES = {
    "red box": ["red box", "redbin", "red-bin", "red object"],
    "blue box": ["blue box", "bluebin", "blue-bin", "blue object", "blue one"],
    "charging station": ["charging station", "charger", "dock"],
}

def parse_command(command: str, objects: Dict[str, Coord], start: Coord) -> List[Coord]:
    command = command.lower()
    waypoints: List[Coord] = []

    # Check for each object
    for canonical, variants in ALIASES.items():
        for v in variants:
            if v in command:
                if canonical in objects:
                    waypoints.append(objects[canonical])
                break

    # Special handling: "back to start"
    if "back to start" in command or "go back to start" in command:
        waypoints.append(start)

    return waypoints
