import requests
import re
import urllib.parse
import sys
from bs4 import BeautifulSoup

# Create a session object to reuse TCP connections
session = requests.Session()

def check_security_headers(url):
    """Check for important security HTTP headers."""
    try:
        response = session.get(url, timeout=10)
        headers = response.headers
        security_headers = {
            'X-Frame-Options': headers.get('X-Frame-Options', 'Not Set'),
            'X-XSS-Protection': headers.get('X-XSS-Protection', 'Not Set'),
            'Content-Security-Policy': headers.get('Content-Security-Policy', 'Not Set'),
            'Strict-Transport-Security': headers.get('Strict-Transport-Security', 'Not Set')
        }
        return security_headers
    except requests.RequestException as e:
        return f"Error checking security headers: {str(e)}"

def check_access(url, item_name):
    """Generalize access checking for directories and files."""
    try:
        response = session.get(url, timeout=5)
        if response.status_code == 200:
            return f"{item_name}: Accessible (possibly unsecured)"
        elif response.status_code == 403:
            return f"{item_name}: Properly secured (access forbidden)"
        elif response.status_code == 404:
            return f"{item_name}: Not Found (likely secured)"
        else:
            return f"{item_name}: Error: {response.status_code}"
    except requests.RequestException as e:
        return f"{item_name}: Network error during access check: {str(e)}"

def check_directory_access(wp_url):
    """Check access to common WordPress directories."""
    directories = ['wp-admin', 'wp-content', 'wp-includes']
    results = []
    for directory in directories:
        dir_url = urllib.parse.urljoin(wp_url, directory)
        results.append(check_access(dir_url, directory))
    return results

def check_file_access(wp_url):
    """Check access to common WordPress files including robots.txt."""
    files = ['readme.html', 'license.txt', 'wp-config-sample.php', 'robots.txt']
    results = []
    for file in files:
        file_url = urllib.parse.urljoin(wp_url, file)
        results.append(check_access(file_url, file))
    return results

def get_wordpress_info(wp_url):
    """Perform comprehensive checks on a WordPress website."""
    try:
        response = session.get(wp_url, timeout=10)
        if response.status_code == 200:
            print(f"Successfully connected to {wp_url}")
            headers = check_security_headers(wp_url)
            for header, status in headers.items():
                print(f"Security Header - {header}: {status}")

            print("\nDirectory Access:")
            directory_results = check_directory_access(wp_url)
            for result in directory_results:
                print(result)

            print("\nFile Access:")
            file_results = check_file_access(wp_url)
            for result in file_results:
                print(result)
        else:
            print(f"Failed to retrieve data from the website, status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Network error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wpscan.py <WordPress_URL>")
        sys.exit(1)
    wordpress_url = sys.argv[1]
    get_wordpress_info(wordpress_url)
