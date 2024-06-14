from unittest import TestCase
from unittest.mock import Mock
from hardware_interface import FlashMemoryDevice
from device_driver import DeviceDriver


class DeviceDriverTest(TestCase):

    def setUp(self):
        self.device = Mock(spec=FlashMemoryDevice)
        self.driver = DeviceDriver(self.device)

    def test_read_raise_exception(self):
        self.device.read.side_effect = [0x0, 0x0, 0x0, 0x4, 0x0]

        with self.assertRaises(Exception) as context:
            self.driver.read(0xFF)
        self.assertEqual(str(context.exception), "ReadFailException")

    def test_successful_read(self):
        self.device.read.side_effect = [0x0, 0x0, 0x0, 0x0, 0x0]

        self.assertEqual(0x0, self.driver.read(0xFF))

        self.device.read.side_effect = [0x1 for _ in range(5)]

        self.assertEqual(0x1, self.driver.read(0xFF))
