

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

_Add dashboard screenshot here._

### IOC Management

_Add IOC page screenshot here._

### Firewall Synchronization

_Add firewall page screenshot here._

## Future Improvements

- IOC export/import support
- Scheduled synchronization
- IOC whitelist support
- Multiple firewall profile management
- IOC statistics and reporting

## License

This project is intended for educational and research purposes.