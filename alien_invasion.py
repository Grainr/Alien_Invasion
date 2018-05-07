#import sys
import pygame
from settings import Settings
from ship import Ship
from rocket import Rocket
import game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,\
		ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	ship = Ship(screen,ai_settings)

	#bg_color = (110,130,130)

	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings,screen,ship)

run_game()

