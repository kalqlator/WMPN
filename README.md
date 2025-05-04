# Raspberry Pi HATs Setup

This project demonstrates how to set up and use both the WM8950 HAT (audio codec) and PN532 HAT (NFC/RFID reader) on Raspberry Pi 3.

## Hardware Requirements

- Raspberry Pi 3
- WM8950 HAT
- PN532 HAT
- NFC/RFID tags for testing

## Installation

1. Enable I2C and SPI interfaces:
   ```bash
   sudo raspi-config
   ```
   - Navigate to "Interfacing Options"
   - Enable I2C and SPI
   - Reboot the Raspberry Pi

2. Install the required packages:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip python3-smbus python3-spidev
   pip3 install -r requirements.txt
   ```

3. Connect the HATs:
   - Connect the WM8950 HAT to the Raspberry Pi's GPIO header
   - Connect the PN532 HAT to the Raspberry Pi's SPI interface

## Usage

Run the test script:
```bash
python3 test_hats.py
```

The script will:
1. Initialize both HATs
2. Test NFC functionality
3. Test audio functionality

## Notes

- Make sure to connect the HATs in the correct order
- The WM8950 HAT should be connected first
- The PN532 HAT should be connected to the SPI interface

## Troubleshooting

If you encounter any issues, check:
1. That both HATs are properly connected
2. That I2C and SPI interfaces are enabled
3. That the required packages are installed
4. That the GPIO pins are not being used by other processes
