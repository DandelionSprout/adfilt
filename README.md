# adfilt

This is the place where I, Imre Kristoffer Eilertsen, host my web filter lists, for use in adblock tools and the likes. Github was by far the easiest way for laymen like me to store pure TXT files, which I thought was a necessity to share my filter lists across multiple units.

• ExperimentalNorwegianList.txt is a Norwegian-focused adblock list intended for public consumption. If you've been directed here by uBlock Origin or by Adblock Plus, then this is the list you're using.

• Staying On The Phone Browser was created as a proof of concept, and for the benefit of people who really like their phone's web browsers and who are less keen on using various apps.

• NorwegianExtensionsForUBOandNano.txt was created, following a good piece of advice that various adblockers now allow lists to embed other lists into them, for the purpose of preventing uBlock Origin-formatted entries from bothering Adblock Plus users who wouldn't be able to use them. It is not recommended to sub to this list separately, since it already is a part of ExperimentalNorwegianList.txt per se for whom it is concerned.

• a.txt is intended as an archive of my personal private filters, stored on GitHub in such a way that I can share them between my browsers and E-mail clients. It is __NOT__ intended for public consumption, because it includes hundreds of filters that remove everything I don't like online, which includes filters that remove features that are liked by 95% of all other humans on the planet.

## I hereby request help with:

• Discovering filters that I may have missed, especially on websites that I refuse to visit due to personal tastes (e.g. far-right "newssites", or conspiracist mouthpiece blogs).

• Telling me that you're using those lists, through taking a quick ~4-question survey in Norwegian (https://dandelionsprout.polldaddy.com/s/adfilt-brukerundersøkelse), and/or by giving this repository a ꙨWatch and/or ★Star.

• Generating versions of ExperimentalNorwegianList.txt for the following formats: .tpl (_Tracking Protection List_ format, for Internet Explorer 9-11), WebKit (iOS), hosts files (Routers and local computer tools), and Privoxy (HTTP filtering, from what I can determine).

• Testing box-removal filters on widescreen monitors, since I almost always test my filters on a 9:16 portrait monitor.

• Telling me if ExperimentalNorwegianList.txt remove things that in fact shouldn't be removed (e.g. Non-sponsored articles, entire pages, etc.). Bonus points if you know which filter entry it was that caused the problem.

I allow both _Issues_ and _Pull requests_ reports about any of the above, for the time being. Don't be shy to ask/tell me.

Jeg forsikrer dere også om at det såklart er fullt mulig å kontakte meg om adblock-listen på norsk bokmål, norsk nynorsk, dansk eller svensk, dersom dette er ønskelig for deg/dere.

## The tools that I use:

• Checker for redundant/duplicate filter entries, made by Famlam: https://arestwo.org/famlam/redundantRuleChecker.html

Ways one can use Sublime Text to improve his/her filter lists (https://www.sublimetext.com/):

• To sort filter entries in alphabetic order: F9 / Edit → Sort Lines

• To remove "www." from most entries: Ctrl+H / Find → Replace…

• To remove duplicates: Edit → Permute Lines → Unique

• To remove duplicates across files: Paste the content of the file that shall retain its filters on top, and paste the content of the file that shall delete its duplicates on bottom.
