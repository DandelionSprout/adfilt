# adfilt

![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/Adfilt%20logo%202.png)

This is the place where I, Imre Kristoffer Eilertsen, host my web filter lists, for use in adblock tools and the likes. Github was by far the easiest way for laymen like me to store pure TXT files, which I thought was a necessity to share my filter lists across multiple units.

• _ExperimentalNorwegianList.txt_ is a Norwegian-focused adblock list intended for public consumption. If you've been directed here by uBlock Origin or by Adblock Plus, then this is the list you're using. The list is natively available in uBlock Origin (from v1.15.11 onwards), Adblock Plus' secondary [subscriptions](https://adblockplus.org/subscriptions) list, and from [FilterLists.com](https://filterlists.com/). It can also be added through pasting [its raw address](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/ExperimentalNorwegianList.txt) into your adblocker's custom URL section.

Alternate but amputated and untested versions now exist for iOS (.json), Internet Explorer (.tpl), and a misformatted hosts file that nonetheless seems to be fully supported by uBlock Origin's hosts-file support. Help with testing their usefulness and installation process would've come in handy, especially if people want to use those versions.

• _Staying On The Phone Browser_ was created as a proof of concept, and for the benefit of people who really like their phone's web browsers and who are less keen on using various apps. [Raw link](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/stayingonbrowser/Staying%20On%20The%20Phone%20Browser).

• _List for Chrome Personal Blocklist_ is designed for users of [Personal Blocklist](https://chrome.google.com/webstore/detail/personal-blocklist-by-goo/nolijncfnkgaikbjbdaogikpmpbdcdef), and potentially also for similar search result filter tools as well. Due to its buffet nature, in which it merely suggests which URLs you can paste into the extension's import function, I don't currently accept issue reports about adding URLs to it for the time being, but would be very happy to be told about other search result filter tools for other engines/browsers, so that I can learn about them, as well as bug reports.

• _NorwegianExtensionsForUBOandNano.txt_ was created, following a good piece of advice that various adblockers now allow lists to embed other lists into them, for the purpose of preventing uBlock Origin-formatted entries from bothering Adblock Plus users who wouldn't be able to use them. It is not recommended to sub to this list separately, since it already is a part of ExperimentalNorwegianList.txt per se for whom it is concerned.

• _a.txt_ is intended as an archive of my personal private filters, stored on GitHub in such a way that I can share them between my browsers and E-mail clients. It is __NOT__ intended for public consumption, because it includes hundreds of filters that remove everything I don't like online, which includes filters that remove features that are liked by 95% of all other humans on the planet.

## I hereby request help with:

• Discovering filters that I may have missed, especially on websites that I refuse to visit due to personal tastes (e.g. far-right "newssites", clothes-"selling" scam shops, conspiracist mouthpiece blogs, and so on).

• Telling me that you're using those lists, through taking a quick ~4-question survey in Norwegian (https://dandelionsprout.polldaddy.com/s/adfilt-brukerundersøkelse), and/or by giving this repository a ꙨWatch and/or ★Star.

• Generating and/or testing versions of ExperimentalNorwegianList.txt for the following formats: .tpl (_Tracking Protection List_ format, for Internet Explorer 9-11), WebKit (iOS), hosts files (Routers and local computer tools), and Privoxy (HTTP filtering, from what I can determine).

• Testing box-removal filters on widescreen monitors, since I almost always test my filters on a 9:16 portrait monitor.

• Telling me if ExperimentalNorwegianList.txt remove things that in fact shouldn't be removed (e.g. Non-sponsored articles, entire pages, etc.). Bonus points if you know which filter entry it was that caused the problem.

I allow both _Issues_ and _Pull requests_ reports about any of the above, for the time being. Don't be shy to ask/tell me.

Jeg forsikrer dere også om at det såklart er fullt mulig å kontakte meg om adblock-listen på norsk bokmål, norsk nynorsk, dansk eller svensk, dersom dette er ønskelig for deg/dere.

![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/Spr%C3%A5kflagg.png)

## The tools that I use:

• Checker for redundant/duplicate filter entries, made by Famlam: https://arestwo.org/famlam/redundantRuleChecker.html

• Tool I used to create a JSON file for WebKit, made by the Adblock Plus developers: https://github.com/adblockplus/abp2blocklist

• Recentmost tool I used to test IP server availability, made by Funilrys: https://github.com/funilrys/funceble (I previously used the _Find dead, redirected and/or parked domains_ tool at https://arestwo.org/famlam/redundantRuleChecker.html to great effect, but it had a ludicrously long and hardcoded 120sec waiting time before it'd label domains as dead).

Ways one can use Sublime Text to improve his/her filter lists (https://www.sublimetext.com/):

• To sort filter entries in alphabetic order: F9 / Edit → Sort Lines

• To remove "www." from most entries: Ctrl+H / Find → Replace…

• To remove duplicates: Edit → Permute Lines → Unique

• To remove duplicates across files: Paste the content of the file that shall retain its filters on top, and paste the content of the file that shall delete its duplicates on bottom.
