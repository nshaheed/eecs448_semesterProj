from pygame.locals import *
import unittest
import unit    # unit.py, will contain the unit class and its derivations

# test things related to the Enemy class
class TestUnitInitializationsEnemy(unittest.TestCase):
	filepath  = "test.png"
	weap      = Weapon(0)                    # filler, I haven't defined how to Weapon yet
	def mvmtPatt((x,y)):                     # basic pattern that moves unit diagonally
		return (x+1,y+1)
		
	enemyTest = Enemy(filepath, 100, weap, 0, 0, mvmtPatt) # (sprite filepath, health, weapon, xinit, yinit, movement pattern)
	
	def test_getHealth(self):
		self.assertEqual(enemyTest.getHealth(), 100)
		
	def test_setHealth(self):
		enemyTest.setHealth(50)
		self.assertEqual(enemyTest.getHealth(), 50)

if __name__ == '__main__':
    unittest.main()

