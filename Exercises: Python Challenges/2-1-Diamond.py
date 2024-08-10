# The diamond exercise takes as its input a letter, and outputs it in a 
# diamond shape. Given a letter, it prints a diamond starting with 'A', with
# the supplied letter at the wildest point.

# * The first row contains one 'A'.
# * The last row contains one 'A'.
# * All rows, exxcept the first and last, have exactly two identical letters.
# * The diamond is horizontally symmetric.
# * The diamond is vertically symmetric.
# * The diamond has a square shape (width equals height).
# * The letters form a diamond shape.
# * The top half has the letters in ascending order.
# * The bottom half has the letters in descending order.
# * The four corners (containing the spaces) are triangles.

# Examples:

# Diamond for letter 'A':

# A

# Diamond for letter 'C':

#   A
#  B B
# C   C
#  B B
#   A

# Diamond for letter 'E':

#     A
#    B B
#   C   C
#  D     D
# E       E
#  D     D
#   C   C
#    B B
#     A

# Solution:

class Diamond:

    ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']

    @classmethod
    def make_diamond(cls, letter):
        diamond = None
        if letter == 'A':
            return "A\n"
        else:
            diamond = cls._top_half(letter) + cls._bottom_half(letter)  
        return ''.join(diamond)

    @staticmethod
    def _top_half(letter):
        alphabet = Diamond.ALPHABET
        length = alphabet.index(letter)
        top_half = [f"{' ' * length}A{' ' * length}\n"]
        for top_index in range(1, length):
            top_half.append(
                f"{' ' * (length-top_index)}{alphabet[top_index]}" +
                f"{' ' * (2 * top_index - 1)}" + 
                f"{alphabet[top_index]}{' ' * (length-top_index)}\n"
                )
        return top_half
    
    @staticmethod
    def _bottom_half(letter):
        bottom_half = []
        alphabet = Diamond.ALPHABET        
        length = alphabet.index(letter)
        for bottom_index in range(length, 0, -1):
            bottom_half.append(
                f"{' ' * (length - bottom_index)}{alphabet[bottom_index]}" +
                f"{' ' * (2 * bottom_index - 1)}" + 
                f"{alphabet[bottom_index]}{' ' * (length - bottom_index)}\n"
                )
        bottom_half.append(f"{' ' * length}A{' ' * length}\n")
        return bottom_half

# Examples:

import unittest

class DiamondTest(unittest.TestCase):

    def test_letter_a(self):
        answer = Diamond.make_diamond('A')
        self.assertEqual("A\n", answer)

    def test_letter_b(self):
        answer = Diamond.make_diamond('B')
        expected = " A \nB B\n A \n"
        self.assertEqual(expected, answer)

    def test_letter_c(self):
        answer = Diamond.make_diamond('C')
        expected = "  A  \n" \
                   " B B \n" \
                   "C   C\n" \
                   " B B \n" \
                   "  A  \n"
        self.assertEqual(expected, answer)

    def test_letter_e(self):
        answer = Diamond.make_diamond('E')
        expected = "    A    \n" \
                   "   B B   \n" \
                   "  C   C  \n" \
                   " D     D \n" \
                   "E       E\n" \
                   " D     D \n" \
                   "  C   C  \n" \
                   "   B B   \n" \
                   "    A    \n"
        self.assertEqual(expected, answer)

if __name__ == '__main__':
    unittest.main()