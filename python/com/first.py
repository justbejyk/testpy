
import unittest

class Test(unittest.TestCase):
    
    def test_robot(self):
        from core import Robot
        robot = Robot(x=0,y=0);
        robot.print_mood()
        robot.walk(x=2, y=1);
        self.assertEqual(robot.get_position(), (2,1));
        robot.print_mood()
        