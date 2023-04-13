import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 1266169265 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_value = ks_2samp(x, y)[1]
    if p_value < 0.03:
        return True
    else:
        return False

