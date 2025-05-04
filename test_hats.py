import time
import board
import busio
import digitalio
import adafruit_pn532.spi
import RPi.GPIO as GPIO
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

def setup_pn532():
    # Create SPI interface
    spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
    
    # Create CS (Chip Select) pin
    cs = digitalio.DigitalInOut(board.D5)
    
    # Create PN532 instance
    pn532 = adafruit_pn532.spi.SPN532(spi, cs)
    
    # Initialize PN532
    ic, ver, rev, support = pn532.get_firmware_version()
    print(f"Found PN532 with firmware version: {ver}.{rev}")
    
    # Configure PN532 to read NFC tags
    pn532.SAM_configuration()
    return pn532

def setup_wm8950():
    # Initialize GPIO
    GPIO.setmode(GPIO.BCM)
    
    # Configure GPIO pins for WM8950
    GPIO.setup(18, GPIO.OUT)  # WM8950 reset pin
    GPIO.setup(23, GPIO.OUT)  # WM8950 enable pin
    
    # Reset WM8950
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(18, GPIO.HIGH)
    
    # Enable WM8950
    GPIO.output(23, GPIO.HIGH)
    
    print("WM8950 initialized successfully")

def test_nfc(pn532):
    print("\nWaiting for NFC tags...")
    while True:
        # Check if a card is available to read
        uid = pn532.read_passive_target(timeout=0.5)
        if uid is not None:
            print(f"Found card with UID: {uid.hex()}")
            break
        time.sleep(0.5)

def test_audio():
    print("\nTesting audio output...")
    # Add your audio testing code here
    # This will depend on your specific audio setup
    print("Audio test complete")

if __name__ == "__main__":
    try:
        print("Starting HATs test...")
        
        # Setup PN532
        pn532 = setup_pn532()
        
        # Setup WM8950
        setup_wm8950()
        
        # Test NFC
        test_nfc(pn532)
        
        # Test Audio
        test_audio()
        
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        GPIO.cleanup()
