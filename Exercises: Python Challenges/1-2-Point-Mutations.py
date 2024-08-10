# Write a program that can calculate the Hamming distance between two distance
# strands.

# A mutation is simply a mistake that occurs during the creation or copying
# of a nucleic acid, in particular DNA. Because nucleic acids are vital to
# cellular functions, mutations tend to cause a ripple effect throughout the
# cell. Although mutations are technically mistakes, a very rare mutation
# may equip the cell with a beneficial attribute. In fact, the macro effects
# of evolution are attributable to the accumulated result of beneficial 
# microsopic mutations over many generations.

# The simplest and most common type of nucleic acid mutation is a point 
# mutation, which replaces one base with another at a single nucleotide.

# By counting the number of differences between two homologous DNA strands
# taken from different genomes with a common ancestor, we get a measure of
# the minimum number of point mutations that could have occurred on the 
# evolutionary path between the two strands.

# This is called the Hamming distance.

# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# ^ ^ ^  ^ ^    ^^

# The Hamming distance between these two DNA strands is 7.

# The Hamming distance is only defined for sequences of equal length. If you
# have two sequences of unequal length, you should compute the Hamming distance
# over the shorter length.

# Solution:

class DNA:

    def __init__(self, strand):
        self._strand = strand

    @property
    def strand(self):
        return self._strand

    def hamming_distance(self, distance):
        self.distance = distance
        count = 0
        length = min(len(self.strand), len(self.distance))
        characters_strand = list(self.strand[:length])
        characters_distance = list(self.distance[:length])
        for index in range(length):
            if characters_strand[index] != characters_distance[index]:
                count += 1
        return count

# Examples:

import unittest

class TestDNAMutations(unittest.TestCase):

    def test_no_difference_between_empty_strands(self):
        self.assertEqual(0, DNA("").hamming_distance(""))

    def test_no_difference_between_identical_strands(self):
        self.assertEqual(0, DNA("GGACTGA").hamming_distance("GGACTGA"))

    def test_complete_hamming_distance_in_small_strand(self):
        self.assertEqual(3, DNA("ACT").hamming_distance("GGA"))

    def test_hamming_distance_in_off_by_one_strand(self):
        strand = "GGACGGATTCTGACCTGGACTAATTTTGGGG"
        distance = "AGGACGGATTCTGACCTGGACTAATTTTGGGG"
        self.assertEqual(19, DNA(strand).hamming_distance(distance))

    def test_small_hamming_distance_in_middle_somewhere(self):
        self.assertEqual(1, DNA("GGACG").hamming_distance("GGTCG"))

    def test_larger_distance(self):
        self.assertEqual(2, DNA("ACCAGGG").hamming_distance("ACTATGG"))

    def test_ignores_extra_length_on_other_strand_when_longer(self):
        self.assertEqual(3, DNA("AAACTAGGGG").hamming_distance("AGGCTAGCGGTAGGAC"))

    def test_ignores_extra_length_on_original_strand_when_longer(self):
        strand = "GACTACGGACAGGGTAGGGAAT"
        distance = "GACATCGCACACC"
        self.assertEqual(5, DNA(strand).hamming_distance(distance))

    def test_does_not_actually_shorten_original_strand(self):
        dna = DNA("AGACAACAGCCAGCCGCCGGATT")
        self.assertEqual(1, dna.hamming_distance("AGGCAA"))
        self.assertEqual(4, dna.hamming_distance("AGACATCTTTCAGCCGCCGGATTAGGCAA"))
        self.assertEqual(1, dna.hamming_distance("AGG"))