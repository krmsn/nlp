from pathlib import Path
from wordcloud import WordCloud
import imageio


text = Path("RomeoAndJuliet.txt").read_text()

mask_image = imageio.imread("mask_heart.png")

wc = WordCloud(colormap = "prism", mask = mask_image, background_color = "white")
wc = wc.generate(text)
wc = wc.to_file("RomeoJuliet.png")
