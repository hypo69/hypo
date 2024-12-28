import socket
from typing import Tuple, Optional
from src.logger.logger import logger

def get_free_port(host: str, port_range: Optional[Tuple[int, int]] = None) -> int:
    """
    Finds and returns a free port within the specified range, or the first available port if no range is given.

    :param host: The host address to check for available ports.
    :type host: str
    :param port_range: (Optional) A tuple containing the start and end of the port range to search, if needed.
    :type port_range: Optional[Tuple[int, int]]
    :return: An available port number.
    :rtype: int
    :raises ValueError: If no free port can be found within the specified range, or if the port range is invalid.
    """
    def _is_port_in_use(host: str, port: int) -> bool:
        """
        Checks if a given port is in use on the specified host.

        :param host: The host address to check.
        :type host: str
        :param port: The port number to check.
        :type port: int
        :return: True if the port is in use, False otherwise.
        :rtype: bool
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind((host, port))
                return False  # Port is available
            except OSError:
                return True  # Port is in use


    if port_range:
        if len(port_range) != 2 or port_range[0] >= port_range[1]:
             logger.error(f'Error: Invalid port range {port_range}')
             raise ValueError(f'Invalid port range {port_range}')

        min_port, max_port = port_range
        for port in range(min_port, max_port + 1):
            if not _is_port_in_use(host, port):
                return port
        logger.error(f'Error: No free port found in range {port_range}')
        raise ValueError(f'No free port found in range {port_range}')
    else:
       # If no range given, find first available port
        port = 1024 # start from 1024, since lower ports are system ports
        while True:
            if not _is_port_in_use(host, port):
                return port
            port += 1
            if port > 65535:
                logger.error(f'Error: No free port found')
                raise ValueError('No free port found')