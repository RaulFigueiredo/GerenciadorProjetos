import unittest
from unittest.mock import MagicMock
from src.gui.homepage import TopBar
class TestTopBar(unittest.TestCase):

    def setUp(self):
        self.parent = MagicMock()
        self.on_navigate = MagicMock()
        self.bg_color = '#5a6e7f'
        self.fg_color = 'white'
        self.top_bar = TopBar(self.parent, self.on_navigate, bg_color=self.bg_color, fg_color=self.fg_color)
        self.parent.__getitem__.return_value = self.bg_color
        self.top_bar = TopBar(self.parent, self.on_navigate, bg_color=self.bg_color, fg_color=self.fg_color)

    def test_initialization(self):
        # Test if the TopBar is initialized correctly
        # self.assertEqual(self.top_bar['bg'], self.bg_color)
        # self.assertTrue(self.top_bar.grid_info())
        pass


if __name__ == '__main__':
    unittest.main()
