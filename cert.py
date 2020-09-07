#!/usr/bin/python

import get_request
import datetime
import qparam


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

    cmds = {
        'info': 'echo  | openssl s_client -showcerts -connect {} -servername cloud3.osnova-sib.ru 2>/dev/null  | openssl x509  -text -noout  | grep Not'
    }

    param = qparam.LParam()
    param.register('--host', def_value='localhost:443', help_msg='hostname of hesting host, with define port')
    param.register('--valid-period', def_value=False, help_msg='Show a period when certificate is valid')
    param.register('--rest-of-days', def_value=False, help_msg='Show days before certificate\'ll became invalid')
    param.load_param()

    host = param.param('host') + ":443"

    cmd = cmds['info'].format(host)
    res = get_request.execute_cmd(cmd)
    del res[-1]
    vperiod = valid_period(res)
    if param.param('valid-period'):
        print("from: {} and to: {}".format(vperiod['start'], vperiod['end']))

    days = rest_of_days(datetime.datetime.now().date(), res)
    if param.param('rest-of-days'):
        print("days to end: {}".format(days))
