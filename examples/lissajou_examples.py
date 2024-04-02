# examples/lissajou_examples.py

import sys

import numpy as np

sys.path.append(".")

# pip install lissajou
from lissajou.lissajou import (
    CircularLissajou,
    EllipticLissajou,
    FixedRatioLissajou,
    GenericLissajou,
    SinusoidalAmplitudeLissajou,
    VaryingAmplitudeLissajou,
)


def showcase_generic_lissajou():
    print("Showcasing generic Lissajou curve with default parameters...")
    # Simulate and display a generic Lissajou curve animation with default parameters
    liss = GenericLissajou()
    liss.show()

    print("Showcasing generic Lissajou curve with custom parameters...")
    # Simulate and display a generic Lissajou curve animation with custom parameters
    liss = GenericLissajou(a=7, b=50, delta=np.pi / 3, range=15, nb_points=15000)
    liss.show(max_frames=150, speed=1000 / 30)


def showcase_varying_amplitude_lissajou():
    print("Showcasing Lissajou curve with varying amplitude...")
    # Simulate and display a Lissajou curve with varying amplitude
    liss = VaryingAmplitudeLissajou(a=40, delta=np.pi / 20, range=15, nb_points=12000)
    liss.show(max_frames=200, speed=1000 / 5)


def showcase_sinusoidal_amplitude_lissajou():
    print("Showcasing Lissajou curve with sinusoidal amplitude...")
    # Simulate and display a Lissajou curve with sinusoidal amplitude
    liss = SinusoidalAmplitudeLissajou(a=6, delta=np.pi / 6, range=18, nb_points=18000)
    liss.show()


def showcase_fixed_ratio_lissajou():
    print("Showcasing Lissajou curve with fixed ratio...")
    # Simulate and display a Lissajou curve with fixed ratio
    liss = FixedRatioLissajou(a=8, delta=np.pi / 8, range=22, nb_points=11000, ratio=4)
    liss.show()


def showcase_lissajou_ellipse():
    print("Showcasing Lissajou ellipse animation...")
    # Simulate and display a Lissajou ellipse animation
    liss = EllipticLissajou(a=10, delta=np.pi / 10, range=25, nb_points=20000)
    liss.show()


def showcase_lissajou_circle():
    print("Showcasing Lissajou circle animation...")
    # Simulate and display a Lissajou circle animation
    liss = CircularLissajou(a=12, range=30, nb_points=25000)
    liss.show()


if __name__ == "__main__":
    showcase_generic_lissajou()
    showcase_varying_amplitude_lissajou()
    showcase_sinusoidal_amplitude_lissajou()
    showcase_fixed_ratio_lissajou()
    showcase_lissajou_ellipse()
    showcase_lissajou_circle()
