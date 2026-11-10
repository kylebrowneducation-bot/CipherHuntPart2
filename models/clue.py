
from datetime import date
import random


class ClueModel:
    def __init__(self, id, user_id, clue_text, key, date_created=None, is_solved=False):
        self.__id = id
        self.__user_id = user_id
        self.__clue_text = clue_text
        self.__key = key
        self.__date_created = date_created if date_created is not None else date.today().isoformat()
        self.__is_solved = is_solved

    @property
    def id(self):
        return self.__id

    @property
    def user_id(self):
        return self.__user_id

    @property
    def clue_text(self):
        return self.__clue_text

    @property
    def key(self):
        return self.__key

    @property
    def date_created(self):
        return self.__date_created

    @property
    def is_solved(self):
        return self.__is_solved

    # --- SADIA: check_answer goes here ---


# --- SUGAM: ClueBank goes here ---


# --- TAMI: test block goes here ---
