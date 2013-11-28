__author__  = 'LouK'
__version__ = '1.0'


import b3, threading, thread, time, re
import b3.events
import b3.plugin

class WeaponrecordPlugin(b3.plugin.Plugin):
    _map = ""
    _clientvar_map = ""
 
    def onLoadConfig(self):
        self.registerEvent(b3.events.EVT_CLIENT_KILL)
        self.registerEvent(b3.events.EVT_CLIENT_AUTH)
        self.registerEvent(b3.events.EVT_GAME_ROUND_START)
        self.registerEvent(b3.events.EVT_GAME_EXIT)
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
                    
        self.checkmap()
                    
    def onEvent(self, event):
        if event.type == b3.events.EVT_CLIENT_KILL:
            # Call the function that process kill event
            self.someoneKilled(event.client, event.target, event.data)
            
        elif event.type == b3.events.EVT_CLIENT_AUTH: 
            sclient = event.client
            cursor = self.console.storage.query('SELECT * FROM `weaponrecord` WHERE `client_id` = "%s"' % (sclient.id))
            if cursor.rowcount == 0:
                self.console.storage.query('INSERT INTO `weaponrecord`(`client_id`) VALUES (%s)' % (sclient.id))
            
            r = cursor.getRow()
            mapstats = self.getMapStats(sclient)
            map = r[self._map]
            regex = re.compile(r"""^(?P<stats0>\d+) (?P<stats1>\d+) (?P<stats2>\d+) (?P<stats3>\d+) (?P<stats4>\d+) (?P<stats5>\d+) (?P<stats6>\d+) (?P<stats7>\d+) (?P<stats8>\d+) (?P<stats9>\d+) (?P<stats10>\d+) (?P<stats11>\d+) (?P<stats12>\d+) (?P<stats13>\d+) (?P<stats14>\d+)$""");
            match = regex.match(map)
            stats = []
            i = 0
            while i <= 14:
                stats.insert(1, (int(match.group('stats%s' % i))))
                i += 1
            mapstats.stats = stats
            
                
        elif event.type == b3.events.EVT_GAME_ROUND_START:
            self.checkmap()
            
        elif event.type == b3.events.EVT_GAME_EXIT:
            for c in self.console.clients.getClientsByLevel():
                mapstats = self.getMapStats(c)
                fstats = "%s" % (((("".join("%s" % mapstats.stats)).replace(",", "")).replace("[", "")).replace("]", ""))
                self.console.storage.query('UPDATE weaponrecord SET %s = "%s" WHERE client.id = "%s"' % (self._map, fstats, c.id))
                sql = self.console.storage.query('SELECT %s FROM weaponrecord WHERE client.id = "%s"' % (self._map, c.id))
                regex = re.compile(r"""^(?P<stats0>\d+) (?P<stats1>\d+) (?P<stats2>\d+) (?P<stats3>\d+) (?P<stats4>\d+) (?P<stats5>\d+) (?P<stats6>\d+) (?P<stats7>\d+) (?P<stats8>\d+) (?P<stats9>\d+) (?P<stats10>\d+) (?P<stats11>\d+) (?P<stats12>\d+) (?P<stats13>\d+) (?P<stats14>\d+)$""");
                match = regex.match(sql)
                stats = []
                i = 0
                while i <= 14:
                    stats.insert(1, (int(match.group('stats%s' % i))))
                    i += 1
                mapstats.stats = stats
                
    def checkmap(self):
        self._map = self.console.getCvar('mapname').getString()
        cursor = self.console.storage.query('SELECT * FROM `weaponrecord`')
        r = cursor.getRow()
        try:
            mapname = r[self._map]
        except KeyError:
            self.console.storage.query('ALTER TABLE weaponrecord ADD COLUMN  %s varchar(100) DEFAULT "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"' % (self._map))
        
    def getMapStats(self, client):
        
        if not client.isvar(self, self._clientvar_map):
            client.setvar(self, self._clientvar_map, MapStats())
            
        return client.var(self, self._clientvar_map).value
    
    def getCmd(self, cmd):
        cmd = 'cmd_%s' % cmd
        if hasattr(self, cmd):
            func = getattr(self, cmd)
            return func

        return None
            
    def findWeapon(self, weapon, client):
        if (weapon == "sr8") or (weapon == "SR8"):
            name = "Remington Sr8"
            key = "sr8"
            pos = 10
        elif (weapon == "knife") or (weapon == "KNIFE") or (weapon == "KN") or (weapon == "kn"):
            name = "Knife"
            key = "knife"
            pos = 0
        elif (weapon == "beretta") or (weapon == "BERETTA") or (weapon == "BE") or (weapon == "be"):
            name = "Beretta"
            key = "beretta"
            pos = 1
        elif (weapon == "desert eagle") or (weapon == "DESERT EAGLE") or (weapon == "desert") or (weapon == "DESERT") or (weapon == "DE") or (weapon == "de"):
            name = "Desert Eagle"
            key = "desert"
            pos = 2
        elif (weapon == "spas") or (weapon == "SPAS") or (weapon == "FRANCHI") or (weapon == "franchi"):
            name = "Franchi SPAS12"
            key = "spas"
            pos = 3
        elif (weapon == "mp5") or (weapon == "MP5") or (weapon == "MP5K") or (weapon == "mp5k"):
            name = "HK MP5K"
            key = "mp5k"
            pos = 5
        elif (weapon == "ump") or (weapon == "UMP") or (weapon == "UMP45") or (weapon == "ump45"):
            name = "HK UMP45"
            key = "ump"
            pos = 4
        elif (weapon == "HK69") or (weapon == "hk69") or (weapon == "hk") or (weapon == "HK"):
            name = "HK69 40mm"
            key = "hk"
            pos = 13
        elif (weapon == "lr300") or (weapon == "LR300") or (weapon == "LR") or (weapon == "lr"):
            name = "ZM LR300"
            key = "lr"
            pos = 6
        elif (weapon == "PSG") or (weapon == "psg") or (weapon == "PSG1") or (weapon == "psg1"):
            name = "HK PSG1"
            key = "psg"
            pos = 11
        elif (weapon == "g36") or (weapon == "G36"):
            name = "HK G36"
            key = "g36"
            pos = 9
        elif (weapon == "ak") or (weapon == "AK") or (weapon == "AK103") or (weapon == "ak103"):
            name = "AK103 7.62mm"
            key = "ak"
            pos = 8
        elif (weapon == "NEGEV") or (weapon == "negev") or (weapon == "NE") or (weapon == "ne"):
            name = "IMI Negev"
            key = "negev"
            pos = 12
        elif (weapon == "M4") or (weapon == "m4") or (weapon == "m4a") or (weapon == "M4A"):
            name = "Colt M4A1"
            key = "m4a1"
            pos = 7
        elif (weapon == "grenade") or (weapon == "GRENADE") or (weapon == "HE") or (weapon == "he"):
            name = "HE Grenade"
            key = "he"
            pos = 14
        else:
            client.message('^2%s ^7is not a weapon' % weapon)
            return False
            
        return name, key, pos
            
    def someoneKilled(self, client, target, data=None):
        """\
        Update database weapons for the attacker(killer)
        """
        if data[1] == self.console.UT_MOD_KNIFE:
            key = "kn"
        elif data[1] == self.console.UT_MOD_KNIFE_THROWN:
            key = "kn"
        elif data[1] == self.console.UT_MOD_DEAGLE:
            key = "de"
        elif data[1] == self.console.UT_MOD_BERETTA:
            key = "beretta"
        elif data[1] == self.console.UT_MOD_NEGEV:
            key = "negev"
        elif data[1] == self.console.UT_MOD_SPAS:
            key = "spas"
        elif data[1] == self.console.UT_MOD_HK69:
            key = "hk"
        elif data[1] == self.console.UT_MOD_HK69_HIT:
            key = "hk"
        elif data[1] == self.console.UT_MOD_SR8:
            key = "sr8"
        elif data[1] == self.console.UT_MOD_PSG1:
            key = "psg"
        elif data[1] == self.console.UT_MOD_MP5K:
            key = "mp5"
        elif data[1] == self.console.UT_MOD_UMP45:
            key = "ump"
        elif data[1] == self.console.UT_MOD_HEGRENADE:
            key = "he"
        elif data[1] == self.console.UT_MOD_LR300:
            key = "lr"
        elif data[1] == self.console.UT_MOD_M4:
            key = "m4"
        elif data[1] == self.console.UT_MOD_G36:
            key = "g36"
        elif data[1] == self.console.UT_MOD_AK103:
            key = "ak"
        else:
            return False
        
        weapon = self.findWeapon(key, client)
        key1 = weapon[1]
        key2 = weapon[1]
        pos = weapon[2]
        q=("UPDATE weaponrecord SET `%s` = %s+1 WHERE client_id = '%s'" % (key1, key2, client.id))
        self.debug(q)
        self.console.storage.query(q)
        mapstats = self.getMapStats(client)
        mapstats.stats[pos] += 1
        
    def cmd_weaponstats(self, data, client, cmd=None):
        """\
        <weapon> - Check your weapon stats. <player> to check other's stats
        """
        if not data:
            client.message('Invalid syntax, try !h weaponstats')
            return False
        
        input = self._adminPlugin.parseUserCmd(data)
        weapon = self.findWeapon(input[0], client)
        cname = input[1]
        if cname:
            sclient = self._adminPlugin.findClientPrompt(cname, client)
            cursor = self.console.storage.query('SELECT * FROM weaponrecord WHERE client_id = "%s"' % (sclient.id))
            r = cursor.getRow()
            stats = r[weapon[1]]
            cmd.sayLoudOrPM(client, '^2%s ^7Kills: %s ^7: ^5%s' % (weapon[0], sclient.exactName, stats))
        else:
            cursor = self.console.storage.query('SELECT * FROM weaponrecord WHERE client_id = "%s"' % (client.id))
            r = cursor.getRow()
            stats = r[weapon[1]]
            cmd.sayLoudOrPM(client, '^7You made ^5%s ^7kills with the ^2%s' % (stats, weapon[0]))
            
    def cmd_weaponmapstats(self, data, client, cmd=None):
        """\
        <weapon> - Check your weapon stats FOR THE CURRENT MAP. <player> to check other's stats
        """
        if not data:
            client.message('Invalid syntax, try !h weaponmapstats')
            return False
        
        input = self._adminPlugin.parseUserCmd(data)
        weapon = self.findWeapon(input[0], client)
        cname = input[1]
        if cname:
            sclient = self._adminPlugin.findClientPrompt(cname, client)
            mapstats = self.getMapStats(sclient)
            
            cmd.sayLoudOrPM(client, '^2%s ^7Kills: %s ^7: ^5%s ^7at ^3%s' % (weapon[0], sclient.exactName, mapstats.stats[weapon[2]], self._map))
        else:
            mapstats = self.getMapStats(client)
            
            cmd.sayLoudOrPM(client, '^7You made ^5%s ^7kills with the ^2%s ^7at ^3%s' % (mapstats.stats[weapon[2]], weapon[0], self._map))
           
    def cmd_weaponrecords(self, data, client, cmd=None):
        """\
        <weapon> - list the top 3 players with the selected weapon
        """
        if not data:
            client.message('Invalid syntax, try !h weaponrecords')
            return False
        
        input = self._adminPlugin.parseUserCmd(data)
        if input[1]:
            regex = re.compile(r"""^(?P<string>\w+) (?P<number>\d+)$""");
            match = regex.match(data)

            weapon = self.findWeapon(match.group('string'), client)
            limit = int(match.group('number'))
        else:
            weapon = self.findWeapon(input[0], client)
            limit = 3
        
        thread.start_new_thread(self.doTopList, (data, limit, client, weapon, cmd))
    
    def doTopList(self, data, limit, client, weapon, cmd=None):
        if limit > 10:
            limit = 10
        cursor = self.console.storage.query("""SELECT c.id, c.name, w.* 
                                            FROM weaponrecord w, clients c  
                                            WHERE c.id = w.client_id 
                                            AND c.id NOT IN ( SELECT distinct(c.id) FROM penalties p, clients c WHERE (p.type = "Ban" OR p.type = "TempBan") AND inactive = 0 AND p.client_id = c.id  AND ( p.time_expire = -1 OR p.time_expire > UNIX_TIMESTAMP(NOW()) ) )
                                            ORDER BY w.%s DESC LIMIT 0, %s""" % (weapon[1], limit))
        if cursor and (cursor.rowcount > 0):
            message = '^2%s ^7Top ^5%s ^7Kills:' % (weapon[0], limit)
            cmd.sayLoudOrPM(client, message)
            i = 1
            while not cursor.EOF:
                r = cursor.getRow()
                name = r['name']
                score = r[weapon[1]]
                message = '^3# %s: ^7%s : ^2%s ^7Kills' % (i, name, score)
                cmd.sayLoudOrPM(client, message)
                cursor.moveNext()
                i += 1
                time.sleep(1)

        return
        
class MapStats():
    stats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
