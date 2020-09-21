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
        url, data = dvmdb_parse(kwargs)
        try:
            with self.fmgconnector() as instance:
                self.logger.info("{}".format(str(instance)))
                self.logger.info("{}".format("FortiManager instance endpoint {}".format(url)))
                status, result = instance.get(url, **data)
            self.logger.info("{}".format("FortiManager instance disonnected"))

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


def dvmdb_parse(runnerdata):
    """dvmdb data parser"""
    data = {k: v for k, v in runnerdata.items() if v is not None}
    if 'loadsub' not in data:  # stackstorm doesn't like to send a zero
        data['loadsub'] = 0

    database = data.pop('database')
    if '_global' in data:
        if data['_global']:
            database = f"{database}/{data['_global']}"
    if 'adom' in data:
        adom = data.pop('adom')
        adom_url = f"adom/{adom}"
        database = f"{database}/{adom_url}"

    table = data.pop('table')
    subtable = ""
    if '/' in table:
        table, subtable = table.split('/', 1)
        if 'ha_slave' in data:
            ha_slave = data['ha_slave']
            subtable = f"ha_slave/{ha_slave}"
        if 'vdom' in data:
            vdom = data['vdom']
            subtable = f"vdom/{vdom}"

    if 'name' in data:
        name = data.pop('name')
        table = f"{table}/{name}"

    url = f"{database}/{table}/{subtable}"
    return url, data
