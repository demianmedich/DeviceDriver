from unittest import TestCase
from unittest.mock import Mock
from hardware_interface import FlashMemoryDevice
from device_driver import DeviceDriver


class DeviceDriverTest(TestCase):

    def test_read_raise_exception(self):
        device = Mock(spec=FlashMemoryDevice)
        device.read.side_effect = [0x0, 0x0, 0x0, 0x4, 0x0]

        driver = DeviceDriver(device)
        with self.assertRaises(Exception) as context:
            driver.read(0xFF)
        self.assertEqual(str(context.exception), "ReadFailException")

    def test_successful_read(self):
        hardware: FlashMemoryDevice = Mock()
        driver = DeviceDriver(hardware)
        self.assertEqual(0x0, driver.read(0xFF))
