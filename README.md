# WeaponRecord Plugin
##### Plugin for B3 (www.bigbrotherbot.com)
##### Author: LouK(8thelouk8@gmail.com) - http://sniperjum.com
=
### Installation -

* Place weaponrecord.py in /extplugins/ and weaponrecord.xml in /extplugins/conf/
* In your b3.xml config, add this line: <plugin name="weaponrecord" config="@b3/extplugins/conf/weaponrecord.xml"/>
* Insert the weaponrecord.sql in your SQL database
* Change command levels in the weaponrecord.xml

-
### Description -
This plugin saves every kill made with every weapon at the b3's database. You can check how many kills you made with a weapon, check other's stats or see top kills with a weapon (which players are the top killers with that weapon).

Also tracks weapon stats for all maps to check weapons records (who are the players that made more kills with that weapon at that map until map finishes) or your own weapon stats for the current map.

-
### Commands -

#### !weaponstats (!wstats)
> &lt;weapon&gt; - Check your weapon stats. &lt;player&gt; to check other's stats

#### !weapontopstats (!wtopstats)
> &lt;weapon&gt; &lt;number&gt; - list the top 3 players with the selected weapon


#### !weaponmapstats (!wmapstats)
> &lt;weapon&gt; - Check your weapon stats at the current map. &lt;player&gt; to check other's stats

#### !weaponmaprecord (!wmaprecord)
> &lt;weapon&gt; (&lt;number&gt; or &lt;map&gt;) - list the top 3 players with the selected weapon for the selected map