import can
import logging
import os
import sys
import time

# Create logging object
logger = logging.getLogger(__name__)

def main():

    current_file_name = os.path.basename(sys.argv[0])
    logger.info("Starting", current_file_name)
    # Create a CAN bus object with the virtual CAN interface
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

    # Start an ever-increasing counter
    counter = 0

    try:
        while True:
            # Pack the counter value into a CAN message
            msg = can.Message(arbitration_id=0x123, data=[counter], is_extended_id=False)

            # Send the message
            bus.send(msg)

            # Print the sent message
            logger.info("Sent:", msg)

            # Increment the counter
            counter += 1

            # Guard counter from overflowing can message data (2^64)
            if(counter > 18446744073709551616):
                counter = 0

            # Wait for a short time before sending the next message
            time.sleep(3)

    except KeyboardInterrupt:
        print("\nExiting.")

if __name__ == "__main__":
    main()

