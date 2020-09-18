from lib.actions import BaseFortiManagerAction


__all__ = [
    'Add'
]


class Add(BaseFortiManagerAction):
    """Default add action class"""

    def run(self, url, **kwargs):
        """
        Default add action.

        :url: URL to add - FortiManager version
        :kwargs: keyword arguments

        :return: (boolean, result)
        """
        with self.fmgconnector() as fmg:
            status, result = fmg.get(url, **kwargs)
        if status == 0:
            return (True, result)
        return (False, result)
