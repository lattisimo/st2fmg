from lib.actions import BaseFortiManagerAction


__all__ = [
    'Get'
]


class Get(BaseFortiManagerAction):
    """Default get action class"""

    def run(self, url):
        """
        Default get action.

        :url: URL to get - FortiManager version

        :return: (boolean, result)
        """
        with self.fmgconnector() as fmg:
            status, result = fmg.get(url)
        if status == 0:
            return (True, result)
        return (False, result)
