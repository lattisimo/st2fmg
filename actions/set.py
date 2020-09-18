from lib.actions import BaseFortiManagerAction


__all__ = [
    'Set'
]


class Set(BaseFortiManagerAction):
    """Default set action class"""

    def run(self, url, **kwargs):
        """
        Default set action.

        :url: URL to set - for FortiManager version
        :kwargs: keyword arguments

        :return: (boolean, result)
        """
        with self.fmgconnector() as fmg:
            status, result = fmg.get(url, **kwargs)
        if status == 0:
            return (True, result)
        return (False, result)
