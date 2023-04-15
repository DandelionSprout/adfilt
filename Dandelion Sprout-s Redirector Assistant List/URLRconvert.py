import requests
import re

SOURCES = ['https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Dandelion%20Sprout-s%20Redirector%20Assistant%20List/TorRedirectorList.json']

UNSUPPORTED_URLR = ['exampleResult', 'patternType']

OUTPUT = 'xyzzyx.txt'
OUTPUT_URLR = 'TorRedirectorList-URLRedirector.json'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

def is_supported_urlr(line) -> bool:
    for token in UNSUPPORTED_URLR:
        if token in line:
            return False

    return True

# function that prepares the filter list for AdGuard Home
def prepare_urlr(lines) -> str:
    text = ''

    previous_line = None

    for line in lines:
            
        if line == previous_line:
            continue

        line = re.sub(
           r"includePattern", 
           "origin", 
           line
        )

        line = re.sub(
           r"excludePattern", 
           "exclude", 
           line
        )

        line = re.sub(
           r"appliesTo", 
           "types", 
           line
        )

        line = re.sub(
           r"exampleUrl", 
           "example", 
           line
        )

        line = re.sub(
           r'patternDesc.*', 
           '_originRe": {},', 
           line
        )

        line = re.sub(
           r'"disabled": false', 
           '"enable": true', 
           line
        )

        line = re.sub(
           r'"disabled": true', 
           '"enable": false', 
           line
        )

        line = re.sub(
           r"redirectUrl", 
           "target", 
           line
        )

        line = re.sub(
           r'"disabled": true', 
           '"enable": false', 
           line
        )

        line = re.sub(
           r'createdBy": "Redirector.*', 
           'version": "1.3.17.20190813",', 
           line
        )

        line = re.sub(
           r'redirects": ', 
           'rules": ', 
           line
        )

        line = re.sub(
           r'processMatches": "noProcessing"', 
           'process": ""', 
           line
        )

        line = re.sub(
           r'([a-z0-9/])\*', 
           r'\1(.*)', 
           line
        )

        line = re.sub(
           r'"\*', 
           '"(.*)', 
           line
        )

        line = re.sub(
           r'patternType.*', 
           'methods": [],', 
           line
        )

        if is_supported_urlr(line):
            text += line + '\n'

    return text



if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    urlr_filter = prepare_urlr(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_URLR, "w") as text_file:
        text_file.write(urlr_filter)

    print('The list versions have been generated.')