### All up-to-date significant adblockers¹

#### Element removal (a.k.a. cosmetic rules, a.k.a. hiding rules, a.k.a. ##-rules)
* `##.`: Hides parts of a page, based on one or more `class` values in the F12 filetree (separated with full-stops).
* `##`: Hides parts of a page based on the element type, e.g. `a`, `li`, `button`, `iframe`, etc., usually highlighted in purple in the F12 filetree.
* `###`: Hides parts of a page based on the `id` value.
* `#@#.`/`#@#`/`#@##`: Whitelists parts of a page to make them load.
* `[href="text"]`: Finds page elements whose values in the F12 filetree console contains such a value. The value can be `href`, `id`, `class`, `type`, or numerous other things. Does not support RegEx.
* `[href^="text"]`: Finds page elements whose value *begins* with the text.
* `[href$="text"]`: Finds page elements whose value *ends* with the text.
* `[href*="text"]`: Finds page elements whose value contains the text anywhere within it.
* `[href="text" i]`: Save as above, except case-insensitive.
* `:not(.element)`: Finds page elements that doesn't contain a specified element or text string. Can be paired with other syntaxes à la `:not(:-abp-contains(Example text))`.
* `:-abp-contains(text)`: Finds page elements that contains such text within it.
* `:-abp-has(.element)`: Finds page elements that contains such an element within it.
* `:nth-of-type(n)` / `:nth-last-of-type(n)`: Finds page elements that are at a specific numerical position in a set. Note that `:nth-last-of-type(n)`'s numbering goes in reverse order.
* `:only-of-type` / `first-of-type` / `:last-of-type`: Less versatile versions of the above, for which numbers can't be chosen.
* `:first-child` / `:last-child`: Appears to be synonymous with `first-of-type` and `last-of-type` for adblocking purposes.
* `:before` / `:after`: Removes the pseudo-elements that belong to a page element.
* `>`: Creates chain criteria, in which a selected page element must have a specific element on the floor above it in the filetree.
* `+`: Blocks the element that is right below the criteria in the filetree. Example: `##.element + div` blocks that particular `div`.
* `~`, as in `##.element ~ div`: Similar to `+`, but blocks *all* such elements that are below it on the same floor in the filetree, and not just the one right below.
* Spacing between elements, e.g. `##.element .element`: Similar to `>`, but can mean *any* number of floors between the elements, and not just those that are one floor apart.

##### Advanced examples:
* The first two `##` of an element entry, are not used for elements written after e.g. `>`, `+` or `:-abp-has`. In those cases, the `##` in `##element` gets removed, `##.class` becomes `.class`, and `###id` becomes `#id`.
* `##element.element2`: Hide something both based on its element (##element1) and `class` value (.element2). Note the placement/absence of fullstops.
* While they're based on the same `class` values, `##.element1` will match any `class` (sub-)value, whereas `##div[class="element1"]` and their modifiers are based on the *entire* `class` string in the F12 filetree.
* `##.` / `##` / `###` entries can either be *generic*, in which they have no domains in front of them; or (domain-)specific, where they have one or more domains in front of them, separated by commas. Only Nano and uBO support wildcard asterisks (`*`) in such domains, while other adblockers do not.
* In `$domain=` below, top-level domains can be added through e.g. `$domain=tk` and `$domain=~tk`. No other types of wildcardings are supported by `$domain=`.

#### File blocking (a.k.a. blocking rules, a.k.a. non-#-rules)
* `||`: Blocks resources from domains or parts thereof from being loaded. For non-domain-specific resources, no pre-emption is needed at all.
* `@@`: Whitelists resources from specific URLs to make them load.
* `^`: Wildcard for anything that isn't alphanumerical or "_-.%" . Often used to cover both slash ( / ) and non-slash domain name endings at the same time.
* `$third-party`: Ensures that resources from a domain are only blocked if you're not visiting the domain itself.
* `$~third-party`: Ensures that resources from a domain are only blocked if you're visiting the domain itself.
* `$domain=`: Ensures that resources from a domain are only blocked if you're visiting a specified website. Multiple domains are separated with `|` (Vertical line) and not commas.
* `@@||` + `$generichide`: Prevents all non-domain-specific (a.k.a. generic) hiding entries from working on a website. On Nano/uBO it prevents *all* non-domain-specific entries from working.
* `@@||` + `$specifichide`: Prevents all domain-specific hiding entries from working on a website. On Nano/uBO it seems to prevent *all* domain-specific entries from working.
* `@@||` + `$elemhide`: Combines `$generichide` and `$specifichide`. Also completely breaks the element picker in Nano/uBO on that site as of the 14th of December 2019.
* `$script`: Blocks resources from domains or parts thereof from being loaded, but only if it's a script, e.g. a JavaScript runtime.
* `$csp`: Inserts additional *Content Security Policies* into the page.
* `$xmlhttprequest` / `$websocket`: Prevents such resources from being downloaded through the titular JavaScript APIs.
* `$popup` / `$image` / `$object` / `$font` / `$other`: These ones should hopefully be self-explanatory (Give me a heads-up in an issue report if it isn't).
* `|text`: Matches URLs that *begin* with the text.
* `text|`: Matches URLs that *end* with the text.
* `~`: Means that an entry does *not* apply to a specific domain.

#### Universal
* `! ` / `# `: Marks the start of a comment that shall not be interpreted as an entry.
* `/\/\/\/`, `/regextext/`, and similar: Text detections in RegEx format. Supported in most (if not all) blocking rules, as well as in `:-abp-contains` and `:has-text`. Note that *all* blocking rules that start and end with `/` are treated as RegEx; a workaround is to add a `*` before or after.
* `[Adblock Plus n.n]`: Mandatory for Adblock Plus, AdBlock, and forks of them, as they use the tag to determine if they should load the filterlist. Number is the intended minimum ABP version. `2.0` and `1.1` are most common; `3.1` and higher is on the rise and can be used to block support for old or low-quality forks. This has no effect on uBO or its forks. Tags like `[uBlock Origin 1.20.0]` are just for clarification of intent, and have no effect on anything whatsoever.
* `! Title:` Specifies the intended name of the list. Required to make the name automatically show up in the settings of most adblockers, instead of the URL or of manual text input.
* `! Version:` The version number/alphanumeric of the list. Unofficially used to distinguish which version of a list a user is using. Used administratively by Adblock Plus' list report system (which requires a number-only version value). Many lists choose to use `! Last modified` as well or instead.
* `! Expires:`: Determines the timespan between each automated sync attempt with the list's source. Values are given in "n day/days". ABP also supports "hour/hours".

### Nano Adblocker, uBlock Origin, Adblock Plus and AdBlock only:
* `:scope`: Used alongside `:-abp-has` to make it only find elements whose criteria match their immediate subelements.

### Nano Adblocker, uBlock Origin and AdGuard only:
#### Hiding
* `:style`: Changes the CSS values of an element, in much the same way as what userstyle extensions like Stylish would've done.
* `{ }`: Same as above.
* `:has-text`: Same as `:-abp-contains`.
* `:has`: Same as `:-abp-has`.
* `!#if`: Specifies that a section of entries only applies to specific platforms or extensions. Closed out by `!#endif`.
* `:matches-css`: Looks for page elements whose existing native (i.e. non-inherited) CSS values match those of the criteria.
* `:matches-css-before`: Same as above, but looks for CSS values in its pseudo-elements instead.
#### Blocking
* `$badfilter`: Deactivates a resource-blocking entry, even if it is present in another list.
* `$important`: Makes a resource-blocking entry take precedence over another whitelisting entry.
* `$redirect`: Redirects resources to a neutered version that has been embedded in those extensions. Possible options are listed in [this file](https://github.com/gorhill/uBlock/blob/master/src/js/redirect-engine.js) (AdGuard has a [slightly smaller selection](https://github.com/AdguardTeam/AdguardBrowserExtension/blob/master/Extension/lib/filter/rules/scriptlets/redirects.yml)).
* `$empty`: Results in a fake empty page being loaded, instead of an error page.

### Nano Adblocker and uBlock Origin only:
#### Hiding
* `!#include`: Embeds another filterlist that is hosted on the same domain (with a whole lot of restrictions). Despite AdGuard's claim that they also support it, their support only applies to lists that are natively included in AdGuard.
* `##+js` (prev. `##script:inject`): Invokes a script that is embedded in those extensions, and usually using the script to modify a value on the site. Possible options are listed in [this file](https://github.com/gorhill/uBlock/blob/master/assets/resources/scriptlets.js) (The top strings of each paragraph). Nano has a select few additional scripts.
* `:xpath`: An entry written with the very advanced Xpath syntax.
* `##^.element`: Blocks page elements before they've even been loaded, based on their values in *View source* instead of their F12 ones. **Only** works in Firefox.
* `##^script:has-text` (prev. `##script:contains`): Intends to prevent inline scripts from starting up, based on the content of the scripts in the F12 filetree. Also only works in Firefox.
* `:upward` (prev. `:nth-ancestor`): Looks for elements that are a certain amount of indentations (i.e. filetree floors) above the criteria in the F12 filetree. Equivalent to `:xpath(../..)`, but with normal numbers. The ability to look for specific element names at *any* indentation amount, is being tested in uBO beta versions.
* `:min-text-length`: Appears to select elements whose underlying source content has at least that amount of characters. Is completely disassociated from the actual on-page visible text by an order of several magnitudes.
* `:watch-attr`: Claims to be able to reconsider a blocking if something new happens to the element (e.g. to its element types).
#### Blocking
* `127.0.0.1` / `0.0.0.0` / `::1` / `0` / `::`: Used by "*hosts*" system files to signify that network requests to such a domain shall be redirected to a local-only IP address, thus preventing it from loading. Nano and uBO treats it the same as `||`. It only supports whole domains; using `/` or any other non-alphanumeric-or-period characters is not accepted.
* `||` + `$document`: Usually guarantees a danger warning when loading a page, even when the criteria is a subpath.
* `$3p`: Same as `$third-party`.
* `$1p` / `$first-party`: Same as `$~third-party`.
* `$xhr`: Same as `$xmlhttprequest`.
* `$all`: Officially combines all other non-party `$` values. In practice it combines the use of no `$` values at all + `$popup` + `$document`.
* `$redirect-rule`: Similar to `$redirect`, but is only applied if it's already blocked by *another* entry or dynamic rule(set).
* `@@||` + `$ghide`: Same as `@@||` + `$generichide`.
* `@@` + `$cname`: Prevents another site from being strict-blocked if the domain shows up in its CNAME response. `$~cname`, and `$cname` for blocking, also exist, but are poorly documented.

### Adblock Plus, Adblock and AdGuard only:
* `$webrtc`: Prevents such resources from being downloaded through the titular JavaScript API. The uBO equivalent seems to be `##+js(nowebrtc)`, but conversion is not done automatically.

### Adblock Plus and AdBlock only:
* `! Redirect:`: Tells the adblocker to look for list updates from a new URL from that point on.
* `! Checksum:`: No longer in use by *any* adblockers. Was used by ABP/AB on Firefox prior to November 2017, out of a then-decade-old fear that antivirus tools could tamper with list contents to create disastrously miswritten entries. AdGuard adds their own checksums to natively included lists, which do not need any maintainer intervention.
#### Hiding
* `#?#`: Required to make entries with `:-abp-has`, `:-abp-contains` and `:-abp-properties` work in those particular extensions, and to make `:style` entries not break the list extremely heavily.
* `:-abp-properties`: A highly modified version of `:matches-css[-before]`, with some syntax differences. Can also select text encodings (à la Base64) and a few other non-CSS traits.
* `#$#`: Similar to, but incompatible with, `##+js`. Possible options are listed in [this file](https://gitlab.com/eyeo/adblockplus/adblockpluscore/blob/next/lib/content/snippets.js) (text-search `@alias`).
#### Blocking
* `@@||` + `$document`: Turns off adblocking entirely while on that domain.
* `@@||` + `$~document`: Not easily obvious. Could possibly make sure to not turn off adblockers while on that domain, while preventing blockage of on-site elements.
* `@@||` + `$genericblock`: Prevents all non-domain-specific blocking entries from working on a website.
* `$rewrite=abp-resource:`: Similar to `$redirect`, but with a rather different selection of neutered files. Possible options are listed on [this help page](https://help.eyeo.com/adblockplus/how-to-write-filters#rewrite).

### AdGuard only:
#### Hiding
* `#%#//scriptlet`: Similar to, but only partially compatible with, `##+js` and ABP's `#$#`. Possible options are listed in [this file](https://github.com/AdguardTeam/AdguardBrowserExtension/blob/master/Extension/lib/filter/rules/scriptlets/scriptlets.js) (text-search ".names").
* `#%#AG_`: A few extra scriptlets for whom documentation appears to be non-existent.
* `#%#` without `//scriptlet`: Appears to insert JavaScript code that is written into the list, as opposed to from an embedded file. Requires heavy privileges.
* `:properties`: Claims to be similar to `:-abp-properties`, but is incompatible with it.
* `!+ PLATFORM`: Very similar to `!#if`, but is designed to have AdGuard's many versions be used as criteria, and not necessarily the browser that is being used.
#### Blocking
* `$match-case`: Makes the criteria case-sensitive.
* `$$script`: Uses very advanced criteria to block scripts that meet them.
* `$cookie`: Blocks cookies.
* `$cookie=`: Blocks cookies with specific names.
* `$cookie=` + `maxAge`: Changes the cookie to have an expiration time in seconds.
* `$cookie=` + `same-site`: Changes the cookie to use the "Lax" mode of `samesite` known from the `Set-Cookie` browser HTTP response system.
* `$mp4`: Seems to be equivalent to `$redirect=noopmp4`, but does not require any AdGuard trust rights. Allegedly to be obsoleted soon.

### AdGuard for [Windows/Mac/Android] only:

* `! Description:`: Shows a description of the list's purpose, when the question mark next to the list in the AdGuard settings is hovered over. That being said, a description is convenient for users of all adblockers, if they're willing to look up a list's raw content.
* `$network`: When applied to an IP address, it blocks all incoming requests from it, and not just when it's typed into a browser address bar. Individual ports can be specified with `:`. IPv6 addresses must be surrounded by square brackets. Can very easily break legitimate sites as collateral damage, and should be used very sparingly.
* `@@` + `$jsinject`: Prevents `#%#` entries from working on that site.
* `@@` + `$extensions`: Prevents AdGuard userscripts from working on that site.
* `@@` + `$content`: Prevents `$$script` entries from working on that site.
* `@@` + `$stealth`: Turns off Stealth Mode on that site.
* `$replace`: Changes the text of text elements on a site. Supports and requires use of RegEx. Requires ridiculous amounts of trust rights and cannot be used in web-hosted lists.

### AdGuard for [Android/iOS] only:

* `!+ NOT_OPTIMIZED`: Used to state that the entry immediately below is to be discarded, when an end-user has turned on "Simplified rules" mode in the AdGuard settings.

# Other particularly important usage notes

* To make the text detection for `:-abp-contains` and `:has-text` case-insensitive, wrap the paranthesised text into `(/Example text/i)`.
* The `"` in `[href="text"]` is optional, but *only* if the criteria text is only a single word, and has no numbers, slashes, or certain other characters.
* `:style` and `{ }` do not allow the use of URL values.
* It is claimed in [this comment](https://github.com/DandelionSprout/adfilt/issues/7#issuecomment-481978609) that Safari does not properly accept the use of `$third-party`.
* Amazingly, using `! Redirect: ` in the intended target link's list, will cause an infinite loop that prevents the list from being loaded.
* In Opera, the F12 filetree is not actually opened with F12 by default, but instead with Ctrl+Shift+I (Capital İ).
* No entries can use both `||` and `##` at the same time.

¹ = Includes Nano Adblocker, uBlock Origin ≥1.20.0, AdGuard, AdNauseum, Adblock Plus version ≥3.5, and AdBlock. It does **not** include AdGuard Home, Brave Browser, Slimjet, uBlock non-Origin, Tracking Protection List, or Blokada, whose syntax supports are considerably inferior to the above list.
