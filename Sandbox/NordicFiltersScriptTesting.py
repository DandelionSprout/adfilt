import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/NorwegianList.txt',
           'https://raw.githubusercontent.com/DandelionSprout/adfilt/master/uBO%20list%20extensions/NordicExtensionsForUBO%26Nano.txt']

UNSUPPORTED_ABP = ['$redirect=', ',redirect=', ':style', '##+js', '.*#' , ':xpath', ':matches-css']

OUTPUT = 'filter.txt'
OUTPUT_AG = 'filter_ag.txt'
OUTPUT_ABP = 'filter_abp.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += '! ' + url + '\r\n'
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_ag(lines) -> str:
    text = ''

    for line in lines:
        # until this is done: https://github.com/AdguardTeam/CoreLibs/issues/152
        text += re.sub(
           r"\$document.*", 
           "$empty,important", 
           line
       ) + '\r\n'

    return text

def is_supported_abp(line) -> bool:
    for token in UNSUPPORTED_ABP:
        if token in line:
            return False

    return True

# function that prepares the filter list for ABP
def prepare_abp(lines) -> str:
    text = ''

    # remove entries with unsupported modifiers
    for line in lines:
        if is_supported_abp(line):
            text += line + '\r\n'

    return text

    for line in lines:
        text += re.sub(
           r"\$document.*", 
           "", 
           line
       ) + '\r\n'

    return text

    for line in lines:
        text += re.sub(
           r"\$important.*", 
           "", 
           line
       ) + '\r\n'

    return text

    for line in lines:
        text += re.sub(
           r"\,important.*", 
           "", 
           line
       ) + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    ag_filter = prepare_ag(lines)
    abp_filter = prepare_abp(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_AG, "w") as text_file:
        text_file.write(ag_filter)

    with open(OUTPUT_ABP, "w") as text_file:
        text_file.write(abp_filter)

    print('The script has finished its work')
