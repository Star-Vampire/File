import os,time,platform
os.system('clear')
os.system("xdg-open https://chat.whatsapp.com/HioQX79LjEECatjG15h0RO")
print('[>] Checking Updates')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
 import Extractor
else:
 print('\033[1;31m[×] Sorry your Device 32 bit Not Support')
