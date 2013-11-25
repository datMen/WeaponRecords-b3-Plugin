__author__  = 'LouK'
__version__ = '1.0'


import b3
import b3.plugin

class WeaponrecordPlugin(b3.plugin.Plugin):
 
    def onLoadConfig(self):
        self._adminPlugin = self.console.getPlugin('admin')
        if not self._adminPlugin:
            self.error('Could not find admin plugin')
            return False

        # Register commands
        if 'commands' in self.config.sections():
            for cmd in self.config.options('commands'):
                level = self.config.get('commands', cmd)
                sp = cmd.split('-')
                alias = None
                # Alias for the command
                if len(sp) == 2:
                    cmd, alias = sp

                # Find function for this command
                func = self.getCmd(cmd)
                if func:
                    self._adminPlugin.registerCommand(self, cmd, level, func, alias)