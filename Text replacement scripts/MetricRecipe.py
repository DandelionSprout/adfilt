import requests
import re

# Paste the webpage you want to translate into this
SOURCES = ['https://natashaskitchen.com/creamy-chicken-and-rice-recipe/']

OUTPUT = 'xyzzyx.html'
OUTPUT_METRIC = 'MetricRecipe.html'

# function that downloads the burgerland recipe
def download_filters() -> str:
    text = ''
    for url in SOURCES:
        r = requests.get(url)
        text += r.text
    return text

def prepare_metric(lines) -> str:
    text = ''
    
    for line in lines:

        # Cups → Deciliter
        line = re.sub(
           r"1 - 1 1[/⁄]2 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"2.5-3.5dl", 
           line
        )

        line = re.sub(
           r"(1[/⁄]4|¼|<sup>1</sup>⁄<sub>4</sub>)-(1[/⁄]2|½|<sup>1</sup>⁄<sub>2</sub>) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"0.6-1.2dl", 
           line
        )

        line = re.sub(
           r"1 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c[. ])", 
           r"2.5dl", 
           line
        )

        line = re.sub(
           r"1 (1[/⁄]4|¼|<sup>1</sup>⁄<sub>4</sub>) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"3dl", 
           line
        )

        line = re.sub(
           r"1 (1[/⁄]2|½|<sup>1</sup>⁄<sub>2</sub>) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ? (cups?|c\.)", 
           r"3.5dl", 
           line
        )

        line = re.sub(
           r"1 (3[/⁄]4|¾|<sup>3</sup>⁄<sub>4</sub>) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"4dl", 
           line
        )

        line = re.sub(
           r"2 (1[/⁄]4|¼|<sup>1</sup>⁄<sub>2</sub>) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"5.5dl", 
           line
        )

        line = re.sub(
           r"2 (1[/⁄]2|½|<sup>1</sup>⁄<sub>2</sub>) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"6dl", 
           line
        )

        line = re.sub(
           r"3 (1[/⁄]2|½|<sup>1</sup>⁄<sub>2</sub>) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?cups?", 
           r"8.5dl", 
           line
        )

        line = re.sub(
           r"(1[/⁄]2|½|<sup>1</sup>⁄<sub>2</sub>) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"1.2dl", 
           line
        )

        line = re.sub(
           r"(1[/⁄]3|⅓|<sup>1</sup>⁄<sub>3</sub>) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"1.6dl", 
           line
        )

        line = re.sub(
           r"(3[/⁄]4|¾|<sup>3</sup>⁄<sub>4</sub>) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"1.8dl", 
           line
        )

        line = re.sub(
           r"(1[/⁄]4|¼|<sup>1</sup>⁄<sub>4</sub>) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"0.6dl", 
           line
        )

        line = re.sub(
           r"(1[/⁄]3|⅓|<sup>1</sup>⁄<sub>3</sub>) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c[. ])", 
           r"0.8dl", 
           line
        )

        line = re.sub(
           r"2 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"4.5dl", 
           line
        )

        line = re.sub(
           r"3 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"7dl", 
           line
        )

        line = re.sub(
           r"4 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"9.5dl", 
           line
        )

        line = re.sub(
           r"5 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(cups?|c\.)", 
           r"1.2L", 
           line
        )

        # Pounds → Grams

        line = re.sub(
           r"1 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(lb|pound)", 
           r"450g", 
           line
        )

        line = re.sub(
           r"1 (1[/⁄]2|½) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(lb[s.]|pounds)", 
           r"675g", 
           line
        )

        line = re.sub(
           r"2 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(lb[s.]|pounds)", 
           r"900g", 
           line
        )

        line = re.sub(
           r"2 (1[/⁄]2|½) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(lb[s.]|pounds)", 
           r"1.15kg", 
           line
        )

        line = re.sub(
           r"3 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(lb[s.]|pounds)", 
           r"1.35kg", 
           line
        )

        line = re.sub(
           r"3 (1[/⁄]2|½) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(lb[s.]|pounds)", 
           r"1.6kg", 
           line
        )

        line = re.sub(
           r"4 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(lb[s.]|pounds)", 
           r"1.8kg", 
           line
        )

        # Ounce → Deciliter

        line = re.sub(
           r"5 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"1.5dl", 
           line
        )

        line = re.sub(
           r"6 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"1.75dl", 
           line
        )

        line = re.sub(
           r"7 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"2dl", 
           line
        )

        line = re.sub(
           r"8 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"2.25dl", 
           line
        )

        line = re.sub(
           r"9 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"2.5dl", 
           line
        )

        line = re.sub(
           r"10 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"3dl", 
           line
        )

        line = re.sub(
           r"10(\.25| 1[/⁄]4) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"3dl", 
           line
        )

        line = re.sub(
           r"12 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"3.5dl", 
           line
        )

        line = re.sub(
           r"14(\.5| 1[/⁄]2) ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"3dl", 
           line
        )

        line = re.sub(
           r"15 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"3dl", 
           line
        )

        line = re.sub(
           r"20 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"6dl", 
           line
        )

        line = re.sub(
           r"28 ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"8.5dl", 
           line
        )

        # Fahrenheit → Celsius

        line = re.sub(
           r"200 ?([°˚]|degrees?|&deg;|\\u00b0F)? ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)?", 
           r"90°C", 
           line
        )

        line = re.sub(
           r"250 ?([°˚]|degrees?|&deg;|\\u00b0F)? ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)?", 
           r"120°C", 
           line
        )

        line = re.sub(
           r"300 ?([°˚]|degrees?|&deg;|\\u00b0F)? ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)?", 
           r"150°C", 
           line
        )

        line = re.sub(
           r"300 degrees[ .]", 
           r"150°C", 
           line
        )

        line = re.sub(
           r"300(°|\\u00b0F)F?[ .]", 
           r"150°C ", 
           line
        )

        line = re.sub(
           r"325 ?([°˚]|degrees?|&deg;|\\u00b0F)? ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)?", 
           r"165°C", 
           line
        )

        line = re.sub(
           r"325 degrees[ .]", 
           r"165°C", 
           line
        )

        line = re.sub(
           r"325(°|\\u00b0F)F?[ .]", 
           r"165°C ", 
           line
        )

        line = re.sub(
           r"350 ?([°˚]|degrees?|&deg;|\\u00b0F)? ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)?", 
           r"175°C", 
           line
        )

        line = re.sub(
           r"350 degrees[ .]", 
           r"175°C", 
           line
        )

        line = re.sub(
           r"350(°|\\u00b0F)F?[ .]", 
           r"175°C ", 
           line
        )

        line = re.sub(
           r"365 ?([°˚]|degrees?|&deg;|\\u00b0F)? ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)?", 
           r"185°C", 
           line
        )

        line = re.sub(
           r"365 degrees[ .]", 
           r"185°C", 
           line
        )

        line = re.sub(
           r"365(°|\\u00b0F)F?[ .]", 
           r"185°C ", 
           line
        )

        line = re.sub(
           r"at (<strong>)?365 for", 
           r"at\1 185°C for", 
           line
        )

        line = re.sub(
           r"375 ?([°˚]|degrees?|&deg;|\\u00b0F)? ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)?", 
           r"190°C", 
           line
        )

        line = re.sub(
           r"375 degrees[ .]", 
           r"190°C", 
           line
        )

        line = re.sub(
           r"375(°|\\u00b0F)F?[ .]", 
           r"190°C ", 
           line
        )

        line = re.sub(
           r"at (<strong>)?375 for", 
           r"at\1 190°C for", 
           line
        )

        line = re.sub(
           r"400 ?([°˚]|degrees?|&deg;|\\u00b0F)? ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)?", 
           r"205°C", 
           line
        )

        line = re.sub(
           r"400 degrees[ .]", 
           r"205°C", 
           line
        )

        line = re.sub(
           r"400(°|\\u00b0F)F?[ .]", 
           r"205°C ", 
           line
        )

        line = re.sub(
           r"at (<strong>)?400 for", 
           r"at\1 205°C for", 
           line
        )

        line = re.sub(
           r"425 ?([°˚]|degrees?|&deg;|\\u00b0F)? ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)?", 
           r"220°C", 
           line
        )

        line = re.sub(
           r"425 degrees[ .]", 
           r"220°C", 
           line
        )

        line = re.sub(
           r"425(°|\\u00b0F)F?[ .]", 
           r"220°C ", 
           line
        )

        line = re.sub(
           r"at (<strong>)?425 for", 
           r"at\1 220°C for", 
           line
        )

        line = re.sub(
           r"450 ?([°˚]|degrees?|&deg;|\\u00b0F)? ?(</span>(&#32;)?<span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)?", 
           r"230°C", 
           line
        )

        line = re.sub(
           r"450 degrees[ .]", 
           r"230°C", 
           line
        )

        line = re.sub(
           r"450(°|\\u00b0F)F?[ .]", 
           r"230°C ", 
           line
        )

        line = re.sub(
           r"at (<strong>)?450 for", 
           r"at\1 230°C for", 
           line
        )

        # Inches → Centimeters

        line = re.sub(
           r"1[ -]?(\" )?inch", 
           r"2.5cm", 
           line
        )

        line = re.sub(
           r" 1(\"|”|\\u201d)[ .]", 
           r" 2.5cm ", 
           line
        )

        line = re.sub(
           r"1 ?(1[/⁄]2|½)[ -]?(\" )?inch", 
           r"3.75cm", 
           line
        )

        line = re.sub(
           r" 1 ?(1[/⁄]2|½|<sup>1</sup>⁄<sub>2</sub>)(\"|”|\\u201d)[ .]", 
           r" 3.75cm ", 
           line
        )

        line = re.sub(
           r"2[ -]?(\" )?inch", 
           r"5cm", 
           line
        )

        line = re.sub(
           r" 2(\"|”|\\u201d)[ .]", 
           r" 5cm ", 
           line
        )

        line = re.sub(
           r"3[ -]?(\" )?inch", 
           r"7.5cm", 
           line
        )

        line = re.sub(
           r" 3(\"|”|\\u201d)[ .]", 
           r" 7.5cm ", 
           line
        )

        line = re.sub(
           r"4[ -]?(\" )?inch", 
           r"10cm", 
           line
        )

        line = re.sub(
           r" 4(\"|”|\\u201d)[ .]", 
           r" 10cm ", 
           line
        )

        line = re.sub(
           r"9[ -]?(\" )?inch", 
           r"22cm", 
           line
        )

        line = re.sub(
           r" 9(\"|”|\\u201d)[ .]", 
           r" 22cm ", 
           line
        )

        line = re.sub(
           r"(1[/⁄]2|½)[ -]?( of an )?(\" )?inch", 
           r"1.25cm", 
           line
        )

        line = re.sub(
           r" (1[/⁄]2|½|<sup>1</sup>⁄<sub>2</sub>)(\"|”|\\u201d)[ .]", 
           r" 1.25cm ", 
           line
        )

        line = re.sub(
           r"(1[/⁄]3|⅓)[ -]?( of an )?(\" )?inch", 
           r"8mm", 
           line
        )

        line = re.sub(
           r" (1[/⁄]3|⅓|<sup>1</sup>⁄<sub>3</sub>)(\"|”|\\u201d)[ .]", 
           r" 8mm ", 
           line
        )

        line = re.sub(
           r"(1[/⁄]4|¼)[ -]?( of an )?(\" )?inch", 
           r"6mm", 
           line
        )

        line = re.sub(
           r" (1[/⁄]4|¼|<sup>1</sup>⁄<sub>4</sub>)(\"|”|\\u201d)[ .]", 
           r" 6mm ", 
           line
        )

        line = re.sub(
           r"(1[/⁄]8|⅛)[ -]?( of an )?(\" )?inch", 
           r"3mm", 
           line
        )

        line = re.sub(
           r" (1[/⁄]8|⅛|<sup>1</sup>⁄<sub>8</sub>)(\"|”|\\u201d)[ .]", 
           r" 3mm ", 
           line
        )

        line = re.sub(
           r" 13[x×]9(\"|”|\\u201d)[ .]", 
           r" 33x22cm ", 
           line
        )

        # Butter stick (?!?!?!?) → Grams

        line = re.sub(
           r"1 stick", 
           r"115g", 
           line
        )

        line = re.sub(
           r"(3[/⁄]4|¾) stick", 
           r"85g", 
           line
        )

        line = re.sub(
           r"(1[/⁄]2|½) stick", 
           r"55g", 
           line
        )

        line = re.sub(
           r"(1[/⁄]4|¼) stick", 
           r"30g", 
           line
        )

        # Technical language that is non-existent in Europe

        line = re.sub(
           r"quarts", 
           r"liters", 
           line
        )

        line = re.sub(
           r"-qt[. ]", 
           r"L", 
           line
        )

        line = re.sub(
           r"(\d) quart ", 
           r"\1-liter ", 
           line
        )

        line = re.sub(
           r"kosher salt", 
           r"salt", 
           line
        )

        line = re.sub(
           r"Kosher salt", 
           r"Salt", 
           line
        )

        # Corrections of odd writing introduced by this script

        line = re.sub(
           r"cminch", 
           r"cm", 
           line
        )

        line = re.sub(
           r"cmes", 
           r"cm", 
           line
        )

        # We can just as well remove common ad scripts used by US cooking sites while we're at it

        line = re.sub(
           r".*adthrive.*", 
           r"", 
           line
        )

        line = re.sub(
           r".*cookielaw\.org.*", 
           r"", 
           line
        )

        text += line + '\r\n'

    return text

if __name__ == "__main__":
    print('Starting the script')
    text = download_filters()
    lines = text.splitlines(False)
    print('Total number of rules: ' + str(len(lines)))

    metric_filter = prepare_metric(lines)

    with open(OUTPUT, "w") as text_file:
        text_file.write(text)

    with open(OUTPUT_METRIC, "w") as text_file:
        text_file.write(metric_filter)

    print('The metric recipe webpage has been generated.')