# Utility function to calculate Y positions dynamically
def calculate_y_positions(num_turtles, screen_height):
    spacing = screen_height // (num_turtles + 1)  # Divide space by number of turtles + 1 (for padding)
    y_positions = [(-screen_height // 2 + spacing * (i + 1)) for i in range(num_turtles)]
    return y_positions
