from ConfigParser import ConfigParser
import os.path

class NoConfigFileError(Exception):
    def __init__(self, path):
        self.path = path
    def __str__(self):
        return "No configuration file found at " + self.path

class Config(ConfigParser):
    config_file = os.path.expanduser("~/.aurum")
    prompt = "aurum> "
    dsn = {}

    def __init__(self):
        ConfigParser.__init__(self)

        read_files = self.read([self.config_file])
        if len(read_files) == 0:
            raise NoConfigFileError(self.config_file)

        self.dsn = self._tuples_to_dict(self.items("dsn"))

        try:
            general = self._tuples_to_dict(self.items("general"))
            if "prompt" in general:
                self.prompt = general["prompt"]
        except:
            pass

    def _tuples_to_dict(self, tuples):
        """ Converts a list of tuples to a dict """
        d = {}
        for key, value in tuples:
            d[key] = value
        return d
