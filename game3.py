import pygame
from random import randint,choice
from sys import exit

def display_score():
	current_time=int(pygame.time.get_ticks()/1000 - start_time)
	score_surf = test_font.render(f'Wynik:{current_time}',False,(64,64,64))
	score_rect=score_surf.get_rect(center = (400,50))
	screen.blit(score_surf,score_rect)
	return current_time	

def rot_center(image,angle,x,y):
	global rotated_image, sashimi_rect1
	rotated_image=pygame.transform.rotate(image,angle)
	sashimi_rect1=rotated_image.get_rect(center=image.get_rect(center=(x,y)).center)

	return rotated_image, sashimi_rect1

pygame.init() #Starts pygame
programIcon=pygame.image.load('graphics/dokku_icon.png')
pygame.display.set_icon(programIcon)
pygame.display.set_caption('Dokku Runner')
screen=pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
test_font=pygame.font.Font('font/Amatic.ttf', 50)


game_active=False
start_time=0
 
sky_surface=pygame.image.load('graphics/skyalpha.png').convert()
#sky_rect=sky_surface.get_rect(center=(0,0))
ground_surface=pygame.image.load('graphics/Asphalt.png').convert()

#play button
play_surf=pygame.image.load('graphics/play_button.png').convert_alpha()
play_surf=pygame.transform.scale(play_surf,(30,30))
play_rect=play_surf.get_rect(topleft=(10,10))

pause_surf=pygame.image.load('graphics/pause_button.png').convert_alpha()
pause_surf=pygame.transform.scale(pause_surf,(30,30))

####snail####
snail_surf = pygame.image.load('graphics/rolki/futomak.png')
snail_surf=pygame.transform.scale(snail_surf,(60,60))
snail_rect= snail_surf.get_rect(bottomright=(600,300))

snail_gravity=0

####Cool_snail####
smoke=0
snailsmoke_surf=pygame.image.load('graphics/rolki/nigiri.png')
snailsmoke_surf=pygame.transform.scale(snailsmoke_surf,(80,60))
snailsmoke_rect=snailsmoke_surf.get_rect(bottomright=(1200,300))

###SASHIMI####
sashimi_y=300
sashimi_surf=pygame.image.load('graphics/rolki/Sashimi.png').convert_alpha()
sashimi_surf=pygame.transform.scale(sashimi_surf,(200,200))
sashimi_rect=sashimi_surf.get_rect(center=(1200,sashimi_y))
ROTATE=rot_center
sashimi_rect1=sashimi_surf.get_rect(center=(1200,sashimi_y))

player_surf = pygame.image.load('graphics/player2/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom= (80,300))

player_gravity=0


surftest=1
dumbtest=1
sashimitest=0

#####Game screen#####

text1='Dokku Runner'
title=test_font.render(text1,False,(111,196,169))
title_rect=title.get_rect(center=(400,50))

title_screen=pygame.image.load('graphics/dokkurunner.png')
player_surf1 = pygame.image.load('graphics/player2/dokku_runner_logo.png')
player_surf1= pygame.transform.scale(player_surf1,(70,70))
player_surf2 = pygame.image.load('graphics/player2/dokku_runner_logo1.png')
player_surf2 = pygame.transform.scale(player_surf2,(70,70))
rotate_value=0
text2='Wciśnij Spacje'
title1=test_font.render(text2,False,(111,196,169))
title_rect1=title.get_rect(center=(400,300))

score = 0
destroy=0

#####Sounds#####
pygame.mixer.init(44100,-16,2,2048)
jump_sound = pygame.mixer.Sound('audio/jump1.mp3')
jump_sound.set_volume(0.5)
bg_music = pygame.mixer.Sound('audio/dokku_runner2_0.mp3')
bg_music.set_volume(0.5)

death_sound=pygame.mixer.Sound('audio/sashimi_intro.mp3')
death_sound.set_volume(0.5)
music=1
musicon=1
honk=0
rotsash=0
ground_x=0
i=0
undead=0

light=pygame.image.load('graphics/player2/light.png').convert_alpha()
turn_light_on=0
shift_count=0

####MiniUramak####

uramak_surf=pygame.image.load('graphics/rolki/MiniUramak.png').convert_alpha()
uramak_surf1=pygame.transform.scale(uramak_surf,(30,30))
uramak_surf2=pygame.transform.scale(uramak_surf,(30,30))
uramak_y=300
uramak_rect1=uramak_surf.get_rect(midbottom=(1280,293))
uramak_rect2=uramak_surf.get_rect(midbottom=(1360,100))

uramak_spawn=0
launch2=0
launch3=0

####kontrols####

text2='Sterowanie'
control_surf=test_font.render(text2,False,(111,196,169))
control_surf=pygame.transform.scale(control_surf,(80,30))
control_rect=control_surf.get_rect(topright=(780,20))
menu=0

instrukcja_surf=pygame.image.load('graphics/instrukcja.png').convert_alpha()
instrukcja_rect=instrukcja_surf.get_rect(center=(400,200))

####Przedstawienie####

text3='Poznaj Przeciwników'
przeciwnicy_surf=test_font.render(text3,False,(111,196,169))
przeciwnicy_surf=pygame.transform.scale(przeciwnicy_surf,(160,30))
przeciwnicy_rect=przeciwnicy_surf.get_rect(topright=(780,80))
menusushi=0

grafika=pygame.image.load('graphics/przedstawienie.png')
grafika_rect=grafika.get_rect(center=(400,200))

###Restauracja###

rest_surf=pygame.image.load('graphics/restaur/Domek1.png').convert_alpha()
rest_surf=pygame.transform.scale(rest_surf,(100,80))
rest_rect=rest_surf.get_rect(bottomleft=(100,300))
nazwa_surf=pygame.image.load('graphics/restaur/logo.png').convert_alpha()
nazwa_rect=nazwa_surf.get_rect(center=(0,280))

jump_h=-23

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()


		if play_rect.collidepoint((pygame.mouse.get_pos())):
			if event.type == pygame.MOUSEBUTTONDOWN:
				if music == 1:
					music = 0
				else:
					music = 1

		if control_rect.collidepoint((pygame.mouse.get_pos())):
			if event.type == pygame.MOUSEBUTTONDOWN:
				if menu==0:
					menu = 1
				else:
					menu = 0

		if przeciwnicy_rect.collidepoint((pygame.mouse.get_pos())):
			if event.type == pygame.MOUSEBUTTONDOWN:
				if menusushi==0:
					menusushi = 1
				else:
					menusushi = 0
		if music ==1 and musicon==1:
			bg_music.play(loops = -1)
			musicon=0
		elif music ==0:
			bg_music.stop()
			musicon=1

		if game_active:

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
					player_gravity=jump_h
					jump_sound.play()
										
			if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
				jump_h=-15
			if event.type == pygame.KEYUP and event.key == pygame.K_LCTRL:
				jump_h=-23

			if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
				turn_light_on=1
				shift_count+=1
			if event.type == pygame.KEYUP and event.key == pygame.K_LSHIFT:
				turn_light_on=0
			if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
				honk=1
			if event.type == pygame.KEYUP and event.key == pygame.K_h:
				honk=0


		else:
			if event.type == pygame.KEYDOWN and pygame.K_SPACE:
					game_active=True
					snail_rect.x=1000
					start_time = int(pygame.time.get_ticks()/1000)
					if smoke ==1:
						snailsmoke_rect.left = 800
					destroy =0
					sashimi_rect.x=1200
					sashimi_rect1.x=1200
					player_rect.midbottom=(80,300)
					shift_count=0
					undead=0
					uramak_rect1.x=1280
					uramak_rect2.x=1360
					rest_rect.x=100
					nazwa_rect.x=0
		

	if game_active:

	
		#Ruch strzałkami#
		
		key_pressed = pygame.key.get_pressed()
		if key_pressed[pygame.K_RIGHT] and player_rect.right <700:
			player_rect.x+=5
			ruch=1
		elif key_pressed[pygame.K_LEFT] and player_rect.left > 20:
			player_rect.x-=5
			lruch=1
		else:
			ruch=0
			lruch=0


		#Animacja kół#
		if ruch ==1:
			if surftest ==1:
				player_surf = pygame.image.load('graphics/player2/player_walk_1.png').convert_alpha()
			if surftest ==2:
				player_surf = pygame.image.load('graphics/player2/player_walk_2.png').convert_alpha()
			if surftest ==3:
				player_surf = pygame.image.load('graphics/player2/player_walk_3.png').convert_alpha()			
			if surftest ==4:
				player_surf = pygame.image.load('graphics/player2/player_walk_4.png').convert_alpha()
			if surftest ==5:
				player_surf = pygame.image.load('graphics/player2/player_walk_5.png').convert_alpha()
			if surftest ==6:
				player_surf = pygame.image.load('graphics/player2/player_walk_6.png').convert_alpha()
			if surftest ==7:
				player_surf = pygame.image.load('graphics/player2/player_walk_7.png').convert_alpha()
			if surftest ==8:
				player_surf = pygame.image.load('graphics/player2/player_walk_8.png').convert_alpha()
			if surftest ==9:
				player_surf = pygame.image.load('graphics/player2/player_walk_9.png').convert_alpha()
			surftest += 1
			if surftest >=9:
				surftest=1

		if lruch ==1:
			if surftest ==1:
				player_surf = pygame.image.load('graphics/player2/player_walk_9.png').convert_alpha()
			if surftest ==2:
				player_surf = pygame.image.load('graphics/player2/player_walk_8.png').convert_alpha()
			if surftest ==3:
				player_surf = pygame.image.load('graphics/player2/player_walk_7.png').convert_alpha()			
			if surftest ==4:
				player_surf = pygame.image.load('graphics/player2/player_walk_6.png').convert_alpha()
			if surftest ==5:
				player_surf = pygame.image.load('graphics/player2/player_walk_5.png').convert_alpha()
			if surftest ==6:
				player_surf = pygame.image.load('graphics/player2/player_walk_4.png').convert_alpha()
			if surftest ==7:
				player_surf = pygame.image.load('graphics/player2/player_walk_3.png').convert_alpha()
			if surftest ==8:
				player_surf = pygame.image.load('graphics/player2/player_walk_2.png').convert_alpha()
			if surftest ==9:
				player_surf = pygame.image.load('graphics/player2/player_walk_1.png').convert_alpha()
			surftest += 1
			if surftest >=9:
				surftest=1
		if ruch==0 and lruch==0 and player_rect.bottom >= 300:
			if dumbtest >=1 and dumbtest <4:
				player_surf = pygame.image.load('graphics/player2/player_walk_1.png').convert_alpha()
			if dumbtest >=4 and dumbtest <7:
				player_surf = pygame.image.load('graphics/player2/player_walk_2.png').convert_alpha()
			if dumbtest >=7 and dumbtest <10:
				player_surf = pygame.image.load('graphics/player2/player_walk_3.png').convert_alpha()			
			if dumbtest >=10 and dumbtest <13:
				player_surf = pygame.image.load('graphics/player2/player_walk_4.png').convert_alpha()
			if dumbtest >=13 and dumbtest <16:
				player_surf = pygame.image.load('graphics/player2/player_walk_5.png').convert_alpha()
			if dumbtest >=16 and dumbtest <19:
				player_surf = pygame.image.load('graphics/player2/player_walk_6.png').convert_alpha()
			if dumbtest >=19 and dumbtest <22:
				player_surf = pygame.image.load('graphics/player2/player_walk_7.png').convert_alpha()
			if dumbtest >=22 and dumbtest <25:
				player_surf = pygame.image.load('graphics/player2/player_walk_8.png').convert_alpha()
			if dumbtest >=25 and dumbtest <28:
				player_surf = pygame.image.load('graphics/player2/player_walk_9.png').convert_alpha()
			dumbtest += 1
			if dumbtest >=28:
				dumbtest=1


		screen.blit(sky_surface,(0,0))
		if music==1:
			screen.blit(pause_surf, play_rect)
		else:
			screen.blit(play_surf,play_rect)
		
		screen.blit(ground_surface,(ground_x,300))
		ground_x-=4
		if ground_x <=-800:
			ground_x=0
		#pygame.draw.rect(screen,'#c0e8ec',score_rect)
		#screen.blit(score_surf,score_rect)
		score = display_score()	


		#restuaracja
		screen.blit(rest_surf,rest_rect)
		screen.blit(nazwa_surf,nazwa_rect)
		rest_rect.x-=3
		nazwa_rect.x-=3
		


		#player
		if player_rect.bottom >= 300: player_rect.bottom=300
		screen.blit(player_surf,player_rect)
		player_gravity+= 1
		if turn_light_on == 1:
			screen.blit(light,player_rect)

		if honk == 1:
			random_honk=randint(0,2)
			if random_honk == 2:
				honk_sound=pygame.mixer.Sound('audio/honk2.mp3')
			elif random_honk ==1:
				honk_sound=pygame.mixer.Sound('audio/honk1.mp3')
			elif random_honk ==0:
				honk_sound=pygame.mixer.Sound('audio/honk.mp3')
			honk_sound.set_volume(0.5)
			honk_sound.play()
			honk=0
		else:
			random_honk=randint(0,1)
			if random_honk == 1:
				honk_sound=pygame.mixer.Sound('audio/honk2.mp3')
			elif random_honk ==0:
				honk_sound=pygame.mixer.Sound('audio/honk1.mp3')
			honk_sound.stop()
		
	
		#snail
		if snail_rect.bottom >=300: snail_rect.bottom=300
		snail_gravity+=1
		
		if score > 5:
			if snail_rect.bottom >=300:
				random_value = randint(1,300)
				if score > 5 and score < 15:		
					if random_value==17: snail_gravity=-10
				elif score >15 and score <30:
					if random_value==17: snail_gravity=-15
				elif score >30 and score<45:
					if random_value==17: snail_gravity=-21
				elif score >45:
					if random_value==17: snail_gravity=-15
								
		screen.blit(snail_surf,snail_rect)
		snail_rect.x -=5
		
		if score >=30: destroy=1

		if score > 7:
			if smoke == 0:
				random_smoke=randint(1,100)
				if random_smoke ==6:
					smoke =1
			if smoke ==1 and destroy==0:
				screen.blit(snailsmoke_surf,snailsmoke_rect)
				snailsmoke_rect.x-=7
				if snailsmoke_rect.right < 0:
					snailsmoke_rect.left = 900
					smoke=0
			elif smoke==1 and destroy==1:
				screen.blit(snailsmoke_surf,snailsmoke_rect)
				speed = randint(1,3)
				if speed == 1:
					snailsmoke_rect.x-=9
				if speed == 2:
					snailsmoke_rect.x-=11
				if speed == 3:
					snailsmoke_rect.x-=13
				if snailsmoke_rect.right < 0 and score <40:
					snailsmoke_rect.left = 900
					smoke=0
				if snailsmoke_rect.right < 0 and score >46:
					snailsmoke_rect.left = 1100
					smoke=0

		

		if snail_rect.right < 0 and score <40 or snail_rect.right <0 and score > 46:
			snail_rect.left = 900
		
		#Sashimi
		if sashimi_rect1.left > 800 and sashimi_rect1.left < 900:
			shift_count=0
		if sashimi_rect1.left < 800 and shift_count >= 10:
			undead=1

		if score > 40:
			ROTATE(sashimi_surf,rotsash,sashimi_rect.x,sashimi_rect.y)
			screen.blit(rotated_image,sashimi_rect1)
			rotsash+=3
			if rotsash >= 360:
				rotsash=0
			sashimi_rect.x-=3
			if sashimi_rect.right<0:
				sashimi_rect.left = 2200
			if sashimi_rect1.right<0:
				sashimi_rect1.left = 2200
	
		if undead==1 and sashimi_rect.left < 2200:
			sashimi_rect.x+=20
		if sashimi_rect.left==2200:
			undead=0
			loop=0
	
		#Miniuramak
		if score>45:
			x1=randint(1,250)
			speed_list=[9,11,13]
			speed1=choice(speed_list)
			if x1 == 7:
				launch2=1
			if x1 == 9:
				launch3=1

		if launch2==1	:
			uramak_rect1.x-=speed1			
			screen.blit(uramak_surf1,uramak_rect1)
		if launch3==1	:
			uramak_rect2.x-=speed1			
			screen.blit(uramak_surf2,uramak_rect2)


		if uramak_rect1.right<0:
			uramak_rect1.right=1280
			launch2=0
		if uramak_rect2.right<0:
			uramak_rect2.right=1320
			launch3=0












		#game-end
		if player_rect.colliderect(snail_rect):
			game_active=False
			death_sound.play()
		if player_rect.colliderect(snailsmoke_rect):
			game_active=False
			death_sound.play()
		if player_rect.colliderect(sashimi_rect):
			game_active=False
			death_sound.play()

		if player_rect.colliderect(sashimi_rect1):
			game_active=False
			death_sound.play()

		if player_rect.colliderect(uramak_rect1):
			game_active=False
			death_sound.play()

		if player_rect.colliderect(uramak_rect2):
			game_active=False
			death_sound.play()




		player_rect.y += player_gravity
		snail_rect.y += snail_gravity

	else:
		screen.blit(title_screen,(0,0))
		if music==1:
			screen.blit(pause_surf, play_rect)
		else:
			screen.blit(play_surf,play_rect)

		screen.blit(title,title_rect)
		i+=1
		if i<100:
			player_surf1_scaled=pygame.transform.rotozoom(player_surf1,rotate_value,2)
		elif i >100 and i<120:
			random1=randint(0,1)
			if random1==0:
				player_surf1_scaled=pygame.transform.rotozoom(player_surf2,rotate_value,2)
			elif random1==1:
				player_surf1_scaled=pygame.transform.rotozoom(player_surf1,rotate_value,2)
		elif i >120 and i<220:
			player_surf1_scaled=pygame.transform.rotozoom(player_surf2,rotate_value,2)
		elif i>220 and i<240:
			random1=randint(0,1)
			if random1==0:
				player_surf1_scaled=pygame.transform.rotozoom(player_surf2,rotate_value,2)
			elif random1==1:
				player_surf1_scaled=pygame.transform.rotozoom(player_surf1,rotate_value,2)		
		elif i >240:
			i=0

		player_rect1 = player_surf1_scaled.get_rect(center=(400,175))
		if rotate_value >=360:
			rotate_value=0
		else:
			rotate_value+=1

		screen.blit(player_surf1_scaled,player_rect1)

		score_message = test_font.render(f'Twój Wynik: {score}',False,(111,196,169))
		score_message_rect=score_message.get_rect(center = (400,300))
		if score >0: screen.blit(score_message,score_message_rect)
		else: screen.blit(title1,title_rect1)
		screen.blit(control_surf,control_rect)
		screen.blit(przeciwnicy_surf,przeciwnicy_rect)
		if menu==1:
			screen.blit(instrukcja_surf,instrukcja_rect)
		if menusushi==1:
			screen.blit(grafika,grafika_rect)



	pygame.display.update()
	clock.tick(60) 


















