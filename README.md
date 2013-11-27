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
This plugin saves every kill made with every weapon at the b3's database. You can check how many kills you made with a weapon, check other's stats or see top kills with a weapon (which players are the top killers with that weapon)

-
### Commands -

#### !weaponstats (!wstats)
> &lt;weapon&gt; - Check your weapon stats. &lt;player&gt; to check other's stats

#### !weaponrecords (!wrecords)
> &lt;weapon&gt; - list the top 3 players with the selected weapon
