import requests
import re

SOURCES = ['https://gitlab.com/DandelionSprout/adfilt/raw/master/AdGuard%20Home%20Compilation%20List/TopDescription.notlist', 'https://easylist-downloads.adblockplus.org/easylist_noelemhide.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt', 'https://raw.githubusercontent.com/NanoAdblocker/NanoFilters/master/NanoMirror/NanoDefender.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt', 'https://easylist-downloads.adblockplus.org/liste_fr.txt', 'https://www.i-dont-care-about-cookies.eu/abp/', 'https://easylist-downloads.adblockplus.org/easylistgermany.txt', 'https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt', 'https://easylist-downloads.adblockplus.org/antiadblockfilters.txt', 'https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/sections/push-notifications.txt']

UNSUPPORTED_AGH = ['##', '@#', '#?#', '#%#', '!+', 'domain=', 'generichide', '$csp', 'xmlhttprequest', '$xhr', '$stylesheet', '$elemhide', '$inline-script', '$other', '$~object', 'redirect=', '#$#', '$domain', ',domain' ]
UNSUPPORTED_IP = ['##', '@#', '#?#', '#%#', 'domain=', 'generichide', '$csp', 'badfilter', 'xmlhttprequest', '$xhr', '$stylesheet', '$elemhide', '$inline-script', '$other', '$~object', 'redirect=', '#$#', '!+']

OUTPUT = 'xyzzyx.txt'
OUTPUT_AGH = 'AdGuardHomeCompilationList.txt'
OUTPUT_IP = 'AdGuardHomeCompilationListIPs.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

def is_supported_agh(line) -> bool:
    for token in UNSUPPORTED_AGH:
        if token in line:
            return False

    return True

# function that prepares the filter list for AdGuard Home
def prepare_agh(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"([$,])third-party", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])~third-party", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])3p", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])first-party", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])1p", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])image", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])media", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])script", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])popup", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])popunder", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])document", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])subdocument", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])object", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])~object-subrequest", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])frame", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])all", 
           "", 
           line
        )

        line = re.sub(
           r",important", 
           "$important", 
           line
        )

        line = re.sub(
           r".*\^[*$,][ac-hj-z?].*", 
           "", 
           line
        )

        line = re.sub(
           r".*\.js$", 
           "", 
           line
        )

        line = re.sub(
           r"^[&+-.=?^_%].*", 
           "", 
           line
        )

        line = re.sub(
           r"^([a-z])", 
           r"||\1", 
           line
        )

        line = re.sub(
           r"^[0-9].*", 
           "", 
           line
        )

        line = re.sub(
           r"^!#.*", 
           "", 
           line
        )

        line = re.sub(
           r"^\|[a-z0-9].*", 
           "", 
           line
        )

        line = re.sub(
           r"^;[a-z0-9].*", 
           "", 
           line
        )

        line = re.sub(
           r"^Amasty_.*", 
           "", 
           line
        )

        line = re.sub(
           r"^\*.*", 
           "", 
           line
        )

        line = re.sub(
           r"^\\.*", 
           "", 
           line
        )

        line = re.sub(
           r"^:[a-z0-9?!].*", 
           "", 
           line
        )

        line = re.sub(
           r"^@[a-z0-9].*", 
           "", 
           line
        )

        line = re.sub(
           r"^[/\\].*", 
           r"", 
           line
        )

        line = re.sub(
           r"@?@?\|\|.*/.*", 
           r"", 
           line
        )

        line = re.sub(
           r"\^,badfilter", 
           r"^badfilter", 
           line
        )

        line = re.sub(
           r"\^badfilter", 
           r"^$badfilter", 
           line
        )

        line = re.sub(
           r".*\^\*.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*\*\^[a-z0-9?].*", 
           r"", 
           line
        )

        line = re.sub(
           r".*\^&.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|.*/.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*\*[&?@].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!$", 
           r"", 
           line
        )

        line = re.sub(
           r"^@@/.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*\*/[a-z0-9]*", 
           r"", 
           line
        )

        line = re.sub(
           r"^[,=^/?~].*", 
           r"", 
           line
        )

        if is_supported_agh(line) and not line == '':
            text += line + '\r\n'

    return text

# ——— IP version ———

def is_supported_ip(line) -> bool:
    for token in UNSUPPORTED_IP:
        if token in line:
            return False

    return True

    # function that prepares the filter list for AdGuard Home
def prepare_ip(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"([$,])third-party", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])~third-party", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])3p", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])first-party", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])1p", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])image", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])media", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])script", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])popup", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])popunder", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])document", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])subdocument", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])~subdocument", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])object", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])~object-subrequest", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])frame", 
           "", 
           line
        )

        line = re.sub(
           r"([$,])all", 
           "", 
           line
        )

        line = re.sub(
           r",important", 
           "$important", 
           line
        )

        line = re.sub(
           r".*\^[*$,].*", 
           "", 
           line
        )

        line = re.sub(
           r".*\.js$", 
           "", 
           line
        )

        line = re.sub(
           r"^[&+-.=?^_%].*", 
           "", 
           line
        )

        line = re.sub(
           r"^([a-z])", 
           r"||\1", 
           line
        )

        line = re.sub(
           r"^[0-9].*", 
           "", 
           line
        )

        line = re.sub(
           r"^\|[a-z0-9].*", 
           "", 
           line
        )

        line = re.sub(
           r"^;[a-z0-9].*", 
           "", 
           line
        )

        line = re.sub(
           r"^Amasty_.*", 
           "", 
           line
        )

        line = re.sub(
           r"^\*.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^\\.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^:.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^@[a-z0-9].*", 
           r"", 
           line
        )

        line = re.sub(
           r"[@]?[@]?\|\|.*[a-zみ].*", 
           r"", 
           line
        )

        line = re.sub(
           r"! (Version: .*[a-z].*)", 
           r"# \1", 
           line
        )

        line = re.sub(
           r"^![a-z #].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!-.*", 
           r"", 
           line
        )

        line = re.sub(
           r"^!$", 
           r"", 
           line
        )

        line = re.sub(
           r"\[Adblock Plus 2\.0\]", 
           r"", 
           line
        )

        line = re.sub(
           r"\[Nano Adblocker\]", 
           r"", 
           line
        )

        line = re.sub(
           r"\|\|", 
           r"", 
           line
        )

        line = re.sub(
           r"\^$", 
           r"", 
           line
        )

        line = re.sub(
           r"^([0-9][0-9]?[0-9]?\.[0-9][0-9]?[0-9]?\.[0-9][0-9]?[0-9]?)\.$", 
           r"\1.0/24", 
           line
        )

        line = re.sub(
           r"^([0-9][0-9]?[0-9]?\.[0-9][0-9]?[0-9]?)\.$", 
           r"\1.0.0/16", 
           line
        )

        line = re.sub(
           r"^[/\\].*", 
           r"", 
           line
        )

        line = re.sub(
           r"^@@.*[a-z].*", 
           r"", 
           line
        )

        line = re.sub(
           r"\[Adblock Plus 3\.4\]", 
           "! Title: IP Entries from Adblock Lists\n! Contains transformated entries from: EasyList, uBlock Filters, uBlock Filters - Badware Risks, Nano Defender Integration, Liste FR, I Don't Care About Cookies, EasyList Germany, ABP Anti-Circumvention Filters\n! Expires: 14 days\n! Licence: In accordance with the Dandelicence, the borrowed entries are considered to have been changed and reduced enough from their original lists, that they're counted as transformative work, meaning that creditation and seperate paragraphs are not necessary unless one of the lists' makers were to ask for such.\n! Description: This was made as a proof-of-concept to see if the IP-based entries of major adblock lists, could be used to create an IP adblocker list for IP blockers, despite how IP lists are normally only meant to block malware, E-mail spam, or port scanners.", 
           line
        )

        line = re.sub(
           r"# Version: (.*)-.*", 
           r"! Version: \1-Alpha", 
           line
        )

        line = re.sub(
           r"^!$", 
           r"", 
           line
        )

        if is_supported_ip(line) and not line == '':
            text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    agh_filter = prepare_agh(lines)
    ip_filter = prepare_ip(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_AGH, "w") as text_file:
        text_file.write(agh_filter)

    with open(OUTPUT_IP, "w") as text_file:
        text_file.write(ip_filter)

    print('The list versions have been generated.')