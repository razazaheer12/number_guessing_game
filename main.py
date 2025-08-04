#!/usr/bin/env python3
"""
Main entry point for the Number Guessing Game application.
This file runs the game based on user selection.
"""

from src.game_engine import GameEngine
from src.game_types import NumberGuessedAIAgent, AdvancedGame
from src.utils import clear_screen, get_user_choice

def main():
    """Main function to run the application."""
    clear_screen()
    print("=" * 50)
    print("    NUMBER GUESSING AI AGENT")
    print("=" * 50)
    
    while True:
        print("\nSelect Game Mode:")
        print("1. Basic Number Guessing Game")
        print("2. Advanced Number Guessing Game")
        print("3. Exit")
        
        choice = get_user_choice(["1", "2", "3"])
        
        if choice == "1":
            game = NumberGuessedAIAgent()
        elif choice == "2":
            game = AdvancedGame()
        else:
            print("Thanks for playing!")
            break
            
        game.play()
        game.display_results()
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break
    
    print("\nGoodbye!")

if __name__ == "__main__":
    main()
