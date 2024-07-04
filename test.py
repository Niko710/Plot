import unittest
from main import Plot
from pathlib import Path


class FuncTest(unittest.TestCase):
    # compare the value we expect and get, in this case we compare paths
    def test_paths(self):
        paths = Plot('deviation.json').draw_plots()
        self.assertEqual(paths.sort(), [path for path in Path('plots').iterdir()].sort())


if __name__ == '__main__':
    unittest.main()
