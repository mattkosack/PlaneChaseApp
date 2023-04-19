from PIL import Image
from requests import get
from json import loads, load, dump
import time

# Save all the info for planar cards
with open("download_info/planar.json", "w") as f:
    dump(loads(get("https://api.scryfall.com/cards/search?q=layout:planar").text), f)

# Download all the images
with open("download_info/planar.json", "r") as file1:
    data = load(file1)
    important_info = {}
    for card in data["data"]:
        name = card["name"].replace(" ", "_")
        oracle_text = card["oracle_text"]
        type_line = card["type_line"]
        important_info[name] = {
            "path" : f"cards/{name}.png",
            "oracle_text" : oracle_text,
            "type_line" : type_line
        }
        response = get(card["image_uris"]["border_crop"], stream=True)
        response.raw.decode_content = True
        with Image.open(response.raw) as im:
            im = im.rotate(-90, expand=True) 
            im.save(f"cards/{name}.png")

        # It's only ~100 cards, I don't feel like playing with the API rate limit or making a more optimal request
        time.sleep(0.5) 

    with open("important_info.json", "w") as file2:
        dump(important_info, file2)
