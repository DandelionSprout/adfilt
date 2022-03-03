Important note to self: Running Python scripts in Cygwin and PowerShell seems to create **COMPLETELY** different file encodings that completely overwrite one another. Stick to the Cygwin output versions if at all humanly possible for logkeeping's sake.

Recommended adblockers for the various list versions:

• uBlock Origin, AdNauseam: **[NorwegianList.txt](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianList.txt)**<br>
• —||—, but without tracker whitelistings: **NordicFiltersPrivacy.txt**<br>
• AdGuard: **NordicFiltersAdGuard.txt**<br>
• AdBlock, ABP users who want anti-anti-adblock: **NordicFiltersABP.txt**<br>
• General ABP users: **NordicFiltersABP-Inclusion.txt**<br>
• Blokada, DNS66: **DandelionSproutsNorskeFiltreDomains.txt** + **NordicFiltersDomainsAllowlist.txt**<br>
• Google Hit Hider by Domain, uMatrix, personalDNSfilter, Samsung Knox, dnscrypt-proxy, Diversion, FireHOL: **DandelionSproutsNorskeFiltreDomains.txt**<br>
• pfBlockerNG, AdAway, Gas Mask, hostsmgr, Hosts File Editor: **AdawayHosts**<br>
• Internet Explorer 11: **DandelionSproutsNorskeFiltre.tpl**<br>
• AdGuard Home: **NordicFiltersAdGuardHome.txt**<br>
• Pi-hole: **NordicFiltersPiHole.txt** + **NordicFiltersDomainsAllowlist.txt**<br>
• Little Snitch: **LittleSnitchNorwegianList.lsrules**<br>
• dnsmasq: **NordicFiltersDnsmasq.conf**<br>
• Privoxy: **NordicFiltersPrivoxy.action**<br>
• BIND: **NordicFiltersRPZ.txt**<br>
• Shadowrocket, Shadowsocks (all versions), Surge: **NordicFiltersSocks5.list**<br>
• Unbound: **NordicFiltersUnbound.conf**<br>
• minerBlock: **NordicFiltersForMinerBlock.txt**

—————————————————————————

### How to run the list generation script

This is only recommended for Adfilt team members or those who want to test the script, and is not recommended for pull requests.

1) Right-click on https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/XYZPrepareFilters.py and save it on your PC, preferably in its own folder.
2) If you're on Windows, install [Cygwin 64-bit](https://www.cygwin.com/), and pick the <i>python38</i> package when you're prompted to install any packages.
3) In the folder where you placed `XYZPrepareFilters.py`, create two new subfolders with the names of `Anti-Malware List` and `Domeneversjoner`.
4) Open Cygwin (on Windows) or the default terminal (on macOS or Linux), use `cd` to navigate to the folder that contains `XYZPrepareFilters.py`, and run `Python3 XYZPrepareFilters.py`. Due to GitHub line end conflicts, avoid using PowerShell for this if at all physically possible.
5) If it worked, it'll lead to a few lines with text along the lines of "The list versions have been generated."
