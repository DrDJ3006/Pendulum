# Pendulum Simulation with Air Resistance

## Description
This program simulates the motion of a pendulum under the influence of gravity, viscous friction, and air resistance. It provides a visual animation of the motion along with a graph showing linear velocity as a function of angle.

The graphical interface (Tkinter) allows users to configure different physical parameters before starting the simulation.

## Features
- Graphical interface to set pendulum parameters
- Animated visualization of the pendulum motion
- Graph showing linear velocity vs. angle
- Modeling of friction effects (viscous and air resistance)

## Prerequisites
This program requires Python 3 and the following libraries:

```sh
pip install numpy matplotlib scipy tkinter
```

## Usage
1. Run the Python script:
   ```sh
   python script.py
   ```
2. Adjust the parameters in the graphical interface (optional).
3. Click "Start Simulation" to visualize the animation.

## Available Parameters
| Parameter | Description | Default Value |
|-----------|------------|---------------|
| Gravity (g) | Gravitational acceleration (m/s²) | 9.81 |
| Length (L) | Length of the pendulum (m) | 5.0 |
| Mass (m) | Mass of the pendulum (kg) | 70.0 |
| Viscous friction (b) | Linear friction coefficient | 0.1 |
| Drag coefficient (Cd) | Air resistance coefficient | 0.6 |
| Air density (ρ) | Air mass density (kg/m³) | 1.225 |
| Frontal area (A) | Exposed surface area (m²) | 0.01 |
| Initial angle (θ₀) | Initial angular position (°) | -80 |
| Initial angular velocity (ω₀) | Starting velocity (rad/s) | 0.0 |

## Physical Model Explanation
The differential equation used to model the pendulum considers:
- Gravity effect:
  ```math
  - (g / L) * sin(θ)
  ```
- Viscous friction:
  ```math
  - (b / (m * L^2)) * ω
  ```
- Air resistance (modeled quadratically):
  ```math
  - (0.5 * Cd * ρ * A * (L^2) / m) * ω * |ω|
  ```

Numerical integration is performed using `solve_ivp` (Runge-Kutta 5th order method).

## Author
Developed by [Your Name]

## License
This project is licensed under the MIT License.
