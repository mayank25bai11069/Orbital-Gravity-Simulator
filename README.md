# N-Body Orbital Gravity Simulator

## Project Overview

This project is a 2D physics engine built in Python that simulates the gravitational interactions between multiple celestial bodies. Instead of hard-coding orbital paths, this simulator uses Newton's Law of Universal Gravitation to calculate the real-time forces, accelerations, and velocities of each body in the system. 

## Features

* **Dynamic N-Body Physics:** Calculates mutual gravitational pull across all entities simultaneously.
* **Object-Oriented Design:** Modular `CelestialBody` class makes it easy to add new planets, stars, or rogue entities.
* **Real-Time Rendering:** Utilizes `matplotlib.animation` to visualize the simulation and plot orbital trails.

## Prerequisites

To run this project, you need Python 3.x installed on your system.
You will also need the `matplotlib` library. Install it via terminal:
`pip install matplotlib`

## How to Run

1. Clone this repository to your local machine or download the `main.py` file.
2. Open your terminal and navigate to the project directory.
3. Execute the simulation by running:
`python main.py`

## Customizing the Simulation

You can easily create your own solar systems by modifying the system list variables in `main.py`. Try changing the mass or velocity of the "Rogue Planet" to see how chaotic gravity can get!
