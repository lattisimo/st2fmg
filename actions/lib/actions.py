"""Base module for Fortimanager pack"""
from st2common.runners.base_action import Action
from pyFMG.fortimgr import FortiManager

__all__ = [
    'BaseFortiManagerAction'
]


class BaseFortiManagerAction(Action):
    """ Base Action for Fortimanager pack"""

    def __init__(self, config):
        super(BaseFortiManagerAction, self).__init__(config=config)
        self.fortimanager = self.config['fortimanager']
        self.username = self.config['username']
        self.password = self.config['password']
        self.conn_debug = self.config['conn_debug']
        self.conn_ssl = self.config['conn_ssl']
        self.conn_warn = self.config['conn_warn']
        self.conn_verify = self.config['conn_verify']
        self.conn_timeout = self.config['conn_timeout']
        self.fmg = FortiManager

    def fmgconnector(self):
        """Default connector for FortiManager"""

        fmg = self.fmg(self.fortimanager,
                       self.username,
                       self.password,
                       debug=self.conn_debug,
                       use_ssl=self.conn_ssl,
                       disable_request_warnings=self.conn_warn,
                       verify_ssl=self.conn_verify,
                       timeout=self.conn_timeout)

        self.logger.debug("{}".format(fmg.__repr__))
        self.logger.info("API User {} connected to {}".format(
            self.username, self.fortimanager))

        return fmg
