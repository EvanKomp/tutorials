"""Description of this module.

Examples
--------
>>>give an example
"""
import numpy


def convert_to_float(x, full_precision=False):
    """Convert an input to a float with desired precision.

    Parameters
    ----------
        x : :obj: or :obj:numpy.ndarray of :obj:
            Input to convert to float.
        full_precision : bool
            Whether or not to use 64 bit float precision.

    Returns
    -------
        x_out : numpy.floatXX
            The converted input. Desired 32 or 64 bit precision.
    """
    try:
        if full_precision:
            x_out = numpy.float64(x)
        else:
            x_out = numpy.float32(x)
    except BaseException:
        raise TypeError(
            'Cannot convert input type {} to float'.format(type(x))
        )
    return x_out
