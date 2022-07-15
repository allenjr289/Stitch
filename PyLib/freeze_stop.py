# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

if status := nt_kl.get_frz_status():
    nt_kl.stop_freeze()
    status = nt_kl.get_frz_status()
    resp = (
        '[!] System failed to unfreeze\n'
        if status
        else '[+] System has been successfully unfrozen\n'
    )

else:
    resp = '[+] System is already unfrozen\n'
send(client_socket,resp)
