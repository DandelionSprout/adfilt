# Original license:
# Copyright © 2021 rusty-snake
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# this code has been modified by https://github.com/iam-py-test and others, as to improve compatibility and fix issues

import json
import sys
import hashlib
from datetime import date
from typing import IO

import requests  # type: ignore

HEAD = """\
! Title: ClearURLs for uBo (unofficial)
! Homepage: https://github.com/DandelionSprout/adfilt/discussions/163
! Description: Want to use ClearURLs' tracking protection without installing another extension? This list is a (unofficial) version of the ClearURLs rules, designed for use in uBlock Origin and AdGuard. This ONLY includes the URL parameter removal functionality from ClearURLs, and not the other functions.
! Last updated: {date}
! Script last updated: 29/2/2024
! Expires: 1 day
! Licence: https://github.com/DandelionSprout/adfilt/blob/master/LICENSE.md
! Warning: This list may break websites, and contains many problematic rules. Worse, it may even prevent other filterlists from working. There is not much the Adfilt maintainers can do, as this list is just the ClearURLs rules converted into a uBo/AdGuard filterlist. Use with caution.
! Note: This was based off of https://gist.github.com/rusty-snake/5cd83a87d680ecbd03e79a1a06758207, which is based off of https://github.com/ClearURLs/Rules. The maintainers of Adfilt (DandelionSprout and iam-py-test, and contributors) have made some modifications as to keep it up-to-date with the source and to fix issues.
! Note: Please do not use this list in Brave Shields, as it may not work properly (https://github.com/DandelionSprout/adfilt/issues/986)
! IMPORTANT NOTE: Do not modify this file in pull requests. This file is auto-generated and therefore any direct edit to it will be undone. Instead, modifications must be made to https://github.com/DandelionSprout/adfilt/blob/master/ClearURLs%20for%20uBo/compile.py or to the upstream ClearURLs rules. If you experience an issue, please report it to https://github.com/DandelionSprout/adfilt/discussions/163, and we (the Adfilt maintainers and community) will look into it and either add an exclusion or report it to the ClearURLs team.
! Important note about the purpose of this list: this list can not bypass tracker redirects through third-party domains. This can be done by strict-blocking said domain and using the ability to view params on the strict-block page to bypass it.
! The Adfilt maintainers would like to thank https://github.com/rusty-snake for helping create this Python script

"""
KNOWN_BAD_FILTERS = [
    # Conflicts with can never be made generic in LegitimateURLShortener
    "$removeparam=/^ref_?=/",
    # Break google search links (https://github.com/DandelionSprout/adfilt/discussions/163#discussioncomment-1598337)
    "$removeparam=sa,domain=google.*",
    "||google.*^$removeparam=sa",
    "$removeparam=usg,domain=google.*",
    # This looks like it could break things 
    "$removeparam=referrer",
    # I remember this breaking something
    "||google.*/search?$removeparam=client",
    # breaks Google redirect links - https://github.com/DandelionSprout/adfilt/discussions/163#discussioncomment-1666162
    "$removeparam=source,domain=google.*",
    "||google.*^$removeparam=source",
    # breaks Twitter - https://github.com/DandelionSprout/adfilt/discussions/163#discussioncomment-1677828
    "$removeparam=s,domain=twitter.com",
    "||twitter.com^$removeparam=s",
    # https://github.com/DandelionSprout/adfilt/discussions/163#discussioncomment-1726673
    "||microsoft.com^$removeparam=ru",
    # https://github.com/DandelionSprout/adfilt/discussions/163#discussioncomment-1749912
    "$removeparam=type,domain=amazon.com",
    "||amazon.com^$removeparam=type",
    # https://github.com/DandelionSprout/adfilt/commit/e5894c3b70c028cd47235457fbf13fc8617d989a
    "$removeparam=sa,domain=google.*",
    "||google.*^$removeparam=sa",
    "$removeparam=usg,domain=google.*",
    "||google.*^$removeparam=usg",
    # https://github.com/DandelionSprout/adfilt/discussions/163#discussioncomment-1796961
    "$removeparam=ved,domain=google.*",
    "||google.*^$removeparam=ved",
    # https://github.com/DandelionSprout/adfilt/discussions/163#discussioncomment-2408392
    '$removeparam=s,domain=amazon.*',
    "||amazon.*^$removeparam=s",
    # https://github.com/DandelionSprout/adfilt/commit/8c3520f272162c70bd48dd27fb7c37a9abf00fa8 - I don't think it is in this list, but added anyway
    "||bing.com^$removeparam=filters",
    # unknown breakage
    "||google.com^$removeparam=dpr",
    "$~xmlhttprequest,removeparam=psc",
    "||walmart.$removeparam=wl13",
    # https://github.com/DandelionSprout/adfilt/discussions/163#discussioncomment-4123725
    "||amazon.*^$removeparam=rnid",
    "||amazon.*/s?$removeparam=rnid",
    # breaks GSB lookup - https://github.com/DandelionSprout/adfilt/discussions/163#discussioncomment-4337362
    "||google.*^$removeparam=site",
    # https://github.com/DandelionSprout/adfilt/discussions/163#discussioncomment-5017320
    "||firefox.com^$removeparam=entrypoint",
    "||firefox.com^$removeparam=context",
    # https://github.com/DandelionSprout/adfilt/issues/975 and https://github.com/uBlockOrigin/uAssets/issues/21079
    "||bing.*^$removeparam=cvid",
]

ALLOWLIST = """
! This is an allowlist added by the Adfilt maintainers
@@||tix.axs.com^$removeparam=utm_campaign
@@||tix.axs.com^$removeparam=utm_content
@@||tix.axs.com^$removeparam=utm_medium
@@||tix.axs.com^$removeparam=utm_source
@@||tix.axs.com^$removeparam=utm_term
! https://github.com/DandelionSprout/adfilt/issues/678
@@||transfernow.net/*/dltransfer$removeparam
! https://github.com/DandelionSprout/adfilt/discussions/163#discussioncomment-4081177
! https://github.com/ClearURLs/Rules/issues/54
@@||webapps.sftc.org/captcha/captcha.dll$removeparam
! https://github.com/ClearURLs/Rules/issues/46
@@||track.sendle.com/tracking$removeparam=ref
! https://github.com/DandelionSprout/adfilt/issues/1012
@@||google.com^$xmlhttprequest,removeparam=ei
"""


def normalize_url_pattern(url_pattern: str) -> str:
    # No need for protocol and subdomain
    url_pattern = url_pattern.replace(r"^https?:\/\/(?:[a-z0-9-]+\.)*?", "", 1)
    url_pattern = url_pattern.replace(r"https?:\/\/([a-z0-9-.]*\.)", "", 1)
    url_pattern = url_pattern.replace(r"^https?:\/\/", "", 1)
    url_pattern = url_pattern.replace(r"^https?://(?:[a-z0-9-]+\.)*?", "", 1)
    url_pattern = url_pattern.replace(r"^https?:\/\/(?:[a-z0-9-]+\.)*?", "", 1)
    # domain= style TLD globbing
    url_pattern = url_pattern.replace(r"(?:\.[a-z]{2,}){1,}", ".*", 1)
    # Remove backslashes
    url_pattern = url_pattern.replace("\\", "")
    # Specific fixups
    url_pattern = url_pattern.replace("(?:accounts.)?", "", 1)
    url_pattern = url_pattern.replace("(?:support.)?", "", 1)
    url_pattern = url_pattern.replace("(?:yandex.*|ya.ru)", "yandex.*", 1)
    #https://github.com/DandelionSprout/adfilt/commit/9dfcd0c3d3bb5a880a4c473c0b9ad5579e963a3f#r62388808
    url_pattern = url_pattern.replace("weibo.(cn|com)", "weibo.*", 1) 
    url_pattern = url_pattern.replace("nikkei.co(?:m|.jp)", "nikkei.com", 1)
    #airbnb.(com|ae|ca|co.in|co.nz|co.uk|co.za|com.au|com.mt|com.sg|de|gy|ie)
    url_pattern = url_pattern.replace(".(com|ae|ca|co.in|co.nz|co.uk|co.za|com.au|com.mt|com.sg|de|gy|ie)", ".*", 1)
    
    if "(" in url_pattern and ")" in url_pattern:
    	# something went wrong
    	print("Something went wrong. Error code WEIRDDOMAINPATTERN. Please see https://github.com/DandelionSprout/adfilt/commit/9dfcd0c3d3bb5a880a4c473c0b9ad5579e963a3f#r62692350")

    return url_pattern


def normalize_exception(exception: str) -> tuple[str, str]:
    orig_exception = exception
    
    exception = exception.replace(r"^https?:\/\/(?:[a-z0-9-]+\.)*?", "||", 1)
    exception = exception.replace(r"^https?:\/\/", "||", 1)
    # FIXME: |ws://
    exception = exception.replace(r"^wss?:\/\/(?:[a-z0-9-]+\.)*?", "|wss://", 1)
    exception = exception.replace(r"(?:\.[a-z]{2,}){1,}", "TLD_WILDCARD", 1)

    exception = exception.replace("=[^/?&]*", "=")
    exception = exception.replace("=.*?", "=")
    exception = exception.replace("=.", "=")
    exception = exception.replace("[^?]*\\?.*?", "*?*")
    exception = exception.replace("[^?]+.*?&?", "*?*")
    exception = exception.replace("\\?.*?", "?")
    exception = exception.replace(".*?&?", "*")
    exception = exception.replace(".*?", "*")

    exception = exception.replace("\\", "")

    exception = exception.replace("||.","||")

    if any(c in "([" for c in exception):
        exception = orig_exception
        exception = exception.replace("(?:", "(")
        return "regex", exception
    elif any(c in "/?" for c in exception):
        exception = exception.replace("TLD_WILDCARD", ".*", 1)
        exception = exception.replace("|wss://zoom.us", "|wss://zoom.us^", 1)
        return "path", exception
    else:
        exception = exception.replace("TLD_WILDCARD", ".*", 1)
        exception = exception.replace("||", "", 1)
        return "domain", exception


def expand_se(rule: str) -> list[str]:
    # https://stackoverflow.com/questions/20061268/python-regex-string-expansion
    # Is there a lib for that?
    #
    # 1. foo_(1|2)_bar -> foo_1_bar + foo_2_bar
    # 2. foo_[12]_bar -> foo_1_bar + foo_2_bar
    # 3. foo_?bar -> foobar + foo_bar
    # But foo_[a-z]*_bar -> foo_[a-z]*_bar
    raise NotImplementedError


def is_regex(rule: str) -> bool:
    return any(c in r".^$*+?{}[]\|()" for c in rule)


def write_rules(
    url_pattern: str,
    rules: list[str],
    regex_fromat: str,
    plain_format: str,
    filterlist: IO[str],
) -> None:
    for rule in rules:
        filter_ = (regex_fromat if is_regex(rule) else plain_format).format(
            rule, url_pattern
        )
        if filter_ not in KNOWN_BAD_FILTERS:
            filterlist.write(filter_ + "\n")


def getrules() -> str:
    RULES = "https://raw.githubusercontent.com/ClearURLs/Rules/master/data.min.json"
    return requests.get(RULES).text

def haschanged() -> bool:
    changed = False
    try:
        hashes = json.loads(open("hash.txt").read())
    except:
        hashes = []
    toph = hashlib.sha256(HEAD.encode()).hexdigest()
    if toph not in hashes:
        changed = True
    ruleshash = hashlib.sha256(getrules().encode()).hexdigest()
    if ruleshash not in hashes:
        changed = True
    exchash = hashlib.sha256(",".join(KNOWN_BAD_FILTERS).encode()).hexdigest()
    if exchash not in hashes:
        changed = True
    extra_allowlist_hash = hashlib.sha256(ALLOWLIST.encode()).hexdigest()
    if extra_allowlist_hash not in hashes:
        changed = True
    with open("hash.txt","w") as rulesf:
        rulesf.write(json.dumps([toph,ruleshash,exchash,extra_allowlist_hash]))
        rulesf.close()
    return changed

def main() -> int:
    data_min_json = json.loads(getrules())
    if haschanged() == False:
        print("No change in rules. Exiting...")
        sys.exit()
    filterlist = open("clear_urls_uboified.txt", "w")
    filterlist.write(HEAD.format(date=date.today().strftime("%d/%m/%Y")))

    # TODO: referralMarketing
    providers = {
        provider["urlPattern"]: provider["rules"]
        for provider in data_min_json["providers"].values()
        if provider["rules"]
    }

    # TODO:
    # - URL encoded
    # $removeparam=%24deep_link,domain=reddit.com
    # - Better is_regex
    # $removeparam=/^p\[\]=/,domain=flipkart.com
    for url_pattern, rules in providers.items():
        url_pattern = normalize_url_pattern(url_pattern)
        rules = [
            rule.replace("(?:%3F)?", "", 1).replace("(?:", "(").replace(r"\$", r"\x24")
            for rule in rules
        ]
        if url_pattern == ".*":
            write_rules(
                url_pattern,
                rules,
                "$removeparam=/^{0}=/",
                "$removeparam={0}",
                filterlist,
            )
        elif "/" in url_pattern:
            write_rules(
                url_pattern,
                rules,
                "||{1}$removeparam=/^{0}=/",
                "||{1}$removeparam={0}",
                filterlist,
            )
        elif url_pattern.startswith("(") and url_pattern.endswith(")"):
            write_rules(
                url_pattern[1:-1],
                rules,
                "$removeparam=/^{0}=/,domain={1}",
                "$removeparam={0},domain={1}",
                filterlist,
            )
        else:
            write_rules(
                url_pattern,
                rules,
                "||{1}^$removeparam=/^{0}=/",
                "||{1}^$removeparam={0}",
                filterlist,
            )

    exceptions = [
        exception
        for provider in data_min_json["providers"].values()
        for exception in provider["exceptions"]
    ]
    for exception in exceptions:
        kind, exception = normalize_exception(exception.replace("\\\\", "\\"))
        if kind == "regex":
            filterlist.write("@@/{0}/$removeparam".format(exception) + "\n")
        elif kind == "path":
            filterlist.write("@@{0}$removeparam".format(exception) + "\n")
        elif kind == "domain":
            filterlist.write("@@||{0}^$removeparam".format(exception) + "\n")
        else:
            raise ValueError
    filterlist.write(ALLOWLIST)
    filterlist.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
