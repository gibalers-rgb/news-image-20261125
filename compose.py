#!/usr/bin/env python3
"""Build entry.png for news-image-20261125.

Lays out a newspaper front page for Wednesday 25 November 2026:
a masthead with the date, the AI-generated hero illustration (a dawn
globe ringed by the day's scenes, no text in it), and six story cards
whose words are rendered here with PIL, so every letter stays crisp.

Run from the entry directory:  python3 compose.py
Writes entry.png (1024x1024, under 1 MiB) next to this file.
"""

import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
HERO = os.path.join(
    HERE,
    "assets",
    "media-generation-hero-globe-20261125-0-98250858-b715-464a-a781-01d96c6276d8.png",
)
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 242, 231)      # warm newsprint
INK = (24, 24, 22)           # near-black
RED = (178, 34, 28)          # kicker red
GREY = (96, 90, 80)          # captions
RULE = (24, 24, 22)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)   # noqa: E731
SERIF = lambda s: font("DejaVuSerif.ttf", s)         # noqa: E731
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)     # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)           # noqa: E731


def wrap(draw, text, fnt, width):
    """Greedy word wrap returning a list of lines that fit `width` px."""
    lines = []
    for chunk in text.split("\n"):
        line = ""
        for word in chunk.split():
            trial = (line + " " + word).strip()
            if draw.textlength(trial, font=fnt) <= width:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
    return lines


def draw_lines(draw, lines, fnt, x, y, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


# The six stories of the day, each as reported on 25 November 2026.
STORIES = [
    (
        "WAR AT SEA",
        "Ukraine hits Russian ships in the Baltic and off Libya",
        "Zelenskyy confirms it; Putin vows retaliation.",
    ),
    (
        "CLIMATE",
        "COP31 collapses in Antalya with no deal",
        "Oil states block a fossil-fuel phaseout; no deal.",
    ),
    (
        "MIDDLE EAST",
        "Houthi missile strikes Riyadh\u2019s tallest tower",
        "Eleven wounded in the Riyadh attack.",
    ),
    (
        "DEFENCE",
        "NATO sends early-warning planes to Poland",
        "Follows missiles landing in Poland during the war.",
    ),
    (
        "WASHINGTON",
        "Trump awards Giuliani the Medal of Freedom",
        "The ex-mayor gets the top US honour.",
    ),
    (
        "MARKETS",
        "Anthropic shares slide below their $83 IPO price",
        "The AI firm tumbles days after its Nasdaq debut.",
    ),
]


def main():
    page = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(page)

    # ---- Masthead -----------------------------------------------------
    draw.rectangle([0, 0, W, 8], fill=INK)
    title = "THE WORLD IN ONE DAY"
    tf = SERIF_B(62)
    tw = draw.textlength(title, font=tf)
    draw.text(((W - tw) / 2, 22), title, font=tf, fill=INK)
    draw.line([48, 104, W - 48, 104], fill=RULE, width=2)
    date = "WEDNESDAY  \u00b7  25 NOVEMBER 2026"
    df = SANS_B(26)
    dw = draw.textlength(date, font=df)
    draw.text(((W - dw) / 2, 116), date, font=df, fill=RED)
    sub = "Six stories that defined the day"
    sf = SERIF(22)
    sw = draw.textlength(sub, font=sf)
    draw.text(((W - sw) / 2, 150), sub, font=sf, fill=GREY)
    draw.line([48, 186, W - 48, 186], fill=RULE, width=2)

    # ---- Hero illustration -------------------------------------------
    hero = Image.open(HERO).convert("RGB")
    # Centre-crop the 1920x1280 hero to the 1024x240 band.
    target_w, target_h = 976, 240
    scale = max(target_w / hero.width, target_h / hero.height)
    nw, nh = int(hero.width * scale), int(hero.height * scale)
    hero = hero.resize((nw, nh), Image.LANCZOS)
    left = (nw - target_w) // 2
    top = (nh - target_h) // 2 - 30  # favour the globe, not the sky
    hero = hero.crop((left, max(top, 0), left + target_w, max(top, 0) + target_h))
    page.paste(hero, (24, 200))
    draw.rectangle([24, 200, 1000, 440], outline=INK, width=3)
    caption = ("The day in one picture: war at sea, a climate summit in collapse, "
               "and a missile over Riyadh.")
    cf = SERIF(19)
    draw.text((24, 450), caption, font=cf, fill=GREY)

    # ---- Story cards --------------------------------------------------
    card_w, card_h = 476, 148
    gap_x, gap_y = 24, 12
    x0, y0 = 24, 482
    for i, (kicker, head, deck) in enumerate(STORIES):
        cx = x0 + (i % 2) * (card_w + gap_x)
        cy = y0 + (i // 2) * (card_h + gap_y)
        draw.rectangle([cx, cy, cx + card_w, cy + card_h], outline=RULE, width=2)
        draw.line([cx + 14, cy + 36, cx + card_w - 14, cy + 36], fill=(200, 190, 170), width=1)
        draw.text((cx + 14, cy + 8), kicker, font=SANS_B(18), fill=RED)
        head_lines = wrap(draw, head, SERIF_B(25), card_w - 28)
        draw_lines(draw, head_lines[:2], SERIF_B(25), cx + 14, cy + 44, INK, 27)
        deck_lines = wrap(draw, deck, SANS(18), card_w - 28)
        draw_lines(draw, deck_lines[:1], SANS(18), cx + 14, cy + 108, GREY, 22)

    # ---- Footer -------------------------------------------------------
    draw.line([48, 968, W - 48, 968], fill=RULE, width=2)
    foot = "Every story above was reported on Wednesday 25 November 2026."
    ff = SERIF(18)
    fw = draw.textlength(foot, font=ff)
    draw.text(((W - fw) / 2, 978), foot, font=ff, fill=GREY)

    page.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} {page.size} {os.path.getsize(OUT)} bytes")


if __name__ == "__main__":
    main()
