from unittest import TestCase
from unittest.mock import Mock
from hardware_interface import FlashMemoryDevice
from device_driver import DeviceDriver

FAILED_READ_RESULT = [0x0, 0x0, 0x0, 0x4, 0x0]

NON_WRITABLE_READ_RESULT = [0x1 for _ in range(5)]

WRITABLE_READ_RESULT = [0x0 for _ in range(5)]


class DeviceDriverTest(TestCase):

    def setUp(self):
        self.device = Mock(spec=FlashMemoryDevice)
        self.driver = DeviceDriver(self.device)

    def test_read_raise_exception(self):
        self.device.read.side_effect = FAILED_READ_RESULT

        with self.assertRaises(Exception) as context:
            self.driver.read(0xFF)
        self.assertEqual(str(context.exception), "ReadFailException")

    def test_successful_read(self):
        self.device.read.side_effect = WRITABLE_READ_RESULT

        self.assertEqual(0x0, self.driver.read(0xFF))

        self.device.read.side_effect = NON_WRITABLE_READ_RESULT

        self.assertEqual(0x1, self.driver.read(0xFF))

    def test_write_raise_exception(self):
        self.device.read.side_effect = NON_WRITABLE_READ_RESULT

        with self.assertRaises(Exception) as context:
            self.driver.write(0x3A, 1)
        self.assertEqual(str(context.exception), "WriteFailException")
