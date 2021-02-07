from st2tests.base import BaseActionTestCase
from dvmdb_get import DvmdbGet

__all__ = [
    "DvmdbDeviceGetActionTestCase"
]


class DvmdbDeviceGetActionTestCase(BaseActionTestCase):
    action_cls = DvmdbGet

    def test_get_device(self):
        action = self.get_action_instance(config={'foo': 'bar'})
        result = action.run()
        # ...
