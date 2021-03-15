import numpy as np
from fast_functions.haversine_jax import haversine_array_jax

avon_lat, avon_lng = 45.6091, -94.4517
minneapolis_lat, minneapolis_lng = 44.9778, -93.2650

def test_haversine_array():
    lat1 = np.array([avon_lat] * 10000)
    lng1 = np.array([avon_lng] * 10000)
    lat2 = np.array([minneapolis_lat] * 10000)
    lng2 = np.array([minneapolis_lng] * 10000)
    results = haversine_array_jax(lat1, lng1, lat2, lng2)
    assert all([round(result, 0) == 116.0 for result in results]), round(results[0], 0)

if __name__ == "__main__":
    test_haversine_array()