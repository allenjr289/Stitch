# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

f_name = receive(client_socket)
system = sys.platform
if os.path.exists(f_name):
    if win_client():
        resp = run_command(f"attrib +H {f_name}")
    if osx_client():
        resp = run_command(f"chflags hidden {f_name}")
    if lnx_client():
        resp = (
            '[*] File is already hidden.\n'
            if f_name.startswith('.')
            else run_command(f"mv {f_name} .{f_name}")
        )

elif lnx_client():
    if os.path.exists(f".{f_name}"):
        resp = '[*] File is already hidden.\n'
else:
    resp = f"[!] {f_name}: No such file or directory\n"
send(client_socket,resp)
