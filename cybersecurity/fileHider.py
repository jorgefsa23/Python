#To hide a file or a folder
import ctypes

attribute_hide = 0x02 #hexadecimal

#File (or Folder) name... 
reply = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', attribute_hide)

if reply:
    print("File was hidden")
else:
    print("File was NOT hidden")