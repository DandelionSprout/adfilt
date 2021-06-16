After 1½ years of trial setups and tinkering until March 2021, I now offer my DNS server to be used by the public! That being said, there are a considerable number of drawbacks with it that means that it should ***NOT*** be used in setups where uptime, privacy, or impartiality is important. By using this server, you agree to at least having *read* and being aware of all the info written below.

### DNS IP addresses

The main connection addresses are:
* DNS-over-HTTPS: `https://dandelionsprout.asuscomm.com:2501/dns-query`
* DNS-over-TLS: `tls://dandelionsprout.asuscomm.com:853`
* DNS-over-QUIC: `quic://dandelionsprout.asuscomm.com:853`

Although I do also offer standard IPv4 and IPv6 addresses, they change fairly frequently due to ASUS routers bizarrely insisting on getting a new IPv4 address each time most of its settings are changed in any way; the newest ones are usually available at https://www.ntppool.org/a/DandelionSprout.

The encrypted addresses may also go down during (pretty rare) Raspberry Pi restarts, or if ASUS' lookup servers for Asuscomm are acting wonky.

### What is being blocked

The server attempts to block ads, malware, fake webshops, push notifications, and TV- and gaming-interface ads, with considerably better blocking of those than what AdGuard DNS offers. It also offers partial support for Wiimmfi online gaming, such as *Pokémon Pearl Version*, and *42 All-Time Classics*.

On the other hand, it goes easy on trackers, and blocks things I really don't like, such as rightwing tabloids (Daily Mail, Breitbart, 4chan), near-entire top-level domains (.tk, .top), scat, websites specifically dedicated to unfairly popular media (Azur Lane, Friendship is Magic), Pokémon GO, Scientology, a fair few US Evangelist hate preachers, and Twitch's "Prime Loot Reminder" plugin.

Current list set as of 16th of June 2021:

* Dandelion Sprout's AdGuard Home Compilation List — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuard%20Home%20Compilation%20List/AdGuardHomeCompilationList.txt
* Dandelion Sprout's AdGuard Home Compilation - Web Push Notifications — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuard%20Home%20Compilation%20List/AdGuardHomeCompilationList-Notifications.txt
* Dandelion Sprout's Nordic Filters (for AdGuard Home) — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/NordicFiltersAdGuardHome.txt
* 💊 Dandelion Sprout's Anti-Malware List (for AdGuard Home) — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareAdGuardHome.txt
* Perflyst and Dandelion Sprout's Smart-TV Blocklist for AdGuard Home — https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV-AGH.txt
* Ad Domains Filter List — https://raw.githubusercontent.com/LanikSJ/ubo-filters/main/filters/combined-filters.txt
* AdGuard DNS Filter - Extra Exclusions — https://raw.githubusercontent.com/AdguardTeam/AdGuardSDNSFilter/master/Filters/exceptions.txt
* AdGuard Home Gradual Syntax Inclusion Test List — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sandbox/AGHSyntaxTester.txt
* AdGuard Mobile Ads filter — https://filters.adtidy.org/extension/chromium/filters/11.txt
* DodgySiteBlocker — https://raw.githubusercontent.com/callmenemo491/DodgySiteBlocker/master/DodgySiteBlocker.txt
* Fake-Local-Journals-List — https://raw.githubusercontent.com/MassMove/AttackVectors/master/LocalJournals/fake-local-journals-list.txt
* Frellwit's Swedish Hosts File — https://raw.githubusercontent.com/lassekongo83/Frellwits-filter-lists/master/Frellwits-Swedish-Hosts-File.txt
* Hexxium Creations Threat List — https://raw.githubusercontent.com/HexxiumCreations/threat-list/gh-pages/hexxiumthreatlist.txt
* Magento - Burner Domains — https://raw.githubusercontent.com/gwillem/magento-malware-scanner/master/rules/burner-domains.txt
* noads.online anti scumware list — https://raw.githubusercontent.com/deletescape/noads/master/lists/fo-scumware.txt
* Nolovia - Government Malware — https://raw.githubusercontent.com/parseword/nolovia/master/skel/hosts-government-malware.txt
* RiiConnect24/Wiimmfi List for Users of AdGuard Home and Pi-Hole — https://raw.githubusercontent.com/RiiConnect24/DNS-Server/master/dns_zones-hosts.txt
* Scam Blocklist by DurableNapkin — https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/adguard.txt
* Spam404 Domains — https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt
* Steam Scam Site — https://raw.githubusercontent.com/PoorPocketsMcNewHold/steamscamsites/master/steamscamsite.txt
* Grayware Blocklist — https://raw.githubusercontent.com/VernonStow/Filterlist/master/Filterlist.txt
* Windscribe Clickbait — https://assets.windscribe.com/custom_blocklists/clickbait.txt
* ☔ Anti-'Steven Universe' List (Domains version) — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Other%20domains%20versions/AntiStevenUniverseListDomains.txt
* 🍚 Extremely Condensed Adblocking List — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/ExtremelyCondensedList.txt
* 🎮 Game Console Adblock List — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/GameConsoleAdblockList.txt
* 🏗 Remover for Mainstream Tabloid and Alt-Right Sites — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/TabloidRemover.txt
* 🐨 Anti-'Hivemind cartoon trashing' List (Domains version) — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Other%20domains%20versions/AntiHivemindCartoonTrashingListDomains.txt
* 👸 Anti-FiM list — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Anti-F%D1%96%D0%9C%20List.txt
* 💸 Anti-'Insane religious preachers' List — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/AntiPreacherList.txt
* 📭 Anti-Amazon List for Twitch — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AntiAmazonListForTwitch.txt
* 🚪 Browse websites without logging in (for AdGuard Home) — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Other%20domains%20versions/BrowseWebsitesWithoutLoggingInAGH.txt
* 🚸 Anti-'Anthro combat-equipment gacha waifu' List — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AntiAnthroCombatWaifuList.txt
* 🛀 Pokémon No-GO Zone — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Pok%C3%A9monNoGOZone.txt
* 🏘 Semi-public stuff for Dandelion Sprout's Official DNS Server — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/a%20%E2%80%94%20AdGuard%20Home%20Miscellaneous.txt
* 🤗 Anti-'Abuse porn' list — https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AntiAbusePorn.txt

### Who can use the server

Users from PR-China will not have their queries processed by the server, due to considerable amounts of query spam from that country, some of which even came from residential networks.

Additionally, company networks from The Netherlands, Romania, Russia and Ukraine will usually be prohibited as well. Residential networks from those countries are fine.

Many companies known to look through the fingers with port-scanners and spammers, are also prohibited. Full list: https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuardHomeDisallowedIPs.txt

### Other technical aspects

The server runs on a Raspberry Pi 4 4GB, with Raspberry Pi OS 32-bit. Several attempts at upgrading to a 64-bit distro have failed, including Raspberry Pi OS Beta (Couldn't handle backports), openSUSE (RaspPi version is broken), and Ubuntu MATE (Very bad optimising).

The AdGuard Home update channel in use is the Beta channel (As opposed to Stable or Nightly).

Average uptime is more than 23h59min per day, but is not close enough to 24h00min00sec to be suited for life-or-death scenarios.

### Known problems

* Many (but not all) redirection/affiliation links on e.g. price comparison sites, may be blocked too. This is a known problem inherent to all major DNS adblocker servers, incl. AdGuard DNS.
* <i>Grayware Blocklist</i> blocks TLDs that aren't 100.0% malware, most notably `||club^`. Problems with specific `.club` sites are therefore extra important for me to be told about.

### Privacy

Since the server is based on AdGuard Home, the user's IP addresses and the domains they query, are stored on the server, and I reserve the right to browse through the queries if I feel bored for some reason. Additionally, the query log will occasionally help improve the lists that are used ([Example](https://github.com/DandelionSprout/adfilt/commit/cd222a03bf37ee133604008227238bc52d5932b2#diff-4f9e07c6df3e782fd76b51a2dcbe332049dcc066bad61fa0997b737dfe62e22a)), and to determine the (hopefully) least interruptive times to run updates for AdGuard Home or apt-get.

No query or IP data are shared or sold to third-parties, especially so because I dislike user data buyers, and because Linux does not support OneDrive.

Current non-LAN upstreams as of 16th of June 2021:

* `https://mozilla.cloudflare-dns.com/dns-query`
* `https://dns.google/dns-query`
* `tls://unicast.censurfridns.dk`

The DNS server has one server-PC and location, in Norway. This (most likely) makes the server more suited for European users than for users elsewhere.

This README is licenced under [the Dandelicence](https://github.com/DandelionSprout/adfilt/blob/master/LICENSE.md).

Contacting me about the server, should be done at https://github.com/DandelionSprout/adfilt/issues
