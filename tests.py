#from pygame.locals import *
import pygame
import math
import unittest
#import unit    # unit.py, will contain the unit class and its derivations
#import weapon
import projectile2

# tests related to Projectile class
class TestProjectile(unittest.TestCase):
# inputs: (x, y, speed, angle, damage, sprite filepath)
	x        = 0
	y        = 0
	speed    = 20 # 20 pixels/frame?
	angle    = math.pi / 2 # radians, going straight down (or, increasing the y value)
	damage   = 10
	filepath = "Assets/Art/player_ship.png"
	
	projTest = projectile2.Projectile(x, y, speed, angle, damage, filepath)
	
	def test_getx(self):
		self.assertEqual(self.projTest.getx(), self.x)
		
	def test_setx(self):
		x2 = 50
		self.projTest.setx(x2)
		self.assertEqual(self.projTest.getx(), x2)
		
	def test_gety(self):
		self.assertEqual(self.projTest.gety(), self.y)
		
	def test_sety(self):
		y2 = 50
		self.projTest.sety(y2)
		self.assertEqual(self.projTest.gety(), y2)
		
	def test_setNextLocation(self):
		self.projTest.setx(self.x)
		self.projTest.sety(self.y)
		self.assertEqual((0,20), self.projTest.setNextLocation())
		
	def test_setNextLocationGet(self):
		self.projTest.setx(self.x)
		self.projTest.sety(self.y)
		self.projTest.setNextLocation()
		
		self.assertEqual((0,20), (self.projTest.getx(), self.projTest.gety()))
		
	# def test_getSprite(self):
		# sprite2     = pygame.image.load(self.filepath)
		# sprite2Px	= pygame.PixelArray(sprite2)
		# spritePx	= pygame.PixelArray(self.projTest.getSprite())
		# self.assertEqual(type(self.projTest.getSprite()), pygame.Surface)
		# self.assertEqual(pygame.PixelArray(self.projTest.getSprite()), pygame.PixelArray(sprite2))
		# self.assertEqual(sprite2Px, spritePx)
		
	# def test_setSprite(self):
		# sprite2path = "Assets/Art/enemy_ship.png"
		# sprite2     = pygame.image.load(sprite2path)
		# self.projTest.setSprite(sprite2path)
		# self.assertEqual(self.projTest.getSprite(), sprite2)
		
# class TestWeapon(unittest.TestCase):
	# x        = 0
	# y        = 0
	# speed    = 20 # 20 pixels/frame?
	# angle    = math.pi # radians
	# damage   = 10
	# filepath = "Assets/Art/player_ship.png"
	
	# projTest = projectile.Projectile(x, y, speed, angle, damage, self.filepath)
	
	# weapTest = Weapon(x, y, projTest)
	
	# def test_getx(self):
		# self.assertEqual(weapTest.getx(), x)
		
	# def test_setx(self):
		# x2 = 50
		# projTest.setx(x2)
		# self.assertEqual(weapTest.getx(), x2)
		
	# def test_gety(self):
		# self.assertEqual(weapTest.gety(), y)
		
	# def test_sety(self):
		# y2 = 50
		# projTest.setY(y2)
		# self.assertEqual(weapTest.gety(), y2)
		
	# def test_getProj(self):
		# projArray = weapTest.getProj()
		# self.assertEqual(projArray[0], projTest)
		
	# def test_updateProj(self):
		# weapTest.updateProj()
		# projArray = weapTest.getProj()
		# projVal   = projArray[0]
		
		# self.assertEqual((0,20), (projVal.getx(), projVal.gety()))
		
	# def test_setProjType(self):
		# speed2    = 30
		# projTest2 = Projectile(x, y, speed2, angle, damage, self.filepath)
		# weapTest.setProjType(projTest)
		# projArr   = weapTest.getProj()
		# proj      = projArr[0]
		
		# self.assertEqual(proj, projTest2)
		
	# inputs: (x, y, ProjType)
	# initializations:
		# setx()
		# sety()
		# setProjType()
		# updateProj()
	# attributes:
		# proj :: [Projectile] # array of projectiles being fired from this weapon
		# xloc :: Int
		# yloc :: Int
		
	# methods:
		# getx() 					 :: Int
		# setx(Int)				 :: Void
		# gety() 					 :: Int
		# sety(Int)				 :: Void
		# getProj()       		 :: [Projectile]
		# first updateProj updates the weapons x,y location,
			# then it checks if it is time to add another projectile,
				# if so, it appends it to the proj array
			# then it cycles through all the projectiles, calls setNextLocation,
				# and then if the projectile is off screen, removes it.
		# updateProj(Int,Int)      :: Void 
		# setProjType(Projectile)  :: Void # sets projectile type to use

# test things related to the Enemy class
# class TestUnitInitializationsEnemy(unittest.TestCase):
	# filepath  = "Assets/Art/player_ship.png"
	# x		  = 0
	# y         = 0
	# health    = 100
	
	# weap      = Weapon(0,0,Type1)            # TODO: change projectile type once we agree on actual projectiles
	# def mvmtPatt((x,y)):                     # basic pattern that moves unit diagonally
		# return (x+1,y+1)
		
	# enemyTest = Enemy(self.filepath, health, weap, x, y, mvmtPatt) # (sprite filepath, health, weapon, xinit, yinit, movement pattern)
	
	# def test_getHealth(self):
		# self.assertEqual(enemyTest.getHealth(), health)
		
	# def test_setHealth(self):
		# enemyTest.setHealth(50)
		# self.assertEqual(enemyTest.getHealth(), 50)
		
	# def test_getWeapon(self):
		# self.assertEqual(enemyTest.getWeapon, weap)
		
	# def test_setWeapon(self):
		# weap2 = Weapon(100,100,Type2)	# TODO: change projectile type once we agree on actual projectiles
		# enemyTest.setWeapon(weap2)
		# self.assertEqual(enemyTest.getWeapon, weap2)
	
	# def test_getSprite(self):
		# sprite2     = pygame.image.load(self.filepath)
		# self.assertEqual(enemyTest.getSprite(), sprite2)
		
	# def test_setSprite(self):
		# sprite2path = "test2.png"
		# sprite2     = pygame.image.load(sprite2path)
		# enemyTest.setSprite(sprite2path)
		# self.assertEqual(enemyTest.getSprite(), sprite2)
		
	# def test_getx(self):
		# self.assertEqual(enemyTest.getx(), x)
		
	# def test_setx(self):
		# x2 = 50
		# enemyTest.setx(x2)
		# self.assertEqual(enemyTest.getx(), x2)
		
	# def test_gety(self):
		# self.assertEqual(enemyTest.gety(), y)
		
	# def test_sety(self):
		# y2 = 50
		# enemyTest.setY(y2)
		# self.assertEqual(enemyTest.gety(), y2)
		
		
# test things related to the Player class
# class TestUnitInitializationsPlayer(unittest.TestCase):
	# filepath  = "Assets/Art/player_ship.png"
	# x		  = 0
	# y         = 0
	# health    = 100
	
	# weap      = Weapon(0,0,Type1)            # TODO: change projectile type once we agree on actual projectiles
		
	# playerTest = Player(self.filepath, health, weap, x, y) # (sprite filepath, health, weapon, xinit, yinit, movement pattern)
	
	# def test_getHealth(self):
		# self.assertEqual(playerTest.getHealth(), health)
		
	# def test_setHealth(self):
		# playerTest.setHealth(50)
		# self.assertEqual(playerTest.getHealth(), 50)
		
	# def test_getWeapon(self):
		# self.assertEqual(playerTest.getWeapon, weap)
		
	# def test_setWeapon(self):
		# weap2 = Weapon(100,100,Type2)	# TODO: change projectile type once we agree on actual projectiles
		# playerTest.setWeapon(weap2)
		# self.assertEqual(playerTest.getWeapon, weap2)
	
	# def test_getSprite(self):
		# sprite2     = pygame.image.load(self.filepath)
		# self.assertEqual(playerTest.getSprite(), sprite2)
		
	# def test_setSprite(self):
		# sprite2path = "test2.png"
		# sprite2     = pygame.image.load(sprite2path)
		# playerTest.setSprite(sprite2path)
		# self.assertEqual(playerTest.getSprite(), sprite2)
		
	# def test_getx(self):
		# self.assertEqual(playerTest.getx(), x)
		
	# def test_setx(self):
		# x2 = 50
		# playerTest.setx(x2)
		# self.assertEqual(playerTest.getx(), x2)
		
	# def test_gety(self):
		# self.assertEqual(playerTest.gety(), y)
		
	# def test_sety(self):
		# y2 = 50
		# playerTest.setY(y2)
		# self.assertEqual(playerTest.gety(), y2)


# defines projectile test suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestProjectile())
    return suite

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	test_suite = unittest.TestLoader().loadTestsFromTestCase(TestProjectile)
    # test_suite = suite()
	runner.run (test_suite)
#unittest.main()

