import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()

whites_turn = True

def switchTabs():
	global whites_turn
	x = None
	y = None
	if whites_turn:
		x = 1180
		y = 870
	else:
		x = 1150
		y = 870

	pyautogui.moveTo(x, y)
	time.sleep(1)
	pyautogui.click()
	whites_turn = not whites_turn
	time.sleep(1)

def moveToFace():
	pyautogui.moveTo(290, 270)
	time.sleep(1)
	pyautogui.click()

def moveToPlayButton():
	pyautogui.moveTo(950, 600)
	time.sleep(1)
	pyautogui.click()

def movePiece(from_x, from_y, to_x, to_y):
	switchTabs()
	pyautogui.moveTo(from_x, from_y)
	#print(pyautogui.position())
	time.sleep(1)
	pyautogui.click()
	time.sleep(1)
	pyautogui.moveTo(to_x, to_y)
	pyautogui.click()

def play():
	global whites_turn
	time.sleep(3)
	moveToFace()
	moveToPlayButton()
	time.sleep(4)
	movePiece(750, 630, 750, 500) #white pawn
	movePiece(680, 620, 680, 480) #black pawn
	movePiece(686, 704, 967, 415) #white queen
	movePiece(964, 624, 964, 555) #black pawn
	movePiece(470, 620, 470, 555) #white pawn
	movePiece(964, 555, 964, 485) #black pawn
	movePiece(470, 555, 470, 485) #white pawn
	movePiece(900, 620, 900, 550) #black pawn
	movePiece(550, 625, 550, 550) #white pawn
	movePiece(680, 700, 680, 625) #black king
	movePiece(970, 415, 750, 415) #white queen
	whites_turn = True
	time.sleep(10)

try:
	while True:
		for x in range(1000):
			play()
except KeyboardInterrupt:
	pass

print(pyautogui.position())

print(screenWidth)
print(screenHeight)



