from requests import get
from json import loads, load, dump
import time

# Save all the info for planar cards
with open("planar.json", "w") as f:
    dump(loads(get("https://api.scryfall.com/cards/search?q=layout:planar").text), f)

# Download all the images
with open("planar.json", "r") as file:
    data = load(file)
    for card in data["data"]:
        name = card["name"].replace(" ", "_")
        with open(f"cards/{name}.png", "wb") as im:
            im.write(get(card["image_uris"]["border_crop"]).content)
        time.sleep(1) # I didn't feel like looking up their request limit, it's only ~100 cards anyways
