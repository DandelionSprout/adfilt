## Anti-Pepe List
### Regular emotes (22th of January 2021)
`! ([a-z][a-zA-Z0-9]{1,})( .*)?$` → `! ——\1\2——\n!#if !env_mobile\nwww.twitch.tv##.emote-button__link[name=\1]\nwww.twitch.tv##button[data-tooltip-type=emote][data-name=\1]\n!#endif`
### Extension emotes (12th of February 2021)
`! ([a-zA-Z0-9]{1,})( .*)?$` → `! ——\1\2——\nwww.twitch.tv##button[data-tooltip-type=emote][data-name=\1]`

## Add `?` to `:-abp-` entries that lack them (18th of November 2021)
`([a-z])##([#.]?[a-z_].*:-abp-)` → `\1#?#\2`

## Anti-PPG List
### Standard (20th of February 2021; not in active use currently)
`! (.*)` → `artstation.com#?#.gallery-grid-item:-abp-contains(\1)\nknowyourmeme.com#?#.c.rel:-abp-contains(\1)\nosu.ppy.sh#?#.beatmapsets__item:-abp-contains(\1)\npinterest.*#?#div[class*=_brioPin]:-abp-contains(\1)\npixiv.net#?#div[data-gtm-recommend-zone=discovery] > div:-abp-has(> figure[style] > figcaption  > ul:-abp-contains(\1))\npixiv.net#?#.works-item:-abp-has(img[alt*="\1"])\npixiv.net#?#li:-abp-has(a[href*="/artworks/"] img[alt*="\1"])\nplay.google.com#?#div:-abp-has(> c-wiz[autoupdate]):-abp-has(a[href^="/store/"]):-abp-contains(\1)\nreddit.com#?#.Comment,.Post,.thing,.entry:-abp-contains(\1)\nrule34.xxx,gelbooru.com,booru.org,rule34.paheal.net,sankakucomplex.com,tbib.org,xbooru.com,rule34hentai.net,megabooru.com,hard55.com,zombooru.com,zumki.ru,kusubooru.com,tentaclerape.net,wh40kart.im#?#.thumb:-abp-has(img[title*="\1"])\ntumblr.com#?#.post:-abp-contains(\1)\ntwitch.tv#?#div[class$=message]:not(.tw-inline):-abp-contains(\1)\ntwitter.com#?#article:-abp-contains(\1)\nwww.youtube.com#?##dismissable:-abp-contains(\1)\nkonachan.com,yande.re,hypnohub.net,lolibooru.moe#?##post-list-posts > li:-abp-has(img[title*="\1"])\ne621.net,donmai.us,allthefallen.moe#?#article[data-tags*="\1"]\nm.youtube.com#?#.compact-media-item:-abp-contains(\1)\nyoutubekids.com#?#.ytk-item-section-renderer[id^=ytk-compact-video-renderer-],#related > ytk-compact-video-renderer:-abp-contains(\1)`
### For double-criteria conversions (20th of February 2021; not in active use currently)
`(.*) \+ (.*)` → `artstation.com#?#.gallery-grid-item:-abp-contains(\1):-abp-contains(\2)\nknowyourmeme.com#?#.c.rel:-abp-contains(\1):-abp-contains(\2)\nosu.ppy.sh#?#.beatmapsets__item:-abp-contains(\1):-abp-contains(\2)\npinterest.*#?#div[class*=_brioPin]:-abp-contains(\1):-abp-contains(\2)\npixiv.net#?#div:-abp-has(> figure[style] > figcaption:-abp-contains(\1):-abp-contains(\2))\npixiv.net#?#.works-item:-abp-has(img[alt*="\1"][alt*="\2"])\npixiv.net#?#li:-abp-has(a[href*="/artworks/"]:not([data-gtm-recommend-zone=discovery])):-abp-contains(\1):-abp-contains(\2)\nplay.google.com#?#div:-abp-has(> c-wiz[autoupdate]):-abp-has(a[href^="/store/"]):-abp-contains(\1):-abp-contains(\2)\nreddit.com#?#.Comment,.Post,.thing,.entry:-abp-contains(\1):-abp-contains(\2)\nrule34.xxx,e621.net,gelbooru.com,booru.org,rule34.paheal.net,sankakucomplex.com,tbib.org,xbooru.com,rule34hentai.net,megabooru.com,hard55.com,zombooru.com,zumki.ru,kusubooru.com,tentaclerape.net,wh40kart.im#?#.thumb:-abp-has(img[title*="\1"][title*="\2"])\ntumblr.com#?#.post:-abp-contains(\1):-abp-contains(\2)\ntwitch.tv#?#div[class$=message]:not(.tw-inline):-abp-contains(\1):-abp-contains(\2)\ntwitter.com#?#.tweet,.r-1j63xyz:-abp-contains(\1):-abp-contains(\2)\nyoutube.com#?##dismissable:-abp-contains(\1):-abp-contains(\2)`

## Various deviantART lists (12th of February 2023)
* `(.*)` → 
`deviantart.com##a[data-hook][href*="/art/"][href*=\1 i]\ndeviantart.com#?#div[style^="width:"][style*="display:"]:has(a[href*="/art/"][href*=\1 i])`
* `("\]\[href\*=)(/.*)/ i` → `\1"\2/"`
* `("\]\[href\*=)(/.*[a-zA-Z0-9-]) ` → `\1"\2" `
* `\ \+\ ` → `\ i][href*=`
