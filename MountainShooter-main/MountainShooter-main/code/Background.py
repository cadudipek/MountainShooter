#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect

from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED


class Background:
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED.get(name, 1)  # Default speed if not specified

    def move(self):
        self.rect.centerx -= self.speed
        if self.rect.centerx < -WIN_WIDTH:
            self.rect.centerx = WIN_WIDTH
