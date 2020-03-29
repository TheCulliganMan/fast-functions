import numpy as np
from fast_functions.geodesic import geodesic_single, geodesic_array

avon_lat, avon_lng = 45.6091, -94.4517
minneapolis_lat, minneapolis_lng = 44.9778, -93.2650

def test_geodesic_single():
    result = geodesic_single(avon_lat, avon_lng, minneapolis_lat, minneapolis_lng) 
    assert round(result, 2) == 116.38

def test_geodesic_array():
    lat1 = np.array([avon_lat] * 1_000)
    lng1 = np.array([avon_lng] * 1_000)
    lat2 = np.array([minneapolis_lat] * 1_000)
    lng2 = np.array([minneapolis_lng] * 1_000)
    results = geodesic_array(lat1, lng1, lat2, lng2)
    assert all([round(result, 2) == 116.38 for result in results])

if __name__ == "__main__":
    test_geodesic_single()
    test_geodesic_array()