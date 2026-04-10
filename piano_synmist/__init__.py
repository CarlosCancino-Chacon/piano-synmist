import sys
from importlib.metadata import version
from importlib.resources import files

from .simulate_mistakes import Mistaker
from .region_classifier import RegionClassifier


# define a version variable
__version__ = version("piano_synmist")

# mistake sampling probabilities
SAMPLING_PROB = str(files("piano_synmist") / "assets" / "sampling_prob.csv")