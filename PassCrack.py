"""
Offline Hash Auditing Tool
A command-line utility for executing dictionary attacks against common cryptographic hashes.
"""
import argparse
import hashlib
import logging
import sys
from pathlib import Path
from typing import Optional

# Configure clean logging for CLI output
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

class HashAuditor:
    def __init__(self, target_hash: str, wordlist_path: str, algorithm: str = 'md5'):
        self.target_hash = target_hash.lower()
        self.wordlist_path = Path(wordlist_path)
        self.algorithm = algorithm.lower()

        # Validate that the requested algorithm is supported by the local system
        if self.algorithm not in hashlib.algorithms_available:
            logger.error(f"[!] Unsupported algorithm: '{self.algorithm}'")
            logger.info(f"[*] Available algorithms: {', '.join(hashlib.algorithms_guaranteed)}")
            sys.exit(1)

    def execute(self) -> Optional[str]:
        """Executes the dictionary attack against the provided hash."""
        if not self.wordlist_path.exists():
            logger.error(f"[!] Wordlist not found at: {self.wordlist_path}")
            sys.exit(1)

        logger.info("[*] Initializing offline dictionary attack...")
        logger.info(f"[*] Target Hash: {self.target_hash}")
        logger.info(f"[*] Algorithm:   {self.algorithm.upper()}")
        logger.info(f"[*] Wordlist:    {self.wordlist_path.name}\n")

        try:
            # Using utf-8 with errors='ignore' prevents crashes on massive, messy wordlists (e.g., rockyou.txt)
            with self.wordlist_path.open('r', encoding='utf-8', errors='ignore') as file:
                for line_num, line in enumerate(file, 1):
                    word = line.strip()
                    
                    # Dynamically generate hash based on selected algorithm
                    h = hashlib.new(self.algorithm)
                    h.update(word.encode('utf-8'))
                    hashed_word = h.hexdigest()

                    if hashed_word == self.target_hash:
                        logger.info(f"[+] SUCCESS! Match found on line {line_num:,}")
                        logger.info(f"[+] Plaintext Password: {word}")
                        return word
                        
            logger.warning("[-] Exhausted wordlist. No match found.")
            return None
            
        except KeyboardInterrupt:
            logger.warning("\n[!] Execution aborted by user.")
            sys.exit(0)
        except Exception as e:
            logger.error(f"[!] An unexpected error occurred: {e}")
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Offline Hash Auditing Utility")
    parser.add_argument("-t", "--target", required=True, help="The target hash to crack")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the dictionary wordlist")
    parser.add_argument("-a", "--algo", default="md5", help="Hashing algorithm (e.g., md5, sha256, sha512. Default: md5)")
    
    args = parser.parse_args()
    
    auditor = HashAuditor(args.target, args.wordlist, args.algo)
    auditor.execute()

if __name__ == "__main__":
    main()