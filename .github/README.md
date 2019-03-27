![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/Adfilt%20logo%202.png)<br>
[![licence](https://img.shields.io/badge/Licence-Custom%20open%20source%20licence%20based%20on%20BSD3-green.svg)](https://github.com/DandelionSprout/adfilt/blob/master/LICENSE.md)
![GitHub repo size in bytes](https://img.shields.io/github/repo-size/dandelionsprout/adfilt.svg)
[![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/Flattr%20button.png)](https://flattr.com/@DandelionSprout)
[![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/RSS-knapp.png)](https://github.com/DandelionSprout/adfilt/commits/master.atom)

This is the place where I, Imre Kristoffer Eilertsen, host my web filter lists, for use in adblock tools and the likes. GitHub was by far the easiest way for laymen like me to store pure TXT files, which I thought was a necessity to share my filter lists across multiple units.

This is a hobby project of mine, in which I work just as much on these lists and this repo as I feel like. But don't be fooled by the appearance, as these are nevertheless some lists that I've placed considerable energy and effort into, for your enjoyment.

* [Official repo mirror](https://repo.or.cz/FilterMirrorRepo.git/tree/refs/heads/master) (A GitLab mirror also exists, but it currently has branch sync problems.)
* [Official donation links](https://sproutsluckycorner.wordpress.com/2017/11/14/my-work-and-contact-resume/#donations)

For a basic overview of the lists in this repo, go to [FilterLists.com](https://filterlists.com/), click on the Maintainers button in the bottom right, and choose Imre Kristoffer Eilertsen in the Maintainers dropdown menu. It proved to be too much work for me to maintain a GitHub spreadsheet for my lists, unfortunately.

However, if you were led here by uBlock Origin, AdGuard, AdBlock, or [Adblock Plus' secondary subscription page](https://adblockplus.org/en/subscriptions), it was most likely due to **[Dandelion Sprout's Nordic Filters](https://github.com/DandelionSprout/adfilt/blob/master/NorwegianList.txt)**, my signature list for all up-to-date adblockers, whose userbase is very loosely estimated to measure in the low 6-digits.

## I hereby request help from other people with:

• Discovering filters that I may have missed, especially on websites that I refuse to visit due to personal tastes (e.g. far-right "newssites", clothes-"selling" scam shops, conspiracist mouthpiece blogs, and so on). <br>
• Telling me that you're using those lists, through taking [a quick user survey](https://docs.google.com/forms/d/e/1FAIpQLSc7DB9MKrUTbF4znDQ7LKdy4EpSciL6ooh5ru-HUZkdGxmpKg/viewform) on Google Forms, and/or by giving this repository a ꙨWatch and/or ★Star. <br>
• Testing out lists that are marked as _Beta_, and double-checking the syntaxes of and testing the lists that are marked as _Alpha_. <br>
• Testing box-removal filters on widescreen monitors, since I almost always test my filters on a 9:16 portrait monitor. <br>
• Telling me if the national lists remove things that in fact shouldn't be removed (e.g. Non-sponsored articles, entire pages, etc.). Bonus points if you know which filter entry it was that caused the problem. <br>
• Showing your support for wildcard domains in element rules when using Adblock Plus, such as in [this issue tracker thread](https://issues.adblockplus.org/ticket/6773).

I allow both _Issues_ and _Pull requests_ reports about any of the above, for the time being. Don't be shy to ask/tell me.

Jeg forsikrer dere også om at det såklart er fullt mulig å kontakte meg om adblock-listen på bokmål, nynorsk, dansk eller svensk, dersom dette er ønskelig for deg/dere.

![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/Spr%C3%A5kflagg2.png)

## The tools that I use:

• [Checker for redundant filter entries and for ABP syntaxes](https://arestwo.org/famlam/redundantRuleChecker.html), made by Famlam. It does however not account for uBO-syntax-specific entries. ([Alternate link](https://web.archive.org/web/20171209102004/https://arestwo.org/famlam/redundantRuleChecker.html)) <br>
• [Recentmost tool I used to test IP server availability](https://github.com/funilrys/PyFunceble), made by [Funilrys](https://github.com/funilrys).  (I previously used the _Find dead, redirected and/or parked domains_ tool at https://arestwo.org/famlam/redundantRuleChecker.html to great effect, but it had a ludicrously long and hardcoded 120sec waiting time before it'd label domains as dead). <br>
• To create direct addition links that can be linked to on GitHub, I don't use _abp:subscribe_ in the URLs, but instead _subscribe.adblockplus.org_, which works the same way if the addition link has been correctly constructed. <br>
• To easily create GitCDN links to the lists, in case anyone have list connection problems: [GitHub GitCDN Button](https://greasyfork.org/nb/scripts/373361-github-gitcdn-button) by [mikhoul](https://greasyfork.org/users/3930-mikhoul)

### Ways one can use [Sublime Text](https://www.sublimetext.com/) (made by Jon Skinner and Will Bond) to improve his/her filter lists:

• To sort filter entries in alphabetic order: F9 / Edit → Sort Lines <br>
• To remove "www." from most entries: Ctrl+H / Find → Replace… <br>
• To remove duplicates: Edit → Permute Lines → Unique <br>
• To remove duplicates across files: Paste the content of the file that shall retain its filters on top, and paste the content of the file that shall delete its duplicates on bottom. <br>

## Special thanks to:

• [gorhill](https://github.com/gorhill), [Collin Barrett](https://github.com/collinbarrett), the [AdGuard team](https://github.com/AdguardTeam), and the [AdBlock team](https://getadblock.com/contributors/), for having included at least one of my lists into uBlock Origin, Filterlists, AdGuard, and AdBlock respectively. <br>
• [lassekongo83](https://github.com/lassekongo83) for being the best filter writer on planet Earth, for helping heaps of people (Me included) with writing specific filters, and for having made several lists that I often look through to learn more about how to write filters. <br>
• [THEtomaso](https://github.com/THEtomaso) for waterproofing parts of the Nordic list, and for several contributions to the same list. <br>
• The contributor communities that surround uBlock Origin and Nano Adblocker in general (including [okieshsch](https://github.com/okiehsch) and [gwarser](https://github.com/gwarser)), for generally being helpful, reasonably debating, and for providing various solutions and advices. <br>
• [krystian3w](https://github.com/krystian3w) for teaching me that using `:style` entries completely breaks a list *and* its entries in ABP.
• [okiehsch](https://github.com/okiehsch) (individually) for taking the time to oversee the copying of entries (Mostly from *Browse Websites Without Logging In*) to *uBlock Filters - Annoyances*.

If you've contributed to or helped me and you aren't on the above list, don't feel bad about it. I still give my regular thanks to you.
