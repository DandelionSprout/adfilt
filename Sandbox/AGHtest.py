import requests
import re

SOURCES = ['https://easylist-downloads.adblockplus.org/easylist_noelemhide.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt', 'https://raw.githubusercontent.com/NanoAdblocker/NanoFilters/master/NanoMirror/NanoDefender.txt', 'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt', 'https://easylist-downloads.adblockplus.org/liste_fr.txt']

UNSUPPORTED_AGH = ['##', '#@#', '#?#', 'domain=', 'generichide', '$csp', 'badfilter', 'xmlhttprequest', '$xhr', '$stylesheet', '~image', '$elemhide', '$inline-script', '$other', '$~object', 'redirect=']

OUTPUT = 'xyzzyx.txt'
OUTPUT_AGH = 'AdGuardHomeCompilationList.txt'

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

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

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

        if is_supported_agh(line):
            text += line + '\r\n'

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

    print('The domains-based list versions have been generated.')