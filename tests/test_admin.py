import ctypes

if ctypes.windll.shell32.IsUserAnAdmin():
    print("Administrator")
else:
    print("Normal User")
