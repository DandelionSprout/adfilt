#### Test environment(s)

* Last tested on the 25th of February 2020 from Trondheim, Norway.
* The default browser locale was set to Norwegian Bokmål.
* Facebook domains were tested in Chrome on Windows 10 Pro. Facebookcorewwwi domains were tested in Tor Browser for Windows.
* No proxies were used.
* No user-agent changes were made to the browsers (which may explain some strange outcomes regarding phone-specific domains between Facebook and Facebookcorewwwi; and between Chromium and Gecko browsers).

# Results

## Tier 1 (Computers and laptops):

![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/facebooktier1.png)
* https://www.facebook.com/StrawberryShortcake/
* All currently known language-code versions of Facebook (e.g. https://en-gb.facebook.com/StrawberryShortcake/
* https://www.beta.facebook.com/StrawberryShortcake/ (Note that removing the `www.` part will cause it to redirect to facebook.com)
* https://b-www.facebook.com/StrawberryShortcake/
* https://secure.facebook.com/StrawberryShortcake/
* https://pixel.facebook.com/StrawberryShortcake/ (I didn't expect this to work, since it's usually only a 3rd-party tracking domain, but it does)
* https://error.facebook.com/StrawberryShortcake/ (?!?!?!?!?)
* https://www.facebookcorewwwi.onion/StrawberryShortcake/
* https://www.beta.facebookcorewwwi.onion/StrawberryShortcake/ (Its HTTPS certificate is currently broken)
* https://b-www.facebookcorewwwi.onion/StrawberryShortcake/
* https://secure.facebookcorewwwi.onion/StrawberryShortcake/
* https://pixel.facebookcorewwwi.onion/StrawberryShortcake/
* https://error.facebookcorewwwi.onion/StrawberryShortcake/

#### Tested 16th of March 2020
* https://t.facebook.com/StrawberryShortcake/
* https://t.facebookcorewwwi.onion/StrawberryShortcake/

## Tier 2 (Phones and non-keyboard tablets):

(I couldn't find any ways to remove the extreme banner image crust on the Tier 2 domains. My apologies in advance for your sore eyes.)
![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/facebooktier2.png)
* https://touch.facebook.com/StrawberryShortcake/
* https://mtouch.facebook.com/StrawberryShortcake/
* https://x.facebook.com/StrawberryShortcake/
* https://iphone.facebook.com/StrawberryShortcake/
* https://m.beta.facebook.com/StrawberryShortcake/
* https://touch.beta.facebook.com/StrawberryShortcake/
* https://mtouch.beta.facebook.com/StrawberryShortcake/
* https://x.beta.facebook.com/StrawberryShortcake/
* https://iphone.beta.facebook.com/StrawberryShortcake/
* https://touch.facebookcorewwwi.onion/StrawberryShortcake/
* https://mtouch.facebookcorewwwi.onion/StrawberryShortcake/
* https://x.facebookcorewwwi.onion/StrawberryShortcake/
* https://iphone.facebookcorewwwi.onion/StrawberryShortcake/
* https://touch.beta.facebookcorewwwi.onion/StrawberryShortcake/ (Its SSL certificate is currently broken)

## Tier 2.5 (Domains that may or may not change between Tier 2 and 3 based on the user-agent and/or country)

* https://m.facebook.com/StrawberryShortcake/ (T2 in Chrome and Vivaldi, T3 in Firefox and Tor Browser)
* https://m.facebookcorewwwi.onion/StrawberryShortcake/ (T3 in Tor Browser)
* https://b-m.facebook.com/StrawberryShortcake/ (T2 in Chrome and Vivaldi, T3 in Firefox and Tor Browser)
* https://b-m.facebookcorewwwi.onion/StrawberryShortcake/ (T3 in Tor Browser)
* https://mobile.facebook.com/StrawberryShortcake/ (T2 in Chrome and Vivaldi, T3 in Firefox and Tor Browser)
* https://mobile.facebookcorewwwi.onion/StrawberryShortcake/ (T3 in Tor Browser)

## Tier 3 (Old phones):

![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/facebooktier3.png)
* https://mbasic.facebook.com/StrawberryShortcake/
* https://d.facebook.com/StrawberryShortcake/
* https://free.facebook.com/StrawberryShortcake/ (Available in southeast Asia only. Elsewhere redirects to m.facebook.com)
* https://free.facebookcorewwwi.onion/StrawberryShortcake/
* https://mbasic.facebookcorewwwi.onion/StrawberryShortcake
* https://d.facebookcorewwwi.onion/StrawberryShortcake (Some image placements are broken)

## Tier 4 (Old phones; images are not loaded unless clicked on):

![alt text](https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Images/facebooktier4.png)
* https://0.facebookcorewwwi.onion/StrawberryShortcake
* https://0.facebook.com/StrawberryShortcake/ (Normally redirects to mobile.facebook.com except in some non-Western countries)

## Unclear status:
* https://zero.facebook.com/StrawberryShortcake/ (This and the 3 links below redirects to mobile.facebook.com)
* https://zero.beta.facebook.com/StrawberryShortcake/
* https://o.facebook.com/StrawberryShortcake/
* https://o.beta.facebook.com/StrawberryShortcake/
* https://0.beta.facebook.com/StrawberryShortcake/ (Redirects to mobile.beta.facebook.com)
* https://apps.facebook.com/StrawberryShortcake/ (Requires being logged on to access)
* https://web.facebook.com/StrawberryShortcake/ (Redirects to facebook.com)
* https://web.beta.facebook.com/StrawberryShortcake/ (Redirects to beta.facebook.com)
* https://intern.facebook.com/StrawberryShortcake/ (Requires being logged on to access, and may or may not require actually being hired by Facebook)
* https://m.beta.facebookcorewwwi.onion/StrawberryShortcake/ (Its SSL certificate is currently broken)

## Currently presumed to be discontinued:
* https://h.facebook.com/StrawberryShortcake/ (Redirects to `https://m.facebook.com/StrawberryShortcake/?_rdr`)
* https://h.beta.facebook.com/StrawberryShortcake/ (Redirects to `https://m.beta.facebook.com/StrawberryShortcake/?_rdr`)
* https://vvv.facebook.com/StrawberryShortcake/
* https://z.facebook.com/StrawberryShortcake/ (Redirects to facebook.com)
* https://z-m.facebook.com/StrawberryShortcake/ (Redirects to facebook.com)
* https://ssl.facebook.com/StrawberryShortcake/ (Redirects to facebook.com)
* https://lookaside.facebook.com/StrawberryShortcake ("Error 400" browser page)
* https://star.facebook.com/StrawberryShortcake/ (Redirects to facebook.com)
* https://l.facebook.com/StrawberryShortcake/ (Redirects to facebook.com)
* https://lm.facebook.com/StrawberryShortcake/ (Redirects to m.facebook.com)
