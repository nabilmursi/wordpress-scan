# WordPress Security Scanner

## Description
This Python script performs a security scan on a WordPress website to check for common vulnerabilities and misconfigurations. It checks security headers, file and directory access permissions, and identifies potentially insecure files and directories.

## Features
- **Security Headers**: Checks for crucial HTTP security headers like X-Frame-Options, X-XSS-Protection, Content-Security-Policy, and Strict-Transport-Security.
- **Directory Access**: Verifies access permissions for critical WordPress directories (`wp-admin`, `wp-content`, `wp-includes`).
- **File Access**: Tests accessibility of important files (`readme.html`, `license.txt`, `wp-config-sample.php`, `robots.txt`) that should typically be protected.
- **Output**: Provides a clear and readable report directly in the command line, indicating potential security risks.

## Installation

### Prerequisites
- Python 3.x installed on your system.
- Access to the command line or terminal.
- `requests` and `beautifulsoup4` libraries, which can be installed via pip.

### Setup
1. Clone the repository or download the script to your local machine:
   ```bash
   git clone https://github.com/nabilmursi/wordpress-scan.git
   cd wordpress-security-scanner

2. Install required Python libraries:
   
$ pip install requests beautifulsoup4

Usage
To use the script, navigate to the directory containing the script and run:

$ python wpscan.py <WordPress_URL>

Replace <WordPress_URL> with the URL of the WordPress site you want to scan. For example:

$python wpscan.py https://example.com

Output
The script will output the scan results directly in the console. Here is what you might expect:

Security headers status
Directory access results
File access results
Each category will indicate whether the item is secure, accessible, or has issues that need to be addressed.

Contributing
Feel free to fork the repository and submit pull requests. You can also open issues to discuss potential improvements or report bugs.

Contact
If you have any questions, you can contact me at info@isky.ae

License
This project is licensed under the MIT License - see the LICENSE.md file for details.


### Notes for the README:
- **Repository URL and Contact Email**: Update these placeholders with your actual GitHub repository URL and your contact email.
- **License Information**: If you have a different preferred license or specific licensing details, adjust the licensing section accordingly.

This README should provide all the necessary information for someone who wants to use your script, contributing to the project, or reaching out for more information.






