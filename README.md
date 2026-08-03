

# IOC Firewall Manager

A Windows desktop application for managing Indicators of Compromise (IOCs) and automatically synchronizing Windows Firewall rules using threat intelligence feeds published by the Turkish National Cyber Incident Response Center (USOM).

## Features

- Synchronize IOC feeds from the USOM Threat Intelligence API
- Support for IPv4, IPv6 and Domain indicators
- Store IOC data in Microsoft SQL Server
- Manual IOC management (add, edit, delete)
- Automatic Windows Firewall (for IPs) and hosts file (for Domains) synchronization
- IOC search and filtering
- Dashboard with IOC statistics
- Multi-page desktop interface built with PySide6

## Technologies

- Python 3.13
- PySide6
- Microsoft SQL Server
- pyodbc
- Requests
- Windows Defender Firewall

## Project Structure

```
api/            API communication
core/           Configuration
database/       SQL Server operations
firewall/       Windows Firewall management
logs/           Logging
models/         Data models
services/       Business logic
ui/             PySide6 user interface
workers/        Background tasks
```

## Installation

Clone the repository

```bash
git clone https://github.com/ardaysuf/ioc_firewall_manager.git
cd ioc_firewall_manager
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure

- Microsoft SQL Server
- Database connection
- API settings

Run

```bash
python main.py
```

## Screenshots

### Dashboard

<img width="1917" height="650" alt="image" src="https://github.com/user-attachments/assets/bce3fe35-2916-4574-bd7e-dd7e8110c9df" />

### IOC Management

<img width="1916" height="1096" alt="image" src="https://github.com/user-attachments/assets/b57596bd-a81b-4c6f-9a91-80885cf2a31d" />

### Firewall Synchronization

<img width="1917" height="422" alt="image" src="https://github.com/user-attachments/assets/cf7aad54-7072-468f-b7e3-af8f6954cbee" />

## Future Improvements

- IOC export/import support
- Scheduled synchronization
- IOC whitelist support
- Multiple firewall profile management
- IOC statistics and reporting

## License

This project is intended for educational and research purposes.
