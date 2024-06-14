from hardware_interface import FlashMemoryDevice

WRITABLE_VALUE = 0xFF


class DeviceDriver:
    """
    This class is used by the operating system to interact with the hardware 'FlashMemoryDevice'.
    """

    def __init__(self, device: FlashMemoryDevice):
        """
        :type device: hardware_interface.FlashMemoryDevice
        """
        self.__device = device

    def write(self, address: int, data: int) -> None:
        if self.read(address) != WRITABLE_VALUE:
            raise Exception("WriteFailException")
        self.__device.write(address, data)

    def read(self, address: int) -> int:
        result = set(self.__device.read(address) for _ in range(5))
        if len(result) > 1:
            raise Exception("ReadFailException")
        return result.pop()
