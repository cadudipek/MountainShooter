#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
from typing import List, Tuple, Dict, Any


class DBProxy:
    def __init__(self, db_name: str):
        self.connection = sqlite3.connect(f'{db_name}.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
            date TEXT NOT NULL
        )''')
        self.connection.commit()

    def save(self, record: Dict[str, Any]):
        self.cursor.execute('INSERT INTO scores (name, score, date) VALUES (?, ?, ?)',
                            (record['name'], record['score'], record['date']))
        self.connection.commit()

    def retrieve_top10(self) -> List[Tuple[int, str, int, str]]:
        self.cursor.execute('SELECT * FROM scores ORDER BY score DESC LIMIT 10')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
