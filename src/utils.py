"""
Utility functions for the Number Guessing Game.
"""

import os
import platform


def clear_screen():
    """Clear the terminal screen based on the operating system."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def get_user_choice(valid_choices: list) -> str:
    """
    Get and validate user input from a list of valid choices.
    
    Args:
        valid_choices: List of valid string choices
        
    Returns:
        Valid user choice as string
    """
    while True:
        choice = input("Enter your choice: ").strip()
        if choice in valid_choices:
            return choice
        else:
            print(f"Invalid choice! Please enter one of: {', '.join(valid_choices)}")


def display_banner(text: str, width: int = 50, char: str = "=") -> None:
    """
    Display a formatted banner with text.
    
    Args:
        text: Text to display in the banner
        width: Total width of the banner
        char: Character to use for the border
    """
    print(char * width)
    print(text.center(width))
    print(char * width)


def format_time(seconds: float) -> str:
    """
    Format time duration in a human-readable format.
    
    Args:
        seconds: Time in seconds
        
    Returns:
        Formatted time string
    """
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes}m {secs}s"
    else:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        return f"{hours}h {minutes}m"


def get_number_input(prompt: str, min_val: int, max_val: int) -> int:
    """
    Get a valid number input from the user within a specified range.
    
    Args:
        prompt: Input prompt to display
        min_val: Minimum valid value
        max_val: Maximum valid value
        
    Returns:
        Valid integer within the specified range
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a valid number!")


def create_progress_bar(current: int, total: int, length: int = 20) -> str:
    """
    Create a text-based progress bar.
    
    Args:
        current: Current progress value
        total: Total value for 100%
        length: Length of the progress bar
        
    Returns:
        String representation of the progress bar
    """
    if total == 0:
        return "[" + " " * length + "] 0%"
    
    percentage = min(current / total, 1.0)
    filled = int(length * percentage)
    bar = "█" * filled + "░" * (length - filled)
    percent_text = f"{int(percentage * 100)}%"
    
    return f"[{bar}] {percent_text}"


def save_game_stats(filename: str, stats: dict) -> None:
    """
    Save game statistics to a file.
    
    Args:
        filename: Name of the file to save to
        stats: Dictionary containing game statistics
    """
    try:
        with open(filename, 'a') as f:
            f.write(f"Game played at: {stats.get('timestamp', 'Unknown')}\n")
            f.write(f"Difficulty: {stats.get('difficulty', 'Unknown')}\n")
            f.write(f"Attempts: {stats.get('attempts', 0)}\n")
            f.write(f"Time taken: {stats.get('time_taken', 0)}s\n")
            f.write(f"Won: {stats.get('won', False)}\n")
            f.write("-" * 30 + "\n")
    except IOError as e:
        print(f"Error saving stats: {e}")


def load_game_stats(filename: str) -> list:
    """
    Load game statistics from a file.
    
    Args:
        filename: Name of the file to load from
        
    Returns:
        List of game statistics dictionaries
    """
    stats = []
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            game = {}
            for line in lines:
                line = line.strip()
                if line.startswith("Game played at:"):
                    game['timestamp'] = line.split(": ", 1)[1]
                elif line.startswith("Difficulty:"):
                    game['difficulty'] = line.split(": ", 1)[1]
                elif line.startswith("Attempts:"):
                    game['attempts'] = int(line.split(": ", 1)[1])
                elif line.startswith("Time taken:"):
                    game['time_taken'] = float(line.split(": ", 1)[1])
                elif line.startswith("Won:"):
                    game['won'] = line.split(": ", 1)[1] == 'True'
                elif line == "-" * 30:
                    if game:
                        stats.append(game)
                        game = {}
    except (IOError, ValueError) as e:
        print(f"Error loading stats: {e}")
    
    return stats
