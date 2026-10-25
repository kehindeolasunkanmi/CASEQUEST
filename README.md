# CASEQUEST — Confidential Information Protection System

CASEQUEST is a Python desktop application developed to demonstrate classical cryptographic techniques through a graphical user interface.

## Features

- Graphical interface built with CustomTkinter.
- Encryption and decryption using four classical ciphers:
  - Caesar Cipher
  - Additive Cipher
  - Vigenere Cipher
  - Affine Cipher
- Input validation and key-based cipher operations.
- Local protection-history recording and operation monitoring.

## Technology Stack

- Python
- CustomTkinter
- Tkinter
- JSON

## Getting Started

### Requirements

- Python 3.10 or later recommended
- pip

### Installation

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Install the required dependency:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python gui.py
   ```

The application creates a local `history.json` file when needed to store operation history.

## Security Note

CASEQUEST is an educational project demonstrating classical ciphers. These algorithms are not suitable for protecting real confidential information against modern attacks. Do not use this application as a replacement for modern, vetted encryption.

## Project Purpose

This project demonstrates Python GUI development, classical cryptography, input validation, and local JSON-based history management.
