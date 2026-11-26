import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/4chan.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\4chan.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — 4chan",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The 4chan AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/500px.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\500px.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — 500px",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The 500px AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/9gag.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\9gag.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — 9gag",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The 9gag AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/aliexpress.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\aliexpress.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — AliExpress",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The AliExpress AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/amazon.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\amazon.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Amazon",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Amazon AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/amazon_streaming.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\amazon_streaming.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Amazon streaming",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Amazon streaming AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/amino.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\amino.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Amino",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Amino AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/apple_streaming.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\apple_streaming.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Apple streaming",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Apple streaming AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/bigo_live.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\bigo_live.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Bigo live",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Bigo live AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/bilibili.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\bilibili.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Bilibili",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Bilibili AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/blaze.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\blaze.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Blaze",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Blaze AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/bluesky.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\bluesky.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Bluesky",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Bluesky AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/canaisglobo.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\canaisglobo.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Canaisglobo",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Canaisglobo AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/claro.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\claro.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Claro",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Claro AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/cloudflare.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\cloudflare.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Cloudflare",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Cloudflare AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/clubhouse.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\clubhouse.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Clubhouse",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Clubhouse AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/coolapk.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\coolapk.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Coolapk",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Coolapk AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/crunchyroll.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\crunchyroll.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Crunchyroll",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Crunchyroll AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/douban.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\douban.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Douban",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Douban AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/ebay.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\ebay.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — eBay",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The eBay AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/espn.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\espn.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — ESPN",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The ESPN AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/facebook.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\facebook.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Facebook",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Facebook AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/fifa.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\fifa.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — FIFA",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The FIFA AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/flickr.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\flickr.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Flickr",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Flickr AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/globoplay.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\globoplay.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Globoplay",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Globoplay AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/icloud_private_relay.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\icloud_private_relay.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — iCloud Private Relay",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The iCloud Private Relay AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/iheartradio.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\iheartradio.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — iHeartRadio",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The iHeartRadio AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/imgur.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\imgur.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Imgur",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Imgur AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/instagram.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\instagram.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Instagram",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Instagram AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/iqiyi.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\iqiyi.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Iqiyi",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Iqiyi AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/kakaotalk.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\kakaotalk.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — KakaoTalk",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The KakaoTalk AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/kik.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\kik.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Kik",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Kik AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/lazada.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\lazada.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Lazada",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Lazada AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/line.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\line.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — LINE (social app)",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Line AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/linkedin.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\linkedin.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — LinkedIn",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The LinkedIn AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/looke.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\looke.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Looke",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Looke AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/mail_ru.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\mail_ru.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — MailRU",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The MailRU AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/mastodon.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\mastodon.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Mastodon",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Mastodon AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/mercado_libre.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\mercado_libre.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — mercado libre",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The mercado libre AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/nebula.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\nebula.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Nebula",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Nebula AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/ok.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\odnoklassniki.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Odnoklassniki",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Odnoklassniki AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/olvid.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\olvid.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Olvid",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Olvid AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/onlyfans.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\onlyfans.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — OnlyFans",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The OnlyFans AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/pinterest.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\pinterest.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Pinterest",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Pinterest AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/plenty_of_fish.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\plenty_of_fish.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Plenty of Fish",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Plenty of fish AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/plex.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\plex.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Plex",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Plex AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/privacy.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\privacyBrasil.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — PrivacyBrasil",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The PrivacyBrasil AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/qq.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\qq.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — QQ",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"\^$denyallow=([a-z0-9])",
           r"^$all,domain=~\1",
           line
        )

        line = re.sub(
           r"\^\$denyallow=([a-z0-9])",
           r"^$all,domain=~\1",
           line
        )

        line = re.sub(
           r"(\^\$all,domain=.*\|)([a-z0-9])",
           r"\1~\2",
           line
        )

        line = re.sub(
           r"(\^\$all,domain=.*\|)([a-z0-9])",
           r"\1~\2",
           line
        )

        line = re.sub(
           r"(\^\$all,domain=.*\|)([a-z0-9])",
           r"\1~\2",
           line
        )

        line = re.sub(
           r"(\^\$all,domain=.*\|)([a-z0-9])",
           r"\1~\2",
           line
        )

        line = re.sub(
           r"(\^\$all,domain=.*\|)([a-z0-9])",
           r"\1~\2",
           line
        )

        line = re.sub(
           r"(\^\$all,domain=.*\|)([a-z0-9])",
           r"\1~\2",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The QQ AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/rakuten_viki.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\rakuten_viki.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Rakuten Viki",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Rakuten Viki AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/reddit.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\reddit.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Reddit",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Reddit AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/shein.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\shein.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Shein",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Shein AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/shopee.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\shopee.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Shopee",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Shopee AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/signal.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\signal.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Signal",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Signal AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/skype.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\skype.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Skype",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Skype AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/snapchat.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\snapchat.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Snapchat",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Snapchat AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/spotify.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\spotify.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Spotify",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Spotify AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/telegram.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\telegram.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Telegram",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Telegram AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/temu.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\temu.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Temu",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Temu AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/tidal.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\tidal.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Tidal",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Tidal AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/tiktok.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\tiktok.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — TikTok",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The TikTok AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/tinder.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\tinder.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Tinder",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Tinder AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/tumblr.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\tumblr.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Tumblr",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Tumblr AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/twitch.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\twitch.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Twitch",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Twitch AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/twitter.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\twitter.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Twitter",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Twitter AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/viber.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\viber.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Viber",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Viber AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/vk.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\vk.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — VK",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The VK AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/voot.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\voot.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Voot",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Voot AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/wechat.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\wechat.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — WeChat",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The WeChat AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/weibo.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\weibo.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Weibo",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Weibo AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/whatsapp.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\whatsapp.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — WhatsApp",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The WhatsApp AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/wizz.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\wizz.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Wizz",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Wizz AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/xiaohongshu.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\xiaohongshu.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Xiaohongshu",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Xiaohongshu AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/zhihu.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\zhihu.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Zhihu",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Zhihu AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/chatgpt.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\chatgpt.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — ChatGPT",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The ChatGPT AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/gemini.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\gemini.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Google Gemini",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Google Gemini AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/copilot.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\copilot.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Microsoft Copilot",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Copilot AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/claude.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\claude.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Claude",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Claude AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/grok.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\grok.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Grok",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Grok AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/meta_ai.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\meta_ai.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Meta Aİ",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Meta Aİ AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/samsung_tv_plus.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\samsung_tv_plus.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           r"! Title: Conversion of AdGuard Services Lists — Samsung TV Plus",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Samsung TV Plus AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/disneyplus.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\disneyplus.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           "! Title: Conversion of AdGuard Services Lists — Disney+",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Disney+ AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/nvidia.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\nvidia.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           "! Title: Conversion of AdGuard Services Lists — NVIDIA",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The NVIDIA AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/perplexity.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\perplexity.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           "! Title: Conversion of AdGuard Services Lists — PerplexityAİ",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The PerplexityAİ AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/yy.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\yy.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           "! Title: Conversion of AdGuard Services Lists — YY",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The YY AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/odysee.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\odysee.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           "! Title: Conversion of AdGuard Services Lists — Odysee",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Odysee AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/paramountplus.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\paramountplus.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           "! Title: Conversion of AdGuard Services Lists — Paramount+",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Paramount+ AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/questionai.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\questionai.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           "! Title: Conversion of AdGuard Services Lists — QuestionAİ",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The QuestionAİ AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/max.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\max.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           "! Title: Conversion of AdGuard Services Lists — MAX (Russia-based SoMe)",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Max AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/pluto_tv.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\pluto_tv.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           "! Title: Conversion of AdGuard Services Lists — Pluto TV",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Pluto TV AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/deepseek.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\deepseek.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           "! Title: Conversion of AdGuard Services Lists — DeepSeek",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The DeepSeek AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/dola.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\dola.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           "! Title: Conversion of AdGuard Services Lists — Dola",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Dola AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/qwen.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\qwen.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           "! Title: Conversion of AdGuard Services Lists — Qwen",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Qwen AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re

SOURCES = ['https://raw.githubusercontent.com/AdguardTeam/HostlistsRegistry/main/services/slack.yml']
OUTPUT_CONV = 'Conversions of AdGuard Services lists\\slack.txt'

# function that downloads the filter list
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

# function that prepares the filter list for AdGuard
def prepare_conversion(lines) -> str:
    text = ''

    for line in lines:

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^(icon_|rules:|id:).*$",
           "",
           line
        )

        line = re.sub(
           r"^ {0,}- '(.*)$",
           r"\1",
           line
        )

        line = re.sub(
           r"^(.*)'$",
           r"\1",
           line
        )

        line = re.sub(
           r"^name: (.*)$",
           "! Title: Conversion of AdGuard Services Lists — Slack",
           line
        )

        line = re.sub(
           r"^(.*\^)$",
           r"\1$all",
           line
        )

        line = re.sub(
           r"^group:.*$",
           "",
           line
        )

        text += line + '\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    conversion_filter = prepare_conversion(lines)

    with open(OUTPUT_CONV, "w", encoding="utf-8-sig", newline='\n') as text_file:
        text_file.write(conversion_filter)

        print('The Slack AdGuard Services conversion has been generated.')

# ———————————————————————

import requests
import re