"""Testing contents of amodule."""
import pytest

import numpy as np

import package.amodule


def test_convert_to_float():
    """Correct conversion to float types."""
    # try individual values
    for inp in [5, 3.0, '9.5']:
        subject = package.amodule.convert_to_float(inp)
        assert isinstance(subject, np.float32),\
            "Did not convert to float."

    # and the full precision option
    subject = package.amodule.convert_to_float(5, full_precision=True)
    assert isinstance(subject, np.float64),\
        "Did not convert to float with full precision"

    # invalid argument
    with pytest.raises(TypeError):
        subject = package.amodule.convert_to_float('string')

    # try an array
    subject = package.amodule.convert_to_float(
        np.array([1, 2, 3]),
        full_precision=True
    )
    assert subject.dtype == np.float64,\
        "Array not converted with correct precision."
    return
