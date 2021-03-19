import os

depart = int(input("Episode de départ ? : "))
number = int(input("Episode de fin ? : "))
tags = str(input("Tags ? : "))
title = str(input("Title ? : "))
saison = str(input("Saison ? : "))
cc = str(input("cc ? : "))


for i in range(depart,number+1):
    if len(str(i)) == 1:
        i = '0' + str(i)
    

    File = open(str(i)+".md", "w+")
    File.write(f'''---
layout: lecteur.njk
tags : {tags}

title : {title}
episode : {i}
saison : {saison}
iframe :
cc :  {cc}
    
---''')





