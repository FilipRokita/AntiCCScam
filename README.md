# AntiCCScam

AntiCCScam is a Python script designed to combat credit card fraud by flooding scam websites with fake data. This project automates the process of sending random, yet plausible, credit card information to a specified URL in order to overload and potentially disrupt the malicious operations of these sites.

## Files

1. `AntiCCScam.py`  
    This is the main script that sends fake credit card information to the specified URL.
2. `myconfig.py`  
    This configuration file contains the URL of the target site and the headers and data structure for the requests. It imports functions from randomdata.py to generate fake credit card details.
3. `randomdata.py`  
    This script generates random credit card numbers, expiration dates, and CVV codes.

## How to Use

1. Change `myconfig.py` to match request you want to send
2. Run `AntiCCScam.py`

1. Install dependencies: Make sure you have requests installed. You can install it using pip if you haven't already:
2. Configure: Update the url and data fields in myconfig.py with the target URL and the appropriate data structure that the scam site expects.
3. Run the script: Execute the AntiCCScam.py script.

## Disclaimer

This script is intended for educational purposes only. Use it responsibly and only against sites you have permission to test. Unauthorized use against any website without permission is illegal and unethical. The author does not take any responsibility for misuse of this script.

## Author

Filip Rokita  
Website: [www.filiprokita.com](http://www.filiprokita.com)

## Legal

This program is provided as-is, without warranties or conditions of any kind, either express or implied. By using this program, you agree that the author is not responsible for any damage that may occur as a result of its use.

## License

See the [LICENSE](./LICENSE) file for licensing information.