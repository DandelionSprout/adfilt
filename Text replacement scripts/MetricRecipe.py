import requests
import re

# Paste the webpage you want to translate into this
SOURCES = ['https://thecozycook.com/pioneer-woman-chili/']

OUTPUT = 'xyzzyx.txt'
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
           r"1 - 1 1/2 ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?cups", 
           r"2-3dl", 
           line
        )

        line = re.sub(
           r"1 ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?cup", 
           r"2dl", 
           line
        )

        line = re.sub(
           r"1 (1/4|¼) ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?cups", 
           r"2.5dl", 
           line
        )

        line = re.sub(
           r"1 (1/2|½) ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ? cups", 
           r"3dl", 
           line
        )

        line = re.sub(
           r"1 (3/4|¾) ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?cups", 
           r"3.5dl", 
           line
        )

        line = re.sub(
           r"(1/2|½) ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?cup", 
           r"1dl", 
           line
        )

        line = re.sub(
           r"(3/4|¾) ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?cup", 
           r"1.5dl", 
           line
        )

        line = re.sub(
           r"(1/4|¼) ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?cup", 
           r"0.5dl", 
           line
        )

        line = re.sub(
           r"2 ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?cups", 
           r"4dl", 
           line
        )

        # Pounds → Grams

        line = re.sub(
           r"1 ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?lb", 
           r"400g", 
           line
        )

        line = re.sub(
           r"1 (1/2|½) ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?lbs", 
           r"800g", 
           line
        )

        line = re.sub(
           r"2 ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?lbs", 
           r"1.2kg", 
           line
        )

        line = re.sub(
           r"2 (1/2|½) ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?lbs", 
           r"1.6kg", 
           line
        )

        line = re.sub(
           r"3 ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?lbs", 
           r"2kg", 
           line
        )

        # Ounce → Deciliter

        line = re.sub(
           r"8 ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"2.25dl", 
           line
        )

        line = re.sub(
           r"10 ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"3dl", 
           line
        )

        line = re.sub(
           r"10.25 ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"3dl", 
           line
        )

        line = re.sub(
           r"14.5 ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"3dl", 
           line
        )

        line = re.sub(
           r"15 ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"3dl", 
           line
        )

        line = re.sub(
           r"20 ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?(oz|ounces?)", 
           r"6dl", 
           line
        )

        # Fahrenheit → Celsius

        line = re.sub(
           r"200 ?([°˚]|degrees?)? ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)", 
           r"90°C", 
           line
        )

        line = re.sub(
           r"300 ?([°˚]|degrees?)? ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)", 
           r"150°C", 
           line
        )

        line = re.sub(
           r"300 degrees[ .]", 
           r"150°C", 
           line
        )

        line = re.sub(
           r"300°F?[ .]", 
           r"150°C ", 
           line
        )

        line = re.sub(
           r"350 ?([°˚]|degrees?)? ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)", 
           r"175°C", 
           line
        )

        line = re.sub(
           r"350 degrees[ .]", 
           r"175°C", 
           line
        )

        line = re.sub(
           r"350°F?[ .]", 
           r"175°C ", 
           line
        )

        line = re.sub(
           r"365 ?([°˚]|degrees?)? ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)", 
           r"185°C", 
           line
        )

        line = re.sub(
           r"365 degrees[ .]", 
           r"185°C", 
           line
        )

        line = re.sub(
           r"365°F?[ .]", 
           r"185°C ", 
           line
        )

        line = re.sub(
           r"375 ?([°˚]|degrees?)? ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)", 
           r"190°C", 
           line
        )

        line = re.sub(
           r"375 degrees[ .]", 
           r"190°C", 
           line
        )

        line = re.sub(
           r"375°F?[ .]", 
           r"190°C ", 
           line
        )

        line = re.sub(
           r"400 ?([°˚]|degrees?)? ?(</span> <span class=\"wprm-recipe-ingredient-unit\">)? ?F(ahrenheit)", 
           r"205°C", 
           line
        )

        line = re.sub(
           r"400 degrees[ .]", 
           r"205°C", 
           line
        )

        line = re.sub(
           r"400°F?[ .]", 
           r"205°C ", 
           line
        )

        # Inches → Centimeters

        line = re.sub(
           r"1-?inch", 
           r"2.5cm", 
           line
        )

        line = re.sub(
           r"1 ?(1/2|½)-?inch", 
           r"3.75cm", 
           line
        )

        line = re.sub(
           r"2-?inch", 
           r"5cm", 
           line
        )

        line = re.sub(
           r"(1/2|½)-?inch", 
           r"1.25cm", 
           line
        )

        # Technical language that is non-existent in Europe

        line = re.sub(
           r"quarts", 
           r"liters", 
           line
        )

        line = re.sub(
           r"([0-9]) quart ", 
           r"\1-liter ", 
           line
        )

        line = re.sub(
           r"kosher salt", 
           r"salt", 
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
