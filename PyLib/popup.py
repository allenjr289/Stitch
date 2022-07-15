# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

import ctypes

if win_client():
    message=receive(client_socket)
    cmd = f'powershell "(new-object -ComObject wscript.shell).Popup(\\"{message}\\",0,\\"Windows\\")"'

    start_command(cmd)
    resp = "[+] Popup window successfully executed\n"
    send(client_socket,resp)
if osx_client():
    message=receive(client_socket)
    cmd = "osascript -e 'tell app \"System Events\" to display dialog \"{}\" buttons {{\"OK\"}} default button \"OK\" '".format(message)
    start_command(cmd)
    resp = "[+] Popup window successfully executed\n"
    send(client_socket,resp)
