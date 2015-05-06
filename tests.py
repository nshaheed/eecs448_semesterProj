from pygame.locals import *
import math
import unittest
import unit    # unit.py, will contain the unit class and its derivations

# tests related to Projectile class
class TestUnitProjectile(unittest.TestCase):
# inputs: (x, y, speed, angle, damage, sprite filepath)
	x        = 0
	y        = 0
	speed    = 20 # 20 pixels/frame?
	angle    = math.pi # radians
	damage   = 10
	filepath = "test.png"
	
	projTest = Projectile(x, y, speed, angle, damage, filepath)
	
		# getx() 					 :: Int
		# setx(Int)				     :: Void
		# gety() 					 :: Int
		# sety(Int)				     :: Void
		# setNextLocation() 		 :: (Int, Int) # external function that uses movementPattern to change the x,y values of the projectile
		# getSprite() 			     :: Surface
		# setSprite(String) 		 :: Void
		# setSpeed(Int) 			 :: Void
		# setAngle(Double) 		     :: Void
		# movementPattern(Int,Int)   :: (Int,Int) # internal function that will get location of projectile for next frame, uses speed and angle in calculation
	
	def test_getx(self):
		self.assertEqual(projTest.getx(), x)
		
	def test_setx(self):
		x2 = 50
		projTest.setx(x2)
		self.assertEqual(projTest.getx(), x2)
		
	def test_gety(self):
		self.assertEqual(projTest.gety(), y)
		
	def test_sety(self):
		y2 = 50
		projTest.setY(y2)
		self.assertEqual(projTest.gety(), y2)
		
	def test_setNextLocation(self):
		projTest.setx(x)
		projTest.sety(y)
		self.assertEqual((0,20), projTest.setNextLocation())
		
	def test_setNextLocationGet(self):
		projTest.setx(x)
		projTest.sety(y)
		projTest.setNextLocation()
		
		self.assertEqual((0,20), (projTest.getx(), projTest.gety()))
		
	def test_getSprite(self):
		sprite2     = pygame.image.load(filepath)
		self.assertEqual(projTest.getSprite(), sprite2)
		
	def test_setSprite(self):
		sprite2path = "test2.png"
		sprite2     = pygame.image.load(sprite2path)
		projTest.setSprite(sprite2path)
		self.assertEqual(projTest.getSprite(), sprite2)
		
	# def test_angle(self):
		# angle2 = .75 * math.pi
		# projTest.setAngle(angle2)

# test things related to the Enemy class
class TestUnitInitializationsEnemy(unittest.TestCase):
	filepath  = "test.png"
	x		  = 0
	y         = 0
	health    = 100
	
	weap      = Weapon(0,0,Type1)            # TODO: change projectile type once we agree on actual projectiles
	def mvmtPatt((x,y)):                     # basic pattern that moves unit diagonally
		return (x+1,y+1)
		
	enemyTest = Enemy(filepath, health, weap, x, y, mvmtPatt) # (sprite filepath, health, weapon, xinit, yinit, movement pattern)
	
	def test_getHealth(self):
		self.assertEqual(enemyTest.getHealth(), health)
		
	def test_setHealth(self):
		enemyTest.setHealth(50)
		self.assertEqual(enemyTest.getHealth(), 50)
		
	def test_getWeapon(self):
		self.assertEqual(enemyTest.getWeapon, weap)
		
	def test_setWeapon(self):
		weap2 = Weapon(100,100,Type2)	# TODO: change projectile type once we agree on actual projectiles
		enemyTest.setWeapon(weap2)
		self.assertEqual(enemyTest.getWeapon, weap2)
	
	def test_getSprite(self):
		sprite2     = pygame.image.load(filepath)
		self.assertEqual(enemyTest.getSprite(), sprite2)
		
	def test_setSprite(self):
		sprite2path = "test2.png"
		sprite2     = pygame.image.load(sprite2path)
		enemyTest.setSprite(sprite2path)
		self.assertEqual(enemyTest.getSprite(), sprite2)
		
	def test_getx(self):
		self.assertEqual(enemyTest.getx(), x)
		
	def test_setx(self):
		x2 = 50
		enemyTest.setx(x2)
		self.assertEqual(enemyTest.getx(), x2)
		
	def test_gety(self):
		self.assertEqual(enemyTest.gety(), y)
		
	def test_sety(self):
		y2 = 50
		enemyTest.setY(y2)
		self.assertEqual(enemyTest.gety(), y2)
		
		
# test things related to the Player class
class TestUnitInitializationsPlayer(unittest.TestCase):
	filepath  = "test.png"
	x		  = 0
	y         = 0
	health    = 100
	
	weap      = Weapon(0,0,Type1)            # TODO: change projectile type once we agree on actual projectiles
		
	playerTest = Player(filepath, health, weap, x, y) # (sprite filepath, health, weapon, xinit, yinit, movement pattern)
	
	def test_getHealth(self):
		self.assertEqual(playerTest.getHealth(), health)
		
	def test_setHealth(self):
		playerTest.setHealth(50)
		self.assertEqual(playerTest.getHealth(), 50)
		
	def test_getWeapon(self):
		self.assertEqual(playerTest.getWeapon, weap)
		
	def test_setWeapon(self):
		weap2 = Weapon(100,100,Type2)	# TODO: change projectile type once we agree on actual projectiles
		playerTest.setWeapon(weap2)
		self.assertEqual(playerTest.getWeapon, weap2)
	
	def test_getSprite(self):
		sprite2     = pygame.image.load(filepath)
		self.assertEqual(playerTest.getSprite(), sprite2)
		
	def test_setSprite(self):
		sprite2path = "test2.png"
		sprite2     = pygame.image.load(sprite2path)
		playerTest.setSprite(sprite2path)
		self.assertEqual(playerTest.getSprite(), sprite2)
		
	def test_getx(self):
		self.assertEqual(playerTest.getx(), x)
		
	def test_setx(self):
		x2 = 50
		playerTest.setx(x2)
		self.assertEqual(playerTest.getx(), x2)
		
	def test_gety(self):
		self.assertEqual(playerTest.gety(), y)
		
	def test_sety(self):
		y2 = 50
		playerTest.setY(y2)
		self.assertEqual(playerTest.gety(), y2)

	

if __name__ == '__main__':
    unittest.main()

