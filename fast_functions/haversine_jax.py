import jax.numpy as jnp
from jax import jit

MeterConverter = dict(
    kilometers = 1.0,
    meters = 1000.0,
    miles = 0.621371192,
    nautical_miles = 0.539956803,
    feet = 3280.839895013,
    inches = 39370.078740158,
)


def haversine_array_jax_precompiled(
    lat1: jnp.array, 
    lng1: jnp.array, 
    lat2: jnp.array,
    lng2: jnp.array, 
    unit: float=MeterConverter["kilometers"]
) -> jnp.array:
    """
    Cupy is much faster than numpy
    >>> print(timeit.timeit(statement_cuda, setup_cuda, number=1000))
    2.6088396040004227
    >>> print(timeit.timeit(statement_numpy, setup_numpy, number=1000))
    71.15440212700014
    """
    rad_lat1 = jnp.radians(lat1)
    rad_lng1 = jnp.radians(lng1)
    rad_lat2 = jnp.radians(lat2)
    rad_lng2 = jnp.radians(lng2)
    lat_delta = rad_lat2 - rad_lat1
    lng_delta = rad_lng2 - rad_lng1
    a = jnp.sin(lat_delta / 2) ** 2 + jnp.cos(rad_lat1) * jnp.cos(rad_lat2) * jnp.sin(lng_delta / 2) ** 2
    c = 2 * jnp.arcsin(jnp.sqrt(a))
    km = 6371 * c
    converted = unit * km
    return converted

haversine_array_jax = jit(haversine_array_jax_precompiled)