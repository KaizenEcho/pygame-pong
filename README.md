# Pygame Pong

A classic 2D Pong game prototype built with Python and Pygame.

## Features
- **Frame-independent movement:** Smooth physics powered by `delta_time`.
- **Player Control:** Responsive keyboard control for the left paddle.
- **Simple AI:** The right paddle automatically tracks the ball.
- **Custom Collisions:** AABB collision logic for paddles and walls.
- **Game Over State:** Screen resets with a Game Over message if the ball passes a paddle.

## Controls
- `W` — Move paddle up
- `S` — Move paddle down

## How to Run
```bash
pip install pygame
python Pong.py
```
