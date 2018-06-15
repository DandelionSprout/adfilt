# All adblockers
Note that the list below only features examples of each category, and is not a comprehensive or full list of them.
## Advanced adblockers
Adblockers in this category has support for extended syntaxes, that can be used to filter away more things, create tool-dependent entries, or to bind lists to other lists. There's not a 100% harmony between the tools' syntaxes, but a list that is made for one of them will usually also work in the other ones.

• [Nano Adblocker](https://github.com/NanoAdblocker/NanoCore) ([Chrome](https://chrome.google.com/webstore/detail/nano-adblocker/gabbbocakeomblphkmmnoamkioajlkfo) / [MS Edge](https://www.microsoft.com/store/productId/9NSXDX2TDB3V))<br>
• [uBlock Origin](https://github.com/gorhill/uBlock) ([Chrome](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm) / [Firefox](https://addons.mozilla.org/addon/ublock-origin/)¹ / [Opera native](https://addons.opera.com/extensions/details/ublock/) / [Thunderbird / Pale Moon](https://github.com/gorhill/uBlock/blob/master/dist/README.md#firefox-legacy))<br>
• [Adguard](https://adguard.com/en/welcome.html) ([Chrome](https://chrome.google.com/webstore/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg) / [Firefox](https://addons.mozilla.org/addon/adguard-adblocker/)¹ / [Safari](https://safari-extensions.apple.com/details/?id=com.adguard.safari-N33TQXN8C7) / [Opera native](https://addons.opera.com/en/extensions/details/adguard/) / [MS Edge](https://www.microsoft.com/store/p/adguard-adblocker/9mz607gwkbs7) / [Thunderbird² / Pale Moon](https://github.com/AdguardTeam/AdguardBrowserExtension/releases)² / [iOS](https://itunes.apple.com/app/apple-store/id1047223162) / [Samsung Internet / Yandex.Browser Mobile](https://adguard.com/en/adguard-content-blocker/overview.html) / [Paid pan-Windows version](https://adguard.com/en/adguard-windows/overview.html) / [Paid pan-Mac version](https://adguard.com/en/adguard-mac/overview.html) / [Paid pan-Android version](https://adguard.com/en/adguard-android/overview.html))

## Simple adblockers
These adblockers support a core set of functionality, either to have some degree of mercy on ad-dependent websites, or to keep the coding and options easy to use.

• [Adblock Plus](https://adblockplus.org/) ([Chrome](https://chrome.google.com/webstore/detail/cfhdojbkjhnklbpkdaibdccddilifddb) / [Firefox](https://addons.mozilla.org/addon/adblock-plus/)¹ / Safari / [Opera native](https://addons.opera.com/extensions/details/opera-adblock/) / [MS Edge](https://www.microsoft.com/store/p/adblock-plus/9nblggh4r9nz))<br>
• [AdBlock](https://getadblock.com/) ([Chrome](https://chrome.google.com/webstore/detail/gighmmpiobklfepjocnamgkkbiglidom) / [Firefox](https://addons.mozilla.org/da/firefox/addon/adblock-for-firefox/)¹ / Safari / Opera native / [MS Edge](https://www.microsoft.com/store/productID/9nblggh4rfhk))<br>
• [DNS66](https://github.com/julian-klode/dns66) ([Android without root, through the F-Droid store](https://f-droid.org/packages/org.jak_linux.dns66/))

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

• [AdAway](https://adaway.org/) ([Android with root, through the F-Droid store](https://f-droid.org/packages/org.adaway/))<br>
• [Editing it yourself on Windows, macOS and Linux](https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/)<br>
• [Hosts File Editor](https://github.com/scottlerch/HostsFileEditor) (Windows)

Web-hosted hosts files can also be used with Nano Adblocker and uBlock Origin, but in the case of my Norwegian list it's preferable to use the regular, adblock-formatted list instead when using those adblockers.

# Internet Explorer's Tracking Protection List feature
Starting with Internet Explorer 9, and also being present in 10 and 11, is a feature called <i>Tracking Protection List</i>. It was originally targeted towards those who didn't like trackers, and featured such lists as EasyPrivacy (made by the EasyList team).

There have been attempts at making use of the function to block ads, which has gone so-so. The lists have a different syntax than that of typical adblock lists, which makes conversion difficult. Moreover it usually cannot block all elements either, only some of them; and I haven't had much luck with finding substantial documentation on the matter.

Lists are added to the feature by clicking on (or pasting and opening) special Javascript links that only work in Internet Explorer; and once they have been added, they can be managed through https://www.howtogeek.com/73545/avoid-being-tracked-on-the-internet-using-tracking-protection-list-in-ie9/.

I do not currently have IE on my PC and therefore can't test it, but the address to add the TPL version of my Norwegian adblock to Internet Explorer should be:

<i>javascript:window.external.msAddTrackingProtectionList('https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/DandelionSproutsNorskeFiltre.tpl', 'Dandelion Sprouts norske filtre - IE-versjonen')</i>

### To-write

Non-blocker tools, Little Snitch, personal recommendations for each platform.
