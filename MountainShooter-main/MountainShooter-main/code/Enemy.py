#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from code.Entity import Entity
from code.Const import ENTITY_SPEED, ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE, WIN_WIDTH
from code.EnemyShot import EnemyShot


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED[self.name]
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]

    def move(self):
        self.rect.centerx -= self.speed

    def shoot(self):
        # Implementing shooting mechanism for enemies
        if random.randint(0, 100) < 2:  # Random chance to shoot
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        return None
