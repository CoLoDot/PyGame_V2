import unittest
import pygame
from constants import *

class TestWindow(unittest.TestCase):
    def setUp(self):
        self.w = 510
        self.h = 580

    def test_wh(self):
        self.assertEqual(self.w, winWidth)
        self.assertEqual(self.h, winHeight)


class TestMaze(unittest.TestCase):

    def setUp(self):
        self.item_1 = '0'
        self.item_2 = 'm'
        self.item_3 = 'a'

    def test_type_Items(self):
        self.assertTrue(type.__str__(self.item_1))
        self.assertTrue(type.__str__(self.item_2))
        self.assertTrue(type.__str__(self.item_3))

    def test_Item_1_In(self):
        self.assertIn(self.item_1, maze_1)
        self.assertIn(self.item_1, maze_2)

    def test_Item_2_In(self):
        self.assertIn(self.item_2, maze_1)
        self.assertIn(self.item_2, maze_2)

    def test_Item_3_In(self):
        self.assertIn(self.item_3, maze_1)
        self.assertIn(self.item_3, maze_2)

    def test_type_Mazes(self):
        self.assertTrue(type.__str__(maze_1))
        self.assertTrue(type.__str__(maze_2))


