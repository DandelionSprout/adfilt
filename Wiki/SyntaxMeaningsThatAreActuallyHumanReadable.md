### All up-to-date significant adblockers¹

#### Element removal (a.k.a. cosmetic rules, a.k.a. hiding rules)
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
* `:scope`: Used alongside `:-abp-has` to make it only find elements whose criteria match their immediate subelements.
* `:nth-of-type(n)` / `:last-of-type` / `:only-of-type`: Finds page elements that are at a specific numerical position in a set.
* `:before` / `:after`: Removes the pseudo-elements that belong to a page element.
* `>`: Creates chain criteria, in which a selected page element must have a specific element above it in the filetree.
* `+`: Blocks the element that is right below the criteria in the filetree. Example: `##.element + div` blocks that particular `div`.

##### Advanced examples:
* `##element.element2`: Hide something both based on its element (##element1) and `class` value (.element2). Note the placement/absence of fullstops.
* `##.element1 > #element2`: When used in chain criteria, three `###` are replaced by a single `#`.
* While they're based on the same `class` values, `##.element1` will match any `class` (sub-)value, whereas `##div[class="element1"]` and their modifiers are based on the *entire* `class` string in the F12 filetree.
* `##.` / `##` / `###` entries can either be *generic*, in which they have no domains in front of them; or domain-specific, where they have one or more domains in front of them, separated by commas. Only Nano and uBO support wildcard asterisks (`*`) in such domains, while other adblockers do not.

#### File blocking (a.k.a. blocking rules)
* `||`: Blocks resources from domains or parts thereof from being loaded. For non-domain-specific resources, no pre-emption is needed at all.
* `@@`: Whitelists resources from specific URLs to make them load.
* `^`: Usually ensures that the subdomains are also covered by the entry.
* `$third-party`: Ensures that resources from a domain are only blocked if you're not visiting the domain itself.
* `$~third-party`: Ensures that resources from a domain are only blocked if you're visiting the domain itself.
* `$domain=`: Ensures that resources from a domain are only blocked if you're visiting a specified website.
* `$generichide`: Prevents all non-domain-specific (a.k.a. generic) hiding entries from working on a website. On Nano/uBO it prevents *all* non-domain-specific entries from working.
* `$script`: Blocks resources from domains or parts thereof from being loaded, but only if it's a script, e.g. a JavaScript runtime.
* `$csp`: Inserts additional *Content Security Policies* into the page.

#### Universal
* `! ` / `# `: Marks the start of a comment that shall not be interpreted as an entry.
* `~`: Means that an entry does *not* apply to a specific domain.
* `/\/\/\/` and similar: Text detections in RegEx format.
* `[Adblock Plus n.n]`: Used by Adblock Plus, AdBlock, and forks of them to determine if they should load the filterlist. Number is the intended minimum ABP version. `2.0` and `1.1` are most common; `3.1` and higher is on the rise and can be used to block support for old or low-quality forks. This has no effect on uBO or its forks.

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

### Nano Adblocker and uBlock Origin only:
#### Hiding
* `!#include`: Embeds another filterlist that is hosted on the same domain (with numerous restrictions).
* `##+js` (prev. `##script:inject`): Invokes a script that is embedded in those extensions, and usually using the script to modify a value on the site.
* `:xpath`: An entry written with the very advanced Xpath syntax.
* `##^`: Blocks resources before they've even been loaded, based on their values in *View source* instead of their F12 ones.
#### Blocking
* `127.0.0.1` / `0.0.0.0` / `::1`: Used by "*hosts*" system files to signify that network requests to such a domain shall be redirected to a local-only IP address, thus preventing it from loading. Nano and uBO treats it the same as `||`.
* `||` + `$document`: Guarantees a danger warning when loading a page, which is not 110% guaranteed otherwise.
* `$redirect`: Redirects resources to a neutered version that has been embedded in those extensions.
* `$3p`: Same as `$third-party`.
* `$first-party` / `$1p`: Same as `$~third-party`.
* `$all`: Officially combines all other non-party `$` values. In practice it combines the use of no `$` values at all + `$popup`.

### Adblock Plus and AdBlock only:

* `! Redirect: `: Tells the adblocker to look for list updates from a new URL from that point on.
* `#?#`: Required to make entries with `:-abp-has`, `:-abp-contains` and `:-abp-properties` work in those particular extensions.
* `@@||` + `$document`: Turns off adblocking entirely while on that domain.
* `$genericblock`: Prevents all non-domain-specific blocking entries from working on a website.
* `:-abp-properties`: A highly modified version of `:matches-css[-before]`, with some syntax differences. Can also select text encodings (à la Base64) and a few other non-CSS traits.

### AdGuard only:

* `#%#var AG_`: Similar to `##+js`, except with a completely different set of scriptlets.
* `$empty`: Results in a fake empty page being loaded, instead of an error page.
* `:properties`: Claims to be similar to `:-abp-properties`, but is incompatible with it.

### AdGuard for [Windows/Mac/Android] only:

* `! Description:`: Shows a description of the list's purpose, when the question mark next to the list in the AdGuard settings is hovered over. That being said, a description is convenient for users of all adblockers, if they're willing to look up a list's raw content.
* `$network`: When applied to an IP address, it blocks all incoming requests from it, and not just when it's typed into a browser address bar.

#### I honestly don't know what these ones do:

* `$xmlhttprequest` / `$xhr`

# Particularly important usage notes

* `||` entries do support asterisk wildcards, but only in the criteria text. Additionally, when using `$domain=`, domains are separated with vertical lines, since commas are instead used to stack multiple `$` values.
* `$generichide` entries must start with `@@||`.
* ABP is known to severely struggle with handling `:style` entries, to the point where having ABP try to load a list with such an entry will cause it to invalidate the list *and* all its entries.
* To make the text detection for `:-abp-contains` and `:has-text` case-insensitive, wrap the paranthesised text into `(/Example text/i)`.
* `127.0.0.1` / `0.0.0.0` / `::1` supports only whole domains, and it can not be narrowed down to subdomains or elements.
* The `"` in `[href="text"]` is optional, but *only* if the criteria text is only a single word.
* In `:-abp-has` and `:has`, it is not needed to pre-empt the criteria elements with `##`.
* `:style` and `{ }` does not allow to change `background-image` into a URL value.
* It is claimed in [this comment](https://github.com/DandelionSprout/adfilt/issues/7#issuecomment-481978609) that Safari does not properly accept the use of `$third-party`.
* Domains in `$domain=` are seperated by a vertical line (`|`), instead of the usual comma.
* Amazingly, using `! Redirect: ` in the intended target link's list, will cause an infinite loop that prevents the list from being loaded.
* In Opera, the F12 filetree is not actually opened with F12 by default, but instead with Ctrl+Shift+I (Capital İ).

¹ = Includes Nano Adblocker, uBlock Origin ≥1.14.0, AdGuard, AdNauseum, Adblock Plus version ≥3.1, and AdBlock. It does **not** include AdGuard Home, Brave Browser, Slimjet, uBlock non-Origin, Adblock Plus for IE, Tracking Protection List, AdAway, or Blokada, whose syntax supports are considerably inferior to the above list.
