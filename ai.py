import pandas as pd
import tensorflow as tf
tf.__version__
from tensorflow import keras
keras.__version__

from tensorflow.python.client import device_lib
device_lib.list_local_devices()


import torch
torch.cuda.get_device_name(0) 
torch.cuda.is_available() 
torch.__version__