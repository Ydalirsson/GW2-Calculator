#!/usr/bin/python
import random

STEPS = 1000000
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
			11: [1034, 1166, "Staff"],
			}

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


def main():
	print("Choose your weapon")
	for i in weapon:
		print(weapon[i][2] + " (" + str(i) +")")
	sel = int(input("Enter a number: "))

	avgDmg(2381, 0.5076, 2.1407, sel)	# bes
	avgDmg(1961, 0.7076, 2.1407, sel)	# ass

if __name__ == '__main__':
	main()