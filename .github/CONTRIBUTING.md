(Last updated: 25th of June 2020)

## Notes on how to contribute:

Issues and thoughts can be reported in the Issues tab. If you're reporting about a filter issue, you are expected to either explain the issue in deep detail, or to track down the problematic filter entry on your own. You're also encouraged to write:
* Which adblock lists are you using?
* Which adblock extension are you using?

Pull requests can be done, but they should permit me to be able to edit them, just in case there's some excusable formatting errors in your pull request.

I will normally do the utmost to resolve problems to the best of my ability, but I reserve the right to declare a case to be closed if there's too much back and forth with no end in sight. And especially if the reporter isn't even using the list that (s)he is trying to make changes to.

Issues and problems will normally be tested for in the most recent stable version of Nano Adblocker. In rare cases where the problems are only visible in other extensions, I would also test with uBlock Origin, Adblock Plus, AdGuard (chiefly the paid Windows version), AdBlock, AdGuard Home, Blokada, and/or the Windows system hosts file. For a list of supported, unsupported, and recommended adblockers, [read this](https://github.com/DandelionSprout/adfilt/blob/master/Wiki/Supported%20adblockers%20and%20tools.md).

### Nordic list submissions

When making a submission pull request to the Nordic list, make sure to do the edits to either:
* [The uBlock Origin version](https://github.com/DandelionSprout/adfilt/blob/master/NorwegianList.txt) (for the uBO, AdGuard, Adblock Plus, Adblock Plus Eyeo, Privoxy, TPL, and uBO+privacy versions).
* [The file for anti-anti-adblock entries](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/AntiAdblockEntries.txt).
* [The domains version](https://github.com/DandelionSprout/adfilt/blob/master/NorwegianExperimentalList%20alternate%20versions/DandelionSproutsNorskeFiltreDomains.txt) (for all other versions).

All other versions are generated from those two files.

### Communication languages

All communication and contribution that is permitted above, can also be done in Bokmål, Nynorsk, Swedish and Danish. In those cases, I would take contact with you in Bokmål, unless otherwise is requested.

### Low-priority websites

I will refuse to write, double-check or fix entries for the following sites, and any suggested entries for them will be added verbatim:
* Any websites listed in [Remover for Mainstream Tabloid and Alt-Right Sites](https://github.com/DandelionSprout/adfilt/blob/master/TabloidRemover.txt)
* Any websites listed in [Anti-'Insane religious preachers' List](https://github.com/DandelionSprout/adfilt/blob/master/AntiPreacherList.txt)
* Any websites listed in [Anti-FiM List](https://github.com/DandelionSprout/adfilt/blob/master/Other%20domains%20versions/AntiF%25D1%2596%25D0%259C%2520ListDomains.txt)
* Any websites listed in [Anti-'Steven Universe' List](https://github.com/DandelionSprout/adfilt/blob/master/Other%20domains%20versions/AntiStevenUniverseListDomains.txt)
* Any websites listed in [Anti-'Hivemind cartoon trashing' List](https://github.com/DandelionSprout/adfilt/blob/master/Other%20domains%20versions/AntiHivemindCartoonTrashingListDomains.txt)
* deviantART
* Inkbunny
* LatexStories.net
* answers.microsoft.com
* Any imageboards of any variety whatsoever

Additionally, I'll only write and test fixes for these sites and not brand new entries:
* The Verge

### Other

Should I have missed out on any details that'd be nice to have in this contribution explanation, give me a heads up about it, e.g. in Issues.

I do encourage forking, both for experimentation, archiving, or for any other reason you may come up with.
