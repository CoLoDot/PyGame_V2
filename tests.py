import unittest
from pygame.math import Vector2
from main import *


class TestWindow(unittest.TestCase):

    def setUp(self):
        self.w = 510
        self.h = 580

    def test_wh(self):
        """Test if window's width and height are correct"""
        self.assertEqual(self.w, winWidth)
        self.assertEqual(self.h, winHeight)


class TestMaze(unittest.TestCase):

    def setUp(self):
        self.item_1 = '0'
        self.item_2 = 'm'
        self.item_3 = 'a'
        self.maze_list = [maze_1, maze_2]
        self.choice = random.choice(self.maze_list)
        self.a_level = []

    def test_type_Items(self):
        """Test if item are str"""
        self.assertTrue(self.item_1, str)
        self.assertTrue(self.item_2, str)
        self.assertTrue(self.item_3, str)

    def test_Item_1_In(self):
        """Test if 0 is in maze_1 and maze_2"""
        self.assertIn(self.item_1, maze_1)
        self.assertIn(self.item_1, maze_2)

    def test_Item_2_In(self):
        """Test if m is in maze_1 and maze_2"""
        self.assertIn(self.item_2, maze_1)
        self.assertIn(self.item_2, maze_2)

    def test_Item_3_In(self):
        """Test if a is in maze_1 and maze_2"""
        self.assertIn(self.item_3, maze_1)
        self.assertIn(self.item_3, maze_2)

    def test_type_Mazes(self):
        """Test if maze_1 and maze_2 are str"""
        self.assertTrue(maze_1, str)
        self.assertTrue(maze_2, str)

    def test_choose_Maze(self):
        """Test if a maze is randomly chosen"""
        self.assertTrue(self.choice)

    def test_splitting_file(self):
        """Test if a randomly chosen maze is split"""
        for line in self.choice.split('\n'):
            line = list(line)
            self.a_level.append(line)

        self.assertNotIn('\n', self.a_level)


class TestSurfaceCreation(unittest.TestCase):

    def setUp(self):
        self.position = Vector2(45, 45)
        self.Group = pygame.sprite.Group()
        self.surface = Floor(self.position.x * number_of_sprite,
                             self.position.y * number_of_sprite)

    def test_sprite_got_rect(self):
        """Test if a surface created got a rect"""
        self.assertTrue(self.surface.rect)

    def test_sprite_creation_Floor(self):
        """Test if a sprite is correctly created as a Floor instance"""
        create_surface = Floor(self.position.x * number_of_sprite,
                               self.position.y * number_of_sprite)
        self.Group.add(create_surface)
        self.assertTrue(create_surface)

    def test_sprite_creation_End(self):
        """Test if a sprite is correctly created as an End instance"""
        create_surface = End(self.position.x * number_of_sprite,
                             self.position.y * number_of_sprite)
        self.Group.add(create_surface)
        self.assertTrue(create_surface)

    def test_sprite_creation_PickPotion(self):
        """Test if a sprite is correctly created as a PickPotion instance"""
        create_surface = PickPotion(self.position.x * number_of_sprite,
                                    self.position.y * number_of_sprite)
        self.Group.add(create_surface)
        self.assertTrue(create_surface)

    def test_sprite_creation_PickCoin(self):
        """Test if a sprite is correctly created as a PickCoin instance"""
        create_surface = PickCoin(self.position.x * number_of_sprite,
                                  self.position.y * number_of_sprite)
        self.Group.add(create_surface)
        self.assertTrue(create_surface)

    def test_sprite_creation_PickSafe(self):
        """Test if a sprite is correctly created as a PickSafe instance"""
        create_surface = PickSafe(self.position.x * number_of_sprite,
                                  self.position.y * number_of_sprite)
        self.Group.add(create_surface)
        self.assertTrue(create_surface)

    def test_sprite_creation_Walls(self):
        """Test if a sprite is correctly created as a Walls instance"""
        create_surface = Walls(self.position.x * number_of_sprite,
                               self.position.y * number_of_sprite)
        self.Group.add(create_surface)
        self.assertTrue(create_surface)

    def test_sprite_creation_Player(self):
        """Test if a sprite is correctly created as a Macgyver instance"""
        create_surface = Macgyver(self.position.x * number_of_sprite,
                                  self.position.y * number_of_sprite,
                                  wallsMaze=self.Group)
        self.assertTrue(create_surface)


if __name__ == '__main__':
    unittest.main()
