import sys
import pygame

def check_keydown_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_top = True
		#print(ship.moving_top)
	elif event.key == pygame.K_DOWN:
		ship.moving_bottom = True

def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_top = False
	elif event.key == pygame.K_DOWN:
		ship.moving_bottom = False

def check_events(ship):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship)
			#print(event)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	pygame.display.flip()