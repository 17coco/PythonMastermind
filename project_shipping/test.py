'''
    test suite for mastermind
'''

import unittest
from secret_code import *
from leaderboard import *

class TestFunctions(unittest.TestCase):
    '''test class for mastermind'''
    def test_comparison(self):
        '''test comparison'''
        secret_code = ["red", "blue", "yellow", "green"]
        self.assertEqual(
            (4, 0), comparison(secret_code,
                               ["red", "blue", "yellow", "green"]))
        self.assertEqual(
            (0, 4), comparison(secret_code,
                               ["blue", "red", "green", "yellow"]))
        self.assertEqual(
            (2, 2), comparison(secret_code,
                               ["red", "blue", "green", "yellow"]))
        self.assertEqual(
            (2, 0), comparison(secret_code,
                               ["red", "blue", "black", "purple"]))
        self.assertEqual(
            (0, 2), comparison(secret_code,
                               ["black", "purple", "green", "yellow"]))
        
    def test_leaderboard(self):
        '''test leaderboard fucntions'''
        old_leaderboard = "33: 4\nTrem: 7\n"
        self.assertEqual(
            "33: 4\nTremolo: 4\nTrem: 7\n",
            leaderboard_output(
                leaderboard_requencer(
                    leader_board_reader(
                        old_leaderboard), ["Tremolo", '4'])))
        
        old_leaderboard = "33: 4\nTremolo: 4\nTrem: 7\n"
        self.assertEqual(
            "Zihan: 1\n33: 4\nTremolo: 4\nTrem: 7\n",
            leaderboard_output(
                leaderboard_requencer(
                    leader_board_reader(
                        old_leaderboard), ["Zihan", '1'])))
        
        old_leaderboard = "Zihan: 1\n33: 4\nTremolo: 4\nTrem: 7\n"
        self.assertEqual(
            "Zihan: 1\n33: 4\nTremolo: 4\nTrem: 7\nLast: 9\n",
            leaderboard_output(
                leaderboard_requencer(
                    leader_board_reader(
                        old_leaderboard), ["Last", '9'])))
        
        old_leaderboard = "Zihan: 1\n33: 4\nTremolo: 4\nTrem: 7\nLast: 9\n"
        self.assertEqual(
            "Zihan: 1\n33: 4\nTremolo: 4\nTrem: 7\nLast: 9\n",
            leaderboard_output(
                leaderboard_requencer(
                    leader_board_reader(
                        old_leaderboard), ["Catch", '10'])))
        
        old_leaderboard = "Zihan: 1\n33: 4\nTremolo: 4\nTrem: 7\nLast: 9\n"
        self.assertEqual(
            "Zihan: 1\n33: 4\nTremolo: 4\nInsert: 5\nTrem: 7\n",
            leaderboard_output(
                leaderboard_requencer(
                    leader_board_reader(
                        old_leaderboard), ["Insert", '5'])))
        
if __name__ == "__main__":
    unittest.main(verbosity=3)
