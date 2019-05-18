import requests
import re

SOURCES = ['https://gitlab.com/DandelionSprout/adfilt/raw/master/NorwegianList.txt']

UNSUPPORTED_ABP = ['$document', '$important', ',important' '$redirect=', ',redirect=',
    ':style', '##+js', '.*#' , ':xpath', ':matches-css', 'dk,no##']

UNSUPPORTED_TPL = ['##', '#@#', '#?#', r'\.no\.$']

OUTPUT = 'xyzzyx.txt'
OUTPUT_AG = 'NordicFiltersAdGuard.txt'
OUTPUT_ABP = 'NordicFiltersABP.txt'
OUTPUT_TPL = 'DandelionSproutsNorskeFiltre.tpl'

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
           r"\$document.*", 
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
           "\$document.*", 
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

        # remove $document modifier from the rule
        line = re.sub(
           "! ", 
           "# ", 
           line
        )

        # remove $important modifier from the rule
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

        if is_supported_tpl(line):
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

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_AG, "w") as text_file:
        text_file.write(ag_filter)

    with open(OUTPUT_ABP, "w") as text_file:
        text_file.write(abp_filter)

    with open(OUTPUT_TPL, "w") as text_file:
        text_file.write(tpl_filter)

    print('The script has finished its work')
