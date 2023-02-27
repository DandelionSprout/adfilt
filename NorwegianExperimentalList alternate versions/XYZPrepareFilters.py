import requests
import re

SOURCES = ['https://gitlab.com/DandelionSprout/adfilt/-/raw/master/NorwegianList.txt', 'https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/AntiAdblockEntries.txt', 'https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/NordicFilters-NotBrave.txt']

UNSUPPORTED_ABP = ['$important', ',important', '$redirect=', ',redirect=',
    ':style', '##+js', '.*#' , 'dk,no##', '!#if', '!#endif', '!+ ', '##^', '$$', '$app', '$csp=upgrade-insecure-requests', '$removeparam', 'badfilter', '!#include']
UNSUPPORTED_TPL = ['##', '#@#', '#?#', r'\.no\.$', '!#include']
UNSUPPORTED_PRIVOXY = ['##', '#@#', '#?#', '!#', '$$', '$redirect', ',redirect', '$generichide', '$ghide', 'Expires:', '$removeparam']
UNSUPPORTED_UMATRIX = ['##', '#@#', '#?#', '!#', '$$', '$redirect', ',redirect', 'generichide', 'Expires:', 'subdocument', '$app', '!+', '$doc', ' doc ', 'CSP', '$csp', 'ghide', '$removeparam', '$all']

OUTPUT = 'xyzzyx.txt'
OUTPUT_AG = 'NordicFiltersAdGuard.txt'
OUTPUT_ABP = 'NordicFiltersABP.txt'
OUTPUT_TPL = 'DandelionSproutsNorskeFiltre.tpl'
OUTPUT_PRIVOXY = 'NordicFiltersPrivoxy.action'
OUTPUT_PRIVACY = 'NordicFiltersPrivacy.txt'
OUTPUT_UMATRIX = 'NordicFilters-uMatrixSupplement.txt'
OUTPUT_XUL = 'NordicFilters-uBOLegacy.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# ——— AdGuard version ———

# function that prepares the filter list for AdGuard
def prepare_ag(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"(itle:.*Dandelion Sprout.*)", 
           r"\1 (for AdGuard)", 
           line
        )

        line = re.sub(
           r"\$domain=~in-addr\.arpa$", 
           r"", 
           line
        )

        line = re.sub(
           r"! Version: [0-9]{4}.*", 
           "", 
           line
        )

        line = re.sub(
           r"! Redirect:.*", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])xhr", 
           r"\1xmlhttprequest", 
           line
        )

        line = re.sub(
           r"([$,~])3p", 
           r"\1third-party", 
           line
        )

        line = re.sub(
           r"([$,])1p", 
           r"\1~third-party", 
           line
        )

        line = re.sub(
           "redirect=noopmp4-1s", 
           "mp4", 
           line
        )

        line = re.sub(
           r"^!.*PFBLOCKERNG.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|(([1-2]?[0-9]?[0-9]\.?){4})\^\$.*", 
           r"\1$network", 
           line
        )

        line = re.sub(
           r"^\|\|(([1-2]?[0-9]?[0-9]\.?){4})\^", 
           r"\1$network", 
           line
        )

        line = re.sub(
           r"has\(:scope >", 
           r"has(>", 
           line
        )

        line = re.sub(
           r":-abp-has\(", 
           r":has(", 
           line
        )

        line = re.sub(
           r":-abp-contains\(", 
           r":has-text(", 
           line
        )

        line = re.sub(
           r"!#include NorwegianExperimentalList%20alternate%20versions/NordicFilters-FirefoxAndroidUBOWorkaround\.txt", 
           r"", 
           line
        )

        line = re.sub(
           r"!#include NorwegianExperimentalList%20alternate%20versions/AntiAdblockEntries\.txt", 
           r"", 
           line
        )

        line = re.sub(
           r"##\^script:has-text\((.*)\)", 
           r"$$script[\1]", 
           line
        )

        line = re.sub(
           r"##\^script\[(.*)\]", 
           r"$$script[\1]", 
           line
        )

        line = re.sub(
           r"\$~doc$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$doc(,|$)", 
           r"$document\1", 
           line
        )

        line = re.sub(
           r"!#include uBO%20list%20extensions/TemporaryWaterfoxClassicFixForNordicFilters\.txt", 
           r"", 
           line
        )

        line = re.sub(
           r"^!#include NorwegianExperimentalList%20alternate%20versions/", 
           r"!#include ", 
           line
        )

        line = re.sub(
           r"^!#include NordicFilters-NotBrave\.txt$", 
           r"", 
           line
        )

        line = re.sub(
           r"(#\??#)body(:| )", 
           r"\1html[lang] > body\2", 
           line
        )

        line = re.sub(
           r",~inline-font,~inline-script$", 
           r"", 
           line
        )

        line = re.sub(
           r",~inline-script,~inline-font$", 
           r"", 
           line
        )

        text += line + '\r\n'

    return text

# ——— Adblock Plus version ———

def is_supported_abp(line) -> bool:
    for token in UNSUPPORTED_ABP:
        if token in line:
            return False

    return True

# function that prepares the filter list for ABP
def prepare_abp(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        # remove $document modifier from the rule
        line = re.sub(
           r"\$doc.*", 
           "", 
           line
        )

        # remove $important modifier from the rule
        line = re.sub(
           r"\$important,", 
           "$", 
           line
        )

        line = re.sub(
           r"([$,])important", 
           "", 
           line
        )

        line = re.sub(
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider", 
           "Dandelion Sprouts vestnordiske filtre for ryddigere nettsider (for AdBlock og Adblock Plus)",
           line
        )

        line = re.sub(
           "Dandelion Sprout's Nordic filters for tidier websites", 
           "Dandelion Sprout's West Nordic filters for tidier websites (for AdBlock and Adblock Plus)",
           line
        )

        line = re.sub(
           r"^no##.*", 
           "", 
           line
        )

        line = re.sub(
           r"! Redirect:.*", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])xhr", 
           r"\1xmlhttprequest", 
           line
        )

        line = re.sub(
           r"([$,~])3p", 
           r"\1third-party", 
           line
        )

        line = re.sub(
           r"([$,])1p", 
           r"\1~third-party", 
           line
        )

        line = re.sub(
           ":matches-css-before\(", 
           ":-abp-properties(", 
           line
        )

        line = re.sub(
           ":matches-css\(", 
           ":-abp-properties(", 
           line
        )

        line = re.sub(
           r"(^|,)viaplay.\*(#|,)", 
           r"\1viaplay.no,viaplay.dk,viaplay.is\2", 
           line
        )

        line = re.sub(
           r"(^|,)ticketmaster\.\*(#|,)", 
           r"\1ticketmaster.no,ticketmaster.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)qxl\.\*(#|,)", 
           r"\1qxl.no,qxl.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)expedia\.\*(#|,)", 
           r"\1expedia.no,expedia.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)gamereactor\.\*(#|,)", 
           r"\1gamereactor.no,gamereactor.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)viafree\.\*(#|,)", 
           r"\1viafree.no,viafree.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)momondo\.\*(#|,)", 
           r"\1momondo.no,monondo.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)eurosport\.\*(#|,)", 
           r"\1eurosport.no,eurosport.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)prisjakt\.\*(#|,)", 
           r"\1prisjakt.no\2", 
           line
        )

        line = re.sub(
           r"(^|,)180\.\*(#|,)", 
           r"\g<1>180.no,180.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)kimbino\.\*(#|,)", 
           r"\1kimbino.no,kimbino.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)costume\.\*(#|,)", 
           r"\1costume.no,costume.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)manuall\.\*(#|,)", 
           r"\1manuall.no,manuall.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)intrafish\.\*(#|,)", 
           r"\1intrafish.no\2", 
           line
        )

        line = re.sub(
           r"(^|,)blaklader\.\*(#|,)", 
           r"\1blaklader.no,blaklader.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)ehandel\.\*(#|,)", 
           r"\1ehandel.com,ehandel.dk,ehandel.se,ehandel.fi\2", 
           line
        )

        line = re.sub(
           "^,", 
           "^$", 
           line
        )

        line = re.sub(
           ",script,", 
           "$script,", 
           line
        )

        line = re.sub(
           r"! Version: (.*)January(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>01\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)February(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>02\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)March(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>03\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)April(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>04\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)May(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>05\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)June(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>06\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)July(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>07\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)August(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>08\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)September(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>09\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)October(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>10\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)November(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>11\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)December(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>12\2\3", 
           line
        )

        line = re.sub(
           r"(! Title: 🏔️ Dandelion Sprout.*)", 
           r"[Adblock Plus 3.13]\n\1", 
           line
        )

        line = re.sub(
           "redirect=noopjs", 
           "rewrite=abp-resource:blank-js", 
           line
        )

        line = re.sub(
           r"redirect=noopmp[34]-[0]?[.]?1s", 
           r"rewrite=abp-resource:blank-mp3", 
           line
        )

        line = re.sub(
           r"##\+js\(aopw, (.*)\)", 
           r"#$#abort-on-property-write \1", 
           line
        )

        line = re.sub(
           r"##\+js\(aopr, (.*)\)", 
           r"#$#abort-on-property-read \1", 
           line
        )

        line = re.sub(
           r"##\+js\(acis, (.*)\)", 
           r"#$#abort-current-inline-script \1", 
           line
        )

        line = re.sub(
           r"(#\$#.*),", 
           r"\1", 
           line
        )

        line = re.sub(
           r"^!.*PFBLOCKERNG.*", 
           r"", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(1\)", 
           r"\1#?#\2\3*:-abp-has(> \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(2\)", 
           r"\1#?#\2\3*:-abp-has(> * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(3\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(4\)", 
           r"\1#?#\2\3*:-abp-has(> * > * >  * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(5\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(6\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(7\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(8\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(9\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(10\)", 
           r"\1#?#\2\3*:-abp-has(> * > * > * > * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(1\)", 
           r"\1#?#*:-abp-has(> \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(2\)", 
           r"\1#?#*:-abp-has(> * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(3\)", 
           r"\1#?#*:-abp-has(> * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(4\)", 
           r"\1#?#*:-abp-has(> * > * >  * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(5\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(6\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(7\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(8\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(9\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(10\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r".*mm\.dk##\.fadeout.*", 
           r"", 
           line
        )

        line = re.sub(
           r"tipsbladet\.dk###js-promo-welcome", 
           r"", 
           line
        )

        line = re.sub(
           r"([.?]),script", 
           r"\1$script", 
           line
        )

        line = re.sub(
           r"xmlhttprequest\$", 
           r"xmlhttprequest,", 
           line
        )

        line = re.sub(
           r"^!.* Elgiganten .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!.* elko\.is .*", 
           r"", 
           line
        )

        line = re.sub(
           r":remove()", 
           r"", 
           line
        )

        line = re.sub(
           r"##:xpath\((.*)\)$", 
           r"#$#hide-if-matches-xpath \1", 
           line
        )

        line = re.sub(
           r"\$~doc$", 
           r"", 
           line
        )

        line = re.sub(
           r".*\$.*,app=.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^bt\.dk##\.article-container > \.row > \.sidebar$", 
           r"", 
           line
        )

        line = re.sub(
           r":before", 
           r"::before", 
           line
        )

        line = re.sub(
           r":after", 
           r"::after", 
           line
        )

        line = re.sub(
           r"([$,])frame(,|$)", 
           r"\1subdocument\2", 
           line
        )

        line = re.sub(
           r"^! .*HTTPS(,| ).*", 
           r"", 
           line
        )

        line = re.sub(
           r"^! .* CSP .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$empty,", 
           r"$", 
           line
        )

        line = re.sub(
           r"([$,])frame", 
           r"\1subdocument", 
           line
        )

        line = re.sub(
           r"\$mp4", 
           r"$media,rewrite=abp-resource:blank-mp3", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])viafree\.\*", 
           r"\1viafree.no|viafree.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])discoveryplus\.\*(\|~discoveryplus.it\|~discoveryplus.es)?", 
           r"\1discoveryplus.no|discoveryplus.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])auth.discoveryplus\.\*", 
           r"\1auth.discoveryplus.no|auth.discoveryplus.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])gamereactor\.\*", 
           r"\1gamereactor.no|gamereactor.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])eurosport\.\*", 
           r"\1eurosport.no|eurosport.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])eniro\.\*", 
           r"\1eniro.no|eniro.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])proff\.\*", 
           r"\1proff.no|proff.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])partyking\.\*", 
           r"\1partyking.no|partyking.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])blaklader\.\*", 
           r"\1blaklader.no|blaklader.dk", 
           line
        )

        line = re.sub(
           r"\$ghide", 
           r"$generichide", 
           line
        )

        line = re.sub(
           r"\(\)$", 
           r"", 
           line
        )

        line = re.sub(
           r",mp4", 
           r"", 
           line
        )

        line = re.sub(
           r"(.*)\$all", 
           r"\1\n\1$popup", 
           line
        )

        line = re.sub(
           r'(#\?#)([a-z.]{1,}\[.*) (\*:-abp-.*)( [0-9%;"]{1,})', 
           r"\1\3 \2\4", 
           line
        )

        line = re.sub(
           r"#\?#([a-z0-9]{1,}\[[a-z0-9]{1,}[*^$]?=\" )\*:(-abp-)?has\(> ", 
           r"#?#*:has(> \1", 
           line
        )

        if is_supported_abp(line):
            text += line + '\r\n'

    return text

# Attempts to achieve Internet Explorer TPL support
def is_supported_tpl(line) -> bool:
    for token in UNSUPPORTED_TPL:
        if token in line:
            return False

    return True

# function that prepares the filter list for ABP
def prepare_tpl(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           r"^!!? ", 
           r"# ", 
           line
        )

        line = re.sub(
           r"(# Title: 🏔️ Dandelion Sprout.*)", 
           r"msFilterList\n\1", 
           line
        )

        line = re.sub(
           r"^([@][@][|][|])", 
           "+d ", 
           line
        )

        line = re.sub(
           r"^([|][|])", 
           "-d ", 
           line
        )

        line = re.sub(
           r".*\$\$script.*", 
           "-d ", 
           line
        )

        line = re.sub(
           r"^/", 
           "- ", 
           line
        )

        line = re.sub(
           r".*[a-z0-9]//\$.*$", 
           "", 
           line
        )

        line = re.sub(
           r".*\$removeparam.*", 
           "", 
           line
        )

        line = re.sub(
           r".*\$1p$", 
           "", 
           line
        )

        line = re.sub(
           r".*\$1p,.*", 
           "", 
           line
        )

        line = re.sub(
           r".*,1p$", 
           "", 
           line
        )

        line = re.sub(
           r".*,1p,.*", 
           "", 
           line
        )

    # TO-DO: Figure out how to make this NOT apply to lines that have the character "!" in them.
        line = re.sub(
           "/", 
           " ", 
           line
        )

        line = re.sub(
           "\^", 
           "", 
           line
        )

        line = re.sub(
           r"\$.*", 
           "", 
           line
        )

        line = re.sub(
           r"! Redirect:.*", 
           "", 
           line
        )

        line = re.sub(
           "-d \* ", 
           "- ", 
           line
        )

        line = re.sub(
           "-d \.", 
           "- ", 
           line
        )

        line = re.sub(
           "com\* ", 
           "com ", 
           line
        )

        line = re.sub(
           r"([-][d].*[.][*].*)", 
           "", 
           line
        )

        line = re.sub(
           r"@@\*\..*", 
           "", 
           line
        )

        line = re.sub(
           "@@_", 
           "+d _", 
           line
        )

        line = re.sub(
           r"^([+][d][\s][a-z].*[\s][a-z].*)", 
           "", 
           line
        )

        line = re.sub(
           r"^([-][d].*[o|k|m]\.$)", 
           "", 
           line
        )

        line = re.sub(
           r"!#if.*", 
           "", 
           line
        )

        line = re.sub(
           "!#endif", 
           "", 
           line
        )

        line = re.sub(
           "# Expires: ", 
           ": expires = ", 
           line
        )

        line = re.sub(
           r"^\.([d|i|n]).*", 
           "", 
           line
        )

        line = re.sub(
           "^\.", 
           "- ", 
           line
        )

        line = re.sub(
           r"^@@ .*", 
           "", 
           line
        )

        line = re.sub(
           " 1 day", 
           " 1", 
           line
        )

        line = re.sub(
           "# Redirect:.*", 
           "", 
           line
        )

        line = re.sub(
           r"\+d\s[a-z0-9].*\s[a-z0-9*].*", 
           "", 
           line
        )

        line = re.sub(
           "-d.*-\*$", 
           "", 
           line
        )

        line = re.sub(
           r"^-([a-z][a-z])", 
           r"- -\1", 
           line
        )

        line = re.sub(
           r"(# Version: .*[0-9][A-Z].*)", 
           r"\1-Deprecated", 
           line
        )

        line = re.sub(
           r":  (.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r"://(.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r"([a-z])//", 
           r"\1/ ", 
           line
        )

        line = re.sub(
           r"://(.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r"([a-z])//", 
           r"\1/ ", 
           line
        )

        line = re.sub(
           r"://(.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r"([a-z])//", 
           r"\1/ ", 
           line
        )

        line = re.sub(
           r"://(.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r"([a-z])//", 
           r"\1/ ", 
           line
        )

        line = re.sub(
           r"://(.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r"([a-z])//", 
           r"\1/ ", 
           line
        )

        line = re.sub(
           r"://(.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r"([a-z])//", 
           r"\1/ ", 
           line
        )

        line = re.sub(
           r"( \*$)|( \* )", 
           r" ", 
           line
        )

        line = re.sub(
           r" $", 
           r"", 
           line
        )

        line = re.sub(
           r" $", 
           r"", 
           line
        )

        line = re.sub(
           r"(-d .*? ).*? ", 
           r"\1", 
           line
        )

        line = re.sub(
           r"(-d .*? ).*? ", 
           r"\1", 
           line
        )

        line = re.sub(
           r"(-d .*? ).*? ", 
           r"\1", 
           line
        )

        line = re.sub(
           r"(-d .*? ).*? ", 
           r"\1", 
           line
        )

        line = re.sub(
           r"(-d .*? ).*? ", 
           r"\1", 
           line
        )

        line = re.sub(
           r"(-d .*? ).*? ", 
           r"\1", 
           line
        )

        line = re.sub(
           r"(-d .*? ).*? ", 
           r"\1", 
           line
        )

        line = re.sub(
           r'"@@\|\|', 
           '"+d ', 
           line
        )

        line = re.sub(
           r"^(# Description: .*)", 
           r"\1\n# Pretty important note: Documentation for TPL lists is atrociously bad, and often contradict themselves and omit important details. It wasn't until March 2020 that I discovered that TPL lists refuse to block first-party files, making more than half of this list useless, although it may have a slight effect on some newssites. If you just need a browser to play Flash games on, please switch to Waterfox Classic. If you have to use IE at work, you should either install AdGuard for Windows, or quit the job on the spot in protest against ancient technology.", 
           line
        )

        line = re.sub(
           r"^-d finn\.no$", 
           r"", 
           line
        )

        line = re.sub(
           r"^([a-l]|[n-z])(.*)", 
           r"- \1\2", 
           line
        )

        line = re.sub(
           r"!\+.*", 
           r"", 
           line
        )

        line = re.sub(
           r"@@\..* [a-z0-9].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\* ([a-z0-9])", 
           r"- \1", 
           line
        )

        line = re.sub(
           r"^\|([a-z0-9])", 
           r"- \1", 
           line
        )

        line = re.sub(
           r"(.*)check out https://www\.i-dont-care-about-cookies\.eu/", 
           r"\1check out https://easylist-downloads.adblockplus.org/easylist-cookie.tpl (Can also be subscribed to from https://raw.githack.com/collinbarrett/FilterLists/master/data/TPLSubscriptionAssistant.html)", 
           line
        )

        line = re.sub(
           r"\|$", 
           r"", 
           line
        )

        line = re.sub(
           r"^-d jula\.no$", 
           r"", 
           line
        )

        line = re.sub(
           r"^_", 
           r"- _", 
           line
        )

        line = re.sub(
           r"^(-[a-ce-zA-Z0-9])", 
           r"- \1", 
           line
        )

        line = re.sub(
           r"^@@\.", 
           r"+d ", 
           line
        )

        line = re.sub(
           r"([a-z])\* ", 
           r"\1 ", 
           line
        )

        line = re.sub(
           r"^\* ", 
           r"- ", 
           line
        )

        line = re.sub(
           r"^-d ([a-z0-9-]{1,}\.)?(aftenbladet\.no|aftenposten\.no|aksjelive\.no|app\.bankid\.no|av-avis\.no|bergzeit\.dk|bergzeit\.no|billigvvs\.dk|billigvvs\.no|binabnordic\.no|blog\.ncc\.dk|blog\.ncc\.no|bolighed\.dk|broca\.dk|bt\.no|bygdanytt\.no|chevrolet\.dk|chevrolet\.is|chevrolet\.no|completvvs\.dk|computerworld\.dk|cpot\.dk|cpot\.no|cw\.dk|dantonit\.dk|dimensiondesign\.dk|dinepenger\.no|dnbforsikring\.no|e24\.no|ecreo\.dk|fargerike\.no|ferde\.no|finn\.no|flyingblue\.is|flyingblue\.no|flytpass\.no|forsikring-bedrift\.sparebank1\.no|fotoknudsen\.no|fredensgaard-silkeborg\.dk|freelancer\.is|freelancer\.no|godt\.no|greenline\.dk|hammersborg\.no|hansgrohe\.dk|hansgrohe\.no|havnebryggenstigsborg\.dk|helse\.fremtind\.no|hercules\.dk|herculesfundamentering\.no|interhome\.dk|interhome\.no|it-jobbank\.dk|itegra\.no|jabra\.dk|jabra\.no|jobbsafari\.no|jobindex\.dk|jysk\.dk|jysk\.no|komplett\.dk|komplett\.no|komplettbedrift\.no|kontorvaerket\.dk|kundeforsikring\.sparebank1\.no|lampeguru\.dk|lampeguru\.no|lavprisarbejdstoej\.dk|lavprisel\.dk|lavprisvaerktoej\.dk|lavprisvvs\.dk|ledertalentene\.no|live\.bible\.is|machineseeker\.dk|machineseeker\.is|machineseeker\.no|mine24\.no|minmote\.no|minnebanken\.no|nuento\.dk|obos\.no|obosblockwatne\.no|obosopennet\.no|papiroeen-boliger\.dk|pricerunner\.dk|radio\.dk|skovhaven-hadsund\.dk|stepstone\.dk|stigsborg\.dk|storebrand\.no|strilen\.no|teglgaardenaarhus\.dk|tek\.no|tv\.nrk\.no|vestnytt\.no|vg\.no|vgc\.no|vglab\.no|vglive\.no|vgtv\.no|viagogo\.dk|vilmer\.no|wiggle\.dk|airbnb\.dk|airbnb\.is|airbnb\.no|bnbank\.no|lyse\.no|ncc\.dk|ncc\.no|yr\.no|yelp\.dk|yelp\.no)( .*|$)", 
           r"", 
           line
        )

        line = re.sub(
           r".*NorwegianCashbackAssistant.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^-d$", 
           r"", 
           line
        )

        line = re.sub(
           r"^- ://.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^-.*\\\..*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\*.*", 
           r"", 
           line
        )

        if is_supported_tpl(line) and not line == '':
            text += line + '\r\n'

    return text

# ————— Privoxy version —————

def is_supported_privoxy(line) -> bool:
    for token in UNSUPPORTED_PRIVOXY:
        if token in line:
            return False

    return True

def prepare_privoxy(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider", 
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider (for Privoxy)", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Nordic filters for tidier websites", 
           "Dandelion Sprout's Nordic filters for tidier websites (for Privoxy)", 
           line
        )

        line = re.sub(
           r"\$domain=~in-addr\.arpa$", 
           r"", 
           line
        )

        line = re.sub(
           r"(! Version: .*)", 
           r"\1-Deprecated", 
           line
        )

        line = re.sub(
           r"^!", 
           r"#", 
           line
        )

        line = re.sub(
           r"^\|\|([a-z0-9].*\..*/.*)", 
           r"{+block}\n.\1", 
           line
        )

        line = re.sub(
           r"^@@\|\|(.*)", 
           r"{-block}\n.\1", 
           line
        )

        line = re.sub(
           r"^@@/(.*)", 
           r"{-block}\n./\1", 
           line
        )

        line = re.sub(
           r"^@@_(.*)", 
           r"{-block}\n._\1", 
           line
        )

        line = re.sub(
           r"^@@(\..*)", 
           r"{-block}\n\1", 
           line
        )

        line = re.sub(
           r"^# ([a-zA-Z0-9.-]{1,40})$", 
           r"{+block{\1}}", 
           line
        )

        line = re.sub(
           r"^\|\|([a-z0-9].*\..*/.*)", 
           r"{+block}\n.\1", 
           line
        )

        line = re.sub(
           r"^\|\|", 
           r".", 
           line
        )

        line = re.sub(
           r"^\|", 
           r".", 
           line
        )

        line = re.sub(
           r"^/", 
           r"./", 
           line
        )

        line = re.sub(
           r"[$,]3p$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$image$", 
           r"", 
           line
        )

        line = re.sub(
           r"[$,]important$", 
           r"", 
           line
        )

        line = re.sub(
           r"\^", 
           r"", 
           line
        )

        line = re.sub(
           r".*\$app=.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^# (http.*)", 
           r"{+block{\1}}", 
           line
        )

        line = re.sub(
           r"\$doc.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^# (🇬🇧: .*)", 
           r"{+block{\1}}", 
           line
        )

        line = re.sub(
           r"^_", 
           r".*_", 
           line
        )

        line = re.sub(
           r"\$csp.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^#\+.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\*", 
           r".*", 
           line
        )

        line = re.sub(
           r"\$script$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$domain=~(.*)", 
           r"\n{-block}\n.\1\n{+block}", 
           line
        )

        line = re.sub(
           r"\|~", 
           r"\n.", 
           line
        )

        line = re.sub(
           r".*[$,]domain.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\$xhr.*", 
           r"", 
           line
        )

        line = re.sub(
           r"important,([a-z])", 
           r"\1", 
           line
        )

        line = re.sub(
           r"[$,]subdocument$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$script$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$xhr.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*\$object.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\$script,1p$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$3p$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$image$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$all$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$frame$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$3p.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\./.*\\.*", 
           r"", 
           line
        )

        if is_supported_privoxy(line) and not line == '':
          text += line + '\r\n'

    return text

# function that prepares the filter list for a privacy-focused uBO version
def prepare_privacy(lines) -> str:
    text = ''

    for line in lines:

        # until this is done: https://github.com/AdguardTeam/CoreLibs/issues/152
        line = re.sub(
           r"^@.*tradedoubler\.com.*", 
           "", 
           line
        )

        line = re.sub(
           r"^@.*\.zanox\..*", 
           "", 
           line
        )

        line = re.sub(
           r"^@.*/analytics\..*", 
           "", 
           line
        )

        line = re.sub(
           r"^@.*\.adtraction\..*", 
           "", 
           line
        )

        line = re.sub(
           r"^@.*\.adform\..*", 
           "", 
           line
        )

        line = re.sub(
           r"^@.*/autoTrack.*", 
           "", 
           line
        )

        line = re.sub(
           r"^@.*\|\|mparticle\..*", 
           "", 
           line
        )

        line = re.sub(
           r"^@.*\.adobedtm\..*", 
           "", 
           line
        )

        line = re.sub(
           r"^@@_prebid.*", 
           "", 
           line
        )

        line = re.sub(
           r"^@.*\.googleapis\..*", 
           "", 
           line
        )

        line = re.sub(
           r"^@.*widgets\.spklw\..*", 
           "", 
           line
        )

        line = re.sub(
           r"^@@\|\|fe\.adstate\.net.*", 
           "", 
           line
        )

        line = re.sub(
           r"^@@\|\|.*sp-prod\.net.*", 
           "", 
           line
        )

        line = re.sub(
           r"^@.*easy-ads\.com.*", 
           "", 
           line
        )

        line = re.sub(
           r"^@@\|\|api\.instagram\.com.*", 
           "", 
           line
        )

        line = re.sub(
           r".*#@#.*adform\..*", 
           "", 
           line
        )

        line = re.sub(
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider", 
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider (uten sporerhvitelisting)", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Nordic filters for tidier websites", 
           "Dandelion Sprout's Nordic filters for tidier websites (without tracker whitelistings)", 
           line
        )

        line = re.sub(
           r"! If you wish to remove cookie banners.*", 
           "! Warning: This list version does not exchange tracker protection for added browsing convenience, and is for advanced tech users ONLY! Some web stuff that are unbroken by whitelistings in the normal version, are NOT fixed in this version! Additionally, it is only made with uBO and close derivatives in mind.", 
           line
        )

        line = re.sub(
           r"!#include NorwegianExperimentalList%20alternate%20versions/AntiAdblockEntries\.txt", 
           r"", 
           line
        )

        line = re.sub(
           r"^!#include NorwegianExperimentalList%20alternate%20versions/", 
           r"!#include ", 
           line
        )

        text += line + '\r\n'

    return text

# ——— uMatrix version ———

def is_supported_umatrix(line) -> bool:
    for token in UNSUPPORTED_UMATRIX:
        if token in line:
            return False

    return True

def prepare_umatrix(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        # remove $document modifier from the rule
        line = re.sub(
           r"^\*?/.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*\.\*\..*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-zA-Z0-9.|@].*[a-zA-Z0-9]/[a-zA-Z0-9].*", 
           r"", 
           line
        )

        line = re.sub(
           r".*/\*[a-zA-Z0-9*_=/.-].*", 
           r"", 
           line
        )

        line = re.sub(
           r".*\*/.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-zA-Z0-9_-].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|(.*)\^?\$domain=(.*)", 
           r"\2 \1 * block", 
           line
        )

        line = re.sub(
           r"^\|\|(.*)\^?\$(.*),domain=(.*)", 
           r"\3 \1 \2 block", 
           line
        )

        line = re.sub(
           r"^! [a-z0-9—].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!.*—.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|.*\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|(.*)\^?\$([a-z]{1,14})$", 
           r"* \1 \2 block", 
           line
        )

        line = re.sub(
           r"^@@\|\|(.*)\^?\$domain=(.*)", 
           r"\2 \1 * allow", 
           line
        )

        line = re.sub(
           r"^@@\|\|(.*)\^?\$(.*),domain=(.*)", 
           r"\3 \1 \2 allow", 
           line
        )

        line = re.sub(
           r"^@@\|\|(.*)\^?\$([a-z]{1,14})$", 
           r"* \1 \2 allow", 
           line
        )

        line = re.sub(
           r"^\|\|(.*)\^?\$3p$", 
           r"third-party \1 * block", 
           line
        )

        line = re.sub(
           r"^@@\|\|(.*)\^?\$3p$", 
           r"third-party \1 * allow", 
           line
        )

        line = re.sub(
           r"^\|\|(.*)\^?\$(.*),3p", 
           r"third-party \1 \2 block", 
           line
        )

        line = re.sub(
           r"^@@\|\|(.*)\^?\$(.*),3p", 
           r"third-party \1 \2 allow", 
           line
        )

        line = re.sub(
           r"viafree\.\*", 
           r"viafree.no|viafree.dk", 
           line
        )

        line = re.sub(
           r"discoveryplus\.\*", 
           r"discoveryplus.no|discoveryplus.dk", 
           line
        )

        line = re.sub(
           r"auth.discoveryplus\.\*", 
           r"auth.discoveryplus.no|auth.discoveryplus.dk", 
           line
        )

        line = re.sub(
           r"gamereactor\.\*", 
           r"gamereactor.no|gamereactor.dk", 
           line
        )

        line = re.sub(
           r"eurosport\.\*", 
           r"eurosport.no|eurosport.dk", 
           line
        )

        line = re.sub(
           r"eniro\.\*", 
           r"eniro.no|eniro.dk", 
           line
        )

        line = re.sub(
           r"^\|[a-zA-Z0-9].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^@@_.*", 
           r"", 
           line
        )

        line = re.sub(
           r" empty ([ab])", 
           r" * \1", 
           line
        )

        line = re.sub(
           r"([a-z])  ([a-z])", 
           r"\1 \2", 
           line
        )

        line = re.sub(
           r"^([a-zA-Z0-9.-]{4,50})\|([a-zA-Z0-9.-]{4,50})\|([a-zA-Z0-9.|-]{4,300})( .*)", 
           r"\1\4\n\2\4\n\3\4", 
           line
        )

        line = re.sub(
           r"^([a-zA-Z0-9.-]{4,50})\|([a-zA-Z0-9.|-]{4,300})( .*)", 
           r"\1\3\n\2\3", 
           line
        )

        line = re.sub(
           r"\^ ", 
           r" ", 
           line
        )

        line = re.sub(
           r"^(! Version:.*)", 
           r"\1-Alpha", 
           line
        )

        line = re.sub(
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider", 
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider (uMatrix-regler til å benytte sammen med domeneversjonen)", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Nordic filters for tidier websites", 
           "Dandelion Sprout's Nordic filters for tidier websites (uMatrix rules to use together with the raw domains version)", 
           line
        )

        line = re.sub(
           r" media ", 
           r" other ", 
           line
        )

        line = re.sub(
           r"^~(.*) block$", 
           r"\1 allow", 
           line
        )

        line = re.sub(
           r"^@@/.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\* .* all .*", 
           r"", 
           line
        )

        line = re.sub(
           r"(.*)\|~?([a-z0-9.-]{1,}) (.*)", 
           r"\1 \3\n\2 \3", 
           line
        )

        line = re.sub(
           r"^\*[a-z0-9].*", 
           r"", 
           line
        )

        if is_supported_umatrix(line) and not line == '':
            text += line + '\r\n'

    return text

# ——— XUL uBO version ———

# function that prepares the filter list for AdGuard
def prepare_xul(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"(itle:.*Dandelion Sprout.*)", 
           r"\1 (for «uBlock Origin Legacy»)", 
           line
        )

        line = re.sub(
           r":not\(html, body\)", 
           r":not(html):not(body)", 
           line
        )

        line = re.sub(
           r".*\$removeparam.*", 
           r"", 
           line
        )

        line = re.sub(
           r"domain=([a-z0-9-]{1,})\.\*", 
           r"domain=\1.no|\1.dk", 
           line
        )

        line = re.sub(
           r"(^! Version: .*)", 
           r"\1-Beta", 
           line
        )

        line = re.sub(
           r"(^! If you wish to remove cookie banners .*)", 
           r"\1\n! #IStandWithJustOff", 
           line
        )

        line = re.sub(
           r"!#include NorwegianExperimentalList%20alternate%20versions/", 
           r"!#include ", 
           line
        )

        line = re.sub(
           r"^!\+ NOT_OPTIMIZED$", 
           r"", 
           line
        )

        line = re.sub(
           r"\|([a-z0-9.-]{1,})\.\*(\||$)", 
           r"|\1.no|\1.dk\2", 
           line
        )

        line = re.sub(
           r".*\$\$script.*", 
           r"", 
           line
        )

        line = re.sub(
           r":not\((([a-zA-Z0-9.*^~=-]|\[|\]|\"){1,}), (([a-zA-Z0-9.*^~=-]|\[|\]|\"){1,})\)", 
           r":not(\1):not(\3)", 
           line
        )

        line = re.sub(
           r":not\((([a-zA-Z0-9.*^~=-]|\[|\]|\"){1,}), (([a-zA-Z0-9.*^~=-]|\[|\]|\"){1,}), (([a-zA-Z0-9.*^~=-]|\[|\]|\"){1,})\)", 
           r":not(\1):not(\3):not(\5)", 
           line
        )

        line = re.sub(
           r":not\((([a-zA-Z0-9.*^~=-]|\[|\]|\"){1,}), (([a-zA-Z0-9.*^~=-]|\[|\]|\"){1,}), (([a-zA-Z0-9.*^~=-]|\[|\]|\"){1,}), (([a-zA-Z0-9.*^~=-]|\[|\]|\"){1,})\)", 
           r":not(\1):not(\3):not(\5):not(\7)", 
           line
        )

        line = re.sub(
           r"(\$|,)mp4", 
           r"\1redirect=noopmp4", 
           line
        )

        line = re.sub(
           r".*(\$|,)app=.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*##\^.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!#include AntiAdblockEntries\.txt$", 
           r"", 
           line
        )

        text += line + '\r\n'

    return text


if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    ag_filter = prepare_ag(lines)
    abp_filter = prepare_abp(lines)
    tpl_filter = prepare_tpl(lines)
    privoxy_filter = prepare_privoxy(lines)
    privacy_filter = prepare_privacy(lines)
    umatrix_filter = prepare_umatrix(lines)
    xul_filter = prepare_xul(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_AG, "w") as text_file:
        text_file.write(ag_filter)

    with open(OUTPUT_ABP, "w") as text_file:
        text_file.write(abp_filter)

    with open(OUTPUT_TPL, "w") as text_file:
        text_file.write(tpl_filter)

    with open(OUTPUT_PRIVOXY, "w") as text_file:
        text_file.write(privoxy_filter)

    with open(OUTPUT_PRIVACY, "w") as text_file:
        text_file.write(privacy_filter)

    with open(OUTPUT_UMATRIX, "w") as text_file:
        text_file.write(umatrix_filter)

    with open(OUTPUT_XUL, "w") as text_file:
        text_file.write(xul_filter)

    print('The adblocker-based list versions have been generated.')




    import requests
import re

SOURCES = ['https://gitlab.com/DandelionSprout/adfilt/-/raw/master/NorwegianList.txt', 'https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/NordicFilters-NotBrave.txt', 'https://raw.githubusercontent.com/DandelionSprout/Swedish-List-for-Adblock-Plus/main/Swedish%20List%20for%20Adblock%20Plus.txt', 'https://raw.githubusercontent.com/finnish-easylist-addition/finnish-easylist-addition/master/Finland_adb.txt']

UNSUPPORTED_ABP = ['$important', ',important', '$redirect=', ',redirect=',
    ':style', '##+js', '.*#' , 'dk,no##', '!#if', '!#endif', '!+ ', '##^', '!#i', '$app', ':not(:-abp-', ':not(:has','$csp=upgrade-insecure-requests', '$removeparam', 'badfilter']

OUTPUT = 'xyzzyxeyeo.txt'
OUTPUT_ABP = 'NordicFiltersABP-Inclusion.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# ——— Adblock Plus version ———

def is_supported_abp(line) -> bool:
    for token in UNSUPPORTED_ABP:
        if token in line:
            return False

    return True

# function that prepares the filter list for ABP
def prepare_abp(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        # remove $document modifier from the rule
        line = re.sub(
           r"\$doc.*", 
           "", 
           line
        )

        # remove $important modifier from the rule
        line = re.sub(
           r"\$important,", 
           "$", 
           line
        )

        line = re.sub(
           r"([$,])important", 
           "", 
           line
        )

        line = re.sub(
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider", 
           "Dandelion Sprouts helnordiske filtre for ryddigere nettsider (for Adblock Plus - Møter ABP sine inkluderingsregler)",
           line
        )

        line = re.sub(
           "Dandelion Sprout's Nordic filters for tidier websites", 
           "Dandelion Sprout's All-Nordic filters for tidier websites (for Adblock Plus with ABP inclusion compliance)",
           line
        )

        line = re.sub(
           r"^no##.*", 
           "", 
           line
        )

        line = re.sub(
           r"! Redirect:.*", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])xhr", 
           r"\1xmlhttprequest", 
           line
        )

        line = re.sub(
           r"([$,~])3p", 
           r"\1third-party", 
           line
        )

        line = re.sub(
           r"([$,])1p", 
           r"\1~third-party", 
           line
        )

        line = re.sub(
           ":matches-css-before\(", 
           ":-abp-properties(", 
           line
        )

        line = re.sub(
           ":matches-css\(", 
           ":-abp-properties(", 
           line
        )

        line = re.sub(
           r"(^|,)viaplay.\*(#|,)", 
           r"\1viaplay.no,viaplay.dk,viaplay.is\2", 
           line
        )

        line = re.sub(
           r"(^|,)google.\*(#|,)", 
           r"\1google.no,google.dk,google.is\2", 
           line
        )

        line = re.sub(
           r"(^|,)ticketmaster.\*(#|,)", 
           r"\1ticketmaster.no,ticketmaster.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)qxl.\*(#|,)", 
           r"\1qxl.no,qxl.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)expedia.\*(#|,)", 
           r"\1expedia.no,expedia.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)gamereactor.\*(#|,)", 
           r"\1gamereactor.no,gamereactor.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)viafree.\*(#|,)", 
           r"\1viafree.no,viafree.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)momondo.\*(#|,)", 
           r"\1momondo.no,monondo.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)eurosport.\*(#|,)", 
           r"\1eurosport.no,eurosport.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)prisjakt.\*(#|,)", 
           r"\1prisjakt.no\2", 
           line
        )

        line = re.sub(
           r"(^|,)180.\*(#|,)", 
           r"\g<1>180.no,180.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)kimbino.\*(#|,)", 
           r"\1kimbino.no,kimbino.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)costume.\*(#|,)", 
           r"\1costume.no,costume.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)manuall.\*(#|,)", 
           r"\1manuall.no,manuall.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)intrafish.\*(#|,)", 
           r"\1intrafish.no\2", 
           line
        )

        line = re.sub(
           r"(^|,)blaklader.\*(#|,)", 
           r"\1blaklader.no,blaklader.dk\2", 
           line
        )

        line = re.sub(
           r"(^|,)ehandel\.\*(#|,)", 
           r"\1ehandel.com,ehandel.dk,ehandel.se,ehandel.fi\2", 
           line
        )

        line = re.sub(
           "^,", 
           "^$", 
           line
        )

        line = re.sub(
           ",script,", 
           "$script,", 
           line
        )

        line = re.sub(
           r"! Version: (.*)January(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>01\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)February(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>02\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)March(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>03\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)April(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>04\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)May(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>05\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)June(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>06\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)July(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>07\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)August(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>08\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)September(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>09\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)October(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>10\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)November(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>11\2\3", 
           line
        )

        line = re.sub(
           r"! Version: (.*)December(.*)v([0-9][0-9]?)", 
           r"! Version: \g<1>12\2\3", 
           line
        )

        line = re.sub(
           r"^(! Title: 🏔️ Dandelion Sprout.*)", 
           r"[Adblock Plus 3.13]\n\1", 
           line
        )

        line = re.sub(
           "redirect=noopjs", 
           "rewrite=abp-resource:blank-js", 
           line
        )

        line = re.sub(
           r"redirect=noopmp[34]-[0]?[.]?1s", 
           r"rewrite=abp-resource:blank-mp3", 
           line
        )

        line = re.sub(
           r"(#\$#.*),", 
           r"\1", 
           line
        )

        line = re.sub(
           r"^!.*PFBLOCKERNG.*", 
           r"", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(1\)", 
           r"\1#?#\2\3*:has(> \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(2\)", 
           r"\1#?#\2\3*:has(> * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(3\)", 
           r"\1#?#\2\3*:has(> * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(4\)", 
           r"\1#?#\2\3*:has(> * > * >  * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(5\)", 
           r"\1#?#\2\3*:has(> * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(6\)", 
           r"\1#?#\2\3*:has(> * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(7\)", 
           r"\1#?#\2\3*:has(> * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(8\)", 
           r"\1#?#\2\3*:has(> * > * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(9\)", 
           r"\1#?#\2\3*:has(> * > * > * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*)( |\|)(.*):(upward|nth-ancestor)\(10\)", 
           r"\1#?#\2\3*:has(> * > * > * > * > * > * > * > * > * > \4)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(1\)", 
           r"\1#?#*:has(> \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(2\)", 
           r"\1#?#*:has(> * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(3\)", 
           r"\1#?#*:has(> * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(4\)", 
           r"\1#?#*:has(> * > * >  * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(5\)", 
           r"\1#?#*:has(> * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(6\)", 
           r"\1#?#*:has(> * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(7\)", 
           r"\1#?#*:has(> * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(8\)", 
           r"\1#?#*:has(> * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(9\)", 
           r"\1#?#*:has(> * > * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(10\)", 
           r"\1#?#*:has(> * > * > * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r".*mm\.dk##\.fadeout.*", 
           r"", 
           line
        )

        line = re.sub(
           r"tipsbladet\.dk###js-promo-welcome", 
           r"", 
           line
        )

        line = re.sub(
           r"([.?]),script", 
           r"\1$script", 
           line
        )

        line = re.sub(
           r"xmlhttprequest\$", 
           r"xmlhttprequest,", 
           line
        )

        line = re.sub(
           r"^!.* Elgiganten .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!.* elko\.is .*", 
           r"", 
           line
        )

        line = re.sub(
           r":remove()", 
           r"", 
           line
        )

        line = re.sub(
           r"##:xpath\((.*)\)$", 
           r"#$#hide-if-matches-xpath \1", 
           line
        )

        line = re.sub(
           r"(samebefolkningen\.)", 
           r"\1 Denne versjonen av listen inkluderer ikke anti-anti-reklameblokkering, ettersom slike oppføringer ikke er tillatt for lister som er inkludert i Adblock Plus.", 
           line
        )

        line = re.sub(
           r"(samiske befolkning\.)", 
           r"\1 Den her listeversion indeholder ikke anti-anti-reklameblokkering, eftersom sådanne opføringer ikke er tilladt for lister, der er inkluderet i Adblock Plus.", 
           line
        )

        line = re.sub(
           r"(samefolkesetnadene\.)", 
           r"\1 Denne versjonen av lista inneheld ikkje anti-anti-reklameblokkering, sidan slike oppføringer ikkje er tillete for listar som er inkludert i Adblock Plus.", 
           line
        )

        line = re.sub(
           r"(indigenous population\.)", 
           r"\1 This list version does not contain anti-anti-adblocking, due to how such entries are not allowed in lists that are included in Adblock Plus.", 
           line
        )

        line = re.sub(
           r".*\$\$script.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\$~doc$", 
           r"", 
           line
        )

        line = re.sub(
           r".*\$.*,app=.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^bt\.dk##\.article-container > \.row > \.sidebar$", 
           r"", 
           line
        )

        line = re.sub(
           r":before", 
           r"::before", 
           line
        )

        line = re.sub(
           r":after", 
           r"::after", 
           line
        )

        line = re.sub(
           r"([$,])frame(,|$)", 
           r"\1subdocument\2", 
           line
        )

        line = re.sub(
           r"^ekstrabladet\.dk##a\[href\^=\"https://click-dk\.plista\.com/csc\?\"\]$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! .*HTTPS(,| ).*", 
           r"", 
           line
        )

        line = re.sub(
           r"^! .* CSP .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$empty,", 
           r"$", 
           line
        )

        line = re.sub(
           r"^telenor\.no##\.global-overlay-background$", 
           r"", 
           line
        )

        line = re.sub(
           r"([$,])frame", 
           r"\1subdocument", 
           line
        )

        line = re.sub(
           r"\$mp4", 
           r"$media,rewrite=abp-resource:blank-mp3", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])viafree\.\*", 
           r"\1viafree.no|viafree.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])discoveryplus\.\*", 
           r"\1discoveryplus.no|discoveryplus.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])auth.discoveryplus\.\*", 
           r"\1auth.discoveryplus.no|auth.discoveryplus.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])gamereactor\.\*", 
           r"\1gamereactor.no|gamereactor.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])eurosport\.\*", 
           r"\1eurosport.no|eurosport.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])eniro\.\*", 
           r"\1eniro.no|eniro.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])proff\.\*", 
           r"\1proff.no|proff.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])partyking\.\*", 
           r"\1partyking.no|partyking.dk", 
           line
        )

        line = re.sub(
           r"([a-z*][=|])blaklader\.\*", 
           r"\1blaklader.no|blaklader.dk", 
           line
        )

        line = re.sub(
           r"\$ghide", 
           r"$generichide", 
           line
        )

        line = re.sub(
           r"\(\)$", 
           r"", 
           line
        )

        line = re.sub(
           r",mp4", 
           r"", 
           line
        )

        line = re.sub(
           r"^\[Adblock Plus [1-3]\.[0-6]\]$", 
           r"", 
           line
        )

        line = re.sub(
           r"(.*)\$all", 
           r"\1\n\1$popup", 
           line
        )

        line = re.sub(
           r'(#\?#)([a-z.]{1,}\[.*) (\*:-abp-.*)( [0-9%;"]{1,})', 
           r"\1\3 \2\4", 
           line
        )

        line = re.sub(
           r"og samebefolkningen\.", 
           r"samebefolkningen, Sverige, og Finland.", 
           line
        )

        line = re.sub(
           r"og den samiske befolkning\.", 
           r"den samiske befolkning, Sverige, og Finland.", 
           line
        )

        line = re.sub(
           r"og samefolkesetnadene\.", 
           r"samefolkesetnadene, Sverige, og Finland.", 
           line
        )

        line = re.sub(
           r"and the Sami indigenous population\.", 
           r"the Sami indigenous population, Sweden, and Finland.", 
           line
        )

        line = re.sub(
           r"! Homepage: https://github\.com/finnish-easylist-addition/finnish-easylist-addition", 
           r"! Finnish section's homepage: https://github.com/finnish-easylist-addition/finnish-easylist-addition", 
           line
        )

        line = re.sub(
           r"! Homepage: https://github\.com/DandelionSprout/Swedish-List-for-Adblock-Plus", 
           r"! Swedish section's homepage: https://github.com/DandelionSprout/Swedish-List-for-Adblock-Plus", 
           line
        )

        line = re.sub(
           r"^[a-z0-9^|.$:/=-]{1,5}$", 
           r"", 
           line
        )

        line = re.sub(
           r" $", 
           r"", 
           line
        )

        line = re.sub(
           r"^(! 🇳🇴🏞: Denne lista .*)", 
           r"\1\n! 🇸🇪: Listan omfattar webbplatser för Norge, Danmark, Island, danska territorier, Schleswig-Holsteins danska minoritet, den samiska ursprungsbefolkningen, Sverige och Finland. Denna versionen av listan innehåller inte anti-anti-reklamblockering, eftersom sådana poster inte är tillåtna i listor som ingår i Adblock Plus. För mer information, detaljer, hjälpmedel och andra listor som jag har gjort, besök https://github.com/DandelionSprout/adfilt/blob/master/Wiki/General-info.md#english\n! 🇫🇮: Tämä lista kattaa suomen-, ruotsin-, norjan-, tanskan-, islannin- ja saamenkieliset verkkosivustot. Tämä lista ei poista sivustoilla olevia mainoseston torjujia, koska Adblock Plus ei salli sellaista sisäänrakennetuissa listoissaan. Lisätietoja, yksityiskohtia, hyödyllisiä työkaluja ja muita tekemiäni listoja löytyy täältä: https://github.com/DandelionSprout/adfilt/blob/master/Wiki/General-info.md#suomi", 
           line
        )

        line = re.sub(
           r"^(! 🇳🇴: Generelle #-oppføringer.*)", 
           r"\1\n! 🇸🇪: Generella #-poster med källor\n! 🇫🇮: Yleiset #-merkinnät, joilla on lähteitä", 
           line
        )

        line = re.sub(
           r"^(! 🇳🇴: Generelle oppføringer.*)", 
           r"\1\n! 🇸🇪: Generella poster med källor\n! 🇫🇮: Yleiset merkinnät, joilla on lähteitä", 
           line
        )

        line = re.sub(
           r"#\?#([a-z0-9]{1,}\[[a-z0-9]{1,}[*^$]?=\" )\*:(-abp-)?has\(> ", 
           r"#?#*:has(> \1", 
           line
        )

        if is_supported_abp(line):
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    abp_filter = prepare_abp(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_ABP, "w") as text_file:
        text_file.write(abp_filter)

    print('The Eyeo list version has been generated.')





import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/DandelionSproutsNorskeFiltreDomains.txt']

UNSUPPORTED_HOSTS = ['*', '# ———']
UNSUPPORTED_LS = ['*', '# ———', '# Translated title', '# Version', 'Don\'t be worried', 'General-info', '# Platform notes:']
UNSUPPORTED_DNSMASQ = ['*', '# ']
UNSUPPORTED_DOMAINSALLOWLIST = ['randomplaceholdertext']

OUTPUT = 'xyzzyxdomains.txt'
OUTPUT_HOSTS = 'AdawayHosts'
OUTPUT_LS = 'LittleSnitchNorwegianList.lsrules'
OUTPUT_DNSMASQ = 'NordicFiltersDnsmasq.conf'
OUTPUT_HOSTSDENY = 'NordicFiltersHostsDeny.deny'
OUTPUT_PIHOLE = 'NordicFiltersPiHole.txt'
OUTPUT_AGH = 'NordicFiltersAdGuardHome.txt'
OUTPUT_SHADOWSOCKS = 'NordicFiltersSocks5.list'
OUTPUT_RPZ = 'NordicFiltersRPZ.txt'
OUTPUT_UNBOUND = 'NordicFiltersUnbound.conf'
OUTPUT_MINERBLOCK = 'NordicFiltersForMinerBlock.txt'
OUTPUT_HOSTSIPV6 = 'NordicFiltersHostsIPv6.txt'
OUTPUT_DOMAINSALLOWLIST = 'NordicFiltersDomainsAllowlist.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# ————— .\hosts version —————

def is_supported_hosts(line) -> bool:
    for token in UNSUPPORTED_HOSTS:
        if token in line:
            return False

    return True

def prepare_hosts(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           r"^(?!#)", 
           "127.0.0.1 ", 
           line
        )

        line = re.sub(
           r"127\.0\.0\.1 $", 
           "", 
           line
        )

        line = re.sub(
           "📔 Dandelion Sprouts nordiske filtre \(Domenelisteversjonen\)", 
           "Dandelion Sprouts nordiske filtre («hosts»-versjonen)", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Nordic Filters \(The domains list version\)", 
           "Dandelion Sprout's Nordic Filters (The «hosts» file version)", 
           line
        )

        line = re.sub(
           r"# Platform notes:.*", 
           "# Platform notes: This list version is intended for tools that deal with so-called «hosts» system files, including pfBlockerNG, Gas Mask, Diversion, Hosts File Editor, and many others; as well as those who edit their OS' «hosts» system file.\n# If you use a tool that edits the system's own hosts file, such as Hosts File Editor, Gas Mask, or Magisk Manager, make sure to also use the IPv6 version at https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/NordicFiltersHostsIPv6.txt", 
           line
        )

        line = re.sub(
           r"^(127\.0\.0\.1) (.*)", 
           r"\1 \2 www.\2", 
           line
        )

        line = re.sub(
           r"([a-z]) www\.www\..*", 
           r"\1", 
           line
        )

        line = re.sub(
           r" www\.[1-2]?[0-9]{1,2}\.[1-2]?[0-9]{1,2}\.[1-2]?[0-9]{1,2}\.[1-2]?[0-9]{1,2}", 
           r"", 
           line
        )

        line = re.sub(
           r" www\.[0-9a-f:]{6,71}$", 
           r"", 
           line
        )

        line = re.sub(
           r"127\.0\.0\.1 [!/].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^127\.0\.0\.1 .*/.*", 
           r"", 
           line
        )

        if is_supported_hosts(line):
            text += line + '\r\n'

    return text

# ————— Little Snitch version —————

def is_supported_ls(line) -> bool:
    for token in UNSUPPORTED_LS:
        if token in line:
            return False

    return True

def prepare_ls(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           r"^(?!#)", 
           "{ \"action\": \"deny\", \"process\": \"any\", \"remote-domains\": \"", 
           line
        )

        line = re.sub(
           r"{ \"action\": \"deny\", \"process\": \"any\", \"remote-domains\": \"$", 
           "", 
           line
        )

        line = re.sub(
           r"^# Title:.*", 
           "{ \"title\": \"👒 Dandelion Sprout's Nordic List for LS\",", 
           line
        )

        line = re.sub(
           r"^# Description:.*", 
           "\"description\": \"This list aims to block Norwegian, Danish, Icelandic and Faroese scam sellers, ad servers, and a small handful of tracking servers.\",\n\"rules\": [", 
           line
        )

        line = re.sub(
           r"(.*\..*[a-z0-9]$)", 
           r"\1\" },", 
           line
        )

        line = re.sub(
           "(.*\..*[a-z0-9])\\\"", 
           r"\1\\", 
           line
        )

        line = re.sub(
           "\\\"\"", 
           "\"", 
           line
        )

        line = re.sub(
           r"([a-z0-9])\\", 
           r"\1", 
           line
        )

        line = re.sub(
           r"remote-domains(\": \"[0-9.]{7,15}\")", 
           r"remote-addresses\1", 
           line
        )

        line = re.sub(
           r".*remote-domains(\": \"[0-9a-f:]{4,39})$", 
           r'', 
           line
        )

        line = re.sub(
           r"{ \"action\": \"deny\", \"process\": \"any\", \"remote-domains\": \"!", 
           r'{ "action": "allow", "process": "any", "remote-domains": "', 
           line
        )

        line = re.sub(
           r"(\"annonser\.gess\.no\") },", 
           r'\1 }\n]}', 
           line
        )

        line = re.sub(
           r'.*remote-domains": "/.*', 
           r'', 
           line
        )

        if is_supported_ls(line):
            text += line + '\r\n'

    return text

# ————— dnsmasq version —————

def is_supported_dnsmasq(line) -> bool:
    for token in UNSUPPORTED_DNSMASQ:
        if token in line:
            return False

    return True

def prepare_dnsmasq(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           r"^(?!#)", 
           "server=/", 
           line
        )

        line = re.sub(
           r"(.*\..*[a-z]$)", 
           r"\1/127.0.0.1", 
           line
        )

        line = re.sub(
           r"server=/$", 
           "", 
           line
        )

        line = re.sub(
           r"server=/([1-2]?[0-9]?[0-9])\.([1-2]?[0-9]?[0-9])\.([1-2]?[0-9]?[0-9])\.([1-2]?[0-9]?[0-9])$", 
           r"server=/\4.\3.\2.\1.in-addr.arpa/127.0.0.1", 
           line
        )

        line = re.sub(
           r".*=/[0-9a-f:]{6,71}$", 
           r"", 
           line
        )

        line = re.sub(
           r"server=/!(.*)/127\.0\.0\.1$", 
           r"server=/\1/89.233.43.71", 
           line
        )

        line = re.sub(
           r"^server=//.*", 
           r"", 
           line
        )

        if is_supported_dnsmasq(line) and not line == '':
            text += line + '\r\n'

    return text

# ————— hosts.deny version —————

def prepare_hostsdeny(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           r"^(?!#)", 
           "ALL: ", 
           line
        )

        line = re.sub(
           r"^ALL: $", 
           "", 
           line
        )

        line = re.sub(
           r" Dandelion Sprouts nordiske filtre.*", 
           " Dandelion Sprouts nordiske filtre («hosts.deny»-versjonen)", 
           line
        )

        line = re.sub(
           r" Dandelion Sprout's Nordic Filters.*", 
           " Dandelion Sprout's Nordic Filters (The «hosts.deny» version)", 
           line
        )

        line = re.sub(
           r"# Platform notes:.*", 
           "# Platform notes: This list version is intended for those who still use a Linux system function called «hosts.deny».", 
           line
        )

        line = re.sub(
           r"(# Version: .*)", 
           r"\1-Beta", 
           line
        )

        line = re.sub(
           r"ALL: [!/].*", 
           r"", 
           line
        )

        if is_supported_hosts(line):
            text += line + '\r\n'

    return text

# ————— Pi-hole version —————

def prepare_pihole(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r" Dandelion Sprouts nordiske filtre.*", 
           " Dandelion Sprouts nordiske filtre (for Pi-hole)", 
           line
        )

        line = re.sub(
           r" Dandelion Sprout's Nordic Filters.*", 
           " Dandelion Sprout's Nordic Filters (for Pi-hole)", 
           line
        )

        line = re.sub(
           r"# Platform notes:.*", 
           "# Platform notes: This list version is intended for those who make use of the Regex functionality in Pi-Hole. It is strongly recommended to also add the whitelist at https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/NordicFiltersDomainsAllowlist.txt as a whitelist.", 
           line
        )

        line = re.sub(
           r"(# Version: .*)", 
           r"\1-Alpha", 
           line
        )

        line = re.sub(
           r"^([a-z0-9].*)\.(.*)\.\*", 
           r"(.*\.)?\1\\.\2\\..*$", 
           line
        )

        line = re.sub(
           r"^([a-z0-9].*)\.\*$", 
           r"(.*\.)?\1\\..*$", 
           line
        )

        line = re.sub(
           r"^(.*)\.(.*)-\*", 
           r"(.*\.)?\1\\.\2-*$", 
           line
        )

        line = re.sub(
           r"^([a-z0-9].*)\.\*\.(.*)", 
           r"(.*\.)?\1\\..*\\.\2$", 
           line
        )

        line = re.sub(
           r"^\*\.(.*)\.\*", 
           r"(.*\.)?*\\.\1\\..*$", 
           line
        )

        line = re.sub(
           r"^([a-z0-9].*)\*\.(.*)", 
           r"(.*\.)?\1.*\\.\2$", 
           line
        )

        line = re.sub(
           r"(\(\.\*\\\.\)\?){2}", 
           r"(.*\.)?", 
           line
        )

        line = re.sub(
           r"^\*\.(.*)\.(.*)$", 
           r".*\.\1\.\2$", 
           line
        )

        line = re.sub(
           r"^/(.*)/$", 
           r"\1", 
           line
        )

        line = re.sub(
           r"^([a-z0-9-]{1,})\*([a-z0-9-]{1,})\.([a-z]{2,17})$", 
           r"(.*\\.)?\1.*\2\\.\3$", 
           line
        )

        line = re.sub(
           r"^\*(-[a-z0-9]{1,})\.\*\.([a-z]{2,17})$", 
           r"(.*\\.)?\1\\..*\\.\2$", 
           line
        )

        line = re.sub(
           r"([a-z0-9])\\\\\.", 
           r"\1\.", 
           line
        )

        line = re.sub(
           r"\*\$\\", 
           r".*\\", 
           line
        )

        line = re.sub(
           r"^![a-z0-9*].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^# ——— (Centralised whitelist section|By default, the entries below will only).*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[0-9].*/.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^(\*[a-z0-9].*)\.", 
           r".\1\\.", 
           line
        )

        line = re.sub(
           r"^(\*-.*)\.", 
           r".\1\\.", 
           line
        )

        line = re.sub(
           r"^((\(|\.).*[a-z0-9])\.([a-z0-9])", 
           r"\1\\.\3", 
           line
        )

        line = re.sub(
           r"([a-z0-9-])\*$", 
           r"\1.*", 
           line
        )

        text += line + '\r\n'

    return text

# ————— AdGuard Home version —————

def prepare_agh(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r" Dandelion Sprouts nordiske filtre.*", 
           " Dandelion Sprouts nordiske filtre (for AdGuard Home, og for AdGuard for Android/Windows sine DNS-filtreringer)", 
           line
        )

        line = re.sub(
           r" Dandelion Sprout's Nordic Filters.*", 
           " Dandelion Sprout's Nordic Filters (for AdGuard Home, and for AdGuard for Android/Windows' DNS filtering)", 
           line
        )

        line = re.sub(
           r"# Platform notes:.*", 
           "# Platform notes: This list version is intended for those who use AdGuard Home and its oddly specific subset of adblocker syntaxes.", 
           line
        )

        line = re.sub(
           r"^([a-z0-9*].*)$", 
           r"||\1^", 
           line
        )

        line = re.sub(
           r"^([a-z0-9*].*)$", 
           r"||\1^", 
           line
        )

        line = re.sub(
           r"^\|\|(([1-2]?[0-9]?[0-9]\.?){4})\^", 
           r"\1", 
           line
        )

        line = re.sub(
           r"\.\*\^$", 
           r".", 
           line
        )

        line = re.sub(
           r"\*\^$", 
           r"*", 
           line
        )

        line = re.sub(
           r"^\|\|([0-9a-f:]{6,71})\^", 
           r"\1", 
           line
        )

        line = re.sub(
           r"^\|\|\*\.", 
           r".", 
           line
        )

        line = re.sub(
           r"^!([a-z0-9].*)", 
           r"@@||\1^", 
           line
        )

        line = re.sub(
           r"^\.", 
           r"||", 
           line
        )

        line = re.sub(
           r".*without modification .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|annonser?\.[a-z0-9-]{2,50}\.no\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|ad\.[a-z0-9-]{2,50}\.no\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|ad1\.[a-z0-9-]{2,50}\.dk\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|ads\.[a-z0-9-]{2,50}\.no\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|ads\.[a-z0-9-]{2,50}\.dk\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|ads\.[a-z0-9-]{2,50}\.is\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|adserver\.[a-z0-9-]{2,50}\.dk\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|banner\.[a-z0-9-]{2,50}\.no\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|advert(isement)?\.[a-z0-9-]{2,50}\.no\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|auglysingar\.[a-z0-9-]{2,50}\.is\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|mobilannonce\.[a-z0-9-]{2,50}\.dk\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|\*", 
           r"", 
           line
        )

        line = re.sub(
           r"\|\|prod-adops-proxy.dnitv.net\^", 
           r"||prod-adops-proxy.dnitv.net^$ctag=os_android|os_ios|device_tv", 
           line
        )

        line = re.sub(
           r"\.(no|dk|is)\.$", 
           r".\1.$dnstype=~CNAME", 
           line
        )

        line = re.sub(
           r"^!\*\.([a-z0-9].*)", 
           r"@@||\1^", 
           line
        )

        text += line + '\r\n'

    return text

# ————— Shadowsocks version —————

def prepare_shadowsocks(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r" Dandelion Sprouts nordiske filtre.*", 
           " Dandelion Sprouts nordiske filtre (for Shadowsocks)", 
           line
        )

        line = re.sub(
           r" Dandelion Sprout's Nordic Filters.*", 
           " Dandelion Sprout's Nordic Filters (for Shadowsocks)", 
           line
        )

        line = re.sub(
           r"# Platform notes:.*", 
           "# Platform notes: This list version is intended for those who use Shadowsocks, Shadowrocket, Surge, and other Socks5-based tools that have become popular in PR-China for several reasons.", 
           line
        )

        line = re.sub(
           r"(# Version: .*)", 
           r"\1-Alpha", 
           line
        )

        line = re.sub(
           r"^([a-z0-9].*?\.[a-z0-9].*?\.[a-z].*)$", 
           r"DOMAIN,\1", 
           line
        )

        line = re.sub(
           r"^([^D].*)\.\*.*\.(.*)", 
           r"URL-REGEX,^https?:\\/\\/\1\\.*\\.\2", 
           line
        )

        line = re.sub(
           r"^([^DU].*?\.[a-z]{2,6})$", 
           r"DOMAIN-SUFFIX,\1", 
           line
        )

        line = re.sub(
           r"^([a-z0-9].*)\.(.*)\.\*", 
           r"URL-REGEX,^https?:\\/\\/\1\\.\2\\.*", 
           line
        )

        line = re.sub(
           r"^([a-z0-9].*)\.(.*)-\*$", 
           r"URL-REGEX,^https?:\\/\\/\1\\.\2-*", 
           line
        )

        line = re.sub(
           r"^([a-z0-9].*)\.\*\.(.*)", 
           r"URL-REGEX,^https?:\\/\\/\1\\.*\\.\2", 
           line
        )

        line = re.sub(
           r"^\*\.(.*)\.\*", 
           r"URL-REGEX,^https?:\\/\\/\*\\.\1\\.*", 
           line
        )

        line = re.sub(
           r"^([a-z0-9].*)\.\*$", 
           r"URL-REGEX,^https?:\\/\\/\1\\.*", 
           line
        )

        line = re.sub(
           r"^(([1-2]?[0-9]?[0-9]\.?){4})$", 
           r"IP-CIDR,\1/32,REJECT,no-resolve", 
           line
        )

        line = re.sub(
           r"^DOMAIN(.*),(.*)\*\.([a-z]{2,17})$", 
           r"URL-REGEX,^https?:\\/\\/\2.*\\.\3", 
           line
        )

        line = re.sub(
           r"^([0-9a-f:]{6,71})$", 
           r"IP-CIDR6,\1/64,REJECT,no-resolve", 
           line
        )

        line = re.sub(
           r"^DOMAIN-SUFFIX,\*\.", 
           r"DOMAIN-SUFFIX,", 
           line
        )

        line = re.sub(
           r"^([a-z]{10,25})\*\.([a-z]{2,17})$", 
           r"URL-REGEX,^https?:\\/\\/\1\\*\\.\2", 
           line
        )

        line = re.sub(
           r"DOMAIN-SUFFIX,!(.*)", 
           r"DOMAIN-SUFFIX,\1,resolve", 
           line
        )

        line = re.sub(
           r"URL-REGEX,(\^https\?:\\/\\/)!(.*)", 
           r"URL-REGEX,\1\2,resolve", 
           line
        )

        line = re.sub(
           r".*without modification .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^/(.*)/$", 
           r"URL-REGEX,\1", 
           line
        )

        text += line + '\r\n'

    return text

# ————— RPZ version —————

def prepare_rpz(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"(# Version: .*)", 
           r"\1-Alpha", 
           line
        )

        line = re.sub(
           r"^([a-z0-9*].*)", 
           r"\1 CNAME .", 
           line
        )

        line = re.sub(
           r"# Platform notes:.*", 
           "; Platform notes: This list version is intended for those who use BIND or other DNS server tools that support RPZ files.", 
           line
        )

        line = re.sub(
           r"^# ", 
           "; ", 
           line
        )

        line = re.sub(
           r" Dandelion Sprouts nordiske filtre.*", 
           " Dandelion Sprouts nordiske filtre (for BIND/RPZ)", 
           line
        )

        line = re.sub(
           r" Dandelion Sprout's Nordic Filters.*", 
           " Dandelion Sprout's Nordic Filters (for BIND/RPZ)", 
           line
        )

        line = re.sub(
           r"^!([a-z0-9].*)", 
           r"\1 CNAME rpz-passthru.", 
           line
        )

        line = re.sub(
           r".*without modification .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^/.*", 
           r"", 
           line
        )

        text += line + '\r\n'

    return text

# ————— Unbound version —————

def prepare_unbound(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"(# Version: .*)", 
           r"\1-Alpha", 
           line
        )

        line = re.sub(
           r"^([a-z0-9*].*)", 
           r"local-zone: \"\1\" static", 
           line
        )

        line = re.sub(
           r"\\", 
           r"", 
           line
        )

        line = re.sub(
           r"# Platform notes:.*", 
           "# Platform notes: This list version is intended for those who use the DNS server tool Unbound.", 
           line
        )

        line = re.sub(
           r" Dandelion Sprouts nordiske filtre.*", 
           " Dandelion Sprouts nordiske filtre (for Unbound)", 
           line
        )

        line = re.sub(
           r" Dandelion Sprout's Nordic Filters.*", 
           " Dandelion Sprout's Nordic Filters (for Unbound)", 
           line
        )

        line = re.sub(
           r"^!([a-z0-9].*)", 
           r'local-zone: "\1" transparent', 
           line
        )

        line = re.sub(
           r".*without modification .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^/.*", 
           r"", 
           line
        )

        text += line + '\r\n'

    return text

# ————— MinerBlock version —————

def prepare_minerblock(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"(# Version: .*)", 
           r"\1-Alpha", 
           line
        )

        line = re.sub(
           r"^([a-z0-9*].*)", 
           r"*://*.\1/*", 
           line
        )

        line = re.sub(
           r"# Platform notes:.*", 
           "# Platform notes: So, let's say your company boss is not letting you install any adblocker on your awful work laptop, but (s)he lets you install MinerBlock for some indeterminable reason? In this very unlikely case, I've saved your day.\n# Note: This list does not actually block any mining-related stuff.", 
           line
        )

        line = re.sub(
           r" Dandelion Sprouts nordiske filtre.*", 
           " Dandelion Sprouts nordiske filtre (for MinerBlock)", 
           line
        )

        line = re.sub(
           r" Dandelion Sprout's Nordic Filters.*", 
           " Dandelion Sprout's Nordic Filters (for MinerBlock)", 
           line
        )

        line = re.sub(
           r"(.*For more information and .*)", 
           r"\1\n# PSA: I am currently considering adding entries for filepaths from the uBO version, in addition to the existing entries taken from the raw-domains version. However, to do so, it'd take me an hour of heavy work to modify the conversion script, so first I'd want to know if anyone are actually using this list version in their daily lives, to help motivate me to do this. If you do use it actively, go to https://github.com/DandelionSprout/adfilt/issues/new/choose, choose whatever option, and explain to me that you're using the minerBlock list version and how.", 
           line
        )

        line = re.sub(
           r"^\*://\*\.\*\.", 
           r"*://*.", 
           line
        )

        line = re.sub(
           r"^/.*", 
           r"", 
           line
        )

        text += line + '\r\n'

    return text

# ————— IPv6 .\hosts version —————

def prepare_hostsipv6(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           r"^(?!#)", 
           ":: ", 
           line
        )

        line = re.sub(
           r":: $", 
           "", 
           line
        )

        line = re.sub(
           "📔 Dandelion Sprouts nordiske filtre \(Domenelisteversjonen\)", 
           "Dandelion Sprouts nordiske filtre (IPv6-«hosts»-versjonen)", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Nordic Filters \(The domains list version\)", 
           "Dandelion Sprout's Nordic Filters (The IPv6 «hosts» file version)", 
           line
        )

        line = re.sub(
           r"# Platform notes:.*", 
           "# Platform notes: This list version is meant to be used simultaneously of the regular «Hosts» version when using computer/Android system hosts file editors like Hosts File Editor, Gas Mask, Magisk Manager, etc. It is not needed for tools that strip away the entries' IP address, such as Blokada and pfBlockerNG.", 
           line
        )

        line = re.sub(
           r"^(::) (.*)", 
           r"\1 \2 www.\2", 
           line
        )

        line = re.sub(
           r"([a-z]) www\.www\..*", 
           r"\1", 
           line
        )

        line = re.sub(
           r" www\.[1-2]?[0-9]{1,2}\.[1-2]?[0-9]{1,2}\.[1-2]?[0-9]{1,2}\.[1-2]?[0-9]{1,2}", 
           r"", 
           line
        )

        line = re.sub(
           r" www\.[0-9a-f:]{6,71}$", 
           r"", 
           line
        )

        line = re.sub(
           r"^:: [!/].*", 
           r"", 
           line
        )

        if is_supported_hosts(line):
            text += line + '\r\n'

    return text

# ————— Domains whitelist version —————

def is_supported_domainsallowlist(line) -> bool:
    for token in UNSUPPORTED_DOMAINSALLOWLIST:
        if token in line:
            return False

def prepare_domainsallowlist(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"(# Version: .*)", 
           r"\1-Beta", 
           line
        )

        line = re.sub(
           r"# Platform notes:.*", 
           "# Platform notes: This list version is intended for users of Pi-hole, Blokada and DNS66, as a recommended supplement to their regular list versions. For AdGuard Home, the allowlistings are already incorporated in its regular list version.", 
           line
        )

        line = re.sub(
           r" Dandelion Sprouts nordiske filtre.*", 
           " Dandelion Sprouts nordiske filtre (Domenehviteliste)", 
           line
        )

        line = re.sub(
           r" Dandelion Sprout's Nordic Filters.*", 
           " Dandelion Sprout's Nordic Filters (Domains allowlist)", 
           line
        )

        line = re.sub(
           r"^[a-z0-9*/].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^# ——— .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!([a-z0-9*])", 
           r"\1", 
           line
        )

        if not line == '':    
            text += line + '\r\n'
        
    return text


if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    hosts_filter = prepare_hosts(lines)
    ls_filter = prepare_ls(lines)
    dnsmasq_filter = prepare_dnsmasq(lines)
    hostsdeny_filter = prepare_hostsdeny(lines)
    pihole_filter = prepare_pihole(lines)
    agh_filter = prepare_agh(lines)
    shadowsocks_filter = prepare_shadowsocks(lines)
    rpz_filter = prepare_rpz(lines)
    unbound_filter = prepare_unbound(lines)
    minerblock_filter = prepare_minerblock(lines)
    hostsipv6_filter = prepare_hostsipv6(lines)
    domainsallowlist_filter = prepare_domainsallowlist(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_HOSTS, "w") as text_file:
        text_file.write(hosts_filter)

    with open(OUTPUT_LS, "w") as text_file:
        text_file.write(ls_filter)

    with open(OUTPUT_DNSMASQ, "w") as text_file:
        text_file.write(dnsmasq_filter)

    with open(OUTPUT_HOSTSDENY, "w") as text_file:
        text_file.write(hostsdeny_filter)

    with open(OUTPUT_PIHOLE, "w") as text_file:
        text_file.write(pihole_filter)

    with open(OUTPUT_AGH, "w") as text_file:
        text_file.write(agh_filter)

    with open(OUTPUT_SHADOWSOCKS, "w") as text_file:
        text_file.write(shadowsocks_filter)

    with open(OUTPUT_RPZ, "w") as text_file:
        text_file.write(rpz_filter)

    with open(OUTPUT_UNBOUND, "w") as text_file:
        text_file.write(unbound_filter)

    with open(OUTPUT_MINERBLOCK, "w") as text_file:
        text_file.write(minerblock_filter)

    with open(OUTPUT_HOSTSIPV6, "w") as text_file:
        text_file.write(hostsipv6_filter)

    with open(OUTPUT_DOMAINSALLOWLIST, "w") as text_file:
        text_file.write(domainsallowlist_filter)

    print('The domains-based list versions have been generated.')

#/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\
#•X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X•
#\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Dandelion%20Sprout\'s%20Anti-Malware%20List.txt']

UNSUPPORTED_ABP = ['$important', ',important' '$redirect=', ',redirect=',
    ':style', '##+js', '.*#' , ':xpath', ':matches-css', 'dk,no##', 'version.bind', 'pizzaseo.com', 'gamecopyworld', '$app']
UNSUPPORTED_TPL = ['##', '#@#', '#?#', r'\.no\.$', '/^', 'version.bind', 'pizzaseo.com', 'gamecopyworld', ':  ', 'duckdns.org']
UNSUPPORTED_PRIVOXY = ['##', '#@#', '#?#', '@@', '!#', '/^', 'gamecopyworld', '://']
UNSUPPORTED_HOSTS = ['##', '#@#', '#?#', '@@', '!#', '[Adblock Plus 3.', '*', '/^', '://', 'duckdns.org']
UNSUPPORTED_AGH = ['$redirect=', ',redirect=',
    '##', '.*#' , '#?#', 'gamecopyworld', 'version.bind', 'hostname.bind', '|id.server|', '$app']

OUTPUT = 'Anti-Malware List\\xyzzyx.txt'
OUTPUT_AG = 'Anti-Malware List\\AntiMalwareAdGuard.txt'
OUTPUT_ABP = 'Anti-Malware List\\AntiMalwareABP.txt'
OUTPUT_TPL = 'Anti-Malware List\\AntiMalwareTPL.tpl'
OUTPUT_PRIVOXY = 'Anti-Malware List\\AntiMalwarePrivoxy.action'
OUTPUT_HOSTS = 'Anti-Malware List\\AntiMalwareHosts.txt'
OUTPUT_DOMAINS = 'Anti-Malware List\\AntiMalwareDomains.txt'
OUTPUT_AGH = 'Anti-Malware List\\AntiMalwareAdGuardHome.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_ag(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           "Dandelion Sprout's Anti-Malware List", 
           "Dandelion Sprout's Anti-Malware List (for AdGuard)", 
           line
        )

        line = re.sub(
           r"! Version: [0-9]{4}.*", 
           "", 
           line
        )

        line = re.sub(
           r"\[Adblock Plus 3\..*", 
           r"[AdGuard]", 
           line
        )

        line = re.sub(
           r"! Redirect:.*", 
           "", 
           line
        )

        line = re.sub(
           r"=~ Warning.*", 
           "", 
           line
        )

        line = re.sub(
           r"\|~ Warning.*", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])1p", 
           r"\1~third-party", 
           line
        )

        line = re.sub(
           r"([$,~])3p", 
           r"\1third-party", 
           line
        )

        line = re.sub(
           r"([$,])domain$", 
           "", 
           line
        )

        line = re.sub(
           r"^\|\|(([1-2]?[0-9]?[0-9]\.?){4})\^\$.*", 
           r"\1$network", 
           line
        )

        line = re.sub(
           r"^\|\|\[(.*)\]\^\$.*", 
           r"[\1]$network", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(1\)", 
           r"\1#?#*:has(> \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(2\)", 
           r"\1#?#*:has(> * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(3\)", 
           r"\1#?#*:has(> * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(4\)", 
           r"\1#?#*:has(> * > * >  * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(5\)", 
           r"\1#?#*:has(> * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(6\)", 
           r"\1#?#*:has(> * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(7\)", 
           r"\1#?#*:has(> * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(8\)", 
           r"\1#?#*:has(> * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(9\)", 
           r"\1#?#*:has(> * > * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(10\)", 
           r"\1#?#*:has(> * > * > * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"\$doc(,|$)", 
           r"$document\1", 
           line
        )

        line = re.sub(
           r"(#\??#)body(:| )", 
           r"\1html[lang] > body\2", 
           line
        )

        line = re.sub(
           r"^!#include uBO%20list%20extensions/.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|.*\.(ga|ml|gq|cf|pw|loan|agency|gdn|bid|top|ooo|monster)\^.*", 
           r"", 
           line
        )

        line = re.sub(
           r",~inline-font,~inline-script$", 
           r"", 
           line
        )

        line = re.sub(
           r",~inline-script,~inline-font$", 
           r"", 
           line
        )

        line = re.sub(
           r",~inline-font,~inline-script,~domain=", 
           r",~domain=", 
           line
        )

        text += line + '\r\n'

    return text

def is_supported_abp(line) -> bool:
    for token in UNSUPPORTED_ABP:
        if token in line:
            return False

    return True

# function that prepares the filter list for ABP
def prepare_abp(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           "\$doc", 
           "", 
           line
       )

        line = re.sub(
           ",doc", 
           "", 
           line
       )

        # remove $important modifier from the rule
        line = re.sub(
           r",important", 
           "", 
           line
        )

        line = re.sub(
           r"\$important", 
           "", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Anti-Malware List", 
           "Dandelion Sprout's Anti-Malware List (for AdBlock and Adblock Plus)", 
           line
        )

        line = re.sub(
           r"!#if.*", 
           "", 
           line
        )

        line = re.sub(
           r"!#endif", 
           "", 
           line
        )

        line = re.sub(
           r"^no##.*", 
           "", 
           line
        )

        line = re.sub(
           r"! Redirect:.*", 
           "", 
           line
        )

        line = re.sub(
           r"=~ Warning.*", 
           "", 
           line
        )

        line = re.sub(
           r"\|~ Warning.*", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])1p", 
           r"\1~third-party", 
           line
        )

        line = re.sub(
           r"([$,~])3p", 
           r"\1third-party", 
           line
        )

        line = re.sub(
           "\^,", 
           "^$", 
           line
        )

        line = re.sub(
           r"([$,])domain$", 
           "", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(1\)", 
           r"\1#?#*:-abp-has(> \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(2\)", 
           r"\1#?#*:-abp-has(> * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(3\)", 
           r"\1#?#*:-abp-has(> * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(4\)", 
           r"\1#?#*:-abp-has(> * > * >  * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(5\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(6\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(7\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(8\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(9\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"([a-z*])#[?]?#(.*):(upward|nth-ancestor)\(10\)", 
           r"\1#?#*:-abp-has(> * > * > * > * > * > * > * > * > * > \2)", 
           line
        )

        line = re.sub(
           r"(.*)\$all", 
           r"\1\n\1$popup", 
           line
        )

        line = re.sub(
           r"/,", 
           r"/$", 
           line
        )

        line = re.sub(
           r"\.,", 
           r".$", 
           line
        )

        line = re.sub(
           r"^www\.google\.\*#", 
           r"www.google.com,google.ac,google.ad,google.ae,google.af,google.ag,google.al,google.am,google.as,google.at,google.az,google.ba,google.be,google.bf,google.bg,google.bi,google.bj,google.bs,google.bt,google.by,google.ca,google.cat,google.cc,google.cd,google.cf,google.cg,google.ch,google.ci,google.cl,google.cm,google.cn,google.co.ao,google.co.bw,google.co.ck,google.co.cr,google.co.hu,google.co.id,google.co.il,google.co.im,google.co.in,google.co.je,google.co.jp,google.co.ke,google.co.kr,google.co.ls,google.co.ma,google.co.mz,google.co.nz,google.co.th,google.co.tz,google.co.ug,google.co.uk,google.co.uz,google.co.ve,google.co.vi,google.co.za,google.co.zm,google.co.zw,google.com.af,google.com.ag,google.com.ai,google.com.ar,google.com.au,google.com.bd,google.com.bh,google.com.bn,google.com.bo,google.com.br,google.com.by,google.com.bz,google.com.cn,google.com.co,google.com.cu,google.com.cy,google.com.do,google.com.ec,google.com.eg,google.com.et,google.com.fj,google.com.ge,google.com.gh,google.com.gi,google.com.gr,google.com.gt,google.com.hk,google.com.iq,google.com.jm,google.com.jo,google.com.kh,google.com.kw,google.com.lb,google.com.ly,google.com.mm,google.com.mt,google.com.mx,google.com.my,google.com.na,google.com.nf,google.com.ng,google.com.ni,google.com.np,google.com.nr,google.com.om,google.com.pa,google.com.pe,google.com.pg,google.com.ph,google.com.pk,google.com.pl,google.com.pr,google.com.py,google.com.qa,google.com.ru,google.com.sa,google.com.sb,google.com.sg,google.com.sl,google.com.sv,google.com.tj,google.com.tn,google.com.tr,google.com.tw,google.com.ua,google.com.uy,google.com.vc,google.com.ve,google.com.vn,google.cv,google.cz,google.de,google.dj,google.dk,google.dm,google.dz,google.ee,google.es,google.eus,google.fi,google.fm,google.fr,google.frl,google.ga,google.gal,google.ge,google.gg,google.gl,google.gm,google.gp,google.gr,google.gy,google.hk,google.hn,google.hr,google.ht,google.hu,google.ie,google.im,google.in,google.info,google.iq,google.ir,google.is,google.it,google.je,google.jo,google.jp,google.kg,google.ki,google.kz,google.la,google.li,google.lk,google.lt,google.lu,google.lv,google.md,google.me,google.mg,google.mk,google.ml,google.mn,google.ms,google.mu,google.mv,google.mw,google.ne,google.net,google.ng,google.nl,google.no,google.nr,google.nu,google.pk,google.pl,google.pn,google.ps,google.pt,google.ro,google.rs,google.ru,google.rw,google.sc,google.se,google.sh,google.si,google.sk,google.sm,google.sn,google.so,google.sr,google.st,google.td,google.tg,google.tk,google.tl,google.tm,google.tn,google.to,google.tt,google.ua,google.us,google.uz,google.vg,google.vu,google.ws#", 
           line
        )

        line = re.sub(
           r"^\*#.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!if .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!#include .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|.*\.(ga|ml|gq|cf|pw|loan|agency|gdn|bid|top|ooo|monster)\^.*", 
           r"", 
           line
        )

        line = re.sub(
           r"([a-z])##([#.]?[a-z_].*:has)", 
           r"\1#?#\2", 
           line
        )

        line = re.sub(
           r"\$match-case,", 
           r"$", 
           line
        )

        line = re.sub(
           r",~inline-font,~inline-script$", 
           r"", 
           line
        )

        line = re.sub(
           r",~inline-script,~inline-font$", 
           r"", 
           line
        )

        line = re.sub(
           r"-,popup$", 
           r"-", 
           line
        )

        line = re.sub(
           r".*\$network$", 
           r"", 
           line
        )

        if is_supported_abp(line):
            text += line + '\r\n'

    return text

# Attempts to achieve Internet Explorer TPL support
def is_supported_tpl(line) -> bool:
    for token in UNSUPPORTED_TPL:
        if token in line:
            return False

    return True

# function that prepares the filter list for ABP
def prepare_tpl(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           r"^!!? ", 
           r"# ", 
           line
        )

        line = re.sub(
           r"\[Adblock Plus .*\]", 
           "msFilterList", 
           line
        )

        line = re.sub(
           r"^(@@\|\|)", 
           "+d ", 
           line
        )

        line = re.sub(
           r"^(\|\|)", 
           "-d ", 
           line
        )

        line = re.sub(
           r"^/", 
           "- ", 
           line
        )

    # TO-DO: Figure out how to make this NOT apply to lines that have the character "!" in them.
        line = re.sub(
           "/", 
           " ", 
           line
        )

        line = re.sub(
           r"~(.*?)\|", 
           r"\n+d \1", 
           line
        )

        line = re.sub(
           r"~ Warning.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\$doc,domain=.*", 
           "", 
           line
        )

        line = re.sub(
           r"-d (\..*)\^", 
           r"- *\1", 
           line
        )

        line = re.sub(
           r"^- \^.*", 
           "", 
           line
        )

        line = re.sub(
           r"\^", 
           "", 
           line
        )

        line = re.sub(
           r"! Redirect:.*", 
           "", 
           line
        )

        line = re.sub(
           "-d \* ", 
           "- ", 
           line
        )

        line = re.sub(
           "com\* ", 
           "com ", 
           line
        )

        line = re.sub(
           r"@@\*\..*", 
           "", 
           line
        )

        line = re.sub(
           "@@_", 
           "+d _", 
           line
        )

        line = re.sub(
           r"^\.[a-z]", 
           "", 
           line
        )

        line = re.sub(
           r"^([+][d][\s][a-z].*[\s][a-z].*)", 
           "", 
           line
        )

        line = re.sub(
           r"^([-][d].*[okm]\.$)", 
           "", 
           line
        )

        line = re.sub(
           r"!#if.*", 
           "", 
           line
        )

        line = re.sub(
           "!#endif", 
           "", 
           line
        )

        line = re.sub(
           "# Expires: ", 
           ": expires = ", 
           line
        )

        line = re.sub(
           r"^\.[din].*", 
           "", 
           line
        )

        line = re.sub(
           "^\.", 
           "- ", 
           line
        )

        line = re.sub(
           r"^@@ .*", 
           "", 
           line
        )

        line = re.sub(
           " 12 hours", 
           " 1", 
           line
        )

        line = re.sub(
           " 5 days", 
           " 5", 
           line
        )

        line = re.sub(
           "# Redirect:.*", 
           "", 
           line
        )

        line = re.sub(
           r"\+d\s[a-z0-9].*\s[a-z0-9*].*", 
           "", 
           line
        )

        line = re.sub(
           "-d.*-\*$", 
           "", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Anti-Malware List", 
           "Dandelion Sprout's Anti-Malware List (Internet Explorer TPL)", 
           line
        )

        line = re.sub(
           r"^- [a-z][a-z]$", 
           "", 
           line
        )

        line = re.sub(
           r"^- loan$", 
           "", 
           line
        )

        line = re.sub(
           r"^-d .*\*\..*", 
           "", 
           line
        )

        line = re.sub(
           r"^- https\?.*", 
           "", 
           line
        )

        line = re.sub(
           r":  (.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r":  (.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r"://(.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r"://(.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r"://(.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r"([a-z])//", 
           r"\1/ ", 
           line
        )

        line = re.sub(
           r"://(.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r"([a-z])//", 
           r"\1/ ", 
           line
        )

        line = re.sub(
           r"://(.*?) ", 
           r"://\1/", 
           line
        )

        line = re.sub(
           r"([a-z])//", 
           r"\1/ ", 
           line
        )

        line = re.sub(
           "Windows Mac", 
           "Windows/Mac", 
           line
        )

        line = re.sub(
           r"\$.*", 
           "", 
           line
        )

        line = re.sub(
           r"^-d [a-z]{2,6}$", 
           "", 
           line
        )

        line = re.sub(
           r"^\|([a-z0-9])", 
           r"-d \1", 
           line
        )

        line = re.sub(
           r"\|$", 
           r"", 
           line
        )

        line = re.sub(
           r".* bounty .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^!if .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!#include .*", 
           r"", 
           line
        )

        line = re.sub(
           r"(\+d .*[a-z0-9.-])~([a-z0-9.-].*)", 
           r"\1\n+d \2", 
           line
        )

        line = re.sub(
           r".*\*&\*=.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\?.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\^ \\..*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[0-9&].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^://", 
           r"-d ", 
           line
        )

        line = re.sub(
           r"^- \(.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!\+.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^(# Version: .*[0-9])$", 
           r"\1-Deprecated", 
           line
        )

        if is_supported_tpl(line):
            text += line + '\r\n'

    return text

# ————— Privoxy version —————

# Attempts to achieve Internet Explorer TPL support
def is_supported_privoxy(line) -> bool:
    for token in UNSUPPORTED_PRIVOXY:
        if token in line:
            return False

    return True

def prepare_privoxy(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           r"^!!? ", 
           r"# ", 
           line
        )

        line = re.sub(
           r"\$.*", 
           "", 
           line
        )

        line = re.sub(
           r"^\|\|", 
           ".", 
           line
        )

        line = re.sub(
           "\^", 
           "", 
           line
        )

        line = re.sub(
           r"^\[Adblock Plus 3\..*", 
           r"{+block}", 
           line
        )

        line = re.sub(
           r"^\!.*", 
           "#", 
           line
        )

        line = re.sub(
           "# 🇬🇧: ", 
           "{+block{", 
           line
        )

      # Note the use of parenthesises and "\1" combined.
        line = re.sub(
           r"(\{\+block{.*)", 
           r"\1}}", 
           line
        )

        line = re.sub(
           r"^\.\.", 
           ".", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Anti-Malware List", 
           "Dandelion Sprout's Anti-Malware List (for Privoxy)", 
           line
        )

        line = re.sub(
           r"# Placeholder line.*", 
           "{-block}\n# Manually updated Privoxy version of the whitelisted domains from the other versions of this list.\n.coolcmd.tk\n.budterence.tk\n.intr0.tk\n.google.tk\n.transportnews.tk\n.unicorncardlist.tk\n.c0d3c.tk\n.loljp-wiki.tk\n.ninetail.tk\n.goshujin.tk\n.graph.tk\n.google.ga\n.filtri-dns.ga\n.google.ml\n.deimos.gq\n.1hos.cf\n.intr0.cf\n.ivoid.cd\n.domainvoider.cf\n.google.cf\n.rths.cf\n.anonytext.tk\n.tokelau-info.tk\n.fakaofo.tk\n.nukunonu.tk\n.anpigabon.ga\n.dgdi.ga\n.voitures.ga\n.mobili.ml\n.inege.gq\n.tvgelive.gq\n.comprarcarros.gq\n.voitures.cf\n.assembleenationale-rca.cf\n.cps-rca.cf\n.acap.cf", 
           line
        )

        line = re.sub(
           r"^(\# —.*)", 
           r"{+block}\n\1", 
           line
        )

        line = re.sub(
           "-Beta", 
           "-Alpha", 
           line
        )

        line = re.sub(
           r"^\|", 
           ".", 
           line
        )

        line = re.sub(
           r"\|$", 
           r"", 
           line
        )

        line = re.sub(
           r".* bounty .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\*$", 
           r"#", 
           line
        )

        line = re.sub(
           r"^&.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^(# Version: .*[0-9])$", 
           r"\1-Deprecated", 
           line
        )

        if is_supported_privoxy(line):
         text += line + '\r\n'

    return text

# ————— /hosts file version —————

# Attempts to achieve Internet Explorer TPL support
def is_supported_hosts(line) -> bool:
    for token in UNSUPPORTED_HOSTS:
        if token in line:
            return False

    return True

def prepare_hosts(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           r"^!!? ", 
           r"# ", 
           line
        )

        line = re.sub(
           r"\^.*", 
           "", 
           line
        )

        line = re.sub(
           r"^\!.*", 
           "#", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Anti-Malware List", 
           "Dandelion Sprout's Anti-Malware List («hosts» file version)", 
           line
        )

        line = re.sub(
           r"# Placeholder line.*", 
           "", 
           line
        )

        line = re.sub(
           "-Beta", 
           "-Alpha", 
           line
        )

        line = re.sub(
           r"\|\|.*/.*", 
           "", 
           line
        )

        line = re.sub(
           r"^\|\|", 
           "127.0.0.1 ", 
           line
        )

        line = re.sub(
           r"127\.0\.0\.1 \..*", 
           "", 
           line
        )

        line = re.sub(
           r"^/$", 
           "", 
           line
        )

        line = re.sub(
           r"127\.0\.0\.1 gjtech\.net$", 
           "127.0.0.1 gjtech.net adblock.gjtech.net ww1.gjtech.net ww7.gjtech.net ww12.gjtech.net", 
           line
        )

        line = re.sub(
           r"127\.0\.0\.1 tncrun\.net$", 
           "127.0.0.1 tncrun.net www.tncrun.net amanda.tncrun.net sarah.tncrun.net pamela.tncrun.net jessica.tncrun.net ics.tncrun.net katie.tncrun.net pbu.tncrun.net emily.tncrun.net", 
           line
        )

        line = re.sub(
           r"127\.0\.0\.1 ublock\.org$", 
           "127.0.0.1 ublock.org www.ublock.org demo.ublock.org", 
           line
        )

        line = re.sub(
           r"127\.0\.0\.1 ttnrd\.com$", 
           "127.0.0.1 ttnrd.com www.ttnrd.com amanda.ttnrd.com katie.ttnrd.com briana.ttnrd.com sarah.ttnrd.com pamela.ttnrd.com", 
           line
        )

        line = re.sub(
           r"127\.0\.0\.1 \[(.*)\]", 
           r"", 
           line
        )

        line = re.sub(
           r"^/.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|", 
           "127.0.0.1 ", 
           line
        )

        line = re.sub(
           r"^127\.0\.0\.1 [a-z]{2,6}$", 
           "", 
           line
        )

        line = re.sub(
           r"^#$", 
           "", 
           line
        )

        line = re.sub(
           r".*gamecopyworld.*", 
           "", 
           line
        )

        line = re.sub(
           r"\|$", 
           r"", 
           line
        )

        line = re.sub(
           r".* bounty .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\$.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\..*", 
           r"", 
           line
        )

        line = re.sub(
           r".*\.\$[a-z].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^&.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\?.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^127\.0\.0\.1 [a-z0-9-]{1,}\$.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^127\.0\.0\.1 [a-z]{1,20}$", 
           r"", 
           line
        )

        if is_supported_hosts(line):
         text += line + '\r\n'

    return text

# ————— Domains list version —————

def is_supported_domains(line) -> bool:
    for token in UNSUPPORTED_HOSTS:
        if token in line:
            return False

    return True

def prepare_domains(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           r"^!!? ", 
           r"# ", 
           line
        )

        line = re.sub(
           r"\^.*", 
           "", 
           line
        )

        line = re.sub(
           r"^\!.*", 
           "#", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Anti-Malware List", 
           "Dandelion Sprout's Anti-Malware List (Domains list version)", 
           line
        )

        line = re.sub(
           r"# Placeholder line.*", 
           "", 
           line
        )

        line = re.sub(
           r"\|\|.*/.*", 
           "", 
           line
        )

        line = re.sub(
           r"\|\|\..*", 
           "", 
           line
        )

        line = re.sub(
           r"^\|\|", 
           "", 
           line
        )

        line = re.sub(
           r"^/$", 
           "", 
           line
        )

        line = re.sub(
           r"^\|", 
           "", 
           line
        )

        line = re.sub(
           r"^[a-z]{2,6}$", 
           "", 
           line
        )

        line = re.sub(
           r"^/.*", 
           "", 
           line
        )

        line = re.sub(
           r"^#$", 
           "", 
           line
        )

        line = re.sub(
           r"\|$", 
           r"", 
           line
        )

        line = re.sub(
           r".* bounty .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\$.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\..*", 
           r"", 
           line
        )

        line = re.sub(
           r".*\.\$[a-z].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^&.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\?.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-z0-9-]{1,}\$.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-z]{1,20}$", 
           r"", 
           line
        )

        if is_supported_domains(line):
         text += line + '\r\n'

    return text

def is_supported_agh(line) -> bool:
    for token in UNSUPPORTED_AGH:
        if token in line:
            return False

    return True

# function that prepares the filter list for AdGuard Home
def prepare_agh(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        line = re.sub(
           r"^(\||:)(.*)\$doc,domain=(.*)", 
           r"\1\2$denyallow=\3", 
           line
        )

        line = re.sub(
           r"\$denyallow=~", 
           r"$denyallow=", 
           line
        )

        line = re.sub(
           r"\|~", 
           r"|", 
           line
        )

        line = re.sub(
           "\$doc,", 
           "", 
           line
        )

        line = re.sub(
           r",important", 
           "", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Anti-Malware List", 
           "Dandelion Sprout's Anti-Malware List (for AdGuard Home, and for AdGuard for Android/Windows' DNS filtering)", 
           line
        )

        line = re.sub(
           r"!#if.*", 
           "", 
           line
        )

        line = re.sub(
           r"!#endif", 
           "", 
           line
        )

        line = re.sub(
           r"! Redirect:.*", 
           "", 
           line
        )

        line = re.sub(
           r"~ Warning.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\^\$$", 
           "^", 
           line
        )

        line = re.sub(
           r"\$image", 
           "", 
           line
        )

        line = re.sub(
           r"domain=", 
           "", 
           line
        )

        line = re.sub(
           r"([$])1.*", 
           "", 
           line
        )

        line = re.sub(
           r"\|\|\.", 
           r"||*.", 
           line
        )

        line = re.sub(
           r"\|\|(([1-2]?[0-9]?[0-9]\.?){4})\^.*", 
           r"\1", 
           line
        )

        line = re.sub(
           r"^\|\|\[(.*)\].*", 
           r"\1", 
           line
        )

        line = re.sub(
           r"(.*\.168\.192\.)$", 
           r"||\1in-addr.arpa^", 
           line
        )

        line = re.sub(
           r"\$doc$", 
           r"", 
           line
        )

        line = re.sub(
           r".*\$all,.*\..*$", 
           r"", 
           line
        )

        line = re.sub(
           r"\$all,(.*)?$", 
           r"", 
           line
        )

        line = re.sub(
           r"/(live|fun|popup)([,|]|$).*", 
           r"/", 
           line
        )

        line = re.sub(
           r"\$all$", 
           r"", 
           line
        )

        line = re.sub(
           r"\^~(.*)", 
           r"^\n@@||\1^", 
           line
        )

        line = re.sub(
           r"\.~([a-z0-9.-]{5,})", 
           r".\n@@||\1^", 
           line
        )

        line = re.sub(
           r".* bounty .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\$.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^@?@?\|\|.*/.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\^popup", 
           r"^", 
           line
        )

        line = re.sub(
           r"^!if .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!#include .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^&.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|.*\.(ga|ml|gq|cf|pw|loan|agency|gdn|bid|top|ooo|monster)\^.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[/|].*\.php[/^?].*", 
           r"", 
           line
        )

        line = re.sub(
           r"/match-case,", 
           r"$match-case,", 
           line
        )

        line = re.sub(
           r"^@?@?\|\|[a-z0-9.-]{1,}\|[a-z0-9.-].*", 
           r"", 
           line
        )

        line = re.sub(
           r".*\.png\^.*", 
           r"", 
           line
        )

        # Replaced due to https://github.com/AdguardTeam/HostlistCompiler/issues/42#issuecomment-1360494184
        #line = re.sub(
        #   r"^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\.\*\$network$", 
        #   r"\1.0/24", 
        #   line
        #)

        line = re.sub(
           r"\^dnstype=", 
           r"^$dnstype=", 
           line
        )

        line = re.sub(
           r".*\$popup$", 
           r"", 
           line
        )

        # Test 20th of December 2022; see https://github.com/AdguardTeam/HostlistCompiler/issues/42
        line = re.sub(
           r"^\|\|([a-z]{2,})\^$", 
           r"||*.\1^", 
           line
        )

        line = re.sub(
           r".*\*&\*=\*&\*.*", 
           r"", 
           line
        )

        # Needed due to https://github.com/AdguardTeam/HostlistCompiler/issues/42#issuecomment-1360494184, despite a lack of testing
        line = re.sub(
           r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.\*\$network$", 
           r"/^\1\\.\2\\.\3\\.[0-9]{1,3}$/", 
           line
        )

        line = re.sub(
           r"/\$network$", 
           r"/", 
           line
        )

        line = re.sub(
           r"^(\||/|:).*[&%].*", 
           r"", 
           line
        )

        line = re.sub(
           r"@@\|\|[a-zA-Z0-9.-]{0,}\|[a-zA-Z0-9.-].*", 
           r"", 
           line
        )

        if is_supported_agh(line):
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    ag_filter = prepare_ag(lines)
    abp_filter = prepare_abp(lines)
    tpl_filter = prepare_tpl(lines)
    privoxy_filter = prepare_privoxy(lines)
    hosts_filter = prepare_hosts(lines)
    domains_filter = prepare_domains(lines)
    agh_filter = prepare_agh(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_AG, "w") as text_file:
        text_file.write(ag_filter)

    with open(OUTPUT_ABP, "w") as text_file:
        text_file.write(abp_filter)

    with open(OUTPUT_TPL, "w") as text_file:
        text_file.write(tpl_filter)

    with open(OUTPUT_PRIVOXY, "w") as text_file:
        text_file.write(privoxy_filter)

    with open(OUTPUT_HOSTS, "w") as text_file:
        text_file.write(hosts_filter)

    with open(OUTPUT_DOMAINS, "w") as text_file:
        text_file.write(domains_filter)

    with open(OUTPUT_AGH, "w") as text_file:
        text_file.write(agh_filter)

    print('The script has finished its work')

#/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\
#•X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X•
#\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Anti-F%D1%96%D0%9C%20List.txt']

UNSUPPORTED_DOMAINS = ['/', '##', '#.', '#@', '#?', '!#', '[', '!']

OUTPUT = 'Domeneversjoner/xyzzyxfim.txt'
OUTPUT_DOMAINS = 'Domeneversjoner/AntiF%D1%96%D0%9C%20ListDomains.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

def is_supported_domains(line) -> bool:
    for token in UNSUPPORTED_DOMAINS:
        if token in line:
            return False

    return True

# function that prepares the filter list for AdGuard Home
def prepare_domains(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r".*[$,]document.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|", 
           r"", 
           line
        )

        line = re.sub(
           r"! (Title: .*)", 
           r"# \1 (Domains version)", 
           line
        )

        line = re.sub(
           r"!(.*:)", 
           r"#\1", 
           line
        )

        if is_supported_domains(line) and not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    domains_filter = prepare_domains(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_DOMAINS, "w") as text_file:
        text_file.write(domains_filter)

    print('The list versions have been generated.')

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/WikiaPureBrowsingExperience.txt']

UNSUPPORTED_DOMAINS = ['/', '##', '#.', '#@', '#?', '!#', '[', '!']

OUTPUT = 'Domeneversjoner/xyzzyxwikia.txt'
OUTPUT_DOMAINS = 'Domeneversjoner/WikiaPureBrowsingExperienceDomains.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

def is_supported_domains(line) -> bool:
    for token in UNSUPPORTED_DOMAINS:
        if token in line:
            return False

    return True

# function that prepares the filter list for AdGuard Home
def prepare_domains(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"[$,]document.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|", 
           r"", 
           line
        )

        line = re.sub(
           r"! (Title: .*)", 
           r"# \1 (Domains version)", 
           line
        )

        line = re.sub(
           r"!(.*:)", 
           r"#\1", 
           line
        )

        if is_supported_domains(line) and not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    domains_filter = prepare_domains(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_DOMAINS, "w") as text_file:
        text_file.write(domains_filter)

    print('The list versions have been generated.')

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/BrowseWebsitesWithoutLoggingIn.txt']

UNSUPPORTED_DOMAINS = ['/', '##', '#.', '#@', '#?', '!#', '[', '!']

OUTPUT = 'Domeneversjoner/xyzzyxbrowsewebsites.txt'
OUTPUT_DOMAINS = 'Domeneversjoner/BrowseWebsitesWithoutLoggingInDomains.txt'
OUTPUT_AGH = 'Domeneversjoner/BrowseWebsitesWithoutLoggingInAGH.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

def is_supported_domains(line) -> bool:
    for token in UNSUPPORTED_DOMAINS:
        if token in line:
            return False

    return True

# function that prepares the filter list for AdGuard Home
def prepare_domains(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"[$,]document.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\^", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|", 
           r"", 
           line
        )

        line = re.sub(
           r"! (Title: .*)", 
           r"# \1 (Domains version)", 
           line
        )

        line = re.sub(
           r"!(.*:)", 
           r"#\1", 
           line
        )

        line = re.sub(
           r"/\*", 
           r"", 
           line
        )

        line = re.sub(
           r"\*", 
           r"", 
           line
        )

        line = re.sub(
           r"/\?meter", 
           r"", 
           line
        )

        line = re.sub(
           r"[$,]third-party.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^(# Description: .*)", 
           r"\1 Note that this list version is only meant for lists that support no adblocker syntaxes whatsoever, such as Pi-Hole, Blokada, DNS66, and uMatrix.", 
           line
        )

        line = re.sub(
           r".*removeparam.*", 
           r"", 
           line
        )

        if is_supported_domains(line) and not line == '':
            text += line + '\r\n'

    return text

def prepare_agh(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"[$,]document.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|", 
           r"", 
           line
        )

        line = re.sub(
           r"! (Title: .*)", 
           r"# \1 (for AdGuard Home)", 
           line
        )

        line = re.sub(
           r"!(.*:)", 
           r"#\1", 
           line
        )

        line = re.sub(
           r"/\*", 
           r"", 
           line
        )

        line = re.sub(
           r"\*", 
           r"", 
           line
        )

        line = re.sub(
           r"/\?meter", 
           r"", 
           line
        )

        line = re.sub(
           r"[$,]third-party.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^([a-z0-9].*)", 
           r"||\1^", 
           line
        )

        line = re.sub(
           r"\^\^", 
           r"^", 
           line
        )

        line = re.sub(
           r".*removeparam.*", 
           r"", 
           line
        )

        if is_supported_domains(line) and not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    domains_filter = prepare_domains(lines)
    agh_filter = prepare_agh(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_DOMAINS, "w") as text_file:
        text_file.write(domains_filter)

    with open(OUTPUT_AGH, "w") as text_file:
        text_file.write(agh_filter)

    print('The list versions have been generated.')

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AntiAmazonListForTwitch.txt']

UNSUPPORTED_DOMAINS = ['/', '##', '#.', '#@', '#?', '!#', '[', '!']

OUTPUT = 'Domeneversjoner/xyzzyxantiamazon.txt'
OUTPUT_DOMAINS = 'Domeneversjoner/AntiAmazonListForTwitchDomains.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

def is_supported_domains(line) -> bool:
    for token in UNSUPPORTED_DOMAINS:
        if token in line:
            return False

    return True

# function that prepares the filter list for AdGuard Home
def prepare_domains(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"[$,]document.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|", 
           r"", 
           line
        )

        line = re.sub(
           r"! (Title: .*)", 
           r"# \1 (Domains version)", 
           line
        )

        line = re.sub(
           r"!(.*:)", 
           r"#\1", 
           line
        )

        if is_supported_domains(line) and not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    domains_filter = prepare_domains(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_DOMAINS, "w") as text_file:
        text_file.write(domains_filter)

    print('The list versions have been generated.')

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AntiStevenUniverseList.txt']

UNSUPPORTED_DOMAINS = ['/', '##', '#.', '#@', '#?', '!#', '[', '!']

OUTPUT = 'Domeneversjoner/xyzzyxsu.txt'
OUTPUT_DOMAINS = 'Domeneversjoner/AntiStevenUniverseListDomains.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

def is_supported_domains(line) -> bool:
    for token in UNSUPPORTED_DOMAINS:
        if token in line:
            return False

    return True

# function that prepares the filter list for AdGuard Home
def prepare_domains(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"[$,]document.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|", 
           r"", 
           line
        )

        line = re.sub(
           r"! (Title: .*)", 
           r"# \1 (Domains version)", 
           line
        )

        line = re.sub(
           r"!(.*:)", 
           r"#\1", 
           line
        )

        if is_supported_domains(line) and not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    domains_filter = prepare_domains(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_DOMAINS, "w") as text_file:
        text_file.write(domains_filter)

    print('The list versions have been generated.')

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AntiHivemindCartoonTrashingList.txt']

UNSUPPORTED_DOMAINS = ['/', '##', '#.', '#@', '#?', '!#', '[', '!']

OUTPUT = 'Domeneversjoner/xyzzyxhivemind.txt'
OUTPUT_DOMAINS = 'Domeneversjoner/AntiHivemindCartoonTrashingListDomains.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

def is_supported_domains(line) -> bool:
    for token in UNSUPPORTED_DOMAINS:
        if token in line:
            return False

    return True

# function that prepares the filter list for AdGuard Home
def prepare_domains(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"[$,]document.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|", 
           r"", 
           line
        )

        line = re.sub(
           r"! (Title: .*)", 
           r"# \1 (Domains version)", 
           line
        )

        line = re.sub(
           r"!(.*:)", 
           r"#\1", 
           line
        )

        if is_supported_domains(line) and not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    domains_filter = prepare_domains(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_DOMAINS, "w") as text_file:
        text_file.write(domains_filter)

    print('The list versions have been generated.')

#/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\
#•X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X•
#\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareDomains.txt', 'https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianExperimentalList%20alternate%20versions/DandelionSproutsNorskeFiltreDomains.txt', 'https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuard%20Home%20Compilation%20List/AdGuardHomeCompilationListIPs.txt']

OUTPUT = 'Anti-Malware List/xyzzyxips.txt'
OUTPUT_DOMAINS = 'Anti-Malware List/Dandelion Sprout\'s and other adblocker lists\' IPs.ipset'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard Home
def prepare_domains(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"^[a-zA-Z!_*/İ-].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[0-9].*[a-zA-Z!_*-].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^# [—¤|].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^# [a-zA-Z0-9 ,.'\"()/→≥İ-]{1,}$", 
           r"", 
           line
        )

        line = re.sub(
           r"^# (Translated title|Source|Note|Platform notes):.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^# Title: 📔.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^# Version: [a-zA-Z0-9]{1,}$", 
           r"", 
           line
        )

        line = re.sub(
           r"^# For m.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*Nordic Filters.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*nordiske filtre.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^# Title: .*", 
           r"# Title: Dandelion Sprout's and other adblocker lists' IPs", 
           line
        )

        line = re.sub(
           r"^# Description: .*", 
           r"# Description: This IP set combines IP and CIDR addresses from plentiful of major adblocker lists. It contains heavily altered content from Dandelion Sprout's Anti-Malware List, Dandelion Sprout's Nordic Filters, EasyList, uBlock Filters, uBlock Filters - Badware Risks, AdGuard Base Filter, AdGuard French Filter, EasyList Germany, ABP Anti-Circumvention Filters, RU AdList, Liste AR, and EasyList Spanish.\n# For more information and details about this list and other lists of mine, go to https://github.com/DandelionSprout/adfilt/blob/master/Wiki/General-info.md#english", 
           line
        )

        line = re.sub(
           r"^# (These|Google|Gigabyte|Copied).*", 
           r"", 
           line
        )

        if not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    domains_filter = prepare_domains(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_DOMAINS, "w") as text_file:
        text_file.write(domains_filter)

    print('The combined IP list has been generated.')

#/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\
#•X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X•
#\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Sensitive%20lists/Twitter%20De-Politificator.txt']

OUTPUT = 'Domeneversjoner/xyzzyxnitter.txt'
OUTPUT_DOMAINS = 'Domeneversjoner/Nitter De-Politificator.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard Home
def prepare_domains(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"^twitter\.com,twitter3e4tixl4xyajtrzo62zg5vztmjuricljdp2c5kshju4avyoid\.onion#\?#article", 
           r"nitter.net,nitter.lacontrevoie.fr#?#.timeline-item", 
           line
        )

        line = re.sub(
           r"🕊 Twitter and Mastodon De-Politificator", 
           r"🌂 Twitter De-Politificator - Nitter Supplement", 
           line
        )

        line = re.sub(
           r"^! 📛 .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^mas.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[*#].*", 
           r"", 
           line
        )

        line = re.sub(
           r".*position: absolute; .*", 
           r"", 
           line
        )

        line = re.sub(
           r".*astodon.*", 
           r"", 
           line
        )

        line = re.sub(
           r".* flag[ ,].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!!!.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*united species.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*constructive meme.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*prohibitions on .*", 
           r"", 
           line
        )

        line = re.sub(
           r"^(! Homepage: .*)", 
           r"\1\n! Entry syntaxes specific to this supplement:\nnitter.net,nitter.lacontrevoie.fr#?#.timeline-item:has(.fullname[title*=🇺🇸])\nnitter.net,nitter.lacontrevoie.fr#?#.timeline-item:has(.fullname[title*=🇺🇲])\nnitter.net,nitter.lacontrevoie.fr##.timeline-item:has(.fullname[title*=🏴󠁧󠁢])\nnitter.net,nitter.lacontrevoie.fr##.timeline-item:has(.fullname[title*=🇦🇺󠁧󠁢󠁥󠁮󠁧󠁿])\nnitter.net,nitter.lacontrevoie.fr##.timeline-item:has(.fullname[title*=🦕][title*=🌻])\nnitter.net,nitter.lacontrevoie.fr##.timeline-item:has(.fullname[title*=🦖][title*=🧙‍♀️])", 
           line
        )

        if not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    domains_filter = prepare_domains(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_DOMAINS, "w") as text_file:
        text_file.write(domains_filter)

    print('The Nitter list version has been generated.')

#/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\
#•X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X•
#\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AntiKpopSpammersTwitter.txt']

OUTPUT = 'Domeneversjoner/xyzzyxkpop.txt'
OUTPUT_DOMAINS = 'Domeneversjoner/AntiKpopNitter.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard Home
def prepare_domains(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"^twitter\.com,twitter3e4tixl4xyajtrzo62zg5vztmjuricljdp2c5kshju4avyoid\.onion#\?#div\[style\*=\"position: absolute; \"]:not\(\[class\]\)", 
           r"nitter.net,nitter.lacontrevoie.fr#?#.timeline-item", 
           line
        )

        line = re.sub(
           r"^! Title: 🪑 .*", 
           r"🌂 Anti-'K-pop on Twitter' List - Nitter Supplement", 
           line
        )

        if not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    domains_filter = prepare_domains(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_DOMAINS, "w") as text_file:
        text_file.write(domains_filter)

    print('The Nitter list version has been generated.')

#/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\/•\
#•X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X••X•
#\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/\•/

import requests
import re

SOURCES = ['https://easylist-downloads.adblockplus.org/fanboy-notifications.txt', 'https://raw.githubusercontent.com/easylist/easylist/master/fanboy-addon/fanboy_notifications_specific_uBO.txt']

OUTPUT = 'Domeneversjoner/xyzzyxfanboynotifications.txt'
OUTPUT_DOMAINS = 'Domeneversjoner/FanboyNotifications-LoadableInUBO.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard Home
def prepare_domains(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"^!#include fanboy_notifications_specific_uBO\.txt$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! Title: Fanboy's Notifications Blocking List$", 
           r"! Title: Fanboy's Notifications Blocking List - Loadable in uBO", 
           line
        )
        line = re.sub(
           r"^(@@.*)(!.*)", 
           r"\1\n\2", 
           line
        )

        if not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    domains_filter = prepare_domains(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_DOMAINS, "w") as text_file:
        text_file.write(domains_filter)

    print('The Fanboy Notifications uBO version has been generated.')