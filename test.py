# Начнем с импорта необходимых пакетов 
import matplotlib.pyplot as plt 
import seaborn as sns; sns.set() 
import numpy as np
from sklearn.cluster import KMeans

from sklearn.datasets import load_digits 
digits = load_digits() 
digits.data.shape