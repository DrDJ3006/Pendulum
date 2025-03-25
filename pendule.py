import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp
import tkinter as tk
from tkinter import ttk

# --- Function to retrieve values and start the simulation ---
def start_simulation():
    global g, L, m, b, Cd, rho, A, theta0, omega0
    
    # Retrieve values from the interface
    g = float(entry_g.get())
    L = float(entry_L.get())
    m = float(entry_m.get())
    b = float(entry_b.get())
    Cd = float(entry_Cd.get())
    rho = float(entry_rho.get())
    A = float(entry_A.get())
    theta0 = np.radians(float(entry_theta0.get()))  # Convert to radians
    omega0 = float(entry_omega0.get())

    # Start the simulation
    run_simulation()

# --- Function to execute the animation ---
def run_simulation():
    t_max = 10
    dt = 0.05
    t_span = (0, t_max)
    t_eval = np.arange(0, t_max, dt)

    def pendulum_eq(t, y):
        theta, omega = y
        dtheta_dt = omega
        damping = - (b / (m * L**2)) * omega  # Linear friction
        air_resistance = - (0.5 * Cd * rho * A * (L**2) / m) * omega * abs(omega)  # Air resistance
        domega_dt = - (g / L) * np.sin(theta) + damping + air_resistance
        return [dtheta_dt, domega_dt]

    sol = solve_ivp(pendulum_eq, t_span, [theta0, omega0], t_eval=t_eval, method='RK45')

    theta_values = sol.y[0]
    omega_values = np.abs(sol.y[1])
    velocity_values = omega_values * L
    x_values = L * np.sin(theta_values)
    y_values = -L * np.cos(theta_values)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.set_xlim(-L-0.1, L+0.1)
    ax1.set_ylim(-L-0.1, L+0.1)
    ax1.set_aspect('equal')
    ax1.set_title("Pendulum with Air Resistance")

    line, = ax1.plot([], [], 'k-', lw=2)
    mass, = ax1.plot([], [], 'ro', markersize=12)
    velocity_text = ax1.text(-L, L-0.2, '', fontsize=12, color='blue')

    ax2.set_xlim(min(theta_values), max(theta_values))
    ax2.set_ylim(0, max(velocity_values) * 1.1)
    ax2.set_xlabel("Angle θ (rad)")
    ax2.set_ylabel("Linear Velocity v (m/s)")
    ax2.set_title("Linear Velocity as a Function of Angle")

    graph_line, = ax2.plot([], [], 'b-', lw=1.5)
    graph_theta = []
    graph_velocity = []

    def init():
        line.set_data([], [])
        mass.set_data([], [])
        velocity_text.set_text('')
        graph_line.set_data([], [])
        graph_theta.clear()
        graph_velocity.clear()
        return line, mass, velocity_text, graph_line

    def update(frame):
        x = x_values[frame]
        y = y_values[frame]
        velocity = velocity_values[frame]
        theta = theta_values[frame]
        
        line.set_data([0, x], [0, y])
        mass.set_data([x], [y])
        velocity_text.set_text(f"Linear Velocity: {velocity:.2f} m/s")

        graph_theta.append(theta)
        graph_velocity.append(velocity)
        graph_line.set_data(graph_theta, graph_velocity)
        
        return line, mass, velocity_text, graph_line

    ani = animation.FuncAnimation(fig, update, frames=len(t_eval), init_func=init, blit=True, interval=dt*1000, repeat=True)
    
    plt.show()

# --- Create the graphical interface ---
root = tk.Tk()
root.title("Pendulum Simulation - Parameters")

# Labels and input fields
params = [
    ("Gravity (m/s²)", "9.81"),
    ("Length (m)", "5.0"),
    ("Mass (kg)", "70.0"),
    ("Viscous Friction (b)", "0.1"),
    ("Drag Coefficient (Cd)", "0.6"),
    ("Air Density (kg/m³)", "1.225"),
    ("Frontal Area (m²)", "0.01"),
    ("Initial Angle (°)", "-80"),
    ("Initial Angular Velocity (rad/s)", "0.0")
]

entries = []

for i, (label, default) in enumerate(params):
    ttk.Label(root, text=label).grid(row=i, column=0, padx=5, pady=5, sticky="w")
    entry = ttk.Entry(root)
    entry.insert(0, default)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

# Assign input fields
entry_g, entry_L, entry_m, entry_b, entry_Cd, entry_rho, entry_A, entry_theta0, entry_omega0 = entries

# Button to start the simulation
btn_start = ttk.Button(root, text="Start Simulation", command=start_simulation)
btn_start.grid(row=len(params), columnspan=2, pady=10)

root.mainloop()