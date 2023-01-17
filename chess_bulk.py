import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()

num_toon_pairs = 2;
launcher_coordinate_y_axis = 870
launcher_coordinate_x_axis = [1230, 1190, 1160, 1130]
whites_turn = True

def switchTabs(toons_left_for_turn):
	global whites_turn
	x = None
	y = None
	if whites_turn:
		x = launcher_coordinate_x_axis[toons_left_for_turn * 2]
		y = launcher_coordinate_y_axis
	else:
		x = launcher_coordinate_x_axis[toons_left_for_turn * 2 + 1]
		y = launcher_coordinate_y_axis

	pyautogui.moveTo(x, y)
	time.sleep(0.2)
	pyautogui.click()
	#whites_turn = not whites_turn
	#time.sleep(1)

def moveToFace(toons_left_for_turn):
	switchTabs(toons_left_for_turn)
	pyautogui.moveTo(290, 270)
	time.sleep(0.2)
	pyautogui.click()

def moveToPlayButton(toons_left_for_turn):
	switchTabs(toons_left_for_turn)
	pyautogui.moveTo(950, 600)
	time.sleep(0.2)
	pyautogui.click()

def movePiece(from_x, from_y, to_x, to_y, toons_left_for_turn):
	switchTabs(toons_left_for_turn)
	pyautogui.moveTo(from_x, from_y)
	#print(pyautogui.position())
	time.sleep(0.5)
	pyautogui.click()
	time.sleep(0.5)
	pyautogui.moveTo(to_x, to_y)
	pyautogui.click()

def giveBeansToClub():
	for i in range(num_toon_pairs * 2):
		time.sleep(2)
		x = launcher_coordinate_x_axis[i];
		y = launcher_coordinate_y_axis;
		pyautogui.moveTo(x, y)
		time.sleep(0.2)
		pyautogui.click()
		time.sleep(0.2)
		pyautogui.click(1300, 140)
		time.sleep(0.2)
		pyautogui.click(1285, 435)
		time.sleep(0.2)
		pyautogui.click(1285, 255)
		time.sleep(1)
		pyautogui.moveTo(941, 172)
		pyautogui.mouseDown(button='left')
		pyautogui.moveTo(1108, 172, 1)
		pyautogui.mouseUp()
		time.sleep(1)
		pyautogui.moveTo(1060, 216)
		pyautogui.click()
		time.sleep(0.2)
		pyautogui.moveTo(1017, 183)
		pyautogui.click()
		time.sleep(0.2)
		pyautogui.moveTo(1325, 433)
		pyautogui.click()
		time.sleep(0.2)

def play():
	global whites_turn

	time.sleep(3)
	for i in range(num_toon_pairs):
		moveToFace(i)
	for i in range(num_toon_pairs):
		moveToPlayButton(i)
	time.sleep(4)

	for i in range(num_toon_pairs):
		movePiece(750, 630, 750, 500, i) #white pawn

	for i in range(num_toon_pairs):
		whites_turn = False
		movePiece(680, 620, 680, 480, i) #black pawn

	for i in range(num_toon_pairs):
		whites_turn = True
		movePiece(686, 704, 967, 415, i) #white queen

	for i in range(num_toon_pairs):
		whites_turn = False
		movePiece(964, 624, 964, 555, i) #black pawn

	for i in range(num_toon_pairs):
		whites_turn = True
		movePiece(470, 620, 470, 555, i) #white pawn

	for i in range(num_toon_pairs):
		whites_turn = False
		movePiece(964, 555, 964, 485, i) #black pawn

	for i in range(num_toon_pairs):
		whites_turn = True
		movePiece(470, 555, 470, 485, i) #white pawn

	for i in range(num_toon_pairs):
		whites_turn = False
		movePiece(900, 620, 900, 550, i) #black pawn

	for i in range(num_toon_pairs):
		whites_turn = True
		movePiece(550, 625, 550, 550, i) #white pawn

	for i in range(num_toon_pairs):
		whites_turn = False
		movePiece(680, 700, 680, 625, i) #black king

	for i in range(num_toon_pairs):
		whites_turn = True
		movePiece(970, 415, 750, 415, i) #white queen

	whites_turn = True
	time.sleep(10)


try:
	while True:
		for x in range(1000):
			if x % 100 == 0:
				giveBeansToClub()
			play()
except KeyboardInterrupt:
	pass




