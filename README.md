# Service Configuration

```bash
sudo nano /etc/systemd/system/ethereum.service
```

```ini
[Unit]
Description=Ethereum Service
After=network.target

[Service]
ExecStart=/home/beeoz/projects/ethscription-scanner/venv/bin/python3 -m scanner
WorkingDirectory=/home/beeoz/projects/ethscription-scanner/
Environment=ETHEREUM_API=https://mainnet.infura.io/v3/API_KEY
Environment=PROJECT_DIRECTORY=/home/beeoz/projects/ethscription-scanner

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl start ethereum
sudo systemctl enable ethereum
sudo systemctl status ethereum
```

