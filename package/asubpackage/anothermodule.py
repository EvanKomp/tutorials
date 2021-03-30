"""A demonstration class.

This class is inside a subpackage module.
"""
import os


class Demonstration:
    """Class defineing a demonstration.

    Parameters
    ----------
        demo_file : str
            Path to demonstration file.
        description : str, optional
            Description for the demonstration.

    Attributes
    ----------
        demo_file
        description : See Parameters
    """

    def __init__(self, demo_file, description=None):
        self.demo_file = demo_file
        if description is not None:
            assert isinstance(description, str),\
                "Cannot set description as non-string."
            self.description = description
        return

    @property
    def demo_file(self):
        """str: Path to the demonstration file."""
        return self._demo_file

    @demo_file.setter
    def demo_file(self, new_file):
        assert isinstance(new_file, str),\
            "Cannot set file location as non-string."
        assert os.path.exists(new_file),\
            "demo file does not exist in path"
        self._demo_file = new_file
        return
