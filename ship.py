import pygame

class Ship():
	def __init__(self,screen,ai_settings):
		'''初始化飞船并设置其初始位置'''
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		
		self.centerx = float(self.rect.centerx)
		
		self.moving_right = False
		self.moving_left = False
		



	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.ship_speed_factor

		self.rect.centerx = self.centerx

	def blitme(self):
		'''在指定位置绘制飞船'''
		self.screen.blit(self.image,self.rect)