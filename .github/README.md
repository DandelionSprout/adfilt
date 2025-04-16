![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/Adfilt%20logo%203.webp)<br>
![GitHub repo size in bytes](https://img.shields.io/github/repo-size/dandelionsprout/adfilt.svg)
[![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/RSS-knapp.png)](https://github.com/DandelionSprout/adfilt/commits/master.atom)

———————————————————————————

**IMPORTANT NOTE:** My lists do not, can not, and will never ever support Manifest v3, due to the lack of list hotfixes and its various syntax limitations. Issue reports for Manifest v3-based extension versions will **not** be accepted, and if you do submit one, you would be asked to use an alternate web browser instead.

And just in case anyone thinks I'm not serious about it, **I no longer offer support to Safari ≥13 users** (except when using AdGuard's paid version) since Safari has decided to do the exact same things that Chromium is planning to do.

———————————————————————————

Note for UXP browser users: Due to the Pale Moon community being protective of consistent abusive hate speech and grave insults, I will no longer use Pale Moon, Basilisk or Borealis to test any entries or for anything else. PC browser entries that can't be reproduced in Firefox, Vivaldi or Tor Browser, will be delegated to [uAssets](https://github.com/uBlockOrigin/uAssets/blob/master/filters/legacy.txt) instead.

———————————————————————————

**To subscribe to lists from this repo**, go to [FilterLists.com](https://filterlists.com/), click on the **Maintainers** button in the upper right, and choose **Imre Kristoffer Eilertsen** in the Maintainers dropdown menu. It is generally not recommended to subscribe to lists directly from this repo, as the mostly unsorted lists [can be unsuitable for your software(s)](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Pok%C3%A9monNoGOZone.txt), [block things you may not have intended to block at all](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/Twitter%20De-Politificator.txt), or [otherwise cause confusion in general](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/EkstraBladetEroticContentRemover.txt) if they aren't vetted properly before use on hardware.

———————————————————————————

This is the place where I, Imre Eilertsen, host my web filter lists for countless different topics, for use in adblock tools and the like. GitHub was in mid-2017 by far the easiest way for laymen like me to store pure text files, which is a necessity to create subscribable lists.

This is a hobby project of mine, in which I work just as much on these lists and this repo as I feel like. But don't be fooled by the appearance, as these are nevertheless some lists that I've placed lots of energy and effort into, for the enjoyment of all of us.

* [Official repo mirror](https://gitlab.com/DandelionSprout/adfilt)

However, if you were led here by extension teams or extension customer services, it was most likely due to **[Dandelion Sprout's Nordic Filters](https://github.com/DandelionSprout/adfilt/blob/master/NorwegianList.txt)**, my signature list for all up-to-date adblockers, whose userbase is very loosely estimated to measure in the low 6-digits. Various modified versions of it are included in uBlock Origin, AdGuard, AdNauseam, AdBlock, Adblock Plus, AdGuard Home, pfBlockerNG, Brave Browser, and Vivaldi's privacy settings.

## Contact details:

If you have any problems, suggestions, or the desire to help, I allow both _Issues_ and _Pull requests_ reports about any such things. Don't be shy to ask/tell me, but make sure to add screenshots and the lists that were used when testing. Reports will ''usually'' be initially looked into within 72 hours, but major delays can happen if I have health problems at the time. Reports on GitLab are allowed, but I have not yet tested how quickly I'd be able to notice them.

I advice against sending reports on E-mail. From 16 April 2025, E-mail reports will only be processed if a person is not actively using GitHub or GitLab in general once every 2 weeks or more often, and/or if the person is an official representant of a Nordic or German company with 20 or more employees. Clearcut failure to adhere to this will have the E-mails marked as spam.

Jeg forsikrer dere også om at det såklart er fullt mulig å kontakte meg om adblock-listene på bokmål, nynorsk, dansk eller svensk, dersom dette er ønskelig for deg/dere. Man er ikke nødt til å bruke engelsk hele tiden.

Jag anser mig själv att vara kompetent-ish på svenska, og klarer så vel at skrive på noget-til-højt forståeligt dansk.

![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/Spr%C3%A5kflagg%204.webp)

## The tools that I use:

• [Checker for redundant filter entries and for ABP syntaxes](https://abpvn.com/ruleChecker/redundantRuleChecker.html), made by Famlam. It does however not account for uBO-syntax-specific entries, nor for ABP syntaxes newer than 2017. <br>
• [Recentmost tool I've used to test IP server availability](https://github.com/funilrys/PyFunceble), made by [Funilrys](https://github.com/funilrys). <br>
• To easily create GitCDN links to the lists, in case anyone has list connection problems: [GitHub GitCDN Button](https://greasyfork.org/scripts/373361-github-gitcdn-button) by [mikhoul](https://greasyfork.org/users/3930-mikhoul) <br>
• To find very similar domains for Hosts files, or to find all domains hosted by specific IP addresses (both IPv4 and IPv6): [SecurityTrails](https://securitytrails.com/) <br>
• To look for invalidly written entries according to uBO's syntax: Use uBlock Origin, set logger to *All*, and resync the lists. <br>
• To correctly sort IP addresses (which Sublime Text cannot do): [Browserling IP Sort](https://www.browserling.com/tools/ip-sort)<br>
• To correctly sort IP addresses, and also compress them into CIDRs: [Tehnoblog IP Address Aggregator](https://tehnoblog.org/ip-tools/ip-address-aggregator/)<br>
• To find lists of the biggest newssites of most countries: [DomainTyper](https://domaintyper.com/top-websites/most-popular-websites-with-no-domain)<br>
• To search with wildcards for domains, e.g. `ads.*.no`: [SecurityTrails API Free](https://docs.securitytrails.com/reference#domain-search)<br>
• To sort lines by how frequently they occur: [Browserling Numeric Sort](https://www.browserling.com/tools/numeric-sort)

### Ways one can use [Sublime Text](https://www.sublimetext.com/) (made by Jon Skinner and Will Bond) to improve their filter lists:

• To sort filter entries in alphabetic order: F9 / Edit → Sort Lines <br>
• To remove `www.` from most entries: Ctrl+H / Find → Replace… <br>
• To remove duplicates: Edit → Permute Lines → Unique <br>
• To remove duplicates across files: Paste the content of the file that shall retain its filters on top, and paste the content of the file that shall delete its duplicates on bottom. <br>
• To remove element-rule targets from adblock files, so that the rules' domains can be run through PyFunceble: Ctrl+H / Find → Replace, turn on RegEx, and then replace `##.*` and `#?#.*` with nothing.

## Projects known to use my lists:

• [AdGuard](https://adguard.com/welcome.html) - Includes Dandelion Sprout's Nordic Filters, Dandelion Sprout's Serbo-Croatian Filter, Dandelion Sprout's Annoyances List, and Legitimate URL Shortener.<br>
• [AdGuard Home](https://github.com/AdguardTeam/AdGuardHome) - Includes Dandelion Sprout's Nordic Filters, Dandelion Sprout's Anti-Malware List, and Game Console Adblock List.<br>
• [uBlock Origin](https://github.com/gorhill/uBlock) and AdNauseam - Includes Dandelion Sprout's Nordic Filters and Dandelion Sprout's Serbo-Croatian Filter.<br>
• [Adblock Plus](https://adblockplus.org/), Brave Browser, AdBlock, pfBlockerNG, and Vivaldi - Includes various versions of Dandelion Sprout's Nordic Filters.<br>
• [OISD.nl](https://oisd.nl/) - Incorporates Dandelion Sprout's Nordic Filters and Dandelion Sprout's Anti-Malware List.<br>
• [1Hosts](https://github.com/badmojr/1Hosts), [T145's Black Mirror](https://github.com/T145/black-mirror) - Incorporates Dandelion Sprout's Anti-Malware List.<br>
• [Developer Dan](https://blocklist-tools.developerdan.com/blocklists), Bajins, [jgdye](https://git.ovalwonder.com/jgdye/samwiseetc/src/branch/master/pihole), [Molinero](https://hmirror.molinero.dev/) - Stores third-party mirrors of at least one of my lists.

Occasionally, [this link](https://www.google.no/search?q=%22if-a-large-hosts-file-contains-this-entry-then-it%22&filter=0) can be used to find additional projects. However, it is somewhat inaccurate, because most such projects remove non-live domains.

## Special thanks to:

• [lassekongo83](https://github.com/lassekongo83) for being a pretty solid expert on uBO's syntax, for helping heaps of people (Me included) with writing specific filters, and for having made several lists that I would look through to learn more about how to write filters. <br>
• The contributor communities that surround uBlock Origin in general (including [okiehsch](https://github.com/okiehsch) and [gwarser](https://github.com/gwarser) among others), for generally being helpful, reasonably debating, and for providing various solutions and advices. <br>
• [krystian3w](https://github.com/krystian3w) for teaching me that using `:style` entries completely breaks a list *and* its entries in ABP. <br>
• [okiehsch](https://github.com/okiehsch) (individually) for taking the time to oversee the copying of entries (Mostly from *[Browse Websites Without Logging In](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/BrowseWebsitesWithoutLoggingIn.txt)*) to *uBlock Filters - Annoyances*.<br>
• [Andrey Meshkov](https://github.com/ameshkov) for invaluable push-start assistance in creating [the conversion script](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/XYZPrepareFilters.py) for *Dandelion Sprouts nordiske filtre* that eventually became a very important backbone in my adblocker activities. <br>
• [HankAviator](https://github.com/HankAviator) for adding significant support for PR-Chinese websites in ≥3 of my lists. <br>
• [iam-py-test](https://github.com/iam-py-test) for being the day-to-day maintainer of Legitimate URL Shortener as of November 2021, and for contributing to several more of my lists.

If you've contributed to or helped me and you aren't on the above list, don't feel bad about it. I still give my regular thanks to you.
