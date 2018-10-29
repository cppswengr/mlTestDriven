import random

class NumberGuesser:
    """Guesses numbers based on the history of your input"""

    def __init__(self):
        self._guessed_numbers = None

    def number_was(self, guessed_number):
        self._guessed_numbers = [guessed_number]

    def numbers_were(self, guessed_numbers):
        self._guessed_numbers = guessed_numbers

    def guess(self):
        if self._guessed_numbers == None:
            return None
        return random.choice(self._guessed_numbers)
