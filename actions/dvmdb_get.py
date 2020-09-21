"""Device Manager Database Get module"""
from lib.actions import BaseFortiManagerAction
from pyFMG.fortimgr import (FMGBaseException,
                            FMGValidSessionException,
                            FMGConnectTimeout,
                            FMGConnectionError)

__all__ = [
    'DvmdbGet'
]


class DvmdbGet(BaseFortiManagerAction):
    """Default dvmdb get action class"""

    def run(self, **kwargs):
        """
        Default dvmdb get action method.

        :baseurl: root of the url endpoint
        :table: fortimanager database section
        :adom: fortimanager adom
        :device: fortigate device
        :expand_member: fetch all or selected attributes of object members
        :fields: imit the output by returning only the attributes specified
        :filter: filter the result according to a set of criteria.
        :loadsub: enable or disable the return of any sub-objects
        :option: set fetch option for the request
        :meta_fields: Specify the meta field attributes to be returned in the result


        :return: (boolean, result)
        """
        database = kwargs.pop('database')
        table = kwargs.pop('table')
        subtable = ""
        if '/' in table:
            table, subtable = table.split('/', 1)
        if kwargs['device']:
            device = kwargs.pop('device')
            table = f"/{table}/{device}"
        if kwargs['adom']:
            adom = kwargs.pop('adom')
            adom_url = f"/adom/{adom}"
            database = f"{database}/{adom_url}"

        if kwargs['ha_slave']:
            ha_slave = kwargs['ha_slave']
            subtable = f"/ha_slave/{ha_slave}"
        if kwargs['vdom']:
            vdom = kwargs['vdom']
            subtable = f"/vdom/{vdom}"

        url = f"{database}/{table}/{subtable}"
        justargs = {k: v for k, v in kwargs.items() if v is not None}

        try:
            with self.fmgconnector() as instance:
                self.logger.info("{}".format(str(instance)))
                status, result = instance.get(url, **justargs)

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
