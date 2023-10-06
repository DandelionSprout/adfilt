## Anti-Pepe List
### Regular emotes (22th of January 2021)
`! ([a-z][a-zA-Z0-9]{1,})( .*)?$` → `! ——\1\2——\n!#if !env_mobile\nwww.twitch.tv##.emote-button__link[name=\1]\nwww.twitch.tv##button[data-tooltip-type=emote][data-name=\1]\n!#endif`
### Extension emotes (12th of February 2021)
`! ([a-zA-Z0-9]{1,})( .*)?$` → `! ——\1\2——\nwww.twitch.tv##button[data-tooltip-type=emote][data-name=\1]`

## Add `?` to `:-abp-` entries that lack them (18th of November 2021)
`([a-z])##([#.]?[a-z_].*:-abp-)` → `\1#?#\2`

## Various deviantART lists (12th of February 2023)
* `(.*)` → 
`deviantart.com##a[data-hook][href*="/art/"][href*=\1 i]\ndeviantart.com#?#div[style^="width:"][style*="display:"]:has(a[href*="/art/"][href*=\1 i])`
* `("\]\[href\*=)(/.*)/ i` → `\1"\2/"`
* `("\]\[href\*=)(/.*[a-zA-Z0-9-]) ` → `\1"\2" `
* `\ \+\ ` → `\ i][href*=`

## Letters suited for backslash obfuscation when using RegEx
According to Sublime Text build 4143. Case-sensitive.
* i, j, m, o, y, E, F, I, J, M, O, T, Y
