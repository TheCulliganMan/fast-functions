import timeit

setup_cuda = """
import cupy as cp
from fast_functions.haversine_cuda import haversine_array_cuda
avon_lat, avon_lng = 45.6091, -94.4517
minneapolis_lat, minneapolis_lng = 44.9778, -93.2650
lat1 = cp.array([avon_lat] * 1000000)
lng1 = cp.array([avon_lng] * 1000000)
lat2 = cp.array([minneapolis_lat] * 1000000)
lng2 = cp.array([minneapolis_lng] * 1000000)
"""
statement_cuda = """haversine_array_cuda(lat1, lng1, lat2, lng2)"""

setup_numpy = """
from fast_functions.haversine import haversine_array
avon_lat, avon_lng = 45.6091, -94.4517
minneapolis_lat, minneapolis_lng = 44.9778, -93.2650
import numpy as np
lat1 = np.array([avon_lat] * 1000000)
lng1 = np.array([avon_lng] * 1000000)
lat2 = np.array([minneapolis_lat] * 1000000)
lng2 = np.array([minneapolis_lng] * 1000000)
"""
statement_numpy = """haversine_array(lat1, lng1, lat2, lng2)"""
print(timeit.timeit(statement_cuda, setup_cuda, number=1000))
print(timeit.timeit(statement_numpy, setup_numpy, number=1000))
