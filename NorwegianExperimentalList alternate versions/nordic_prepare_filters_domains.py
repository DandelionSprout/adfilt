import requests
import re

SOURCES = ['https://gitlab.com/DandelionSprout/adfilt/raw/master/NorwegianExperimentalList%20alternate%20versions/DandelionSproutsNorskeFiltreDomains.txt']

UNSUPPORTED_HOSTS = ['*', '# ———']
UNSUPPORTED_LS = ['*', '# ———', '# Translated title', '# Version', 'Don\'t be worried', 'General-info']
UNSUPPORTED_DNSMASQ = ['*', '# ']

OUTPUT = 'xyzzyxdomains.txt'
OUTPUT_HOSTS = 'AdawayHosts'
OUTPUT_PRIVOXY = 'NordicFiltersPrivoxy.action'
OUTPUT_LS = 'LittleSnitchNorwegianList.lsrules'
OUTPUT_DNSMASQ = 'NordicFiltersDnsmasq.conf'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

def is_supported_hosts(line) -> bool:
    for token in UNSUPPORTED_HOSTS:
        if token in line:
            return False

    return True

# function that prepares the filter list for ABP
def prepare_hosts(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        # remove $document modifier from the rule
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

        if is_supported_hosts(line):
            text += line + '\r\n'

    return text

# function that prepares the filter list for ABP
def prepare_privoxy(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        # remove $document modifier from the rule

        line = re.sub(
           r"^(?!#)", 
           ".", 
           line
        )

        line = re.sub(
           r"^\.$", 
           "", 
           line
        )

        if is_supported_hosts(line):
            text += line + '\r\n'

    return text

def is_supported_ls(line) -> bool:
    for token in UNSUPPORTED_LS:
        if token in line:
            return False

    return True

# function that prepares the filter list for ABP
def prepare_ls(lines) -> str:
    text = ''

    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        # remove $document modifier from the rule

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

def is_supported_dnsmasq(line) -> bool:
    for token in UNSUPPORTED_DNSMASQ:
        if token in line:
            return False

    return True

# function that prepares the filter list for ABP
def prepare_dnsmasq(lines) -> str:
    text = ''


    # remove or modifiy entries with unsupported modifiers
    for line in lines:

        # remove $document modifier from the rule

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


if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    hosts_filter = prepare_hosts(lines)
    privoxy_filter = prepare_privoxy(lines)
    ls_filter = prepare_ls(lines)
    dnsmasq_filter = prepare_dnsmasq(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_HOSTS, "w") as text_file:
        text_file.write(hosts_filter)

    with open(OUTPUT_PRIVOXY, "w") as text_file:
        text_file.write(privoxy_filter)

    with open(OUTPUT_LS, "w") as text_file:
        text_file.write(ls_filter)

    with open(OUTPUT_DNSMASQ, "w") as text_file:
        text_file.write(dnsmasq_filter)

    print('The script has finished its work')
