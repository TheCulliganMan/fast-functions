cimport numpy as np
import numpy as np
import cupy as cp

cdef struct c_Unit:
    np.float64_t kilometers
    np.float64_t meters
    np.float64_t miles
    np.float64_t nautical_miles
    np.float64_t feet
    np.float64_t inches


MeterConverter = c_Unit(
    kilometers = 1.0,
    meters = 1000.0,
    miles = 0.621371192,
    nautical_miles = 0.539956803,
    feet = 3280.839895013,
    inches = 39370.078740158,
)


cdef np.ndarray[np.float64_t, ndim=1] c_haversine_array_cuda(
    np.ndarray[np.float64_t, ndim=1] lat1, 
    np.ndarray[np.float64_t, ndim=1] lng1, 
    np.ndarray[np.float64_t, ndim=1] lat2, 
    np.ndarray[np.float64_t, ndim=1] lng2, 
    np.float64_t unit=MeterConverter["kilometers"]
):
    cdef np.ndarray[np.float64_t, ndim=1] rad_lat1, rad_lon1, rad_lat2, rad_lon2, lat_delta, lng_delta, a, c, km, converted
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


def haversine_array_cuda(
    lat1: cp.array, 
    lng1: cp.array, 
    lat2: cp.array, 
    lng2: cp.array, 
    unit: float=MeterConverter["kilometers"]
) -> cp.array:
    return c_haversine_array_cuda(lat1, lng1, lat2, lng2)
