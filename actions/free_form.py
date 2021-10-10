from lib.actions import BaseFortiAnalyzerAction
from pyFMG.fortimgr import FortiAnalyzer


__all__ = [
    'FreeForm'
]


class FreeForm(BaseFortiAnalyzerAction):
    def run(self, **kwargs):  # host, url, data, fmg_debug=False
        """
        Pass fortianalyzer host address, freefrom call url, and data payload
        to use generical pyFMG freeform method. 
        """
        fortianalyzer = kwargs.pop("host")
        username = kwargs.pop("username")
        password = kwargs.pop("password")
        faz_debug = kwargs.pop("faz_debug")
        method = kwargs.pop('method')
        fmg_debug = kwargs.pop('fmg_debug')
        url = kwargs.pop('url')
        payload = kwargs.pop('data')
        payload['url'] = url
        freeform = [payload]

        with FortiAnalyzer(fortianalyzer,
                          self.username,
                          self.password,
                          verbose=self.verbose,
                          disable_request_warnings=self.disable_request_warnings,
                          debug=fmg_debug) as fmg_instance:

            rpc_code, result = fmg_instance.free_form(method, data=freeform)

        if rpc_code:
            return (False, result)
        return (True, result)