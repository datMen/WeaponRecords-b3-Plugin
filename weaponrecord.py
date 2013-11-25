__author__  = 'LouK'
__version__ = '1.0'


import b3
import b3.events
import b3.plugin

class WeaponrecordPlugin(b3.plugin.Plugin):
 
    def onLoadConfig(self):
        self.registerEvent(b3.events.EVT_CLIENT_KILL)
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
                    
    def onEvent(self, event):
        if event.type == b3.events.EVT_CLIENT_KILL:
            # Call the function that process kill event
            self.someoneKilled(event.client, event.target, event.data)
            
    def someoneKilled(self, client, target, data=None):
        """\
        Update database weapons for the attacker(killer)
        """
        if data[1] == self.console.UT_MOD_KNIFE or self.console.UT_MOD_KNIFE_THROWN:
            self.console.storage.query('UPDATE `weaponrecord` SET `knife` = knife+1 WHERE client_id = "%s"' % (client.id))
            
        elif data[1] == self.console.UT_MOD_DEAGLE:
            self.console.storage.query('UPDATE `weaponrecord` SET `desert` = desert+1 WHERE client_id = "%s"' % (client.id))

        elif data[1] == self.console.UT_MOD_BERETTA:
            self.console.storage.query('UPDATE `weaponrecord` SET `beretta` = beretta+1 WHERE client_id = "%s"' % (client.id))

        elif data[1] == self.console.UT_MOD_NEGEV:
            self.console.storage.query('UPDATE `weaponrecord` SET `negev` = negev+1 WHERE client_id = "%s"' % (client.id))

        elif data[1] == self.console.UT_MOD_SPAS:
            self.console.storage.query('UPDATE `weaponrecord` SET `spas` = spas+1 WHERE client_id = "%s"' % (client.id))

        elif data[1] == self.console.UT_MOD_HK69 or self.console.UT_MOD_HK69_HIT:
            self.console.storage.query('UPDATE `weaponrecord` SET `hk` = hk+1 WHERE client_id = "%s"' % (client.id))

        elif data[1] == self.console.UT_MOD_SR8:
            self.console.storage.query('UPDATE `weaponrecord` SET `psg` = psg+1 WHERE client_id = "%s"' % (client.id))
            
        elif data[1] == self.console.UT_MOD_PSG1:
            self.console.storage.query('UPDATE `weaponrecord` SET `psg` = psg+1 WHERE client_id = "%s"' % (client.id))
            
        elif data[1] == self.console.UT_MOD_MP5K:
            self.console.storage.query('UPDATE `weaponrecord` SET `ump` = ump+1 WHERE client_id = "%s"' % (client.id))
            
        elif data[1] == self.console.UT_MOD_HEGRENADE:
            self.console.storage.query('UPDATE `weaponrecord` SET `he` = he+1 WHERE client_id = "%s"' % (client.id))
        
        elif data[1] == self.console.UT_MOD_LR300:
            self.console.storage.query('UPDATE `weaponrecord` SET `lr300` = lr300+1 WHERE client_id = "%s"' % (client.id))
        
        elif data[1] == self.console.UT_MOD_M4:
            self.console.storage.query('UPDATE `weaponrecord` SET `m4` = m4a1+1 WHERE client_id = "%s"' % (client.id))
            
        elif data[1] == self.console.UT_MOD_G36:
            self.console.storage.query('UPDATE `weaponrecord` SET `g36` = g36+1 WHERE client_id = "%s"' % (client.id))
            
        elif data[1] == self.console.UT_MOD_AK103:
            self.console.storage.query('UPDATE `weaponrecord` SET `ak` = ak+1 WHERE client_id = "%s"' % (client.id))