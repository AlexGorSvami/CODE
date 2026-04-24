import unittest 
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left, right, free = 0, 0, 0 
        for move in moves:
            if move == 'L':
                left += 1 
            elif move == 'R':
                right += 1 
            else:
                free += 1 

        result = max(abs(left - right - free), abs(right - left - free))

        return result

class Test(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_free(self):
        self.assertEqual(self.solution.furthestDistanceFromOrigin('___'), 3)
        self.assertEqual(self.solution.furthestDistanceFromOrigin('_'), 1)

    def test_fixed(self):
        self.assertEqual(self.solution.furthestDistanceFromOrigin('LLL'), 3)
        self.assertEqual(self.solution.furthestDistanceFromOrigin('RRR'), 3)
        self.assertEqual(self.solution.furthestDistanceFromOrigin('LR'), 0)

    def test_mixed(self):
        self.assertEqual(self.solution.furthestDistanceFromOrigin('L_'), 2)
        self.assertEqual(self.solution.furthestDistanceFromOrigin('R_'), 2)
        self.assertEqual(self.solution.furthestDistanceFromOrigin('L_R'), 1)

    def test_examples(self):
        self.assertEqual(self.solution.furthestDistanceFromOrigin('L_RL__R'), 3)
        self.assertEqual(self.solution.furthestDistanceFromOrigin('_R__LL_'), 5)
        self.assertEqual(self.solution.furthestDistanceFromOrigin('_______'), 7)

if __name__ == '__main__':
    unittest.main()
