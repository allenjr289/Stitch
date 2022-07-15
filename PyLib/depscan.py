# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

import _winreg
import subprocess

def check_dep():
    dep = subprocess.Popen('wmic OS get DataExecutionPrevention_SupportPolicy',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    dep_mode, errors = dep.communicate()
    if errors:
        return errors

    elif not dep_mode:
        return errors

    else:
        if "0" in dep_mode:
            return "DEP is off for the whole system."
        elif "1" in dep_mode:
            return "Full DEP coverage for the whole system with no exceptions."
        elif "2" in dep_mode:
            return "DEP is limited to Windows system binaries."
        elif "3" in dep_mode:
            return "DEP is on for all programs and services."

print check_dep()
