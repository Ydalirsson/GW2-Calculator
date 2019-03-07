#!/usr/bin/python

import sys

from mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

import random

# define gobals

STEPS = 100

profs = ["Warrior", "Guardian", "Revenant",
		 "Ranger", "Thief", "Engineer",
		 "Necromancer", "Elementalist", "Mesmer"]

weapon = {0: [900, 1100, "Axe"],
			1: [970, 1030, "Dagger"],
			2: [940, 1060, "Mace"],
			3: [920, 1080, "Pistol"],
			4: [940, 1060, "Scepter"],
			5: [950, 1050, "Sword"],
			6: [1045, 1155, "Greatsword"],
			7: [1034, 1166, "Hammer"],
			8: [966, 1134, "Longbow"],
			9: [1035, 1265, "Rifle"],
			10: [950, 1050, "Shortbow"],
			11: [1034, 1166, "Staff"]
}

health = {
	0: [9212, [profs[0], profs[6]] ],
	1: [5922, [profs[2], profs[3], profs[5], profs[8]] ],
	2: [1645, [profs[1], profs[4], profs[7]] ]
}
armor = {
	0: [1920, [profs[6], profs[7], profs[8]] ],
	1: [2064, [profs[3], profs[4], profs[5]] ],
	2: [2211, [profs[0], profs[1], profs[2]] ]
}

def getValueByProf(dict, value):
	for i in range(3):
		if value in dict[i][1]:
			return dict[i][0]

def avgDmg(strength, precision, ferocity, sel):
	STRENGTH = strength
	PRECISION = precision
	FEROCITY = ferocity
	dmgLst = []


	for i in range(STEPS):
		WEAPON = random.randrange(weapon[sel][0], weapon[sel][1], 1)
		number = random.uniform(0, 100)

		if number <= PRECISION * 100:
			damage = WEAPON * STRENGTH * FEROCITY
		else:
			damage = WEAPON * STRENGTH

		damage = damage / 2600.0
		dmgLst.append(damage)
	# print(dmgLst)
	print(sum(dmgLst) / len(dmgLst))

def effecLife(vit, tough):
	STD_DMG = 1000000
	i = 0
	while vit > 0:
		vit -= STD_DMG / tough
		i += 1
	print("Hits to death", i)


# define signale, slots, event actions
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, parent = None):
		super(MyApp, self).__init__()
		self.setupUi(self)

		'''
		icBtns = [QPushButton("ic_ele"), QPushButton("ic_eng"), QPushButton("ic_gua")]
		self.ic_btn_group = QButtonGroup()
		for i in range(len(icBtns)):
			self.ic_btn_group.addButton(icBtns[i], i)

		self.ic_eng.clicked.connect(self.getSelected)
		self.ic_ele.clicked.connect(self.getSelected)
		'''

		self.lstWeapons.itemClicked.connect(self.item_click)

	def item_click(self, item):
		print (item.text())

	def getSelected(self, item):
		print(item.text() )

#
def main():
	print("Choose your prof")
	for i in profs:
		print(str(i) + " (" + str(profs.index(i)) + ")" )
	sel = int(input("Enter a number: "))
	effecLife( getValueByProf(health, profs[sel]) , getValueByProf(armor, profs[sel]))
	input()

	print("Choose your weapon")
	for i in weapon:
		print(weapon[i][2] + " (" + str(i) +")")
	sel = int(input("Enter a number: "))

	avgDmg(2381, 0.5076, 2.1407, sel)	# bes

	avgDmg(1961, 0.7076, 2.1407, sel)	# ass

# boilerplate, create window
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon("./assets/icon.png"))
	ui = MyApp()
	ui.show()
	sys.exit(app.exec_())