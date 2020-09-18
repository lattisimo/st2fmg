from lib.actions import BaseFortiManagerAction


__all__ = [
    'Update'
]


class Update(BaseFortiManagerAction):
    """Default Update action class"""

    def run(self, url, **kwargs):
        """
        Default Update action.

        :url: URL to Update - for FortiManager version
        :kwargs: keyword arguments

        :return: (boolean, result)
        """
        with self.fmgconnector() as fmg:
            status, result = fmg.get(url, **kwargs)
        if status == 0:
            return (True, result)
        return (False, result)
