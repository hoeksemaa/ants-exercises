import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path

# resolve paths relative to this file, so it runs from any working directory
IMG_PATH = Path(__file__).parent / "amsterdam.png"
OUT_PATH = Path(__file__).parent / "script-B-output.png"

def random_argmax(channel, rng):
    """Pick a random (row, col) among all pixels tied for this channel's max value.

    The Amsterdam photo saturates each channel at 1.0 across many pixels, so
    exercise item 9 asks us to choose one of the maxima at random.
    """
    max_val = channel.max()
    rows, cols = np.where(channel == max_val)
    pick = rng.integers(len(rows))
    return rows[pick], cols[pick], max_val, len(rows)

def channel_only(img, i):
    """RGB copy showing only channel i (others zeroed) -> a monocolor intensity map."""
    mono = np.zeros_like(img)
    mono[..., i] = img[..., i]
    return mono

if __name__ == '__main__':
    rng = np.random.default_rng()

    # 6. import the picture of Amsterdam
    img = mpimg.imread(IMG_PATH)

    # 2x2 figure: original (with circles) + red/green/blue intensity maps
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    (ax_orig, ax_red), (ax_green, ax_blue) = axes

    # 6. plot the original picture
    ax_orig.imshow(img)
    ax_orig.set_title("Original: brightest pixel per channel")

    # 7. (thick red line) and 8. (magenta star) intentionally skipped

    # 9. circle the brightest pixel of each channel, in that color, on the ORIGINAL only
    for i, color in enumerate(['red', 'green', 'blue']):
        row, col, max_val, n_tied = random_argmax(img[..., i], rng)
        print("{} channel: max={} across {} tied pixels -> circling (row={}, col={})".format(
            color, max_val, n_tied, row, col))
        # imshow's x-axis is the column index, y-axis is the row index
        ax_orig.plot(col, row, marker='o', markersize=18, markerfacecolor='none',
                     markeredgecolor=color, markeredgewidth=2.5)

    # monocolor R/G/B intensity maps (no circles)
    for ax, i, name in [(ax_red, 0, 'Red'), (ax_green, 1, 'Green'), (ax_blue, 2, 'Blue')]:
        ax.imshow(channel_only(img, i))
        ax.set_title("{} intensity".format(name))

    # save a copy so the result is viewable without a GUI, then show interactively
    fig.tight_layout()
    fig.savefig(OUT_PATH, dpi=120)
    plt.show()
