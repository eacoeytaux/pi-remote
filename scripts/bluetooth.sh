systemctl status bluetooth | grep -q "Active: active (running)" && systemctl stop bluetooth || systemctl start bluetooth
systemctl status bluetooth
