#!/usr/bin/env python3
import os
import re
import gzip
import glob
import argparse
from typing import List, Dict, Optional, Any

# TODO 
# Log reader to review failed logins 


# Define a constant for the default log directory
DEFAULT_LOG_DIR = '/var/log/'

def check_permissions(log_dir: str) -> None:
    """
    Checks if the script has the necessary permissions to read log files.
    Exits if permissions are insufficient.
    """
    if os.geteuid() != 0:
        print("Warning: This script may not be able to read all log files without root privileges.")
        print("Please run with 'sudo'.")
    
    if not os.path.isdir(log_dir):
        print(f"Error: Log directory '{log_dir}' not found.")
        exit(1)

def find_auth_log_files(log_dir: str) -> List[str]:
    """
    Finds auth.log and its rotated versions (including gzipped files).

    Args:
        log_dir: The directory where log files are stored.

    Returns:
        A list of file paths for the auth logs.
    """
    auth_log_pattern = os.path.join(log_dir, 'auth.log*')
    return sorted(glob.glob(auth_log_pattern))

def parse_log_line(line: str) -> Optional[Dict[str, Any]]:
    """
    Parses a single log line to find failed login attempts.

    Args:
        line: A single line from a log file.

    Returns:
        A dictionary with extracted information if it's a failed login, otherwise None.
    """
    # Regex patterns for different types of failed logins
    # (service, regex_pattern)
    patterns = [
        ('sshd', re.compile(r"Failed password for (invalid user )?(?P<user>\S+) from (?P<ip>\S+) port \d+ ssh2")),
        ('sudo', re.compile(r"pam_unix\(sudo:auth\): authentication failure;.*user=(?P<user>\S+)")),
        ('login', re.compile(r"FAILED LOGIN \(\d+\) on '.*' FOR '(?P<user>\S+)', Authentication failure"))
    ]

    for service, pattern in patterns:
        match = pattern.search(line)
        if match:
            # Extract common information
            timestamp = ' '.join(line.split()[:3])
            data = match.groupdict()
            
            return {
                "timestamp": timestamp,
                "service": service,
                "user": data.get("user", "N/A"),
                "ip_address": data.get("ip", "N/A (local)"),
                "raw_log": line.strip()
            }
    return None

def process_log_file(filepath: str) -> List[Dict[str, Any]]:
    """
    Opens and processes a single log file (handles .gz).

    Args:
        filepath: The path to the log file.

    Returns:
        A list of dictionaries, where each dictionary represents a failed login.
    """
    failed_attempts = []
    try:
        # Handle gzipped files and regular text files
        open_func = gzip.open if filepath.endswith('.gz') else open
        mode = 'rt' if filepath.endswith('.gz') else 'r'
        
        print(f"--> Processing {os.path.basename(filepath)}...")
        
        with open_func(filepath, mode, errors='ignore') as f:
            for line in f:
                parsed_data = parse_log_line(line)
                if parsed_data:
                    failed_attempts.append(parsed_data)
    except (PermissionError, IOError) as e:
        print(f"    Could not read {filepath}: {e}")
        
    return failed_attempts

def print_results(failed_logins: List[Dict[str, Any]]) -> None:
    """
    Prints the found failed login attempts in a formatted table.
    """
    if not failed_logins:
        print("\nNo failed login attempts found in the scanned logs.")
        return

    print(f"\nFound {len(failed_logins)} failed login attempts:\n")
    # Print table header
    header = f"{'Timestamp':<20} {'Service':<8} {'Username':<20} {'Source IP':<18}"
    print(header)
    print('-' * len(header))

    # Print each failed login attempt
    for login in failed_logins:
        print(f"{login['timestamp']:<20} {login['service']:<8} {login['user']:<20} {login['ip_address']:<18}")

def main():
    """
    Main function to orchestrate the log parsing process.
    """
    parser = argparse.ArgumentParser(
        description="Scan Ubuntu auth logs for failed login attempts.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--log-dir',
        default=DEFAULT_LOG_DIR,
        help=f"The directory where log files are stored.\n(default: {DEFAULT_LOG_DIR})"
    )
    args = parser.parse_args()

    check_permissions(args.log_dir)

    log_files = find_auth_log_files(args.log_dir)
    if not log_files:
        print(f"No 'auth.log' files found in {args.log_dir}")
        return

    all_failed_logins = []
    for log_file in log_files:
        all_failed_logins.extend(process_log_file(log_file))

    print_results(all_failed_logins)


if __name__ == "__main__":
    main()