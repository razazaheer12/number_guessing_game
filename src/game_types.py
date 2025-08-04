"""
Game Types module for the Number Guessing Game.
Contains different game variations and AI agent implementations.
"""

import random
import time
from typing import List, Tuple
from .game_engine import GameEngine


class BaseGame:
    """Base class for all game types."""
    
    def __init__(self):
        self.engine = GameEngine()
        self.score = 0
        self.games_played = 0
        
    def play(self):
        """Abstract method to be implemented by subclasses."""
        raise NotImplementedError
        
    def display_results(self):
        """Display game results."""
        self.engine.display_results()


class NumberGuessedAIAgent(BaseGame):
    """Basic number guessing game where user plays against the AI."""
    
    def __init__(self):
        super().__init__()
        self.engine.max_attempts = 7
        
    def play(self):
        """Run the basic number guessing game."""
        print("\n" + "="*40)
        print("BASIC NUMBER GUESSING GAME")
        print("="*40)
        print("Try to guess the secret number!")
        
        self.engine.start_game()
        
        while self.engine.attempts < self.engine.max_attempts:
            guess = input(f"Attempt {self.engine.attempts + 1}/{self.engine.max_attempts}: Enter your guess: ")
            
            is_valid, number = self.engine.is_valid_guess(guess)
            if not is_valid:
                print(f"Please enter a valid number between {self.engine.min_number} and {self.engine.max_number}")
                continue
            
            self.engine.attempts += 1
            hint = self.engine.get_hint(number)
            self.engine.game_history.append((number, hint))
            
            print(f"→ {hint}")
            
            if number == self.engine.secret_number:
                self.engine.end_game(True)
                self.score += 1
                break
        else:
            self.engine.end_game(False)
        
        self.games_played += 1


class AdvancedGame(BaseGame):
    """Advanced number guessing game with additional features."""
    
    def __init__(self):
        super().__init__()
        self.engine.max_attempts = 5
        self.difficulty_levels = {
            "easy": {"min": 1, "max": 50, "attempts": 8},
            "medium": {"min": 1, "max": 100, "attempts": 6},
            "hard": {"min": 1, "max": 200, "attempts": 4}
        }
        self.ai_hints = []
        
    def select_difficulty(self) -> str:
        """Let user select difficulty level."""
        print("\nSelect difficulty level:")
        print("1. Easy (1-50, 8 attempts)")
        print("2. Medium (1-100, 6 attempts)")
        print("3. Hard (1-200, 4 attempts)")
        
        choice = input("Enter your choice (1-3): ")
        difficulties = {"1": "easy", "2": "medium", "3": "hard"}
        return difficulties.get(choice, "medium")
    
    def get_ai_hint(self, guesses: List[int], last_hint: str) -> str:
        """
        Generate an AI hint based on previous guesses and hints.
        
        Args:
            guesses: List of previous guesses
            last_hint: Last hint given to the user
            
        Returns:
            AI-generated hint string
        """
        if not guesses:
            return "Start with a number in the middle of the range!"
        
        last_guess = guesses[-1]
        
        if last_hint == "Too low!":
            new_range = f"Try between {last_guess + 1} and {self.engine.max_number}"
        elif last_hint == "Too high!":
            new_range = f"Try between {self.engine.min_number} and {last_guess - 1}"
        else:
            return "Keep trying!"
            
        return f"AI Hint: {new_range}"
    
    def play(self):
        """Run the advanced number guessing game."""
        print("\n" + "="*40)
        print("ADVANCED NUMBER GUESSING GAME")
        print("="*40)
        print("Features: Difficulty levels, AI hints, and more!")
        
        difficulty = self.select_difficulty()
        settings = self.difficulty_levels[difficulty]
        
        self.engine.min_number = settings["min"]
        self.engine.max_number = settings["max"]
        self.engine.max_attempts = settings["attempts"]
        
        print(f"\nDifficulty: {difficulty.upper()}")
        print(f"Range: {settings['min']}-{settings['max']}, Attempts: {settings['attempts']}")
        
        self.engine.start_game()
        guesses = []
        
        while self.engine.attempts < self.engine.max_attempts:
            remaining = self.engine.max_attempts - self.engine.attempts
            print(f"\nAttempts remaining: {remaining}")
            
            # Show AI hint every 2 attempts
            if self.engine.attempts > 0 and self.engine.attempts % 2 == 0:
                last_hint = self.engine.game_history[-1][1] if self.engine.game_history else ""
                ai_hint = self.get_ai_hint(guesses, last_hint)
                print(f"💡 {ai_hint}")
            
            guess = input(f"Enter your guess: ")
            
            is_valid, number = self.engine.is_valid_guess(guess)
            if not is_valid:
                print(f"Please enter a valid number between {self.engine.min_number} and {self.engine.max_number}")
                continue
            
            self.engine.attempts += 1
            guesses.append(number)
            hint = self.engine.get_hint(number)
            self.engine.game_history.append((number, hint))
            
            print(f"→ {hint}")
            
            if number == self.engine.secret_number:
                bonus = 0
                if difficulty == "easy":
                    bonus = 10 - self.engine.attempts
                elif difficulty == "medium":
                    bonus = 15 - self.engine.attempts
                else:
                    bonus = 20 - self.engine.attempts
                    
                self.score += max(bonus, 5)
                self.engine.end_game(True)
                break
        else:
            self.engine.end_game(False)
        
        self.games_played += 1
