# Natural Language Based Robot Path Planning

## Overview
This project demonstrates how a robot can interpret **natural language instructions**
and convert them into **safe navigation paths** in a grid-based environment using AI.
It is designed as a compact demonstrator for **human-robot collaboration (HRC)** and
**AI-driven planning**.

## Features
- Natural language command parsing 
- AI path planning on a 2D grid with obstacles
- Simple animated simulation using matplotlib
- CLI interface: pass a command string or a file of commands

natural-language-path-planning/
│── README.md
│── requirements.txt
│── main.py
│── nlp_parser.py
│── path_planner.py
│── simulator.py
│── examples/
│   └── commands.txt


## Simulation and demo
Red ❌ at (2, 5) : red box

Blue ❌ at (5, 4) : blue box

Green ❌ at (7, 1): charging station

Robot (black dot) moves properly according to the comments given

yellow boxes: Obstacles

For demo example comments:
python main.py --command "Move to the blue box."
python main.py --command "Move to the red box."
python main.py --command "Move to the charging station."
 python main.py --command "Move to the blue box and then go to the charging station."

