import os

from matplotlib import pyplot as plt


def save_figure(title):
    if not os.path.exists('../images'):
        os.makedirs('../images')
    plt.savefig(f'../images/{title}.png')


def save_transparent_figure(title):
    if not os.path.exists('../transparent_images'):
        os.makedirs('..//transparent_images')
    plt.savefig(
        f'../transparent_images/{title}.png', dpi=300, transparent=True
    )
