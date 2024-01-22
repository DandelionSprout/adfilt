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

### Trials to put said obfuscations into structural use (Note: Currently also matches square brackets as false positives. MUST be case-sensitive.)
* `(\(/.*)([a-zA-Z])\2([a-zA-Z0-9|/-])` → `\1\2{2}\3`
* `(\(/.*[a-zA-Z0-9 ?}-])([ijmoyEFIJMOTY])([a-zA-Z0-9 |/\\-].*:not)` → `\1\\\2\3`
* `(\(/.*[a-zA-Z0-9 ?}-])([ijmyEFIJMOTY])([a-zA-Z0-9 |{}/\\-].*/i?\))` → `\1\\\2\3`
* `(:has-text\(/[/\\a-zA-Z0-9{}()?|.*#]{1,}) (.*/i?\))` → `\1\\s\2`

#### Similar obfuscation to replace spaces with "\s". (Can be case-insensitive)
* `(:has-text\(/([a-zæøåäöA-Z0-9е{}()|^$.,*'&’-]|\\|\?){0,}) (([a-zæøåäöA-Z0-9е{}()|^$.,*'&’ -]|\\|\?){0,}/i?\))` → `\1\\s\3`

## Convert `#?#*:has(` to `##*:has(` due to new browser (and ABP) guidelines
`^([a-z0-9*,.-]{0,})#\?#((([a-zA-Z0-9.#_*="_+>~/\^ -]|\[|\]|:"){0,}):has\(([_=."+#a-zA-Z0-9~>%&/$',;?^!*一-龯ぁ-んァ-ン・ーㄱ-힣æøåÆØÅäöÄÖ() -]|\[|\]|://){1,}\))$`
↓
`\1##\2`
