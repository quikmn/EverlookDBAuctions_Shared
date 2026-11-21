# Builds the CurseForge/site screenshots (1920x1080) of the Price Feed from UISandbox renders in raw/
# (D:/Dev/UISandbox: render.py EverlookDBAuctions price-feed-<bar|tooltip|options|empty> --zoom 2). Run it from this folder.
from PIL import Image, ImageDraw
import math
W, H = 1920, 1080
BG = Image.new("RGB", (W, H)); px = BG.load()
for y in range(H):
    for x in range(W):
        d = min(1, math.hypot((x - W / 2) / W, (y - H * 0.38) / H) * 1.6)
        px[x, y] = tuple(int(a + (b - a) * d) for a, b in zip((0x13, 0x22, 0x3F), (0x07, 0x0D, 0x1A)))

def raw(name, crop=None, key=True):
    im = Image.open(f"raw/{name}.png").convert("RGBA")
    if crop: im = im.crop(crop)
    elif not key:  # trim the sandbox's grey backdrop: keep the window (its body is near black)
        m = im.convert("L").point(lambda v: 255 if v < 30 else 0)
        b = m.getbbox()
        if b: im = im.crop((max(0, b[0] - 2), max(0, b[1] - 2), min(im.width, b[2] + 2), min(im.height, b[3] + 2)))
    if key:  # the render's empty screen is pure black: make it see-through, then trim
        d = im.get_flattened_data() if hasattr(im, 'get_flattened_data') else im.getdata()
        im.putdata([(0, 0, 0, 0) if p[0] < 3 and p[1] < 3 and p[2] < 3 else p for p in d])
        im = im.crop(im.getbbox())
    return im

def shadow(c, box, r=14):
    sh = Image.new("RGBA", c.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((box[0] + 10, box[1] + 14, box[2] + 10, box[3] + 14), r, fill=(0, 0, 0, 120))
    return Image.alpha_composite(c, sh)

def place(ims, out, gap=70, maxw=1760, maxh=980, shadows=True, up=1.0):
    tw = sum(i.width for i in ims) + gap * (len(ims) - 1); th = max(i.height for i in ims)
    s = min(up, maxw / tw, maxh / th)
    ims = [i.resize((int(i.width * s), int(i.height * s)), Image.LANCZOS) for i in ims]
    g = int(gap * s); tw = sum(i.width for i in ims) + g * (len(ims) - 1)
    c = BG.convert("RGBA"); x = (W - tw) // 2
    for i in ims:
        y = (H - i.height) // 2
        if shadows: c = shadow(c, (x, y, x + i.width, y + i.height))
        c.paste(i, (x, y), i); x += i.width + g
    c.convert("RGB").save(out)


# the bottom of the auction house window: its status bar, the Price Feed's line under the bar's own
BAR = (14, 1078, 1612, 1141)
place([raw("price-feed-bar", crop=BAR, key=False)], "1-price-feed-bar.png", up=1.1)
place([raw("price-feed-tooltip", crop=(32, 32, 892, 240), key=False)], "2-price-feed-tooltip.png", up=1.4)
place([raw("price-feed-options", key=False)], "3-price-feed-settings.png")
place([raw("price-feed-empty", crop=BAR, key=False)], "4-price-feed-no-data.png", up=1.1)
