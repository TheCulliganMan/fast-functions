try:

    import cupy as cp
    from fast_functions.haversine_cuda import haversine_array_cuda

    avon_lat, avon_lng = 45.6091, -94.4517
    minneapolis_lat, minneapolis_lng = 44.9778, -93.2650

    def test_haversine_array_cuda():
        lat1 = cp.array([avon_lat] * 10000)
        lng1 = cp.array([avon_lng] * 10000)
        lat2 = cp.array([minneapolis_lat] * 10000)
        lng2 = cp.array([minneapolis_lng] * 10000)
        results = haversine_array_cuda(lat1, lng1, lat2, lng2)
        assert all([round(result, 2) == 116.38 for result in results])

    if __name__ == "__main__":
        test_haversine_array_cuda()

except ImportError:
    pass  # not everything is cuda