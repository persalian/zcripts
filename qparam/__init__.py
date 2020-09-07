import sys


class LParam(object):
    def __init__(self, configfile=None):
        self.parameters = {}
        self.config_file = configfile

    pass

    def apply_command_line(self):
        """apply parameters from command line"""

        for a in sys.argv:
            c = a.split("=")
            if c[0][0] == '-' and c[0][1] == '-':
                p = c[0].lstrip().rstrip().strip(' -\n\r\t\'')
                if len(c) == 2:
                    v = c[1].lstrip().rstrip().strip(' \n\r\t\'')
                    if v == "True" or v == "true":
                        if self.parameters.get(p) is not None:
                            self.parameters[p]['value'] = True
                    elif v == "False" or v == "false":
                        if self.parameters.get(p) is not None:
                            self.parameters[p]['value'] = False
                    else:
                        if self.parameters.get(p) is not None:
                            self.parameters[p]['value'] = v

                elif len(c) == 1:
                    if self.parameters.get(p) is not None:
                        self.parameters[p]['value'] = True

        return True

    def apply_config_file(self, configfile):
        """reading config file if it is specified"""

        if configfile is not None:
            with open(configfile, 'r') as conf:
                for cfline in conf:
                    c = cfline.split("=")
                    if len(c) == 2:
                        p = c[0].lstrip().rstrip().strip(' \n\r\t\'')
                        v = c[1].lstrip().rstrip().strip(' \n\r\t\'')
                        if v == "True" or v == "true":
                            if self.parameters.get(p) is not None:
                                self.parameters[p]['value'] = True

                        elif v == "False" or v == "false":
                            if self.parameters.get(p) is not None:
                                self.parameters[p]['value'] = False

                        else:
                            if self.parameters.get(p) is not None:
                                self.parameters[p]['value'] = v
            return True
        return False

    def param(self, name):
        if self.parameters.get(name) is None:
            return None
        else:
            return self.parameters[name]['value']

    def register(self, name, def_value=None, help_msg=''):
        self.parameters[name] = {'value': def_value, 'help_msg': help_msg}
        return True

    def load_param(self):
        self.apply_config_file(self.config_file)
        self.apply_command_line()
        return True

    def help_msg(self):
        msg = "HELP MESSAGE:\n"
        for k,v in self.parameters.items():
            msg = msg + "\t--{} : {}, default value '{}'\n".format(k, v["help_msg"], v["value"])

        return msg

    def change(self, name, value):
        self.parameters[name]["value"] = value

