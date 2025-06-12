10th of May 2023: After several years of fine service, this server has become increasingly difficult to maintain and keep up. To get the server's wildcard adblocking benefits with higher uptime, you are welcome to give upvotes to https://github.com/AdguardTeam/HostlistsRegistry/issues/121

————————————————————————————————

After 1½ years of trial setups and tinkering until March 2021, I now offer my DNS server to be used by the public! That being said, there are a considerable number of drawbacks with it that means that it should ***NOT*** be used in setups where uptime, privacy, or impartiality is important. By using this server, you agree to at least having *read* and being aware of all the info written below.

Additionally, downtime has increased in the autumn of 2022, in part due to non-existent feedback nor reports from its users, along with frequent PC problems on my end.

### DNS IP addresses

The main connection addresses are:
* DNS-over-HTTPS: `https://dandelionsprout.asuscomm.com:2501/dns-query` (Works with almost all devices. Windows 11's OS "Settings" has a bug where it refuses to accept custom ports for DNS-over-HTTPS, due to it trying to ping `_2501._https.dandelionsprout.asuscomm.com`, which is not an address that DNS servers can usually handle; third-party Windows programs to handle DoH will still work.)
* DNS-over-TLS: `tls://dandelionsprout.asuscomm.com`(<i>Nebulo</i> and <i>AdGuard for Windows</i> are known to work. <i>AdGuard for Android</i> 4.x support can be forced by clicking the "Save" button multiple times.)
* DNS-over-QUIC: `quic://dandelionsprout.asuscomm.com:41396`
* DNSCrypt IPv4 (Currently not enabled): `sdns://AQEAAAAAAAAAEzg0LjIwMi4xNTUuMjE3OjU0NDMgOKEL1WhWlPWX9yILXMmWEzM6KWDYVv7vFEJQ8UxkUmwsMi5kbnNjcnlwdC1jZXJ0LmRhbmRlbGlvbnNwcm91dC5hc3VzY29tbS5jb20` (The stamp depends on the [current IPv4 address](https://www.ntppool.org/a/DandelionSprout). If the stamp seems to be dead, go to https://dnscrypt.info/stamps/ and choose the following settings: *current IPv4 address*:5443 - 38A10BD5685694F597F7220B5CC99613333A2960D856FEEF144250F14C64526C - 2.dnscrypt-cert.dandelionsprout.asuscomm.com)

Although I do also offer standard IPv4 and IPv6 addresses (both regular and on paper `tcp://`), they change fairly frequently due to ASUS routers bizarrely insisting on getting a new IPv4 address each time most of its settings are changed in any way; the newest ones are usually available at https://www.ntppool.org/a/DandelionSprout.

The encrypted addresses may also go down during Windows restarts, or if ASUS' lookup servers for Asuscomm are acting wonky.

### What is being blocked

The server attempts to block ads, malware, fake webshops, push notifications, and TV- and gaming-interface ads, with considerably better blocking of those than what AdGuard DNS offers. It also offers partial support for Wiimmfi online gaming, such as *Pokémon Pearl Version*, and *42 All-Time Classics*.

On the other hand, it goes easy on trackers, and blocks things I really don't like, such as rightwing tabloids (Daily Mail, Breitbart, 4chan), near-entire top-level domains (.tk, .top), scat, websites specifically dedicated to unfairly popular media (Azur Lane, Friendship is Magic), Scientology, a fair few US Evangelist hate preachers, and Twitch's "Prime Loot Reminder" plugin.

Current list set as of 12 June 2025:

#### Lists against ads, against app notifications, and against a few trackers
* Dandelion Sprout's AdGuard Home Compilation List — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuard%20Home%20Compilation%20List/AdGuardHomeCompilationList.txt
* Dandelion Sprout's AdGuard Home Compilation - Web Push Notifications — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuard%20Home%20Compilation%20List/AdGuardHomeCompilationList-Notifications.txt
* Dandelion Sprout's Nordic Filters (for AdGuard Home) — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/NordicFiltersAdGuardHome.txt
* Perflyst and Dandelion Sprout's Smart-TV Blocklist for AdGuard Home — https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV-AGH.txt
* 🎮 Game Console Adblock List — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/GameConsoleAdblockList.txt
* 📭 Anti-Amazon List for Twitch — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AntiAmazonListForTwitch.txt
* AdGuard Mobile Ads filter — https://filters.adtidy.org/extension/android-content-blocker/filters/11.txt
* Frellwit's Swedish Hosts File — https://raw.githubusercontent.com/lassekongo83/Frellwits-filter-lists/master/Frellwits-Swedish-Hosts-File.txt

#### Lists against malware
* 💊 Dandelion Sprout's Anti-Malware List (for AdGuard Home) — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareAdGuardHome.txt
* Phishing URL Blocklist (AdGuard Home) — https://malware-filter.gitlab.io/malware-filter/phishing-filter-domains.txt
* Hexxium Creations Threat List — https://raw.githubusercontent.com/HexxiumCreations/threat-list/gh-pages/hexxiumthreatlist.txt
* Magento - Burner Domains — https://raw.githubusercontent.com/gwillem/magento-malware-scanner/master/rules/burner-domains.txt
* Nolovia - Government Malware — https://raw.githubusercontent.com/parseword/nolovia/master/skel/hosts-government-malware.txt
* noads.online anti scumware list — https://raw.githubusercontent.com/deletescape/noads/master/lists/fo-scumware.txt
* Scam Blocklist by DurableNapkin — https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/adguard.txt
* Steam Scam Site — https://raw.githubusercontent.com/PoorPocketsMcNewHold/steamscamsites/master/steamscamsite.txt

#### Lists against unfairly popular culture
* 🤗 Anti-'Abuse porn' list — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AntiAbusePorn.txt
* 👸 Anti-FiM list — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Anti-F%D1%96%D0%9C%20List.txt
* ☔ Anti-'Steven Universe' List (Domains version) — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Other%20domains%20versions/AntiStevenUniverseListDomains.txt
* 🐨 Anti-'Hivemind cartoon trashing' List (Domains version) — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Other%20domains%20versions/AntiHivemindCartoonTrashingListDomains.txt
* 🚸 Anti-'Anthro combat-equipment gacha waifu' List — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AntiAnthroCombatWaifuList.txt

#### Lists against alt-right
* 🏗 Remover for Mainstream Tabloid and Alt-Right Sites — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/TabloidRemover.txt + https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/TabloidRemover-MastodonCategoryForImports.csv
* 💸 Anti-'Insane religious preachers' List — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/AntiPreacherList.txt
* Fake-Local-Journals-List — https://raw.githubusercontent.com/MassMove/AttackVectors/master/LocalJournals/fake-local-journals-list.txt
* Windscribe Clickbait — https://assets.windscribe.com/custom_blocklists/clickbait.txt

#### Lists against other things
* 🚪 Browse websites without logging in (for AdGuard Home) — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Other%20domains%20versions/BrowseWebsitesWithoutLoggingInAGH.txt
* 🏘 Semi-public stuff for Dandelion Sprout's Official DNS Server — https://raw.githubusercontent.com/DandelionSprout/adfilt2/master/a%20%E2%80%94%20AdGuard%20Home%20Miscellaneous.txt
<!--* RiiConnect24/Wiimmfi List for Users of AdGuard Home and Pi-Hole — https://raw.githubusercontent.com/RiiConnect24/DNS-Server/master/dns_zones-hosts.txt-->

#### Allowlists
* 🌭 Falukorv List — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/FalukorvList.txt
* AdGuard DNS Filter - Extra Exclusions — https://raw.githubusercontent.com/AdguardTeam/AdGuardSDNSFilter/master/Filters/exceptions.txt

Are you curious about **which** exact list that is blocking a site, without having to do extensive searching? Load [this configuration file](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Wiki/Dandelion%20Sprout's%20Official%20DNS%20Server's%20quick-lookup%20uBO%20config%204th%20of%20November%202021.txt) into uBlock Origin in a secondary web browser, try to visit a site, and see which list is shown as having the entry.

### Who can use the server

Company networks from The Netherlands, Romania, Russia and Ukraine will usually be prohibited as well. Residential networks from those countries are fine.

Many companies known to look through the fingers with port-scanners and spammers, are also prohibited. Full list: https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuardHomeDisallowedIPs.txt

Users from PR-China were originally unsupported, due to considerable amounts of query spam from that country that preceded the server's cataloging by AdGuard; but have been allowed since February 2022 in an attempt to appeal to anti-GFW audiences.

### Other technical aspects

The servers run on workstation multimedia Windows 11 PCs.

The AdGuard Home update channel in use is the Beta channel (As opposed to Stable or Nightly).

Average uptime for `dandelionsprout.` is more than 23h55min per day, but is not close enough to 24h00min00sec to be suited for life-or-death scenarios. The uptime for `dandelionsprout2.` varies heavily, depending on whether and when its computer's owners turn it on or off, for instance when going to bed.

### Known problems

* Many (but not all) redirection/affiliation links on e.g. price comparison sites, may be blocked too. This is a known problem inherent to all major DNS adblocker servers, incl. AdGuard DNS.

### Privacy

Since the server is based on AdGuard Home, the user's IP addresses and the domains they query, are stored on the server, and I reserve the right to browse through the queries if I feel bored for some reason. Additionally, the query log will occasionally help improve the lists that are used ([Example](https://github.com/DandelionSprout/adfilt/commit/cd222a03bf37ee133604008227238bc52d5932b2#diff-4f9e07c6df3e782fd76b51a2dcbe332049dcc066bad61fa0997b737dfe62e22a)), and to determine the (hopefully) least interruptive times to run updates for AdGuard Home or apt-get.

No query or IP data are shared or sold to third-parties, especially so because I dislike user data buyers.

Current non-LAN upstreams as of 2nd of October 2022:

```
quic://dns-unfiltered.adguard.com
https://dns.google/dns-query
tls://unicast.censurfridns.dk
sdns://AQAAAAAAAAAADjIwOC42Ny4yMjAuMjIwILc1EUAgbyJdPivYItf9aR6hwzzI1maNDL4Ev6vKQ_t5GzIuZG5zY3J5cHQtY2VydC5vcGVuZG5zLmNvbQ
https://doh.pub/dns-query
tls://101.101.101.101
```

The DNS server has one server-PC and location, in Norway. This (most likely) makes the server more suited for European users than for users elsewhere.

This README is licenced under [the Dandelicence](https://github.com/DandelionSprout/adfilt/blob/master/LICENSE.md).

Contacting me about the server, should be done at https://github.com/DandelionSprout/adfilt/issues

### Outage log (Oldest first)

* 21st of June 2021 20:15-22:29 UTC: What was planned as a 5min outage to set up a 2.5Gb Ethernet card, escalated when it turned out my soon-to-be-discarded Raspbian installation had *the entire network settings menu* disappear permanently, leading to huge problems assigning a static LAN IP to it.
* Intermittently from 24th to 26th of June 2021: In relation to upgrading to an ARM64 distro, there were problems with *firewalld* and a seemingly dead Ethernet overvoltage protector (APC PNET1GB) that led to frequent downtimes of a few minutes every few hours.
* 12th of July 2021 00:01-01:35 UTC: The AdGuard Home installation was stuck at a "The DNS server is starting" error screen, until I noticed the error by pure coincidence and powercycled the RaspPi.
* 18th of July 2021 17:51-19:10 UTC: My ASUS router's TrendMicro anti-botnet function had a total meltdown. Moreover, attempting to grab the chance to run a Fedora dnf update, took much longer than expected.
* 19th of July 2021 16:??-20:40 UTC: Near-total server failure in general. Shoutout to https://community.home-assistant.io/t/home-assistant-community-add-on-adguard-home/90684/13 for a fix that returned the server to basic functionality; alongside other network fixes and AGH settings tinkering.
* 23rd of July 21:30~22:50 UTC: I decided to try to set up DNSCrypt, which took several attempts.
* 23rd of August 20:45~21:40 UTC: Had to look into https://github.com/AdguardTeam/AdGuardHome/issues/3465#issuecomment-904153260
* 7th of September 01:01-01:30 UTC: One of my two Ethernet switches began bugging out for unknown reasons.
* 9th of September 20:15~23:30 UTC, and intermittently on 10th of September: Replaced my old ASUS RT-AC68U, with an ASUS RT-AX89X.
* 22th of October 09:08-09:14 UTC: What seemed like a Special K flake, had managed to cram its way into the fan of my 400€ network switch, and I had to get it out with an *Anna & Clara* butter knife without destroying the switch.
* 25th of October 14:00~15:45 UTC: I swear to Queen Clarion that the RaspPi just randomly froze with no input, while I was sitting in the couch playing New Super Mario Bros. 2. I need to look into *some* sort of failover server in the near future.
* 4th of November 10:05~11:28 UTC: I did not expect Fedora to need 1 hour 18 minutes to upgrade from Workstation 34 to 35.
* 8th of November 09:30~11:50 UTC: Turns out that clones of Linux disks are *not* able to boot, in sharp contrast to clones of Windows disks. So I figured "Screw this" in regards to setting up a 2nd RaspPi at my parents' house, and hereby open up my Windows 11 AGH installation to the world too.
* 13th of December 03:00-03:30 UTC: My ISP went down, and the ASUS router's failover triggers didn't want to work properly.
* 9th of January 15:00 UTC - 28th of January: All I did was enable Flathub and play Space Cadet Pinball, then the Raspberry Pi froze, and when I restarted it had become permanently unable to connect to public IPs and addresses. I hate Linux more than ever before.
* 15th of February 20:09-20:16 UTC: An ASUS router update caused problems with IPv6, so I had to scramble real quick to fix it.
* 12th of March 13:35 UTC: Some 4 weeks after scheduled, the `dandelionsprout2.` secondary server is back online.
* Early June 2022: Increasingly severe muscle movement problems, coupled with me forgetting to add the SSL certificate expiry dates in my Thunderbird calendar, and the total lack of feedback from server users, resulted in a 3-day outage for DoH and DoQ. I'm hoping to make up for it by attempting to re-enable DNSCrypt.
* Early July 2022: My server gives me the error `[error] handling tcp: reading msg: reading len: remote error: tls: bad certificate`. I have no idea what it means, and I have no idea how to fix it.
* 6th of July 2022 19:42 UTC: Seems to be fixed now, and I have no idea how I did it. Seemed to have been conflicts with an SSL certificate using of 1 of 3 sections (when it was apparently supposed to use 2?), and with trying to use itself as an upstream during testing.
* 14th of September 2022 16:15~19:02 UTC: Both servers seemed to have a breakdown moment when they were upgraded to AdGuard Home v0.108.0-b.14, necessitating server restarts a bit late since I was heading out for shopping when I noticed the problem.
* 21st of September 2022 02:00 UTC - 2nd of October 07:00: Windows 11 22H2 RTM seemed to somehow have completely and massively broken AdGuard Home direct IP functionality, and I was only able to restore DoH on the morning of the 25th. Direct IP seems to have been restored on 02/11 after installing the KB5017389 Windows update.
* Early November 2022: Various problems, including having to reinstall Windows 11, a failed attempt at getting off the IO cap on an Aorus B550 Pro AC that *almost* broke my PC, and apparently forgetting to whitelist the DoT and DoQ ports in Windows Firewall.
