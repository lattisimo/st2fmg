from lib.actions import BaseFortiManagerAction


__all__ = [
    'Call'
]


class Call(BaseFortiManagerAction):
    """Gerneric Call action class"""

    def run(self, **kwargs):
        """
        Call action runner.

        :kwargs: keyword arguments that must include an action and url

        :return: (boolean, result)
        """
        action = kwargs.pop('reqmethod')
        url = kwargs.pop('url')
        with self.fmgconnector() as fmg:
            status, result = getattr(fmg, f"{reqmethod}({url}, {**kwargs}")
        if status == 0:
            return (True, result)
        return (False, result)
