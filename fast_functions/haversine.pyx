from libc.math cimport sin, cos, asin, sqrt
cimport numpy as np
import numpy as np

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

cdef np.float64_t c_haversine_single(np.float64_t lat1, np.float64_t lng1, np.float64_t lat2, np.float64_t lng2, np.float64_t unit=MeterConverter["kilometers"]):
    cdef np.float64_t rad_lat1, rad_lon1, rad_lat2, rad_lon2, lat_delta, lng_delta, a, c, km, converted
    rad_lat1 = np.radians(lat1)
    rad_lng1 = np.radians(lng1)
    rad_lat2 = np.radians(lat2)
    rad_lng2 = np.radians(lng2)
    lat_delta = rad_lat2 - rad_lat1
    lng_delta = rad_lng2 - rad_lng1
    a = sin(lat_delta / 2) ** 2 + cos(rad_lat1) * cos(rad_lat2) * sin(lng_delta / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    converted = unit * km
    return converted


cdef np.ndarray[np.float64_t, ndim=1] c_haversine_array(
    np.ndarray[np.float64_t, ndim=1] lat1, 
    np.ndarray[np.float64_t, ndim=1] lng1, 
    np.ndarray[np.float64_t, ndim=1] lat2, 
    np.ndarray[np.float64_t, ndim=1] lng2, 
    np.float64_t unit=MeterConverter["kilometers"]
):
    cdef np.ndarray[np.float64_t, ndim=1] rad_lat1, rad_lon1, rad_lat2, rad_lon2, lat_delta, lng_delta, a, c, km, converted
    rad_lat1 = np.radians(lat1)
    rad_lng1 = np.radians(lng1)
    rad_lat2 = np.radians(lat2)
    rad_lng2 = np.radians(lng2)
    lat_delta = rad_lat2 - rad_lat1
    lng_delta = rad_lng2 - rad_lng1
    a = np.sin(lat_delta / 2) ** 2 + np.cos(rad_lat1) * np.cos(rad_lat2) * np.sin(lng_delta / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6371 * c
    converted = unit * km
    return converted

def haversine_single(
    lat1: float, 
    lng1: float, 
    lat2: float, 
    lng2: float, 
    unit: float=MeterConverter["kilometers"]
) -> float:
    return c_haversine_single(lat1, lng1, lat2, lng2)

def haversine_array(
    lat1: np.array, 
    lng1: np.array, 
    lat2: np.array, 
    lng2: np.array, 
    unit: float=MeterConverter["kilometers"]
) -> np.array:
    return c_haversine_array(lat1, lng1, lat2, lng2)
