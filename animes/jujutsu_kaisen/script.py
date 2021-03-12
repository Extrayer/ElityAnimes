import os


for i in range(18,22):

    myFile = open(str(i)+".md", "w+")
    myFile.write(f"""---
layout: lecteur.njk
tags: jjk


title: Jujutsu Kaisen
episode: {i}
saison: 1
iframe: 
cc: VostFr

---
    """)


