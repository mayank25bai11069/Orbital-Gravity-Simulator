# N-Body Orbital Gravity Simulator

## Real-World Application & Overview
In aerospace engineering and orbital mechanics, predicting the trajectory of a single satellite is mathematically straightforward. However, once multiple gravitational sources are introduced (such as the Earth, Moon, and Sun), the system becomes highly chaotic—a challenge known as the N-Body Problem. 

This project is a dynamic physics engine built in Python that tackles this computational challenge. It calculates the mutual gravitational pull between multiple celestial entities frame-by-frame. This type of simulation is the foundational logic used for satellite trajectory plotting, deep-space navigation, and predicting near-Earth object collisions.

## Features
* **Dynamic N-Body Physics:** Calculates mutual gravitational pull across all entities simultaneously without hard-coded paths.
* **Object-Oriented Design:** Modular `CelestialBody` class makes it easy to add new planets, stars, or rogue entities.
* **Real-Time Rendering:** Utilizes `matplotlib.animation` to visualize the simulation and plot orbital trails.
* **Mathematical Failsafes:** Includes algorithmic bypasses for division-by-zero collision errors.

## Prerequisites
To run this project, you need Python 3.x installed on your system.
You will also need the `matplotlib` library. Install it via terminal:
`pip install matplotlib`

## How to Run
1. Clone this repository to your local machine or download the `main.py` file.
2. Open your terminal and navigate to the project directory.
3. Execute the simulation by running:
`python main.py`
