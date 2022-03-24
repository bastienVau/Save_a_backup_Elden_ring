import shutil
import os
import time
import ctypes, sys
#save a backup of Elden ring on your disk C:

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    save_path = r"C:\Users\{}\AppData\Roaming\EldenRing".format(os.getlogin())
    save_time = int(time.time())
    os.mkdir(r"C:\elden_ring_backup/")
    shutil.copytree(save_path, r"C:\elden_ring_backup/{}/".format(int(time.time())))
    print("done")
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
