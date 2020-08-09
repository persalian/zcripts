#!/usr/bin/python

import subprocess


D = 1

def log(d, msg):
    if d == True:
            print("LOG: {}".format(msg))

def execute_cmd(cmd):
    log(D, cmd)
    res = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0].split('\n')
    return res


def kvm_list(data):
    tp = 0
    res = []
    vm = {}

    for l in data:
        if tp >= 2:
            f = l.split()
            if len(f) == 3:
                res.append({
                    'name': f[1],
                    'status': f[2]
                })
        else:
            tp = tp + 1
    return res


if __name__ == '__main__':
    cmd = [
        "virsh list --all"
    ]
    d = execute_cmd(cmd[0])
    vms = kvm_list(d)
    print(vms)
