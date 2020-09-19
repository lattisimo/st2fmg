from lib.actions import BaseFortiManagerAction
from pyFMG.fortimgr import (FMGBaseException,
                            FMGValidSessionException,
                            FMGConnectTimeout,
                            FMGConnectionError)

__all__ = [
    'FortimanagerGet'
]


class FortimanagerGet(BaseFortiManagerAction):
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
                self.logger.debug("{}".format(fmg.__repr__))
                self.logger.info("{}".format(fmg.__str__))
            if status == 0:
                return (True, result)
            return (False, result)

        except FMGValidSessionException:
            self.logger.critical("Invalid Session - Check Credentials")
            return (False, "Session Failed")
        except (FMGConnectTimeout, FMGConnectionError):
            self.logger.critical("Unreachable Host - Check Hostname/IP")
            return (False, "Connection Failed")
