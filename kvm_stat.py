#!/usr/bin/python

import json
import subprocess

D = 0

def log(d, msg):
    if d == True:
            print("LOG: {}".format(msg))

def execute_cmd(cmd):
    cmds = {
        "list":"virsh list --all",
        "dominfo":"virsh dominfo {}"
    }

    log(D, cmd)
    res = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0].split('\n')
    return res


def kvm_stat(name):
    tp = 0
    res = []

    return res

if __name__ == '__main__':

    vms = json.dumps(kvm_list(execute_cmd("virsh list --all")))
    print(vms)
