import timeit

setup_cuda = """
import cupy as cp
from fast_functions.haversine_cuda import haversine_array_cuda
lat1 = cp.array([avon_lat] * 10000)
lng1 = cp.array([avon_lng] * 10000)
lat2 = cp.array([minneapolis_lat] * 10000)
lng2 = cp.array([minneapolis_lng] * 10000)
"""
statement_cuda = """haversine_array_cuda(lat1, lng1, lat2, lng2)"""

setup_numpy = """
from fast_functions.haversine import haversine_array
import numpy as np
lat1 = np.array([avon_lat] * 10000)
lng1 = np.array([avon_lng] * 10000)
lat2 = np.array([minneapolis_lat] * 10000)
lng2 = np.array([minneapolis_lng] * 10000)
"""
statement_numpy = """haversine_array(lat1, lng1, lat2, lng2)"""