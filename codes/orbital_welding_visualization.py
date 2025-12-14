#!/usr/bin/env python3
"""
Orbital Welding Tool Frame Visualization
Shows the pipe, world coordinate system, and tool frames at 4 waypoints
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d.proj3d import proj_transform

class Arrow3D(FancyArrowPatch):
    """Custom 3D arrow for better visualization"""
    def __init__(self, x, y, z, dx, dy, dz, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._xyz = (x, y, z)
        self._dxdydz = (dx, dy, dz)

    def draw(self, renderer):
        x1, y1, z1 = self._xyz
        dx, dy, dz = self._dxdydz
        x2, y2, z2 = (x1 + dx, y1 + dy, z1 + dz)

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        super().draw(renderer)

    def do_3d_projection(self, renderer=None):
        x1, y1, z1 = self._xyz
        dx, dy, dz = self._dxdydz
        x2, y2, z2 = (x1 + dx, y1 + dy, z1 + dz)

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))

        return np.min(zs)

def draw_arrow(ax, origin, direction, color, label, linewidth=2, alpha=1.0):
    """Draw a 3D arrow from origin in the given direction"""
    arrow = Arrow3D(
        origin[0], origin[1], origin[2],
        direction[0], direction[1], direction[2],
        mutation_scale=20,
        lw=linewidth,
        arrowstyle="-|>",
        color=color,
        alpha=alpha,
        label=label
    )
    ax.add_artist(arrow)

    # Add text label at the end of arrow
    text_pos = origin + direction * 1.15
    ax.text(text_pos[0], text_pos[1], text_pos[2], label,
            color=color, fontsize=11, fontweight='bold')

def create_cylinder(radius, height, num_points=50):
    """
    Create cylinder mesh for the pipe
    User coordinate system: X=horizontal(right), Y=vertical(up), Z=horizontal(outward)
    Matplotlib 3D plots: first arg=horizontal, second arg=depth, third arg=vertical
    """
    theta = np.linspace(0, 2*np.pi, num_points)
    x_pipe = np.linspace(-height/2, height/2, num_points)
    Theta, X_user = np.meshgrid(theta, x_pipe)

    # User's coordinate system
    Y_user = radius * np.cos(Theta)  # Vertical component
    Z_user = radius * np.sin(Theta)  # Horizontal outward component

    # Map to matplotlib: User(X,Y,Z) → Matplotlib(X,-X,Y,Z) → (-X,Z,Y)
    # User X → matplotlib X (flipped to point right)
    # User Y → matplotlib Z (vertical axis)
    # User Z → matplotlib Y (depth axis)
    X_mpl = -X_user
    Y_mpl = Z_user
    Z_mpl = Y_user

    return X_mpl, Y_mpl, Z_mpl

def plot_tool_frame(ax, theta_deg, radius, scale=40, x_offset=-80):
    """Plot tool frame at given angular position"""
    theta = np.deg2rad(theta_deg)

    # Position on pipe circumference in USER coordinates (X, Y, Z)
    # Y is vertical, Z is horizontal outward
    # Add x_offset to shift left (negative) or right (positive)
    pos_user = np.array([x_offset, radius * np.cos(theta), radius * np.sin(theta)])

    # Tool frame axes in USER coordinates
    # Z-tool: normal (radial outward)
    z_tool_user = np.array([0, np.cos(theta), np.sin(theta)])

    # X-tool: tangent to circle (direction of motion)
    x_tool_user = np.array([0, -np.sin(theta), np.cos(theta)])

    # Y-tool: along pipe axis (always +X direction in user coords, which points right)
    y_tool_user = np.array([1, 0, 0])

    # Convert to matplotlib coordinates: User(X,Y,Z) → Matplotlib(-X, Z, Y)
    def user_to_mpl(vec):
        return np.array([-vec[0], vec[2], vec[1]])

    pos_mpl = user_to_mpl(pos_user)
    x_tool_mpl = user_to_mpl(x_tool_user) * scale
    y_tool_mpl = user_to_mpl(y_tool_user) * scale
    z_tool_mpl = user_to_mpl(z_tool_user) * scale

    # Colors for tool axes - match the world axes colors
    colors = {'x': 'red', 'y': 'green', 'z': 'blue'}

    # Draw tool axes with proper labels
    draw_arrow(ax, pos_mpl, x_tool_mpl, colors['x'],
               f'X-tool ({theta_deg}°)', linewidth=2.5, alpha=0.9)
    draw_arrow(ax, pos_mpl, y_tool_mpl, colors['y'],
               f'Y-tool ({theta_deg}°)', linewidth=2.5, alpha=0.9)
    draw_arrow(ax, pos_mpl, z_tool_mpl, colors['z'],
               f'Z-tool ({theta_deg}°)', linewidth=2.5, alpha=0.9)

    # Draw a small sphere at the tool position
    ax.scatter(*pos_mpl, color='red', s=100, alpha=0.8, edgecolors='darkred', linewidth=2)

    # Add position label - move inward (negative direction of normal)
    label_pos = pos_mpl - z_tool_mpl * 0.3
    ax.text(label_pos[0], label_pos[1], label_pos[2],
            f'θ={theta_deg}°', fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))

def main():
    # Create figure with compact size (not square)
    fig = plt.figure(figsize=(14, 12))
    ax = fig.add_subplot(111, projection='3d')

    # Pipe parameters
    radius = 100  # mm
    length = 250  # mm

    # Create and plot cylinder (pipe) with reduced mesh for smaller SVG
    X, Y, Z = create_cylinder(radius, length, num_points=30)
    ax.plot_surface(X, Y, Z, alpha=0.3, color='silver', edgecolor='gray', linewidth=0.5)

    # Offsets to separate world axes from tool frames
    world_axes_offset = 80  # Shift world axes to the right
    tool_frames_offset = -80  # Shift tool frames to the left

    # Draw world coordinate system at origin (shifted right)
    # User: X=right, Y=up, Z=outward → Matplotlib: (-X, Z, Y)
    def user_to_mpl(vec):
        return np.array([-vec[0], vec[2], vec[1]])

    origin_user = np.array([world_axes_offset, 0, 0])
    origin_mpl = user_to_mpl(origin_user)
    axis_length = 150

    x_axis_user = np.array([axis_length, 0, 0])  # X points right
    y_axis_user = np.array([0, axis_length, 0])  # Y points up
    z_axis_user = np.array([0, 0, axis_length])  # Z points outward

    draw_arrow(ax, origin_mpl, user_to_mpl(x_axis_user), 'red',
               'X (Pipe Axis)', linewidth=4, alpha=1.0)
    draw_arrow(ax, origin_mpl, user_to_mpl(y_axis_user), 'green',
               'Y (Upward)', linewidth=4, alpha=1.0)
    draw_arrow(ax, origin_mpl, user_to_mpl(z_axis_user), 'blue',
               'Z (Outward)', linewidth=4, alpha=1.0)

    # Plot tool frames at 4 waypoints (shifted left)
    waypoints = [0, 90, 180, 270]  # degrees
    for theta in waypoints:
        plot_tool_frame(ax, theta, radius, scale=60, x_offset=tool_frames_offset)

    # Add circular path visualization (in YZ plane in user coords, Y vertical, Z horizontal)
    # Shifted to the left to match tool frames
    circle_theta = np.linspace(0, 2*np.pi, 100)
    circle_y_user = radius * np.cos(circle_theta)
    circle_z_user = radius * np.sin(circle_theta)
    circle_x_user = np.full_like(circle_y_user, tool_frames_offset)

    # Convert circle to matplotlib coordinates
    circle_x_mpl = -circle_x_user
    circle_y_mpl = circle_z_user
    circle_z_mpl = circle_y_user

    ax.plot(circle_x_mpl, circle_y_mpl, circle_z_mpl, 'k--', linewidth=2, alpha=0.5)

    # Set labels to match USER coordinate system
    # Matplotlib X-axis shows user X (pipe axis, horizontal right)
    # Matplotlib Y-axis shows user Z (horizontal outward)
    # Matplotlib Z-axis shows user Y (vertical up)
    ax.set_xlabel('X (mm)', fontsize=14, fontweight='bold', labelpad=15)
    ax.set_ylabel('Z (mm)', fontsize=14, fontweight='bold', labelpad=15)
    ax.set_zlabel('Y (mm)', fontsize=14, fontweight='bold', labelpad=15)

    # Set equal aspect ratio and limits
    max_range = 200
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])

    # Better viewing angle
    ax.view_init(elev=20, azim=135)

    # Add grid
    ax.grid(True, alpha=0.3)

    # Remove margins
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    # Save figure in the same directory as the script
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Save as SVG only (vector format, compact)
    svg_file = os.path.join(script_dir, 'orbital_welding_tool_frames.svg')
    plt.savefig(svg_file, format='svg', bbox_inches='tight', pad_inches=0.1, facecolor='white')
    svg_size = os.path.getsize(svg_file)
    print(f"SVG saved to: {svg_file}")
    print(f"SVG file size: {svg_size / 1024:.1f} KB")

    plt.close()

if __name__ == "__main__":
    main()
