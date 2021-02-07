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
        self.conn_ssl = self.config['conn_ssl']
        self.conn_warn = self.config['conn_warn']
        self.conn_verify = self.config['conn_verify']
        self.conn_timeout = self.config['conn_timeout']
        self._fmg = FortiManager

    def fmgconnector(self, fortimanager=None, username=None, password=None, debug=False):
        """Default connector for FortiManager"""
        if not fortimanager:
            fortimanager = self.fortimanager
        if not username:
            username = self.username
        if not password:
            password = self.password
        fmg = self._fmg(fortimanager,
                        username,
                        password,
                        debug=debug,
                        use_ssl=self.conn_ssl,
                        disable_request_warnings=self.conn_warn,
                        verify_ssl=self.conn_verify,
                        timeout=self.conn_timeout)

        return fmg
