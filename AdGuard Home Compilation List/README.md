### Note, 5 February 2024 (Does not apply to the Notifications list):
When I started this project in what must've been 2021, the situation was that AdGuard DNS Filter had only around 15,000 entries and non-existent wildcarding, so I decided to see <i>"I can do this better than them, big time."</i>

And it did actually go well for 1½-2 years, until my stamina that was already struggling with frequent colds, plummeted to the bottom in December 2022, and updates became steadily less frequent, even more so after contracting severe rashes in November 2023. At the same time, AdGuard DNS Filter had increased to a fair and decent 61,600 entries, so I effectively concede defeat to them.

But it's not the end of the road <i>just</i> yet. Should there be a time in February 2024 where my health permits, I'll run a new list update just to see which entries are exclusive to my or their list, and then adjust the main and IP lists' scope accordingly (and also I need to sync Notifications either way, as it's an opt-in in AdGuard Home).

### Update instructions as of early 2025, still valid unless otherwise stated:
To update `AdGuardHomeCompilationList.txt`:

1) Install Python 3.x.
2) Right-click on https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuard%20Home%20Compilation%20List/AGHtest.py and choose "Save as…" to an empty folder.
3) Open a command line in the folder and run `Python3 AGHtest.py`. Cygwin/Unix is preferred over PowerShell to avoid newline problems. Wait a few minutes until the script finishes.
4) Open the generated `AdGuardHomeCompilationList.txt` file in Sublime Text. Go to its menu bars → Edit → Permute Lines → Unique. Afterwards, go to its menu bars → File → Save.
5) Go to https://abpvn.com/ruleChecker/redundantRuleChecker.html, paste all text in the file into its textbox, and click "Check for redundant rules". Wait up to 1min until the check finishes. While still on that page, go to its "Corrected" tab. Use "Ctrl+A → Backspace" on the textbox to remove all text in it, then use Ctrl+A on the entire page to copy the "Corrected" result, then paste it back into the `AdGuardHomeCompilationList.txt` file. Remove the text including and above `The file without redundancies: open in a new tab`, then save the file.
6) In Sublime Text, use Ctrl+H to open the text replacement menu. Ensure the `.*` button is enabled (which enables RegEx mode). Paste <code>^! ([a-zA-Z0-9а-яА-ЯёЁàé.'"`_?#/,$=<>|+()^&; -]{1,})\n(!.*)$</code> into <i>"Find:"</i>, then paste <code>\2</code> into <i>"Replace:"</i>, then press "Replace all". Repeat until Sublime Text can't find any more matches, then save the file.
7) On top of the page, above `[Adblock Plus 3.4]`, add a line consisting solely of many (em-?)dashes, then paste the contents of https://raw.githubusercontent.com/DandelionSprout/adfilt/master/AdGuard%20Home%20Compilation%20List/AdGuardHomeCompilationList-DeadDomains.notlist above that dashline. Then go to the menu bar → Edit → Permute Lines → Unique. Afterwards, delete the dashline and all text above it, and save the file.
8) It is now ready to be uploaded at https://github.com/DandelionSprout/adfilt/tree/master/AdGuard%20Home%20Compilation%20List → Add file → Upload files.

### Syntax notes
Apparently AdGuard Home doesn't recognise single /'s as prefixes, nor ^ as prefixes. This got awkward for sure.
