from lib.actions import BaseFortiManagerAction


__all__ = [
    'Delete'
]


class Delete(BaseFortiManagerAction):
    """Default delte action class"""

    def run(self, url, **kwargs):
        """
        Default delete action.

        :url: URL to delete - for FortiManager version
        :kwargs: keyword arguments

        :return: (boolean, result)
        """
        with self.fmgconnector() as fmg:
            status, result = fmg.delete(url, **kwargs)
        if status == 0:
            return (True, result)
        return (False, result)
