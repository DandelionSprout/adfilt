import requests
import re

SOURCES = ['https://gitlab.com/DandelionSprout/adfilt/raw/master/NorwegianList.txt']

UNSUPPORTED_ABP = ['$important', ',important' '$redirect=', ',redirect=',
    ':style', '##+js', '.*#' , ':xpath', ':matches-css', 'dk,no##']
UNSUPPORTED_TPL = ['##', '#@#', '#?#', r'\.no\.$']
UNSUPPORTED_PRIVOXY = ['##', '#@#', '#?#', '@@', '!#']

OUTPUT = 'xyzzyx.txt'
OUTPUT_AG = 'NordicFiltersAdGuard.txt'
OUTPUT_ABP = 'NordicFiltersABP.txt'
OUTPUT_TPL = 'DandelionSproutsNorskeFiltre.tpl'
OUTPUT_PRIVOXY = 'NordicFiltersPrivoxy.action'

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
           r"\$doc.*", 
           "$empty,important", 
           line
       )

        line = re.sub(
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider", 
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider (for AdGuard)", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Nordic filters for tidier websites", 
           "Dandelion Sprout's Nordic filters for tidier websites (for AdGuard)", 
           line
        )

        line = re.sub(
           r"! Version: [0-9][0-9][0-9][0-9].*", 
           "", 
           line
        )

        line = re.sub(
           "\[Adblock Plus 3.2\]", 
           "[AdGuard ≥6]", 
           line
        )

        line = re.sub(
           r"! Redirect:.*", 
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

        # remove $document modifier from the rule
        line = re.sub(
           r"\$doc.*", 
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
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider", 
           "Dandelion Sprouts nordiske filtre for ryddigere nettsider (for AdBlock og Adblock Plus)", 
           line
        )

        line = re.sub(
           "Dandelion Sprout's Nordic filters for tidier websites", 
           "Dandelion Sprout's Nordic filters for tidier websites (for AdBlock and AdBlock Plus)", 
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
           "\[Adblock Plus 3.2\]", 
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
           "Expires: ", 
           "expires = ", 
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
           r"^-([a-z])", 
           r"- -\1", 
           line
        )

        line = re.sub(
           r"(# Version: .*[0-9][A-Z].*)", 
           r"\1-Beta", 
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
           "\[Adblock Plus 3.2\]", 
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

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    ag_filter = prepare_ag(lines)
    abp_filter = prepare_abp(lines)
    tpl_filter = prepare_tpl(lines)
    privoxy_filter = prepare_privoxy(lines)

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
           "# Platform notes: This list version is intended for tools that deal with so-called «hosts» system files, including Blokada, DNS66, Gas Mask, Diversion, and many others; as well as those who edit their OS' «hosts» system file.", 
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
           r"$(?<=\.com$)|(?<=\.no$)|(?<=\.dk$)|(?<=\.is$)|(?<=\.org$)|(?<=\.net$)|(?<=\.tc$)|(?<=\.it$)|(?<=\.online$)|(?<=\.top$)|(?<=\.tv$)|(?<=\.eu$)|(?<=\.us$)|(?<=\.info$)|(?<=\.club$)", 
           "\" },", 
           line
        )

        line = re.sub(
           r"\.co$", 
           ".co\" },", 
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
           r"$(?<=\.com$)|(?<=\.no$)|(?<=\.dk$)|(?<=\.is$)|(?<=\.org$)|(?<=\.net$)|(?<=\.tc$)|(?<=\.it$)|(?<=\.online$)|(?<=\.top$)|(?<=\.tv$)|(?<=\.eu$)|(?<=\.us$)|(?<=\.info$)|(?<=\.club$)", 
           "/127.0.0.1", 
           line
        )

        line = re.sub(
           r"\.co$", 
           ".co/127.0.0.1", 
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

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    hosts_filter = prepare_hosts(lines)
    ls_filter = prepare_ls(lines)
    dnsmasq_filter = prepare_dnsmasq(lines)
    hostsdeny_filter = prepare_hostsdeny(lines)

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

    print('The domains-based list versions have been generated.')