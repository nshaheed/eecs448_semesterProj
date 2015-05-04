from pygame.locals import *
import unittest
import unit    # unit.py, will contain the unit class and its derivations

# test things related to the Enemy class
class TestUnitInitializationsEnemy(unittest.TestCase):
	filepath  = "test.png"
	x		  = 0
	y         = 0
	weap      = Weapon(0,0,Type1)            # TODO: change projectile type once we agree on actual projectiles
	def mvmtPatt((x,y)):                     # basic pattern that moves unit diagonally
		return (x+1,y+1)
		
	health = 100
	
		
	enemyTest = Enemy(filepath, health, weap, x, y, mvmtPatt) # (sprite filepath, health, weapon, xinit, yinit, movement pattern)
	
	def test_getHealth(self):
		self.assertEqual(enemyTest.getHealth(), 100)
		
	def test_setHealth(self):
		enemyTest.setHealth(50)
		self.assertEqual(enemyTest.getHealth(), 50)
		
	def test_getWeapon(self):
		self.assertEqual(enemyTest.getWeapon, weap)
		
	def test_setWeapon(self):
		weap2 = Weapon(100,100,Type2)	# TODO: change projectile type once we agree on actual projectiles
		enemyTest.setWeapon(weap2)
		self.assertEqual(enemyTest.getWeapon, weap2)

	

if __name__ == '__main__':
    unittest.main()

