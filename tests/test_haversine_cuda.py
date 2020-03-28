try:

    import numpy as np
    from fast_functions.haversine_cuda import haversine_array_cuda

    avon_lat, avon_lng = 45.6091, -94.4517
    minneapolis_lat, minneapolis_lng = 44.9778, -93.2650

    def test_haversine_array_cuda():
        lat1 = np.array([avon_lat] * 1_000)
        lng1 = np.array([avon_lng] * 1_000)
        lat2 = np.array([minneapolis_lat] * 1_000)
        lng2 = np.array([minneapolis_lng] * 1_000)
        results = haversine_array_cuda(lat1, lng1, lat2, lng2)
        assert all([round(result, 2) == 116.38 for result in results])

except ImportError:
    pass  # not everything is cuda