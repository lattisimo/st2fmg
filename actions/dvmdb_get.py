"""Device Manager Database Get module"""
from lib.actions import BaseFortiManagerAction
from pyFMG.fortimgr import (FMGBaseException,
                            FMGValidSessionException,
                            FMGConnectTimeout,
                            FMGConnectionError)

__all__ = [
    'dvmdbGet'
]


class dvmdbGet(BaseFortiManagerAction):
    """Default dvmdb get action class"""

    def run(self, **kwargs):
        """
        Default dvmdb get action method.

        :url: URL to get - FortiManager version

        :return: (boolean, result)
        """
        url = f"{kwargs.pop('rooturl')}/{kwargs.pop('section')}"
        if 'adom' in kwargs:
            adom = kwargs.pop('adom')
            url = f"{kwargs.pop('root')}/adom/{adom}/device"
        if 'device' in kwargs:
            device = kwargs.pop('device')
            url = f"{url}/{device}"

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
        except FMGBaseException:
            self.logger.exception("Connection Error")
            return (False, "Connection Failed")
