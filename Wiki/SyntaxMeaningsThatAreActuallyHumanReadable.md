#### Recommended lists to look up example entries for the syntaxes below:

* Main example list: [uBlock Filters](https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt)
* AdGuard-specific syntaxes: [AdGuard Base Filters ('AdGuard for Windows' version)](https://filters.adtidy.org/windows/filters/2.txt)
* ABP-specific syntaxes: [ABP Anti-Circumvention List — English sites](https://gitlab.com/eyeo/anti-cv/abp-filters-anti-cv/-/raw/master/english.txt)

## All up-to-date significant adblockers¹

#### Element removal (a.k.a. cosmetic rules, a.k.a. hiding rules, a.k.a. ##-rules)
* `##.`: Hides page elements, based on one or more `class` values in the F12 "Elements" filetree (separated with full-stops).
* `##`: Hides page elements based on the element type, e.g. `a`, `li`, `button`, `iframe`, etc., that are usually highlighted in purple in the F12 DOM (Document Object Model) "Elements" index.
* `###`: Hides page elements based on the `id` value.
* `#@#.`/`#@#`/`#@##`: Whitelists page elements to make them load.
* `[href="text"]`: Finds page elements whose values in the F12 filetree console contains such a value. The value can be `href`, `id`, `class`, `type`, or numerous other things that are highlighted in brown in the F12 DOM (Document Object Model) "Elements" index. Does not support RegEx.
* `[href="text" i]`: Same as above, except <b>case-insensitive</b>.
* `[href^="text"]`: Finds page elements whose value <b>*begins*</b> with the text.
* `[href$="text"]`: Finds page elements whose value <b>*ends*</b> with the text.
* `[href*="text"]`: Finds page elements whose value contains the text <b>anywhere within it</b>.
* `[href~="text"]`: Finds page elements whose value contains the word (with spaces around it) anywhere within it.
* `[href|="text"]`: Same as `[href="text"]`, but can *also* select text that is then followed by a hyphen `-`.
* `:not(.element)`: Finds page elements that <b>doesn't</b> contain a specified element or text string.
* `:has-text(text)`: Finds page elements that contains such text within it.
* `:has(.element)`: Finds page elements that contains such an element within it.
* `:has(>` : Tells `:has` to only find elements whose criteria match their <b>immediate</b> subelement(s).
* `:not(:has-text(Text))` / `:not(:has(.element))`: Looks for elements whose text/subelements *doesn't* meet the selection.
* `:nth-of-type(n)` / `:nth-last-of-type(n)`: Finds page elements that are at a specific numerical position in a set. Note that `:nth-last-of-type(n)`'s numbering goes in reverse order. To select multiple numbers, one has to use `n` calculations (e.g. `(n+2)`), since ranges (e.g. `(3-6)`) are not supported.
* `:only-of-type` / `:first-of-type` / `:last-of-type`: Less versatile versions of the above, for which numbers can't be chosen.
* `:first-child` / `:last-child`: Appears to be synonymous with `first-of-type` and `last-of-type` for adblocking purposes. `:last-child` is easily mistaken for what `:empty` does.
* `::before` / `::after`: Removes the <b>pseudo-elements</b> that belong to a page element. If a pseudo-element is present, they're shown as standalone `::before` or `::after` lines in all-brown in the F12 filetree.
* `>`: Creates chain criteria, in which a selected page element must have a specific element on the floor above it in the filetree.
* `+`: Blocks the element that is <b>right below</b> the criteria in the filetree. Example: `##.element + div` blocks that particular `div`.
* `~`, as in `##.element ~ div`: Similar to `+`, but blocks *all* such `div` elements that are below it on the same floor in the filetree, and not just the one right below.
* Spacing between elements, e.g. `##.element .element`: Similar to `>`, but can mean <b>*any*</b> number of floors between the elements, and not just those that are one floor apart.
* `##element1,element2` (alt. `##element1, element2`): Combines two hiding entries into the same line of text.

##### Advanced examples:
* The first two `##` of an element entry, are not used for elements written after e.g. `>`, `+` or `:has`. In those cases, the `##` in `##element` gets removed, `##.class` becomes `.class`, and `###id` becomes `#id`.
* `##element.class`: Hide something both based on its element (##element1) and `class` value (.class). Note the placement/absence of fullstops.
* While they're based on the same `class` values, `##.element1` will match any `class` (sub-)value, whereas `##div[class="element1"]` and their modifiers are based on the *entire* `class` string in the F12 filetree.
* `##.` / `##` / `###` entries can either be *generic*, in which they have no domains in front of them; or (domain-)specific, where they have one or more domains in front of them, separated by commas. uBO/AdGuard support wildcard asterisks (`*`) in such domains, and only for the immediate pre-TLD part; while ABP/AdBlock do not.
* `##div:is(.element1,.element2)`: Compression of `##div.element1` and `##div.element2`. It is extremely rare that this would be needed in lists for uBlock Origin or Adblock Plus (who would be able to use `##div.element1,div.element2` in all circumstances), but it could help work around problems in AdGuard with `##element1,element2:has(-text)` that are explained in its section below.

#### File blocking (a.k.a. blocking rules, a.k.a. non-#-rules)
* \[no prefix\]: Blocks resources that have this text string *anywhere* in its URL.
* `||`: Blocks resources that have a specific domain or subdomain.
* `@@`: Whitelists resources to make them load.
* `^`: Wildcard for anything that isn't alphanumerical or _-.%, and for end-of-lines.
* `$third-party`: Ensures that resources from a domain are only blocked if you're <b>not</b> visiting the domain itself.
* `$~third-party`: Ensures that resources from a domain are only blocked if you're visiting *the domain itself*.
* `$domain=`: Ensures that resources from a domain are only blocked if you're visiting a <b>specified</b> website. Multiple domains are separated with `|` (Vertical line) and not commas. Supports top-level domain wildcards with e.g. `$domain=tk`.
* `@@||` + `$generichide`: Prevents all non-domain-specific (a.k.a. generic) hiding entries from working on a website. On uBO it prevents *all* generic entries from working.
* `@@||` + `$specifichide`: Prevents all domain-specific <b>element removal</b> entries from working on a website. On uBO it seems to prevent *all* domain-specific entries from working.
* `@@||` + `$elemhide`: Combines `$generichide` and `$specifichide`. Also completely breaks the element picker in uBO on that site as of the 14th of July 2020.
* `$script`: Blocks resources from domains or parts thereof from being loaded, but only if it's a script, e.g. a JavaScript runtime.
* `$csp`: Inserts additional *Content Security Policies* into the page.
* `$xmlhttprequest` / `$websocket`: Prevents such resources from being downloaded through the titular JavaScript APIs.
* `$popup` / `$image` / `$font` / `$other` / `$stylesheet` / `$css`: These ones should hopefully be self-explanatory (Give me a heads-up in an issue report if it isn't).
* `$object`: Despite its name, it refers to blocking resources that use a request type called `object`, and not just all sorts of objects.
* `|text`: Matches URLs that <b>*begin*</b> with the text.
* `text|`: Matches URLs that <b>*end*</b> with the text.
* `~`: Means that an entry does <b>*not*</b> apply to a specific domain.

#### Universal
* `! ` / `# `: Marks the start of a comment that shall not be interpreted as an entry.
* `/\/\/\/`, `/regextext/`, and similar: Text detections in <b>RegEx</b> format. Supported in most (if not all) blocking rules, as well as in `:has-text`. Note that *all* blocking rules that start and end with `/` are treated as RegEx; the intended workaround is to add a `*` after, which makes `*` supposedly serve as a plaintext indicator, instead of as a wildcard.
* * <i>Insider tip for very advanced users: If you see a RegEx that ends with `.*/`, change it to `.*$/`. Likewise, if it starts with `/.*`, change it to `/^.*`. Depending on the entry, this can reduce CPU usage quite a lot.</i>
* `[Adblock Plus n.n]`: Mandatory for Adblock Plus and forks of them, as they use the tag to determine if they should load the filterlist. This has *no* effect on uBO and AdGuard or their forks. Number is the intended minimum ABP version. `2.0` and `1.1` are most common; `3.10` and higher is on the rise and can be used to block support for old or low-quality forks. It also enables the GitHub syntax highlighter for that file.
* * `[uBlock Origin]`, `[AdGuard]`: These activate the syntax highlighter if the file is hosted on GitHub, should be placed on the first line of the list.
* `! Title:` Specifies the intended name of the list. Required to make the name <b>automatically show up</b> in the settings of most adblockers, instead of the URL or of manual text input.
* `! Version:` The version number/alphanumeric of the list. Unofficially used to distinguish which version of a list a user is using. Used administratively by Adblock Plus' list report system (which requires a number-only version value). Many lists choose to use `! Last modified` as well or instead.
* `! Expires:`: Determines the timespan between each automated sync attempt with the list's source. Values are given in "n day/days" or "n hour/hours". uBlock Origin rounds hours up to 6/12/18/24 hours. Usually ignored by AdGuard softwares.
* `! Homepage:` In uBlock Origin, it determines the link that the list's <b>🏠 (house) button in uBO's settings</b> leads to. Often also used in other adblockers for informational purposes.

## uBlock Origin and AdGuard only:
#### Hiding
* `:style`: Changes the CSS values of an element, in much the same way as what userstyle extensions like Stylish would've done.
* `#$#` + `{ }`: Same as above.
* `!#if`: Specifies that a section of entries only apply to specific platforms or extensions. Closed out by `!#endif`. Possible options are listed [here](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax#if-condition), with some additional options listed [here](https://kb-adg.pages.dev/general/ad-filtering/create-own-filters/#conditions-directive).
* `:matches-css`: Looks for page elements whose existing native (i.e. non-inherited) CSS values match those of the criteria.
* `:matches-css-before` / `:matches-css-after`: Same as above, but looks for CSS values in its pseudo-elements instead.
* `:remove()`: Removes the element entirely from the F12 tree. The parentheses are required. Can glitch out spectacularly on a select few sites, most notably Tumblr.
* `#$?#` + `{ remove: true; }`: Same as above.
* `:matches-attr`: Similar to `[href*="text"]`, but adds support for RegEx.
#### Blocking
* `||` + `$document`: Usually guarantees a danger warning when loading a page, even when the criteria is a subpath.
* `$badfilter`: Deactivates a resource-blocking entry, even if it is present in another list. Requires the bad entry to be written verbatim; except for removing Hosts prefix IPs. You can not `badfilter` a `badfilter` rule.
* `$important`: Makes a resource-blocking entry take precedence over another whitelisting entry.
* `$redirect`: Redirects resources to a neutered version that has been embedded in those extensions. Possible options are listed [on this page](https://github.com/gorhill/uBlock/wiki/Resources-Library#available-empty-redirect-resources) (AdGuard has a [slightly bigger selection](https://github.com/AdguardTeam/Scriptlets/blob/master/wiki/about-redirects.md#-available-redirect-resources)).
* `$empty`: Results in a fake empty page or resource being loaded, instead of blocking the resource itself.
* `$removeparam` (prev. `$queryprune`): Removes URL parameters, e.g. `?tracker=sitecampaignpage`. Supports RegEx, but with many differences (One example, is that wildcarding is done with `/^textstart-/` instead of `/textstart-.*/`), since its RegEx blocks based on the parameter *and* its value, that a lack of `/^` will make it search *anywhere* in that string, and a lack of support for backslashing. Whitelistings must match the exact parameter that was blocked.
* `$match-case`: Makes the criteria case-sensitive. uBO only supports it in RegEx entries.

## uBlock Origin and Adblock Plus only
* `##element1,element2:has(-text)`: Combines and subjects two elements to the same `:has`/`:has-text` criteria. Very bad idea to use in AdGuard, where all instances of `element1` would be blocked. This can be worked around by changing it to `##:is(element1,element2):has(-text)`

## uBlock Origin only:
#### Hiding
* `!#include`: Embeds another filterlist that is hosted on the same domain. Despite AdGuard's claim that they also support it, their support only applies to lists that are natively included in AdGuard. Tonnes of restrictions apply, such as refusing to embed lists from another domain / repository / parent-folder.
* `##+js` (prev. `##script:inject`): Invokes a script that is embedded in those extensions, and usually using the script to modify a value on the site. Possible options are listed [on this page](https://github.com/gorhill/uBlock/wiki/Resources-Library#available-general-purpose-scriptlets).
* * `##+js(ra, class, .element)`: Removes the specified element class name from all elements on the page, without removing the elements themselves.
* `:xpath`: An entry written with the very advanced Xpath syntax.
* `##^.element`: Remove page elements _before_ they've even been loaded, based on their values in `View source` instead of their F12 ones. **Only** works in Firefox and Tor Browser.
* `##^script:has-text` (prev. `##script:contains`): Intends to prevent inline scripts from starting up. Do not use the F12 filetree to create these filters, you must use `View source` instead; relying on the F12 filetree has a substantial chance of breaking sites even if they match filetree elements. Also only works in Firefox and Tor Browser.
* * An example of such breakage is at `https://bold•dk/fodbold/stillinger/conference-league/nyheder/stolt-djurgarden-boss-en-fuldstaendig-vanvittig-oplevelse` on 9 May 2025, where not only did `bold.dk##^.mobile-ad-wrapper` not work, but using it and `bold.dk##.mobile-ad-wrapper` at the same time caused both entries to not work.
* `:upward` (prev. `:nth-ancestor`): Looks for elements that are a certain amount of indentations (i.e. filetree floors) above the criteria in the F12 filetree. Equivalent to `:xpath(../..)`, but with normal numbers. Now also has the ability to look for specific element names at *any* indentation amount.
* `:min-text-length`: Appears to select elements whose underlying source content has at least that amount of characters. Is completely disassociated from the actual on-page visible text by an order of several magnitudes.
* `:watch-attr`: Claims to be able to reconsider a blocking if something new happens to the element (e.g. to its element types).
* `/^regextext\.(...)$/##.element`: Allows specifying domains through RegEx for very extensive wildcard possibilities. For example, `/^nitter\..*$/##.element` would match `nitter.*.*`. For practical reasons, the use of sentence-start `^` and sentence-end `$` are highly advised, especially so for `$`. Can be comma-combined with regular domains, for example `/^nitter\..*$/,google.com##.element`.
#### Blocking
* `127.0.0.1` / `0.0.0.0` / `::1` / `0` / `::`: Used by "*hosts*" system files to signify that network requests to such a domain shall be redirected to a local-only IP address, thus preventing it from loading. uBO treats it the same as `||`. It only supports whole domains; using `/` or any other non-alphanumeric-or-period characters is not accepted.
* `$3p`: Same as `$third-party`.
* `$strict3p`: Same as `$third-party`, but also considers other subdomains to be 3rd-party, i.e. if `www.example.org` loads an asset from `subdomain.example.org`, the latter is now considered 3rd-party.
* `$1p` / `$first-party`: Same as `$~third-party`.
* `$strict1p`: Same as `$first-party` but considers other subdomains to not be 1st-party, i.e. if `www.example.org` loads an asset from `subdomain.example.org`, the latter is now considered 3rd-party.
* `$xhr`: Same as `$xmlhttprequest`.
* `$doc`: Same as `$document`. May cause problems in some versions of AdGuard.
* `$all`: De facto combines all other `$` values. Officially combines the use of no `$` values at all + `$popup` + `$document` + `$inline-script` + `$inline-font`.
* `$redirect-rule`: Similar to `$redirect`, but is only applied if it's already blocked by *another* entry or dynamic rule(set).
* `$mp4`: Equivalent to `$redirect=noopmp4-1s,media`.
* `@@` + `$cname`: Prevents another site from being strict-blocked if the domain shows up in its CNAME response. `$~cname`, and `$cname` for blocking, also exist, but are poorly documented. Not needed for entries that already have `$doc`. Only applies to Firefox and Tor Browser.
* `$from`: Same as `$domain`.
* `$denyallow` + `,domain=`: Allows choosing which third-party domain requests to allowlist, instead of which ones to block, while visiting specified domains.
* `$to`: Superset of `$denyallow`. Supports TLD-wildcard (`google.*`) hostnames and negated hostnames (`~example.com`).
* `$ipaddress`: Partially similar to AdGuard's `$network`, but is unable to block webpages outright. Only works in Firefox and Tor Browser.

## Adblock Plus and AdGuard only:
* `$webrtc`: Prevents WebRTC (Real-Time Communication) connections which is usually used by messengers and games. The uBO equivalent is `##+js(nowebrtc)`, but conversion is not done automatically. It is deprecated in AdGuard, which has transitioned over to uBO's `##+js(nowebrtc)`.

## Adblock Plus only:
* `! Redirect:`: Tells the adblocker to look for list updates from a new URL from that point on. To be used in the old file only (Not the new one), to avoid an infitite redirection loop.
* `! Checksum:`: No longer in use by *any* adblockers. Was used by ABP/AB on Firefox prior to November 2017, out of a then-decade-old fear that antivirus tools could tamper with list contents to create disastrously miswritten entries. AdGuard adds their own checksums to natively included lists, which do not need any maintainer intervention.
#### Hiding
* `#?#`: Required to make entries with `:has`, `:has-text` and `:-abp-properties` work in those particular extensions, and to make `:style` entries not break the list extremely heavily.
* `:-abp-properties`: A highly modified version of `:matches-css[-before]`, with some syntax differences. Can also select text encodings (à la Base64) and a few other non-CSS traits.
* `#$#`: Similar to, but incompatible with, `##+js`. Possible options are listed in [this file](https://gitlab.com/eyeo/adblockplus/adblockpluscore/blob/next/lib/content/snippets.js) (text-search `@alias`). Prohibited from use in third-party filters, but can be used in User Filters in Firefox and MV2. Multiple values can be chained with `; ` in-between.
#### Blocking
* `@@||` + `$document`: Turns off adblocking entirely while on that domain.
* `@@||` + `$~document`: Not easily obvious. Could possibly make sure to not turn off adblockers while on that domain, while preventing blockage of on-site elements.
* `@@||` + `$genericblock`: Prevents all non-domain-specific blocking entries from working on a website.
* `$rewrite=abp-resource:`: Similar to `$redirect`, but with a rather different selection of neutered files. Possible options are listed on [this help page](https://help.eyeo.com/adblockplus/how-to-write-filters#rewrite).

## AdGuard only:
* `! Description:`: Shows a description of the list's purpose, when the question mark next to the list in the AdGuard settings is hovered over. That being said, a description is convenient for users of all adblockers, if they're willing to look up a list's raw content.
#### Hiding
* `#%#//scriptlet`: Similar to, but only partially compatible with, `##+js` and ABP's `#$#`. Possible options are listed in [this file](https://github.com/AdguardTeam/Scriptlets/blob/master/wiki/about-scriptlets.md#-available-scriptlets).
* `#%#AG_`: A few extra scriptlets for whom documentation appears to be non-existent.
* `#%#` without `//scriptlet`: Appears to insert JavaScript code that is written into the list, as opposed to from an embedded file. Only works in AdGuard's own lists or User Filters.
* `!+ PLATFORM`: Similar to `!#if`, but is only used during the AdGuard team's compiling of included lists. It has no effect on custom lists.
* `:matches-property`: Selects an HTML element by using a CSS identifier, as detailed under AdGuard's [ExtendedCSS](https://github.com/AdguardTeam/ExtendedCss#extended-css-matches-property) project.
* `[$path]`: Unclear. Most likely limits hiding rules to only have effect on URLs that contain the `$path` value, e.g. `[$path=sport]`.
#### Blocking
* `$$script`: Same as `##^script:has-text`.
* `$cookie`: Blocks cookies.
* `$cookie=`: Blocks cookies with specific names.
* `$cookie=` + `maxAge`: Changes the cookie to have an expiration time in seconds.
* `$cookie=` + `same-site`: Changes the cookie to use the "Lax" mode of `samesite` known from the `Set-Cookie` browser HTTP response system.
* `@@` + `$urlblock`: Turns off file-request blocking entirely while on that domain.
* `$removeheader`: Removes lines found in the F12 Dev Tools → Network → Ctrl+F to let it record the whole page's loading → All → Name → "Response Headers" or "Request Headers".

## AdGuard for [Windows/Mac/Android] only:

* `$app`: Ensures the entry is only applied to a specific phone app(s) or PC executable(s).
* `$network`: When applied to an IP address, it blocks all incoming requests from it, and not just when it's typed into a browser address bar. Individual ports can be specified with `:`. IPv6 addresses must be surrounded by square brackets. Can very easily break legitimate sites as collateral damage, and should be used very sparingly. Despite what AdGuard's syntax guide indicates, it does in fact support wildcarding both with and without RegEx.
* `@@` + `$jsinject`: Prevents `#%#` entries from working on that site.
* `@@` + `$extension`: Prevents AdGuard userscripts from working on that site.
* `@@` + `$content`: Prevents `$$script` entries from working on that site.
* `@@` + `$stealth`: Turns off Stealth Mode on that site.
* `$replace`: Changes the text of text elements on a site. Supports and requires use of RegEx. Requires ridiculous amounts of trust rights and cannot be used in web-hosted lists.
* `$protobuf`: Similar to `$replace`, but strips away numeric values from responses given by the `Protocol Buffers` API.

## AdGuard for [Android/iOS] only:

* `!+ NOT_OPTIMIZED`: Used to state that the entry immediately below is to be discarded, when an end-user has turned on "Simplified rules" mode in the AdGuard settings.

# Other particularly important usage notes

* To make the text detection for `:has-text` case-insensitive, wrap the paranthesised text into `(/Example text/i)`.
* The `"` in `[href="text"]` is optional, but *only* if the criteria text is only a single word, and has no numbers, slashes, or certain other characters.
* `:style` and `{ }` do not allow the use of URL values.
* It is claimed in [this comment](https://github.com/DandelionSprout/adfilt/issues/7#issuecomment-481978609) that Safari does not properly accept the use of `$third-party`.
* In Opera, the F12 filetree is not actually opened with F12, but instead with Ctrl+Shift+I (Capital İ).
* No entries can use both `||` and `##` at the same time.
* Major note to advanced CSS experts: Some advanced terms have been replaced in this guide, because they'd be less than obvious to laymen who'd need this guide.

¹ = Includes uBlock Origin ≥1.20.0, AdGuard (except iOS), AdNauseum, and Adblock Plus versions 3.13-3.20. It does **not** include AdGuard Home, Brave Browser, Adblock Plus ≥4.0, Slimjet, uBlock non-Origin, Tracking Protection List, Blokada, or Pi-hole, whose syntax supports are considerably inferior to the above list.
