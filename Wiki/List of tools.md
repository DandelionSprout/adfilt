# All adblockers
Note that the list below only features examples of each category, and is not a comprehensive or full list of them.
## Advanced adblockers
Adblockers in this category has support for extended syntaxes, that can be used to filter away more things, create tool-dependent entries, or to bind lists to other lists. There's not a 100% harmony between the tools' syntaxes, but a list that is made for one of them will usually also work in the other ones.

• [Nano Adblocker](https://github.com/NanoAdblocker/NanoCore) ([Chrome](https://chrome.google.com/webstore/detail/nano-adblocker/gabbbocakeomblphkmmnoamkioajlkfo) / [MS Edge](https://www.microsoft.com/store/productId/9NSXDX2TDB3V))<br>
• [uBlock Origin](https://github.com/gorhill/uBlock) ([Chrome](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm) / [Firefox](https://addons.mozilla.org/addon/ublock-origin/)¹ / [Opera native](https://addons.opera.com/extensions/details/ublock/) / [Pale Moon²](https://github.com/gorhill/uBlock/blob/master/dist/README.md#firefox-legacy))<br>
• [Adguard](https://adguard.com/en/welcome.html) ([Chrome](https://chrome.google.com/webstore/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg) / [Firefox](https://addons.mozilla.org/addon/adguard-adblocker/)¹ / [Safari](https://safari-extensions.apple.com/details/?id=com.adguard.safari-N33TQXN8C7) / [Opera native](https://addons.opera.com/en/extensions/details/adguard/) / [MS Edge](https://www.microsoft.com/store/p/adguard-adblocker/9mz607gwkbs7) / [Pale Moon](https://github.com/AdguardTeam/AdguardBrowserExtension/releases)² / [iOS](https://itunes.apple.com/app/apple-store/id1047223162) / [Samsung Internet / Yandex.Browser Mobile](https://adguard.com/en/adguard-content-blocker/overview.html) / [Paid pan-Windows version](https://adguard.com/en/adguard-windows/overview.html) / [Paid pan-Mac version](https://adguard.com/en/adguard-mac/overview.html) / [Paid pan-Android version](https://adguard.com/en/adguard-android/overview.html))

## Simple adblockers
These adblockers support a core set of functionality, either to have some degree of mercy on ad-dependent websites, or to keep the coding and options easy to use.

• [Adblock Plus](https://adblockplus.org/) ([Chrome](https://chrome.google.com/webstore/detail/cfhdojbkjhnklbpkdaibdccddilifddb) / [Firefox](https://addons.mozilla.org/addon/adblock-plus/)¹ / Safari / [Opera native](https://addons.opera.com/extensions/details/opera-adblock/) / [MS Edge](https://www.microsoft.com/store/p/adblock-plus/9nblggh4r9nz))<br>
• [AdBlock](https://getadblock.com/) ([Chrome](https://chrome.google.com/webstore/detail/gighmmpiobklfepjocnamgkkbiglidom) / [Firefox](https://addons.mozilla.org/firefox/addon/adblock-for-firefox/)¹ / Safari / Opera native / [MS Edge](https://www.microsoft.com/store/productID/9nblggh4rfhk))<br>

¹ = Have been confirmed to also work on the Android version of Firefox.<br>
² = Download the .xpi file that has <i>firefox-legacy(...)</i> in its filename.

## Additional tools

• There's a significant number of Android web browsers that specialise in ad blocking, e.g. [Adblock Browser](https://play.google.com/store/apps/details?id=org.adblockplus.browser). However, many such browsers are usually based on outdated versions of Firefox, and/or doesn't allow for using other extensions, so therefore I don't normally recommend them.<br>
• There exist several DNS servers that serve as remote adblockers, most notably [Adguard DNS](https://adguard.com/en/adguard-dns/overview.html). While they are very convenient for use in routers, rooted Android phones, and to a small degree media boxes, they don't support <i>any</i> of my lists under normal circumstances due to their lack of customisability.<br>
• I don't have any modern iOS units, and I therefore have no idea which ones that are really available out there, let alone which ones I could've recommended, unfortunately.<br>
• There exists a heavily amputated version of Adblock Plus for Internet Explorer, but it does not allow to subscribe to more than one list at a time. If you're in a situation where you think you need to use Internet Explorer to e.g. play old Flash and Unity Web Player games, I would at the time of writing recommend switching your IE activities over to [Basilisk Browser](https://www.basilisk-browser.org/), which supports old media browser extensions <i>and</i> uBlock Origin.

# Hosts tools
These tools specialise in dealing with one specific system file that originated in networked PCs in the 1980's, which was simply called [<i>hosts</i>](https://en.wikipedia.org/wiki/Hosts_(file)). The file originally served as a decoder of IP addresses at a time when DNS servers hadn't really sprung into life quite yet, but eventually someone realised that if they pointed certain URLs to IP addresses that were reserved for local use, then they'd stop the PC from downloading any data from those URLs, which promptly became used for adblocking by a low 3-digit amount of publicly available lists.

They only support pure IP addresses, and does not ordinarily support any syntaxes or element specifications whatsoever. I would therefore rather recommend the use of adblockers and adblock-tailored lists instead, but for those who need to defend specific products under and from specific circumstances, here's a few tools that can make use of hosts files.

• [Hosts File Editor](https://github.com/scottlerch/HostsFileEditor) (Windows)<br>
• [Gas Mask](https://github.com/2ndalpha/gasmask) (macOS)<br>
• [Pi-hole](https://pi-hole.net/) (Linux)<br>
• [DNS66](https://github.com/julian-klode/dns66) ([Android without root, through the F-Droid store](https://f-droid.org/packages/org.jak_linux.dns66/))<br>
• [AdAway](https://adaway.org/) ([Android with root, through the F-Droid store](https://f-droid.org/packages/org.adaway/))<br>
• [Editing it yourself on Windows, macOS and Linux](https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/)

Web-hosted hosts files can also be used with Nano Adblocker and uBlock Origin, but in the case of my Norwegian list it's preferable to use the regular, adblock-formatted list instead when using those adblockers.

# Internet Explorer's Tracking Protection List feature
Starting with Internet Explorer 9, and also being present in 10 and 11, is a feature called <i>Tracking Protection List</i>. It was originally targeted towards those who didn't like trackers, and featured such lists as EasyPrivacy (made by the EasyList team).

There have been attempts at making use of the function to block ads, which has gone so-so. The lists have a different syntax than that of typical adblock lists, which makes conversion difficult. Moreover it usually cannot block all elements either.

Lists are added to the feature by clicking on (or pasting and opening) special Javascript links that only work in Internet Explorer; and once they have been added, they can be managed through [the settings interface](https://www.howtogeek.com/73545/avoid-being-tracked-on-the-internet-using-tracking-protection-list-in-ie9/).

For info on how to add the Norwegian TPL link to your Internet Explorer, see [here](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/NorskeFiltreTPL-installering.html)

# Little Snitch

Little Snitch is [a paid program](https://www.obdev.at/products/littlesnitch/index.html) for macOS, which specialises in meticulously handling both incoming and outgoing server connections. Unfortunately I don't have readily access to Apple products, so I haven't been able to try out this tool myself.

# Search result blockers

This section is about search result blockers, which takes care of removing websites that you don't like from Google search results.

They can import (through plain pasting) lists of domains, and then it'll remove such search results thereafter. Entries can be removed or turned off individually, and in the case of *Personal Blocklist* a note will be shown on the bottom of the Google page if any search results on that page were blocked by the extensions. In contrast to adblockers, these tools don't use source files for its entries, and therefore cannot auto-update its entries either.

• [Personal Blocklist (by Google)](https://chrome.google.com/webstore/detail/personal-blocklist-by-goo/nolijncfnkgaikbjbdaogikpmpbdcdef) ([Chrome](https://chrome.google.com/webstore/detail/personal-blocklist-by-goo/nolijncfnkgaikbjbdaogikpmpbdcdef))<br>
• [Personal Blocklist (not by Google)](https://github.com/wildskyf/personal-blocklist) ([Firefox](https://addons.mozilla.org/firefox/addon/personal-blocklist/))<br>
• [Google Hit Hider for Domains](https://www.jeffersonscher.com/gm/google-hit-hider/) ([Script for all browsers that support Tampermonkey and similar userscript extensions](https://greasyfork.org/scripts/1682-google-hit-hider-by-domain-search-filter-block-sites))

# Redirector

This is [an extension](http://einaregilsson.com/redirector/) made by the Icelandic developer Einar Egilsson. It has many functions that would be impossible to replicate on any adblockers, even the advanced ones.

While it can't do any real amounts of adblocking, it can help greatly with [utilising URL tricks](https://github.com/DandelionSprout/adfilt/blob/master/Dandelion%20Sprout-s%20Redirector%20Assistant%20List/README.md) that'd be overly convoluted or impossible to pull off otherwise.

# Stylish

This is an extension that aims to work with [thousands upon thousands](https://userstyles.org/) of usermade CSS scripts, which can edit background images, page widths, and a few other things.

After I found out how to convert most Userstyles scripts to [an adblocker-supported syntax](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Dandelion%20Sprout's%20Website%20Stretcher.txt), this extension has been mostly deprecated on Adfilt.

## My personal recommendations for users of each platform

• Chrome desktop, Chromium-based browsers, Edge: Nano Adblocker<br>
• Firefox, Firefox Android, Pale Moon, Basilisk Browser, other Australis-based programs, Safari macOS: uBlock Origin<br>
• Internet Explorer 11 (with paying), Steam desktop client, Thunderbird ≥60, Windows Store apps on desktop: The paid version of Adguard<br>
• Internet Explorer 11 (without paying): Tracking Protection Lists<br>
• Android (non-rooted, non-Firefox): DNS66<br>
• Gaming consoles (e.g. Wii U): Adguard DNS in the console settings<br>
• Android (rooted): Adguard DNS with [DNSForwarder](https://play.google.com/store/apps/details?id=com.evanhe.dnsforward)<br>
• Windows Phone (while at home): Adguard DNS on your router<br>
• SmartTVs: Pi-hole with [the only list in existence that targets SmartTVs](https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt), and which even then is largely privacy-focused instead of anti-ad-focused.
