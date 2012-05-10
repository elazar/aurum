import pkgutil
from os.path import join, abspath, dirname
import inspect
from cmd import Cmd
import readline

from aurum import command, context, config

class CommandModuleMissingClassError(Exception):
    def __init__(self, command):
        self.command = command
    def __str__(self):
        c = self.command
        C = self.command.capitalize()
        return "module aurum.commands.%s missing class %s..." % (c, C)

class CommandClassMissingBaseClass(Exception):
    def __init__(self, command):
        self.command = command
    def __str__(self):
        c = self.command
        C = self.command.capitalize()
        return "class %s in module aurum.commands.%s must inherit from aurum.commands.Command" % (C, c)

class Shell(Cmd):

    def __init__(self):
        Cmd.__init__(self)

        self.context = context.Context()

        self.config = config.Config()
        self.prompt = self.config.prompt

    def default(self, line):
        print 'aurum: Unknown syntax: %s' % (line)

    def __getattr__(self, name):
        if not name.startswith("do_"):
            raise AttributeError

        try:
            command_name = name.replace("do_", "", 1)
            commands_path = join(dirname(abspath(__file__)), "commands")
            module_found = False
            for importer, module, _ in pkgutil.iter_modules([commands_path]):
                if module == command_name:
                    module_found = True
                    break
            if not module_found:
                raise AttributeError

            fullname = "aurum.commands." + command_name
            loader = importer.find_module(fullname)
            command_module = loader.load_module(fullname)
            command_class_name = command_name.capitalize()
            command_class = getattr(command_module, command_class_name)
            if command_class == None:
                raise CommandModuleMissingClassError(command_name)
            if not command.Command in inspect.getmro(command_class):
                raise CommandClassMissingBaseClass(command_name)

            command_instance = command_class(self.config, self.context)
            context_method = "do_" + self.context.get_type()
            return getattr(command_instance, context_method)
        except Exception as msg:
            print msg
