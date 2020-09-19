from lib.actions import BaseFortiManagerAction
from pyFMG.fortimgr import (FMGBaseException,
                            FMGValidSessionException,
                            FMGConnectTimeout)

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
        try:
            with self.fmgconnector() as fmg:
                status, result = fmg.get(url)
        except FMGValidSessionException:
            self.logger.critical("Invalid Session - Check Credentials")
        except FMGConnectTimeout:
            self.logger.critical("Unreachable Host - Check hostname/IP")
        if status == 0:
            return (True, result)
        return (False, result)
