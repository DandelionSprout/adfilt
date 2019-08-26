![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/Adfilt%20logo%202.png)<br>
![GitHub repo size in bytes](https://img.shields.io/github/repo-size/dandelionsprout/adfilt.svg)
[![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/Flattr%20button.png)](https://flattr.com/@DandelionSprout)
[![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/RSS-knapp.png)](https://github.com/DandelionSprout/adfilt/commits/master.atom)

————————————————————————————

<b>IMPORTANT NOTE FOR CHROMIUM-BROWSER USERS:</b> My lists does not, can not, and will never ever support Manifest v3, due to its laughably short rule limit and the removal of `-abp-has` and `-abp-contains`. Issue reports for Manifest v3-based extension versions will not be accepted, and if you do submit one, you would be asked to use an alternate web browser or web browser version instead.

————————————————————————————

This is the place where I, Imre Kristoffer Eilertsen, host my web filter lists, for use in adblock tools and the likes. GitHub was in mid-2017 by far the easiest way for laymen like me to store pure text files, which is a necessity to create subscribable lists.

This is a hobby project of mine, in which I work just as much on these lists and this repo as I feel like. But don't be fooled by the appearance, as these are nevertheless some lists that I've placed considerable energy and effort into, for the enjoyment of all of us.

* [Official repo mirror](https://repo.or.cz/FilterMirrorRepo.git/tree/refs/heads/master)
* [Secondary official repo mirror](https://gitlab.com/DandelionSprout/adfilt)
* [Official donation links](https://sproutsluckycorner.wordpress.com/2017/11/14/my-work-and-contact-resume/#donations)

For a basic overview of the lists in this repo, go to [FilterLists.com](https://filterlists.com/), click on the Maintainers button in the bottom right, and choose Imre Kristoffer Eilertsen in the Maintainers dropdown menu. It proved to be too much work for me to maintain a GitHub spreadsheet for my lists, unfortunately.

However, if you were led here by uBlock Origin, AdGuard, AdBlock, or [Adblock Plus' secondary subscription page](https://adblockplus.org/en/subscriptions), it was most likely due to **[Dandelion Sprout's Nordic Filters](https://github.com/DandelionSprout/adfilt/blob/master/NorwegianList.txt)**, my signature list for all up-to-date adblockers, whose userbase is very loosely estimated to measure in the low 6-digits.

If you have any problems, suggestions, or a desire to help, I allow both _Issues_ and _Pull requests_ reports about any such things for the time being. Don't be shy to ask/tell me. In particular, I have a [wishlist of things](https://github.com/DandelionSprout/adfilt/issues/new?assignees=&labels=I+wish+to+help&template=forms-for-those-who-wish-to-help-me-write-lists.md&title=I+wish+to+help) that I wish for assistance from others with.

Jeg forsikrer dere også om at det såklart er fullt mulig å kontakte meg om adblock-listene på bokmål, nynorsk, dansk eller svensk, dersom dette er ønskelig for deg/dere. Man er ikke nødt til å bruke engelsk hele tiden.

![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/Spr%C3%A5kflagg3.png)

## The tools that I use:

• [Checker for redundant filter entries and for ABP syntaxes](https://arestwo.org/famlam/redundantRuleChecker.html), made by Famlam. It does however not account for uBO-syntax-specific entries, nor for ABP syntaxes newer than 2017. ([Alternate link](https://web.archive.org/web/20171209102004/https://arestwo.org/famlam/redundantRuleChecker.html)) <br>
• [Recentmost tool I used to test IP server availability](https://github.com/funilrys/PyFunceble), made by [Funilrys](https://github.com/funilrys). (I previously used the _Find dead, redirected and/or parked domains_ tool at https://arestwo.org/famlam/redundantRuleChecker.html to great effect, but it had a ludicrously long and hardcoded 120sec waiting time before it'd label domains as dead). <br>
• To create direct addition links that can be linked to on GitHub, I don't use _abp:subscribe_ in the URLs, but instead _subscribe.adblockplus.org_, which works the same way if the addition link has been correctly constructed. <br>
• To easily create GitCDN links to the lists, in case anyone have list connection problems: [GitHub GitCDN Button](https://greasyfork.org/scripts/373361-github-gitcdn-button) by [mikhoul](https://greasyfork.org/users/3930-mikhoul)

### Ways one can use [Sublime Text](https://www.sublimetext.com/) (made by Jon Skinner and Will Bond) to improve his/her filter lists:

• To sort filter entries in alphabetic order: F9 / Edit → Sort Lines <br>
• To remove "www." from most entries: Ctrl+H / Find → Replace… <br>
• To remove duplicates: Edit → Permute Lines → Unique <br>
• To remove duplicates across files: Paste the content of the file that shall retain its filters on top, and paste the content of the file that shall delete its duplicates on bottom. <br>
• To remove element-rule targets from adblock files, so that the rules' domains can be run through PyFunceble: Ctrl+H / Find → Replace, turn on RegEx, and then replace `##.*` and `#?#.*` with nothing.

## Special thanks to:

• [lassekongo83](https://github.com/lassekongo83) for being the best filter writer on planet Earth, for helping heaps of people (Me included) with writing specific filters, and for having made several lists that I often look through to learn more about how to write filters. <br>
• [THEtomaso](https://github.com/THEtomaso) for waterproofing parts of the Nordic list, and for several contributions to the same list. <br>
• The contributor communities that surround uBlock Origin and Nano Adblocker in general (including [okiehsch](https://github.com/okiehsch) and [gwarser](https://github.com/gwarser) among others), for generally being helpful, reasonably debating, and for providing various solutions and advices. <br>
• [krystian3w](https://github.com/krystian3w) for teaching me that using `:style` entries completely breaks a list *and* its entries in ABP. <br>
• [okiehsch](https://github.com/okiehsch) (individually) for taking the time to oversee the copying of entries (Mostly from *[Browse Websites Without Logging In](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/BrowseWebsitesWithoutLoggingIn.txt)*) to *uBlock Filters - Annoyances*.<br>
• [Andrey Meshkov](https://github.com/ameshkov) for invaluable push-start assistance in creating [the conversion script](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/nordic_prepare_filters.py) for *Dandelion Sprouts nordiske filtre* into AdGuard-, AdBlock-, and TPL-specific list versions.

If you've contributed to or helped me and you aren't on the above list, don't feel bad about it. I still give my regular thanks to you.
