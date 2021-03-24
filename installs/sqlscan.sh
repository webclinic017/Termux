#!/data/data/com.termux/files/usr/bin/sh

echo "SQL Scan Install"

apt install php curl
curl https://raw.githubusercontent.com/Cvar1984/sqlscan/dev/build/main.phar --output $PREFIX/bin/sqlscan
chmod +x $PREFIX/bin/sqlscan
sqlscan http://example.gov --scan
sqlscan list_url.txt --scan
