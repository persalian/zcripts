#!/usr/bin/python

import json
import get_request

D = 0


def log(d, msg):
    if d == True:
        print("LOG: {}".format(msg))


def kvm_list(data):
    tp = 0
    res = []

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
    vms = json.dumps(kvm_list(get_request.execute_cmd("virsh list --all")))
    print(vms)
