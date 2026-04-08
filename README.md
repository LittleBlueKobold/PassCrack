# PassCrack
# Offline Hash Cracker

A fast, modular Python utility designed for executing local dictionary attacks against cryptographic hashes. 

This tool was built to facilitate rapid offline hash auditing during Capture The Flag (CTF) events and localized penetration testing exercises. 

## Features
* **Dynamic Algorithm Support:** By leveraging `hashlib.new()`, the tool dynamically supports any hashing algorithm available on the host system (MD5, SHA-1, SHA-256, SHA-512, etc.) without requiring hardcoded logic changes.
* **Resilient File Parsing:** Designed to handle massive, non-standard text files (like `rockyou.txt`) by implementing UTF-8 encoding fallbacks, ensuring the script does not crash when encountering malformed bytes mid-execution.
* **Modular Design:** The `HashAuditor` class is decoupled from the CLI argument parser, allowing it to be easily imported as a module into larger automated testing frameworks.

## Usage

Run the script from the terminal, providing the target hash and the path to your wordlist. The default algorithm is MD5, but can be overridden with the `-a` flag.

**Basic MD5 Attack:**
```bash
python PassCrack.py -t 5f4dcc3b5aa765d61d8327deb882cf99 -w rockyou.txt

Targeting a SHA-256 Hash:
python PassCrack.py -t 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 -w custom_wordlist.txt -a sha256

Available Arguments

    -t, --target: (Required) The string representation of the target hash.

    -w, --wordlist: (Required) File path to the dictionary wordlist.

    -a, --algo: (Optional) The hashing algorithm to use. (Default: md5).