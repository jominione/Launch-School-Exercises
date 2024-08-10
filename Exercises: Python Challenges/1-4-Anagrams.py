# Write a program that takes a word and a list of possible anagrams and selects
# the correct sub-list that contains the anagrams of the word.

# For example, given the word "listen" and a list of candidates like "enlists",
# "google", "inlets", and "banana", the program should return a list containing
# "inlets". Please read the test suite for the exact rules of anagrams.

# Solution:

class Anagram:

    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        anagrams = []
        count_word = { char : 0 for char in set(self.word) }
        for char in list(self.word):
            count_word[char] += 1
        for candidate in candidates:
            candidate_lower = candidate.lower()
            count_candidate = { char : 0 for char in set(candidate_lower) }
            for char in candidate_lower:
                count_candidate[char] += 1
            if (candidate_lower != self.word) and (count_candidate == count_word):
                anagrams.append(candidate) 

        return anagrams

# Examples:

import unittest

class TestAnagram(unittest.TestCase):

    def test_no_matches(self):
        detector = Anagram("diaper")
        self.assertEqual([], detector.match(["hello", "world", "zombies", "pants"]))

    def test_detect_simple_anagram(self):
        detector = Anagram("ant")
        anagrams = detector.match(["tan", "stand", "at"])
        self.assertEqual(["tan"], anagrams)

    def test_detect_multiple_anagrams(self):
        detector = Anagram("master")
        anagrams = detector.match(["stream", "pigeon", "maters"])
        self.assertEqual(sorted(["maters", "stream"]), sorted(anagrams))

    def test_does_not_confuse_different_duplicates(self):
        detector = Anagram("galea")
        self.assertEqual([], detector.match(["eagle"]))

    def test_identical_word_is_not_anagram(self):
        detector = Anagram("corn")
        anagrams = detector.match(
            ["corn", "dark", "Corn", "rank", "CORN", "cron", "park"]
        )
        self.assertEqual(["cron"], anagrams)

    def test_eliminate_anagrams_with_same_checksum(self):
        detector = Anagram("mass")
        self.assertEqual([], detector.match(["last"]))

    def test_eliminate_anagram_subsets(self):
        detector = Anagram("good")
        self.assertEqual([], detector.match(["dog", "goody"]))

    def test_detect_anagram(self):
        detector = Anagram("listen")
        anagrams = detector.match(["enlists", "google", "inlets", "banana"])
        self.assertEqual(["inlets"], anagrams)

    def test_multiple_anagrams(self):
        detector = Anagram("allergy")
        anagrams = detector.match(
            ["gallery", "ballerina", "regally", "clergy", "largely", "leading"]
        )
        self.assertEqual(sorted(["gallery", "largely", "regally"]), sorted(anagrams))

    def test_anagrams_are_case_insensitive(self):
        detector = Anagram("Orchestra")
        anagrams = detector.match(["cashregister", "Carthorse", "radishes"])
        self.assertEqual(["Carthorse"], anagrams)

if __name__ == "__main__":
    unittest.main()