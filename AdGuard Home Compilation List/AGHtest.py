import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuard%20Home%20Compilation%20List/TopDescription.notlist', 'https://easylist-downloads.adblockplus.org/easylist_noelemhide.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2020.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2021.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2022.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2023.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2024.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/quick-fixes.txt', 'https://filters.adtidy.org/extension/ublock/filters/2_without_easylist.txt', 'https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/adservers.txt', 'https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/BaseFilter/sections/general_extensions.txt', 'https://filters.adtidy.org/extension/ublock/filters/16.txt', 'https://easylist-downloads.adblockplus.org/easylistgermany.txt', 'https://raw.githubusercontent.com/abp-filters/abp-filters-anti-cv/master/english.txt', 'https://raw.githubusercontent.com/abp-filters/abp-filters-anti-cv/master/french.txt', 'https://easylist-downloads.adblockplus.org/antiadblockfilters.txt', 'https://easylist-downloads.adblockplus.org/advblock.txt', 'https://easylist-downloads.adblockplus.org/Liste_AR.txt', 'https://easylist-downloads.adblockplus.org/easylistspanish.txt']

UNSUPPORTED_AGH = ['##', '@#', '#?#', '#%#', '!+', 'domain=', 'generichide', '$ghide', ',ghide', '$csp', 'xmlhttprequest', '$xhr', '$stylesheet', '$elemhide', '$inline-script', '$other', '$~object', 'redirect=', '#$#', '$domain', ',domain', '[Adblock Plus 2.0]', 'CV-', '$csp']
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
           r"([$,])(1p|3p|all|doc$|document|first-party|frame|image|media|network|object|popunder|popup|script|subdocument|third-party|~object-subrequest|~third-party)",
           r"", 
           line
        )

        line = re.sub(
           r",important", 
           "$important", 
           line
        )

        line = re.sub(
           r",domain=~?in-addr\.arpa", 
           "", 
           line
        )

        line = re.sub(
           r"^.*\^[*$,][ac-hj-z?].*$", 
           "", 
           line
        )

        line = re.sub(
           r"^([a-z])", 
           r"||\1", 
           line
        )

        line = re.sub(
           r"^[:@][a-z0-9?!].*$", 
           "", 
           line
        )

        line = re.sub(
           r"^@?@?\|.*[/_#,].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"\^,?badfilter", 
           r"^$badfilter", 
           line
        )

        line = re.sub(
           r"^.*\^\*.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*\*\^[a-z0-9?].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*\^&.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*\|.*/.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*\*[&?@].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^(!| |\$|@@)$", 
           r"", 
           line
        )

        line = re.sub(
           r"^([&+=?^_%,~#*]|@@/|\\.|;[a-z0-9]).*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! (AG_|Checksum:|Ref:|http|\||\[|#|!).*$",
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|9anime\.\*(\^|\|)$", 
           r"", 
           line
        )

        line = re.sub(
           r"/\^https\?:\\/\\/([0-9]{1,3})\\\.([0-9]{1,3})\\\.([0-9]{1,3})\\.\(\\d\)\{1,3\}\.\*\/", 
           r"://\1.\2.\3.\n@@://\1.\2.\3.*in-addr.arpa^", 
           line
        )

        line = re.sub(
           r"\|\|([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.$", 
           r"://\1.\2.\3.\n@@://\1.\2.\3.*in-addr.arpa^", 
           line
        )

        line = re.sub(
           r"^(\|\||(:/)?/)?([0-9]{1,3})\.([0-9]{1,3})\.$", 
           r"", 
           line
        )

        line = re.sub(
           r"^://.*/.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/.*[a-z0-9]\\?/[a-z0-9\(].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/.*[a-z]\\/.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/.*[a-z]\/.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/[a-z0-9.*_/-]{1,70}/$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-z0-9@|].*\?.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*\(update frequency\)", 
           r"", 
           line
        )

        line = re.sub(
           r"^! 20(1|2).*$", 
           r"", 
           line
        )

        line = re.sub(
           r"\*(\^|\|)$", 
           r"*", 
           line
        )

        line = re.sub(
           r"^\|\|\*\.", 
           r".", 
           line
        )

        line = re.sub(
           r"\.\*$", 
           r".", 
           line
        )

        line = re.sub(
           r"^[0-9]{1,5}$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-zA-Z0-9.-].*[/?_+=&]$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[@.].*[a-z0-9*]/.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*[$,]jsinject$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.* - .*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^![a-z0-9].*#.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^!\*(\*.*|$)", 
           r"", 
           line
        )

        line = re.sub(
           r"^! ! \+.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|.*:[0-9].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-zA-Z0-9.-].*[a-z0-9.-][/?_+=&][a-zA-Z0-9.$*-].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/.*[_=/;~@%#+,!].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[@|:/.-].*[%&?_=].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[|:/.-].*:.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^(/|:?\|?\||\.)[a-zA-Z0-9-]{1,100}[|^]$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[.:/|a-zA-Z0-9-].*[*.](png|jpe?g|gif|js|swf|gz|exe|php)($|\||\^)", 
           r"", 
           line
        )

        line = re.sub(
           r"^\..*=.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-z0-9./|-].*\^=.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"\^,~", 
           r"^$~", 
           line
        )

        line = re.sub(
           r"^.*\.,badfilter$", 
           r"", 
           line
        )

        line = re.sub(
           r"(.) {1,}$", 
           r"\1", 
           line
        )

        line = re.sub(
           r"^! \*\*\* easylistgermany:easylistgermany/easylistgermany_allowlist_popup\.txt \*\*\*$", 
           r"! Title: ABP Filters", 
           line
        )

        line = re.sub(
           r"^!-------------{1,}!$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-z0-9/-]{1,5}$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\.[a-zA-Z0-9]{3,}\|$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! E[nN][dD].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! Expires: [0-9] .*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! (Good|Bad): .*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.* end ⬆️$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! This section contains the list of .*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! Note, .*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*github\.com/NanoMeow.*$", 
           r"", 
           line
        )

        line = re.sub(
           r" -{4,}(!?)$", 
           r" ---\1", 
           line
        )

        line = re.sub(
           r"! ?-{3,}!?$", 
           r"", 
           line
        )

        line = re.sub(
           r" ={4,}$", 
           r" ===", 
           line
        )

        line = re.sub(
           r"^!-{4,}([ A-ZÉ])", 
           r"!---\1", 
           line
        )

        line = re.sub(
           r"([a-z(])-{4,}!$", 
           r"\1---!", 
           line
        )

        line = re.sub(
           r"^! Last modified: %timestamp%$", 
           r"", 
           line
        )

        line = re.sub(
           r"\*\*\*! Title: ", 
           r"***\n! Title: ", 
           line
        )

        line = re.sub(
           r"^! \*\*\* .*hide.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! Smart ?JSON.*$", 
           r"", 
           line
        )

        line = re.sub(
           r" {2,}", 
           r" ", 
           line
        )

        line = re.sub(
           r"^! \*\*\* easylistspanish:easylistspanish(_adult/adult_thirdparty|/easylistspanish_allowlist_|_adult/adult_allowlist).*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! \*\*\* easylist:easylist_adult/adult_specific_block_popup\.txt \*\*\*", 
           r"", 
           line
        )

        line = re.sub(
           r"^! \*\*\* easylist:easylist_adult/adult_allowlist.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! \*\*\* easylistgermany:easylistgermany/(easylistgermany_allowlist|easylistgermany_specific_block_popup\.).*$", 
           r"", 
           line
        )

        line = re.sub(
           r"! \*\*\* antiadblockfilters.*(czech|dutch|finnish|hebrew|indonesian|latvian|romanian|slovak).*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|51\.89\.187\.1(3[7-9]|4[0-3])(\^|\|)$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/[a-zA-Z]{1,8}$", 
           r"", 
           line
        )

        line = re.sub(
           r"^!.* Adblock Plus($| .*)", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*\.html?(\^|\|)$", 
           r"", 
           line
        )

        line = re.sub(
           r"^!.* property.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^!.*([Éé]lément|CSS|General hid|JS).*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*#\$\?#.*$", 
           r"", 
           line
        )

        # $badfilter-ed entries, as Sublime Text kept complaining about "Ran out of stack space" when I tried to semi-automate it with RegEx.
        line = re.sub(
           r"^(/adblockpopup\.|/ads\.css|/propads\.)(\$badfilter)?$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|.*[a-zA-Z0-9]\|[|a-zA-Z0-9].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*Reek's Anti-Adblock Killer.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^(:/)?/[b-z]([a-z]{1,2})?\.$", 
           r"", 
           line
        )

        # We are in the year 2023 (or later).
        line = re.sub(
           r"http://creativecommons\.org/licenses/", 
           r"https://creativecommons.org/licenses/", 
           line
        )

        line = re.sub(
           r"^/([a-z0-9]{1,8}\.)$", 
           r"://\1", 
           line
        )

        line = re.sub(
           r"([a-zA-Z0-9.,?!'\":; ])(->|=>)([a-zA-Z0-9.,?!'\":; ]|$)", 
           r"\1→\3", 
           line
        )

        line = re.sub(
           r"^.*\$\[.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-zA-Z0-9:/|].*\$\$.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[0-9].*[: ].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^([0-9.]{7,15})(\^|\|)$", 
           r"\1", 
           line
        )

        line = re.sub(
           r"^([.:/|-].*\.(com|org|net|uk|eu|at|it|io|fi|de|nl|agency|es|pl|is|br|gr|ru|su|pro|xyz|win|ch))$",
           r"\1^", 
           line
        )

        line = re.sub(
           r"^[.:/|].*\.(wasm|comm)(\^|\|)$", 
           r"", 
           line
        )

        line = re.sub(
           r"\.\^$", 
           r"^", 
           line
        )

        line = re.sub(
           r"^(\.|:?/?/|\|\|?)[a-z0-9-]{1,}(\^|\|)$", 
           r"", 
           line
        )

        line = re.sub(
           r"^![!#].*$", 
           "", 
           line
        )

        line = re.sub(
           r"^(@@|\.|(:/)?/|\|\|?|-)[a-z0-9]\*\.[a-z]{2,}(\^|\|)?$", 
           "", 
           line
        )

        line = re.sub(
           r"^/([a-zA-Z0-9].*$)", 
           r"|\1", 
           line
        )

        line = re.sub(
           r"^://([a-zA-Z0-9].*$)", 
           r"|\1", 
           line
        )

        line = re.sub(
           r"^\|\|((\d{1,3}\.){3}\d{1,3})\^$", 
           r"\1", 
           line
        )

        line = re.sub(
           r"^@.*(gatewaypundit|wltreport).*$",
           r"", 
           line
        )

        line = re.sub(
           r"^[|:/._a-z0-9-].*akamaiedge.*$",
           r"", 
           line
        )

        line = re.sub(
           r"^([|:/._a-z0-9-].*(akamai|azure[we]|\.cdn77\.org|amazonaws\.).*[^|])$",
           r"\1$dnstype=~CNAME", 
           line
        )

        line = re.sub(
           r"^! {0,}$", 
           r"", 
           line
        )

        if is_supported_agh(line) and not line == '':
            text += line + '\n'

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
           r"^.*\)([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.\..*$",
           r"\1.\2.\3.0/24",
           line
        )

        line = re.sub(
           r"([$,])(1p|3p|all|doc|document|first-party|frame|image|media|network|object|popunder|popup|script|subdocument|third-party|~object-subrequest|~third-party)",
           "", 
           line
        )

        line = re.sub(
           r",important", 
           "$important", 
           line
        )

        line = re.sub(
           r"^.*\^[*$,].*$", 
           "", 
           line
        )

        line = re.sub(
           r"^.*\.js$", 
           "", 
           line
        )

        line = re.sub(
           r"^([&+-.=?^_%:*/@]|\\.).*$", 
           "", 
           line
        )

        line = re.sub(
           r"^([a-z])", 
           r"||\1", 
           line
        )

        line = re.sub(
           r"^\|[a-z0-9].*$", 
           "", 
           line
        )

        line = re.sub(
           r"^;[a-z0-9].*$", 
           "", 
           line
        )

        line = re.sub(
           r"^@[a-z0-9].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"@?@?\|\|.*[a-zа-яみ].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"! (Version: .*[a-z].*)", 
           r"# \1", 
           line
        )

        line = re.sub(
           r"^!([a-z #]|\[).*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^!-.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"\|\|", 
           r"", 
           line
        )

        line = re.sub(
           r"(\^|\|)$", 
           r"", 
           line
        )

        line = re.sub(
           r"^(([0-9]{1,3}\.){3})$", 
           r"\1.0/24", 
           line
        )

        line = re.sub(
           r"^([0-9]{1,3}\.){2}$", 
           r"", 
           line
        )

        line = re.sub(
           r"^@@.*[a-z].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"\[Adblock Plus 3\.[0-9]{1,3}\]", 
           "! Title: IP Entries from Adblock Lists\n! Contains transformated entries from: EasyList, uBlock Filters, uBlock Filters - Badware Risks, AdGuard Base Filter, AdGuard French Filter, EasyList Germany, ABP Anti-Circumvention Filters, RU AdList, Liste AR, EasyList Spanish \n! Expires: 14 days\n! Licence: In accordance with the Dandelicence, the borrowed entries are considered to have been changed and reduced enough from their original lists, that they're counted as transformative work, meaning that creditation and seperate paragraphs are not necessary unless one of the lists' makers were to ask for such.\n! Description: This was made as a proof-of-concept to see if the IP-based entries of major adblock lists, could be used to create an IP adblocker list for IP blockers, despite how IP lists are normally only meant to block malware, E-mail spam, or port scanners.", 
           line
        )

        line = re.sub(
           r"# Version: (.*)-.*$", 
           r"! Version: \1-Alpha", 
           line
        )

        line = re.sub(
           r"^!$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/.*[a-zA-Z0-9_=.,*?|^@&~+;-]$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/.*[\]]$", 
           r"", 
           line
        )

        line = re.sub(
           r"^://.*/.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*104\\\.154\\\.\..*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/\^[h.].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/\\.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/\(https\?:\\/\\/\)([0-9][0-9]?[0-9]?)\\.([0-9][0-9]?[0-9]?)\\.\..*/", 
           r"", 
           line
        )

        line = re.sub(
           r"^![a-zA-Z!*].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[A-Za-z].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^ $", 
           r"", 
           line
        )

        line = re.sub(
           r"^#[a-z0-9.#].*$", 
           "", 
           line
        )

        line = re.sub(
           r"^.*dmcdn\..*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-z.#%$[].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"(.) {1,}$", 
           r"\1", 
           line
        )

        line = re.sub(
           r"^[a-zA-Z0-9].*[#$|a-z].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"\.\.", 
           r".", 
           line
        )

        if is_supported_ip(line) and not line == '':
            text += line + '\n'

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

# ————————————————————————————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuard%20Home%20Compilation%20List/TopDescription-Notifications.notlist', 'https://easylist-downloads.adblockplus.org/fanboy-notifications.txt', 'https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/push-notifications_general.txt', 'https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/AnnoyancesFilter/Popups/sections/push-notifications_specific.txt']

UNSUPPORTED_AGH = ['##', '@#', '#?#', '#%#', '!+', 'domain=', 'generichide', '$ghide', ',ghide', '$csp', 'xmlhttprequest', '$xhr', '$stylesheet', '$elemhide', '$inline-script', '$other', '$~object', 'redirect=', '#$#', '$domain', ',domain', '[Adblock Plus 2.0]', 'CV-']

OUTPUT = 'xyzzyxnotif.txt'
OUTPUT_AGH = 'AdGuardHomeCompilationList-Notifications.txt'

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
           r"([$,])doc", 
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
           r",domain=~?in-addr\.arpa", 
           "", 
           line
        )

        line = re.sub(
           r"/\^https\?:\\/\\/([0-9]{1,3})\\\.([0-9]{1,3})\\\.([0-9]{1,3})\\.\(\\d\)\{1,3\}\.\*\/", 
           "\1.\2.\3.0/24", 
           line
        )

        line = re.sub(
           r"^.*\^[*$,][ac-hj-z?].*$", 
           "", 
           line
        )

        line = re.sub(
           r"^.*\.js$", 
           "", 
           line
        )

        line = re.sub(
           r"^(\.[a-z0-9.]{4,60}\.)$", 
           r"||*\1", 
           line
        )

        line = re.sub(
           r"^[&+=?^_%].*$", 
           "", 
           line
        )

        line = re.sub(
           r"^([a-z])", 
           r"||\1", 
           line
        )

        line = re.sub(
           r"^[0-9].*$", 
           "", 
           line
        )

        line = re.sub(
           r"^!#.*$", 
           "", 
           line
        )

        line = re.sub(
           r"^;[a-z0-9].*$", 
           "", 
           line
        )

        line = re.sub(
           r"^Amasty_.*$", 
           "", 
           line
        )

        line = re.sub(
           r"^\*.*$", 
           "", 
           line
        )

        line = re.sub(
           r"^\\.*$", 
           "", 
           line
        )

        line = re.sub(
           r"^:[a-z0-9?!].*$", 
           "", 
           line
        )

        line = re.sub(
           r"^@[a-z0-9].*$", 
           "", 
           line
        )

        line = re.sub(
           r"@?@?\|\|.*/.*$", 
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
           r"^.*\^\*.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*\*\^[a-z0-9?].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*\^&.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*\|.*/.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*\*[&?@].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^!$", 
           r"", 
           line
        )

        line = re.sub(
           r"^@@/.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[,=^?~].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! \|.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"\.php(\||\?)$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|goo\.gl(\^|\|)$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|9anime\.\*(\^|\|)$", 
           r"", 
           line
        )

        line = re.sub(
           r"^\|\|play-asia\.com(\^|\|)$", 
           r"", 
           line
        )

        line = re.sub(
           r"\|\|([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)\.$", 
           r"://\1.\2.\3.\n@@://\1.\2.\3.*in-addr.arpa^", 
           line
        )

        line = re.sub(
           r"\|\|([0-9][0-9]?[0-9]?)\.([0-9][0-9]?[0-9]?)\.$", 
           r"://\1.\2.\n@@://\1.\2.*in-addr.arpa^", 
           line
        )

        line = re.sub(
           r"^! http.*$",
           r"", 
           line
        )

        line = re.sub(
           r"^://.*/.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*104\\\.154\\\.\..*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/.*[a-z0-9]\\?/[a-z0-9\(].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"\|\|.*_.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/.*[a-z]\\/.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/.*[a-z]\/.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/[a-z0-9.*_/-]{1,70}/$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-z0-9@|].*\?.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! Checksum:.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*\(update frequency\)", 
           r"", 
           line
        )

        line = re.sub(
           r"^! 20(1|2).*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! Ref:.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! #", 
           r"", 
           line
        )

        line = re.sub(
           r"\*(\^|\|)$", 
           r"*", 
           line
        )

        line = re.sub(
           r"^\|\|\*\.", 
           r".", 
           line
        )

        line = re.sub(
           r"\.\*$", 
           r".", 
           line
        )

        line = re.sub(
           r"^[0-9]{1,5}$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-z0-9.-].*[/?_+=&]$", 
           r"", 
           line
        )

        line = re.sub(
           r"^[a-z0-9.-].*[a-z0-9.-][/?_+=&][a-z0-9.$-].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"^/.*[_?=/;~@%#+,].*$", 
           r"", 
           line
        )

        line = re.sub(
           r"\^,~", 
           r"^$~", 
           line
        )

        line = re.sub(
           r"^.*\.,badfilter$", 
           r"", 
           line
        )

        line = re.sub(
           r"^.*dmcdn\..*$", 
           r"", 
           line
        )

        line = re.sub(
           r"([a-zA-Z0-9.,;'?!#_-]) $", 
           r"\1", 
           line
        )

        line = re.sub(
           r"^(! This section contains )", 
           r"! Title: AdGuard Popups filter - Push notifications, specific\n\1", 
           line
        )

        line = re.sub(
           r"^.*/,stylesheet$", 
           r"", 
           line
        )

        line = re.sub(
           r"^%.*$", 
           r"", 
           line
        )

        line = re.sub(
           r"http://creativecommons\.org/licenses/", 
           r"https://creativecommons.org/licenses/", 
           line
        )

        line = re.sub(
           r"^/([a-zA-Z0-9].*$)", 
           r"|\1", 
           line
        )

        line = re.sub(
           r"^! {0,}$", 
           r"", 
           line
        )

        line = re.sub(
           r"^! !SECTION.*$", 
           r"", 
           line
        )

        if is_supported_agh(line) and not line == '':
            text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    agh_filter = prepare_agh(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_AGH, "w") as text_file:
        text_file.write(agh_filter)

    print('The notifications list version has been generated.')