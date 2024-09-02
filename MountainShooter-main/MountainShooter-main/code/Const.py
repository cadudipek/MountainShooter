#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

# Window dimensions
WIN_WIDTH = 800
WIN_HEIGHT = 600

# Color constants
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_RED = (255, 0, 0)
C_GREEN = (0, 255, 0)
C_BLUE = (0, 0, 255)
C_ORANGE = (255, 165, 0)
C_YELLOW = (255, 255, 0)
C_CYAN = (0, 255, 255)

# Menu options
MENU_OPTION = ["Start", "Multiplayer", "Highscore", "Exit", "Help"]

# Background and entity speed
ENTITY_SPEED = {
    'Player1': 5,
    'Player2': 5,
    'Enemy1': 3,
    'Enemy2': 3,
    'Enemy3': 4  # Adding speed for the new enemy
}

# Entity attributes
ENTITY_HEALTH = {
    'Player1': 100,
    'Player2': 100,
    'Enemy1': 50,
    'Enemy2': 50,
    'Enemy3': 60
}

ENTITY_DAMAGE = {
    'Player1': 10,
    'Player2': 10,
    'Enemy1': 5,
    'Enemy2': 5,
    'Enemy3': 8
}

ENTITY_SCORE = {
    'Player1': 0,
    'Player2': 0,
    'Enemy1': 10,
    'Enemy2': 10,
    'Enemy3': 20
}

# Shooting delays
ENTITY_SHOT_DELAY = {
    'Player1': 10,
    'Player2': 10,
    'Enemy1': 30,
    'Enemy2': 30,
    'Enemy3': 20
}

# Events
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# Spawn times and timeout steps
SPAWN_TIME = 2000  # milliseconds
TIMEOUT_STEP = 1000  # milliseconds
TIMEOUT_LEVEL = 20000  # milliseconds (default level duration)

# Score position
SCORE_POS = {
    'Title': (WIN_WIDTH // 2, 50),
    'EnterName': (WIN_WIDTH // 2, WIN_HEIGHT // 2),
    'Name': (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 50),
    'Label': (WIN_WIDTH // 2, WIN_HEIGHT // 2 - 50),
}

# Player controls (example)
PLAYER_KEY_UP = {'Player1': pygame.K_w, 'Player2': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_s, 'Player2': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_a, 'Player2': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_d, 'Player2': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE, 'Player2': pygame.K_RETURN}
