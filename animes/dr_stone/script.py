import os

depart = int(input("Episode de départ ? : "))
number = int(input("Episode de fin ? : "))
tags = str(input("Tags ? : "))
title = str(input("Title ? : "))
saison = str(input("Saison ? : "))
cc = str(input("cc ? : "))

link = open("link.txt", "r")
link = link.readlines()

compteur = 0

for i in range(depart, number+1):
	ep = i

	if len(str(i)) == 1:
		ep = '0' + str(i)

	filename = title.replace(" ","").replace('.','-')+'-'+ 'saison' + '-' + saison + '-' + str(ep) + '-' + cc

	File = open(str(filename)+".md", "w+")
	File.write(
f'''---
layout: lecteur.njk
tags : {tags}

title : {title}
episode : {i}
saison : {saison}
iframe : {link[compteur]}
cc :  {cc}
---'''
)
	compteur += 1
