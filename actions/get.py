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

    def run(self, **kwargs):
        """
        Default get action.

        :url: URL to get - FortiManager version

        :return: (boolean, result)
        """
        url = kwargs.pop('url')

        try:
            with self.fmgconnector() as instance:
                self.logger.info("{}".format(str(instance)))
                status, result = instance.get(url, **kwargs)

            if status == 0:
                return (True, result)
            return (False, result)

        except FMGValidSessionException:
            self.logger.critical("Invalid Session - Check Credentials")
            return (False, "Session Failed")
        except (FMGConnectTimeout, FMGConnectionError):
            self.logger.critical("Unreachable Host - Check Hostname/IP")
            return (False, "Connection Failed")
