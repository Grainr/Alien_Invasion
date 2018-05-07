import pygame

class Rocket():
	def __init__(self,screen,ai_settings):
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.center = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)

		self.moving_right = False
		self.moving_left = False
		self.moving_top = False
		self.moving_bottom = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		if self.moving_top and self.rect.top > self.screen_rect.top:
			#print("T")
			self.bottom -= self.ai_settings.ship_speed_factor
		if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
			self.bottom += self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center
		self.rect.bottom = self.bottom

	def blitme(self):
		'''在指定位置绘制飞船'''
		self.screen.blit(self.image,self.rect)