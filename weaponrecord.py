__author__  = 'LouK'
__version__ = '1.0'


import b3
import b3.plugin

class WeaponrecordPlugin(b3.plugin.Plugin):
    requiresConfigFile = False
 
    def onLoadConfig(self):
        self._adminPlugin = self.console.getPlugin('admin')
        if not self._adminPlugin:
            self.error('Could not find admin plugin')
            return False