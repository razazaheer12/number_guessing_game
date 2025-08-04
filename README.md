# Number Guessing Game with AI Agent

A comprehensive Python-based number guessing game featuring multiple game modes, AI hints, and advanced gameplay mechanics.

## Features

- **Basic Game Mode**: Classic number guessing with configurable attempts
- **Advanced Game Mode**: Multiple difficulty levels with AI-powered hints
- **AI Agent**: Intelligent hint system that adapts to user guesses
- **Statistics Tracking**: Game history and performance metrics
- **Cross-platform**: Works on Windows, macOS, and Linux

## Game Modes

### 1. Basic Number Guessing Game
- Range: 1-100
- Attempts: 7
- Simple feedback: "Too high", "Too low", "Correct!"

### 2. Advanced Number Guessing Game
- **Easy**: 1-50 range, 8 attempts
- **Medium**: 1-100 range, 6 attempts
- **Hard**: 1-200 range, 4 attempts
- AI hints every 2 attempts
- Bonus scoring system

## Installation

1. Clone or download the project
2. Navigate to the `number_guessing_game` directory
3. Run the game:
   ```bash
   python main.py
   ```

## Project Structure

```
number_guessing_game/
├── main.py                 # Entry point
├── README.md              # This file
└── src/
    ├── __init__.py        # Package initialization
    ├── game_engine.py     # Core game engine
    ├── game_types.py      # Game variations and AI agent
    └── utils.py           # Utility functions
```

## Usage

1. Run `python main.py`
2. Select game mode:
   - 1: Basic Number Guessing Game
   - 2: Advanced Number Guessing Game
   - 3: Exit
3. Follow on-screen instructions
4. View results and statistics after each game

## Technical Details

### Core Classes

- **GameEngine**: Base game logic and mechanics
- **NumberGuessedAIAgent**: Basic game implementation
- **AdvancedGame**: Advanced game with AI hints and difficulty levels

### Key Features

- Input validation
- Progress tracking
- Time measurement
- Cross-platform screen clearing
- Statistics persistence

## Future Enhancements

- [ ] Multiplayer support
- [ ] Sound effects
- [ ] GUI version using tkinter
- [ ] Web version using Flask
- [ ] Leaderboard system
- [ ] Custom number ranges

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

This project is open source and available under the MIT License.

## Author

Developed by Raza Zaheer GitHub: @razazaheer12
