# Write a program that, given a word, computes the Scrabble score for that
# word.

# Letter Values

# You'll need the following tile scores:

# |------------------------------|-------|
# | Letter                       | Value |
# |------------------------------|-------|
# | A, E, I, O, U, L, N, R, S, T |   1   |
# | D, G                         |   2   |
# | B, C, M, P                   |   3   |
# | F, H, V, W, Y                |   4   |
# | K                            |   5   |
# | J, X                         |   8   |
# | Q, Z                         |  10   |
# |------------------------------|-------|

# How to Score

# Sum the values of all the tiles used in each word. For instance, lets 
# consider the word CABBAGE which has the following letters and point values:

# * 3 points for C
# * 1 point for each A (there are two)
# * 3 points for B (there are two)
# * 2 points for G
# * 1 point for E

# Thus, to compute the final total (14 points), we count:

# 3 + 2*1 + 2*3 + 2 + 1
# => 3 + 2 + 6 + 3
# => 5 + 9
# => 14

# Solution:

class Scrabble:

    SCORE = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 
        'T': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4,
        'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10,
    }

    def __init__(self, word):
        self.word = word if word else ''

    @classmethod
    def calculate_score(cls, word):
        return cls(word).score()

    def score(self):
        result = sum([Scrabble.SCORE.get(char, 0) for char in \
                      self.word.upper()])
        return result

# Examples:

import unittest

class ScrabbleTest(unittest.TestCase):

    def test_empty_word_scores_zero(self):
        self.assertEqual(0, Scrabble("").score())

    def test_whitespace_scores_zero(self):
        self.assertEqual(0, Scrabble(" \t\n").score())

    def test_nil_scores_zero(self):
        self.assertEqual(0, Scrabble(None).score())

    def test_scores_very_short_word(self):
        self.assertEqual(1, Scrabble("a").score())

    def test_scores_other_very_short_word(self):
        self.assertEqual(4, Scrabble("f").score())

    def test_simple_word_scores_the_number_of_letters(self):
        self.assertEqual(6, Scrabble("street").score())

    def test_complicated_word_scores_more(self):
        self.assertEqual(22, Scrabble("quirky").score())

    def test_scores_are_case_insensitive(self):
        self.assertEqual(41, Scrabble("OXYPHENBUTAZONE").score())

    def test_convenient_scoring(self):
        self.assertEqual(13, Scrabble.calculate_score("alacrity"))

if __name__ == "__main__":
    unittest.main()