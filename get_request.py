import subprocess


def execute_cmd(cmd):
    res = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0].split('\n')
    return res
