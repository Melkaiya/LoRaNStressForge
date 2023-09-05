# class_vNodes.py
# vNodes (Virtual Nodes):
# 
# vNodes can serve as the foundation for creating minimal, lightweight virtual LoRaWAN nodes
# for stress testing and hammering your LNS (LoRaWAN Network Server).
# These virtual nodes can be designed with minimal configuration settings to simplify the process
# of sending data to a virtual gateway and, subsequently, to a real LNS.
# This will be invaluable for stress testing your LNS.

import random
import string

class VNodes:
    def __init__(self, node_id, dev_eui, app_eui, app_key):
        """
        Initialize a virtual LoRaWAN node.

        Args:
            node_id (str): Unique identifier for the node.
            dev_eui (str): Device EUI (EUI64) for the node.
            app_eui (str): Application EUI for the node.
            app_key (str): Application Key for secure communication.
        """
        self.node_id = node_id
        self.dev_eui = dev_eui
        self.app_eui = app_eui
        self.app_key = app_key

    def send_data(self):
        """
        Simulate sending data from the node.

        Returns:
            str: Simulated LoRaWAN-like payload.
        """
        # Generate a random string of 16 characters (uppercase letters, lowercase letters, and numbers)
        random_data = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))

        # Construct the data message
        data_message = f"Hello Server, Random volatile data {random_data}"

        # Create a LoRaWAN-like payload with the data message
        lorawan_payload = {
            "data": data_message,
            "devEUI": self.dev_eui,
            "appEUI": self.app_eui,
            "fCnt": 1,  # Frame counter (increment as needed)
            "fPort": 1,  # Port number
        }

        return lorawan_payload