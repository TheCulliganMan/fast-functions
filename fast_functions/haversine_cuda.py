import cupy as cp

MeterConverter = dict(
    kilometers = 1.0,
    meters = 1000.0,
    miles = 0.621371192,
    nautical_miles = 0.539956803,
    feet = 3280.839895013,
    inches = 39370.078740158,
)


def haversine_array_cuda(
    lat1: cp.array, 
    lng1: cp.array, 
    lat2: cp.array,
    lng2: cp.array, 
    unit: float=MeterConverter["kilometers"]
) -> cp.array:
    """
    Cupy is much faster than numpy
    >>> print(timeit.timeit(statement_cuda, setup_cuda, number=1000))
    2.6088396040004227
    >>> print(timeit.timeit(statement_numpy, setup_numpy, number=1000))
    71.15440212700014
    """
    rad_lat1 = cp.radians(lat1)
    rad_lng1 = cp.radians(lng1)
    rad_lat2 = cp.radians(lat2)
    rad_lng2 = cp.radians(lng2)
    lat_delta = rad_lat2 - rad_lat1
    lng_delta = rad_lng2 - rad_lng1
    a = cp.sin(lat_delta / 2) ** 2 + cp.cos(rad_lat1) * cp.cos(rad_lat2) * cp.sin(lng_delta / 2) ** 2
    c = 2 * cp.arcsin(cp.sqrt(a))
    km = 6371 * c
    converted = unit * km
    return converted

