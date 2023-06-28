# Service Configuration

```bash
sudo nano /etc/systemd/system/ethereum.service
```

```ini
[Unit]
Description=Ethereum Service
After=network.target

[Service]
ExecStart=/home/beeoz/projects/ethscription-scanner/venv/bin/python3 -m scanner -c /home/beeoz/projects/ethscription-scanner/scanner.conf
WorkingDirectory=/home/beeoz/projects/ethscription-scanner/
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=ethereum

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl start ethereum
sudo systemctl enable ethereum
sudo systemctl status ethereum
```
