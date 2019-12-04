import requests
import re

SOURCES = ['https://gitlab.com/DandelionSprout/adfilt/raw/master/NorwegianList.txt']

UNSUPPORTED_ABP = ['$important', ',important', '$redirect=', ',redirect=',
    ':style', '##+js', '.*#' , ':xpath', 'dk,no##']
UNSUPPORTED_TPL = ['##', '#@#', '#?#', r'\.no\.$']
UNSUPPORTED_PRIVOXY = ['##', '#@#', '#?#', '@@', '!#']

OUTPUT = 'xyzzyx.txt'
OUTPUT_AG = 'NordicFiltersAdGuard.txt'
OUTPUT_ABP = 'NordicFiltersABP.txt'
OUTPUT_TPL = 'DandelionSproutsNorskeFiltre.tpl'
OUTPUT_PRIVOXY = 'NordicFiltersPrivoxy.action'
OUTPUT_PRIVACY = 'NordicFiltersPrivacy.txt'

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

        # until this is done: https://github.com/AdguardTeam/CoreLibs/issues/152
        line = re.sub(
           r"([\$,])doc.*", 
           r"\1empty,important", 
           line
        )

        line = re.sub(
           r"(itle:.*Dandelion Sprout.*)", 
           r"\1 (for AdGuard)", 
           line
        )

        line = re.sub(
           r"! Version: [0-9][0-9][0-9][0-9].*", 
           "", 
           line
        )

        line = re.sub(
           "\[Adblock Plus 3.4\]", 
           "[AdGuard ≥6]", 
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
           "viaplay.\*#", 
           "viaplay.no,viaplay.dk#", 
           line
        )

        line = re.sub(
           "google.\*#", 
           "google.no,google.dk,google.is#", 
           line
        )

        line = re.sub(
           r"eurogamer\.\*([#,])", 
           r"eurogamer.dk\1", 
           line
        )

        line = re.sub(
           "ticketmaster.\*#", 
           "ticketmaster.no,ticketmaster.dk#", 
           line
        )

        line = re.sub(
           "qxl.\*#", 
           "qxl.no,qxl.dk#", 
           line
        )

        line = re.sub(
           "expedia.\*#", 
           "expedia.no,expedia.dk#", 
           line
        )

        line = re.sub(
           "gamereactor.\*#", 
           "gamereactor.no,gamereactor.dk#", 
           line
        )

        line = re.sub(
           "viafree.\*#", 
           "viafree.no,viafree.dk#", 
           line
        )

        line = re.sub(
           "momondo.\*#", 
           "momondo.no,monondo.dk#", 
           line
        )

        line = re.sub(
           "eurosport.\*#", 
           "eurosport.no,eurosport.dk#", 
           line
        )

        line = re.sub(
           "prisjakt.\*,", 
           "prisjakt.no,", 
           line
        )

        line = re.sub(
           "redirect=noopmp4-1s", 
           "mp4", 
           line
        )

        line = re.sub(
           r"##\+js\(abort-on-property-write.js, (.*)\)", 
           r'#%#//scriptlet("abort-on-property-write", "\1")', 
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
           r"([$,])important", 
           "", 
           line
        )

        line = re.sub(
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider", 
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider (for AdBlock og Adblock Plus)",
           line
        )

        line = re.sub(
           "Dandelion Sprout's Nordic filters for tidier websites", 
           "Dandelion Sprout's Nordic filters for tidier websites (for AdBlock and Adblock Plus)",
           line
        )

        line = re.sub(
           r"!#.*", 
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
           "viaplay.\*#", 
           "viaplay.no,viaplay.dk#", 
           line
        )

        line = re.sub(
           "google.\*#", 
           "google.no,google.dk,google.is#", 
           line
        )

        line = re.sub(
           r"eurogamer\.\*([#,])", 
           r"eurogamer.dk\1", 
           line
        )

        line = re.sub(
           "ticketmaster.\*#", 
           "ticketmaster.no,ticketmaster.dk#", 
           line
        )

        line = re.sub(
           "qxl.\*#", 
           "qxl.no,qxl.dk#", 
           line
        )

        line = re.sub(
           "expedia.\*#", 
           "expedia.no,expedia.dk#", 
           line
        )

        line = re.sub(
           "gamereactor.\*#", 
           "gamereactor.no,gamereactor.dk#", 
           line
        )

        line = re.sub(
           "viafree.\*#", 
           "viafree.no,viafree.dk#", 
           line
        )

        line = re.sub(
           "momondo.\*#", 
           "momondo.no,monondo.dk#", 
           line
        )

        line = re.sub(
           "eurosport.\*#", 
           "eurosport.no,eurosport.dk#", 
           line
        )

        line = re.sub(
           "prisjakt.\*,", 
           "prisjakt.no,", 
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
           r"(! Version: .*)", 
           r"[Adblock Plus 3.4]\n\1", 
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
           r"##\+js\(abort-on-property-write.js, (.*)\)", 
           r"#$#abort-on-property-write \1", 
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
           "! ", 
           "# ", 
           line
        )

        line = re.sub(
           r"(# Version: .*)", 
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
           " 12 hours", 
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
           r"\1-Beta", 
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
           "! ", 
           "# ", 
           line
        )

        line = re.sub(
           r"\$.*", 
           "", 
           line
        )

        line = re.sub(
           "\|\|", 
           ".", 
           line
        )

        line = re.sub(
           "\^", 
           "", 
           line
        )

        line = re.sub(
           "\[Adblock Plus 3.4\]", 
           "{+block}", 
           line
        )

        line = re.sub(
           r"^$", 
           "#", 
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
           r"(# Version: .*[0-9][A-Z].*)", 
           r"\1-Alpha", 
           line
        )

        if is_supported_privoxy(line):
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
           r"! Version: [0-9][0-9][0-9][0-9].*", 
           "", 
           line
        )

        line = re.sub(
           "\[Adblock Plus 3.4\]", 
           "", 
           line
        )

        line = re.sub(
           r"! If you wish to remove cookie banners.*", 
           "! Warning: This list version does not exchange tracker protection for added browsing convenience, and is for advanced tech users ONLY! Some web stuff that are unbroken by whitelistings in the normal version, are NOT fixed in this version! Additionally, it is only made with uBO and close derivatives in mind.", 
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

    print('The adblocker-based list versions have been generated.')



import requests
import re

SOURCES = ['https://gitlab.com/DandelionSprout/adfilt/raw/master/NorwegianExperimentalList%20alternate%20versions/DandelionSproutsNorskeFiltreDomains.txt']

UNSUPPORTED_HOSTS = ['*', '# ———']
UNSUPPORTED_LS = ['*', '# ———', '# Translated title', '# Version', 'Don\'t be worried', 'General-info', '# Platform notes:']
UNSUPPORTED_DNSMASQ = ['*', '# ']

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
           "# Platform notes: This list version is intended for tools that deal with so-called «hosts» system files, including Gas Mask, Diversion, Hosts File Editor, and many others; as well as those who edit their OS' «hosts» system file.", 
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
           "{ \"action\": \"deny\", \"process\": \"any\", \"remote-hosts\": \"", 
           line
        )

        line = re.sub(
           r"{ \"action\": \"deny\", \"process\": \"any\", \"remote-hosts\": \"$", 
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
           "\"description\": \"This list aims to block Norwegian and Danish scam sellers, ad servers, and a small handful of tracking servers.\",\n\"rules\": [", 
           line
        )

        line = re.sub(
           r"(.*\..*[a-z]$)", 
           r"\1\" },", 
           line
        )

        line = re.sub(
           "(.*\..*[a-z])\\\"", 
           r"\1\\", 
           line
        )

        line = re.sub(
           "\\\"\"", 
           "\"", 
           line
        )

        line = re.sub(
           r"([a-z])\\", 
           r"\1", 
           line
        )

        line = re.sub(
           r"(\"wo.tc\" }),", 
           r"\1\n]}", 
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
           "address=/", 
           line
        )

        line = re.sub(
           r"(.*\..*[a-z]$)", 
           r"\1/127.0.0.1", 
           line
        )

        line = re.sub(
           r"address=/$", 
           "", 
           line
        )

        if is_supported_dnsmasq(line):
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
           "# Platform notes: This list version is intended for those who make use of the Regex functionality in Pi-Hole.", 
           line
        )

        line = re.sub(
           r"(# Version: .*)", 
           r"\1-Alpha", 
           line
        )

        line = re.sub(
           r"^([a-z0-9].*)\.(.*)\.\*", 
           r"(^|\.)\1\\.\2\\..*$", 
           line
        )

        line = re.sub(
           r"^([a-z0-9].*)\.\*$", 
           r"(^|\.)\1\\..*$", 
           line
        )

        line = re.sub(
           r"^(.*)\.(.*)-\*", 
           r"(^|\.)\1\\.\2-*$", 
           line
        )

        line = re.sub(
           r"^([a-z0-9].*)\.\*\.(.*)", 
           r"(^|\.)\1\\..*\\.\2$", 
           line
        )

        line = re.sub(
           r"^\*\.(.*)\.\*", 
           r"(^|\.)*\\.\1\\..*$", 
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
           " Dandelion Sprouts nordiske filtre (for AdGuard Home)", 
           line
        )

        line = re.sub(
           r" Dandelion Sprout's Nordic Filters.*", 
           " Dandelion Sprout's Nordic Filters (for AdGuard Home)", 
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
           "# Platform notes: This list version is intended for those who use Shadowsocks, Shadowrocket, and other Socks5-based tools that have become popular in PR-China for several reasons.", 
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
           r"^([^DU].*?\.[a-z][a-z][a-z]?[a-z]?[a-z]?[a-z]?)$", 
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
           r"^([a-z0-9].*)", 
           r"\1 CNAME .", 
           line
        )

        line = re.sub(
           r"^# ", 
           "; ", 
           line
        )

        line = re.sub(
           r"# Platform notes:.*", 
           "; Platform notes: This list version is intended for those who use BIND or other DNS server tools that support RPZ files.", 
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
           r"^([a-z0-9].*)", 
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
           r"^([a-z0-9].*)", 
           r"*://*.\1/*", 
           line
        )

        line = re.sub(
           r"# Platform notes:.*", 
           "# Platform notes: So, let's say your company boss is not letting you install any adblocker on your awful work laptop, but (s)he lets you install MinerBlock for some indeterminable reason? In this very unlikely case, I've saved your day.\nNote: This list does not actually block any mining-related stuff.", 
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

    print('The domains-based list versions have been generated.')




import requests
import re
import os
os.mkdir('Anti-Malware List')

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Dandelion%20Sprout\'s%20Anti-Malware%20List.txt']

UNSUPPORTED_ABP = ['$important', ',important' '$redirect=', ',redirect=',
    ':style', '##+js', '.*#' , ':xpath', ':matches-css', 'dk,no##']
UNSUPPORTED_TPL = ['##', '#@#', '#?#', r'\.no\.$', '/^']
UNSUPPORTED_PRIVOXY = ['##', '#@#', '#?#', '@@', '!#', '/^']
UNSUPPORTED_HOSTS = ['##', '#@#', '#?#', '@@', '!#', '[Adblock Plus 3.4]', '*', '/^']
UNSUPPORTED_AGH = ['$redirect=', ',redirect=',
    '##', '.*#' , '#?#']

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


        # until this is done: https://github.com/AdguardTeam/CoreLibs/issues/152
        line = re.sub(
           "\$doc", 
           "$empty,important", 
           line
       )

        line = re.sub(
           ",doc", 
           ",empty,important", 
           line
       )

        line = re.sub(
           "Dandelion Sprout's Anti-Malware List", 
           "Dandelion Sprout's Anti-Malware List (for AdGuard)", 
           line
        )

        line = re.sub(
           r"! Version: [0-9][0-9][0-9][0-9].*", 
           "", 
           line
        )

        line = re.sub(
           "\[Adblock Plus 3.4\]", 
           "[AdGuard ≥6]", 
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
           "! ", 
           "# ", 
           line
        )

        line = re.sub(
           r"\[Adblock Plus .*\]", 
           "msFilterList", 
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
           r"~([a-z0-9].*?)\|", 
           r"\n+d \1", 
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
           "! ", 
           "# ", 
           line
        )

        line = re.sub(
           r"\$.*", 
           "", 
           line
        )

        line = re.sub(
           "\|\|", 
           ".", 
           line
        )

        line = re.sub(
           "\^", 
           "", 
           line
        )

        line = re.sub(
           "\[Adblock Plus 3.4\]", 
           "{+block}", 
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
           "! ", 
           "# ", 
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
           "\|\|", 
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
           "! ", 
           "# ", 
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
           "\|\|", 
           "", 
           line
        )

        line = re.sub(
           r"^/$", 
           "", 
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
           r"domain=.*", 
           "", 
           line
        )

        line = re.sub(
           "\$doc,", 
           "$important", 
           line
        )

        line = re.sub(
           r",important", 
           "$important", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Anti-Malware List", 
           "Dandelion Sprout's Anti-Malware List (for AdGuard Home)", 
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
           r"\$domain$", 
           "", 
           line
        )

        line = re.sub(
           r"\|~ Warning.*", 
           "", 
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
           r"! Placeholder line.*", 
           "! Manually updated AdGuard Home version of the whitelisted domains from the other versions of this list.\n@@||coolcmd.tk^$important\n@@||budterence.tk^$important\n@@||intr0.tk^$important\n@@||google.tk^$important\n@@||transportnews.tk^$important\n@@||unicorncardlist.tk^$important\n@@||c0d3c.tk^$important\n@@||loljp-wiki.tk^$important\n@@||ninetail.tk^$important\n@@||goshujin.tk^$important\n@@||graph.tk^$important\n@@||google.ga^$important\n@@||filtri-dns.ga^$important\n@@||google.ml^$important\n@@||deimos.gq^$important\n@@||1hos.cf^$important\n@@||intr0.cf^$important\n@@||ivoid.cd^$important\n@@||domainvoider.cf^$important\n@@||google.cf^$important\n@@||rths.cf^$important\n@@||anonytext.tk^$important\n@@||tokelau-info.tk^$important\n@@||fakaofo.tk^$important\n@@||nukunonu.tk^$important\n@@||anpigabon.ga^$important\n@@||dgdi.ga^$important\n@@||voitures.ga^$important\n@@||mobili.ml^$important\n@@||inege.gq^$important\n@@||tvgelive.gq^$important\n@@||comprarcarros.gq^$important\n@@||voitures.cf^$important\n@@||assembleenationale-rca.cf^$important\n@@||cps-rca.cf^$important\n@@||acap.cf^$important",
           line
        )

        line = re.sub(
           r"([$])1.*", 
           "", 
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