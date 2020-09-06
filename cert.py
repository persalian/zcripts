#!/usr/bin/python

import get_request
import datetime

cmds = {
    'info': 'echo  | openssl s_client -showcerts -connect {1}:443 -servername cloud3.osnova-sib.ru 2>/dev/null  | openssl x509  -text -noout  | grep Not'
}


def valid_period(cert_info):
    r = {}

    if len(cert_info) == 2:
        r['start'] = datetime.datetime.strptime(str(cert_info[0]).strip(), "Not Before: %b %d %X %Y GMT").date()
        r['end'] = datetime.datetime.strptime(cert_info[1].strip(), "Not After : %b %d %X %Y GMT").date()

    return r

def rest_of_days(now, cert_info):
    r = valid_period(cert_info)

    if r != {}:
        days = r['end'] - now
        days = days.days
        return days
    return None

if __name__ == '__main__':

    host = 'cloud3'
    res = get_request.execute_cmd(cmds['info'].format(host))
    valid_period = valid_period(res)
    print("from: {} and to: {}".format(valid_period['start'], valid_period['end']))

    days = rest_of_days(datetime.datetime.now(), res)
    print("days to end: {}".format(days))
