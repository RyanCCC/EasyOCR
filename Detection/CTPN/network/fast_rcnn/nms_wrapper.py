import numpy as np
from .config import cfg
from utils.nms import nms

def nms(dets, thresh):
    if dets.shape[0] == 0:
        return []
    return nms(dets, thresh)
