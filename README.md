# SSH Hostname Collector

A simple Python script to connect to an SSH server and retrieve the hostname. This script uses the `paramiko` library to establish an SSH connection and execute commands on the remote server.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.x
- `paramiko` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/thelovernize/ssh-hostname-collector.git
    cd ssh-hostname-collector
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    On macOS/Linux:
    ```sh
    source venv/bin/activate
    ```

    On Windows:
    ```sh
    .\venv\Scripts\activate
    ```

4. Install the required packages:
    ```sh
    pip install paramiko
    ```

## Usage

1. Run the script:
    ```sh
    python ssh_hostname_collector.py
    ```

2. Enter the SSH server details when prompted:
    - SSH server hostname
    - SSH username
    - SSH password

The script will connect to the SSH server, retrieve the hostname, and display it.

## Project Structure

ssh-hostname-collector/
│
├── ssh_hostname_collector.py # Main script
├── .gitignore # Git ignore file
├── venv/ # Virtual environment directory
└── README.md # Project README file




## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
