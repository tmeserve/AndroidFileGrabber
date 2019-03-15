import os.path as op
import os, subprocess
from subprocess import PIPE, Popen, STDOUT
from ast import literal_eval

test = subprocess.check_output(['adb', 'devices'])
testl = test.decode('ascii', 'ignore')
testll = testl.split(' ')
count = len(testll)
replaced = testll[count - 1].replace('\\', ',')

print(replaced)

# from adb import adb_commands
# from adb import sign_m2crypto

# signer = sign_m2crypto.M2CryptoSigner(
#     op.expanduser('~/.android/adbkey'))


# adbc = adb_commands.AdbCommands()
# # device.ConnectDevice(
# #     rsa_keys=[signer])
# devices = []
# for d in adbc.Devices():
#     devices.append(adbc.ConnectDevice(port_path=d.port_path, rsa_keys=[signer]))

# for device in devices:
#     # print(device.InteractiveShell("cd /storage/emulated/0/'My Documents'"))
#     cmd = device.Shell("cd /storage/emulated/0/'My Documents'")
#     print(cmd, "   cmd")
#     cmd = device.Shell("pwd")
#     print(cmd)
#     cmd = device.List("/storage/emulated/0/My Documents")
#     print(cmd, "       cmd 3")
#     file = device.Pull("SM-G955U", dest_file="./text.txt")
#     print(file)



# devices = subprocess.check_output('adb devices', shell=True)
# devstr = devices.decode("utf-8")
# decoded = []
# for l in devstr:
#     data = l.decode('ascii', 'ignore')
#     if data != "":
#         decoded.append(data)
# new = decoded
# print(new)

# filedir = str(input("Please enter the directory path of the file you want to retrieve")
# cmd = Popen('adb pull ' + filedir + ' ~/documents/pythonadbtool/filegrabber', shell=True, stdout=PIPE, stderr=STDOUT)
# print(cmd.)
