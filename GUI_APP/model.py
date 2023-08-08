import tensorflow as tf
from recource_utils import resource_path
from enum import Enum

class ButterflySpecies(Enum):
    Peacock_butterfly = "Peacock butterfly"
    Silver_washed_fritillary = "Silver-washed fritillary"
    Mourning_cloak = "Mourning cloak"
    Swallowtail_butterfly = "Swallowtail butterfly"
    Red_admiral = "Red admiral"

def load_model():
    return tf.keras.models.load_model(resource_path("CNN_Model1"))