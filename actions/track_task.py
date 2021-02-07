"""Device Manager Database Get module"""
from lib.actions import BaseFortiManagerAction
from pyFMG.fortimgr import (FMGBaseException,
                            FMGValidSessionException,
                            FMGConnectTimeout,
                            FMGConnectionError)


__all__ = [
    'TrackTask'
]


class TrackTask(BaseFortiManagerAction):
    """Default set action class"""

    def run(self, **kwargs):
        """
        Default set action method.

        :host: overwrite fortimanager ip or hostname
        :username: overwriting username
        :password: overwriging password
        :url: api endpoint
        :data: dictionary of data to pass as arguments
        :fmg_debug: print rpc calls to stdout
        :return: (boolean, result)
        """
        fortimanager = kwargs.pop("host")
        username = kwargs.pop("username")
        password = kwargs.pop("password")
        taskid = kwargs.pop("taskid")
        fmg_debug = kwargs.pop("fmg_debug")
        try:
            with self.fmgconnector(fortimanager,
                                   username=username,
                                   password=password,
                                   debug=fmg_debug
                                   ) as instance:
                self.logger.info("{}".format(str(instance)))
                self.logger.info("{}".format(
                    "FortiManager instance endpoint {}".format("Track Task")))
                code, result = instance.track_task(taskid)
            self.logger.info("{}".format("FortiManager instance disonnected"))

            if code:
                return (False, result)
            return (True, result)

        except FMGValidSessionException:
            self.logger.critical("Invalid Session - Check Credentials")
            return (False, "Session Failed")
        except (FMGConnectTimeout, FMGConnectionError):
            self.logger.critical("Unreachable Host - Check Hostname/IP")
        except FMGBaseException:
            self.logger.exception("Connection Error")
            return (False, "Connection Failed")
