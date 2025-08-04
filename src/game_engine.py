"""
Game Engine module for the Number Guessing Game.
Contains the base game engine and common functionality.
"""

import random
import time
from typing import Tuple, Optional

class GameEngine:
    """Base game engine for number guessing games."""
    
    def __init__(self, min_number: int = 1, max_number: int = 100):
        """
        Initialize the game engine.
        
        Args:
            min_number: Minimum number in range (default: 1)
            max_number: Maximum number in range (default: 100)
        """
        self.min_number = min_number
        self.max_number = max_number
        self.secret_number = None
        self.attempts = 0
        self.max_attempts = 10
        self.game_history = []
        self.start_time = None
        self.end_time = None
        
    def generate_secret_number(self) -> int:
        """Generate a random secret number within the specified range."""
        self.secret_number = random.randint(self.min_number, self.max_number)
        return self.secret_number
    
    def get_hint(self, guess: int) -> str:
        """
        Provide a hint based on the user's guess.
        
        Args:
            guess: The user's guess
            
        Returns:
            String hint: "Too high", "Too low", or "Correct!"
        """
        if guess < self.secret_number:
            return "Too low!"
        elif guess > self.secret_number:
            return "Too high!"
        else:
            return "Correct!"
    
    def is_valid_guess(self, guess: str) -> Tuple[bool, Optional[int]]:
        """
        Validate if the input is a valid number within range.
        
        Args:
            guess: String input from user
            
        Returns:
            Tuple of (is_valid, number) where number is None if invalid
        """
        try:
            number = int(guess)
            if self.min_number <= number <= self.max_number:
                return True, number
            else:
                return False, None
        except ValueError:
            return False, None
    
    def start_game(self):
        """Initialize a new game session."""
        self.generate_secret_number()
        self.attempts = 0
        self.game_history = []
        self.start_time = time.time()
        print(f"\nI'm thinking of a number between {self.min_number} and {self.max_number}.")
        print(f"You have {self.max_attempts} attempts to guess it!\n")
    
    def end_game(self, won: bool):
        """End the game and record final time."""
        self.end_time = time.time()
        duration = round(self.end_time - self.start_time, 2)
        
        if won:
            print(f"\n🎉 Congratulations! You guessed the number in {self.attempts} attempts!")
            print(f"⏱️  Time taken: {duration} seconds")
        else:
            print(f"\n😔 Game Over! The number was {self.secret_number}")
            print(f"⏱️  Time taken: {duration} seconds")
    
    def display_results(self):
        """Display game statistics and history."""
        if not self.game_history:
            print("\nNo game played yet!")
            return
            
        print("\n" + "="*50)
        print("GAME STATISTICS")
        print("="*50)
        print(f"Total attempts: {self.attempts}")
        print(f"Secret number: {self.secret_number}")
        print(f"Game history:")
        
        for i, (guess, hint) in enumerate(self.game_history, 1):
            print(f"  Attempt {i}: {guess} - {hint}")
        
        if self.start_time and self.end_time:
            duration = round(self.end_time - self.start_time, 2)
            print(f"Total time: {duration} seconds")
