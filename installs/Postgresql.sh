#!/data/data/com.termux/files/usr/bin/sh

# Postgresql Install

echo "Postgresql Install"

echo "Create skeleton database"

mkdir -p PREFIX/var/lib/postgresql

initdb PREFIX/var/lib/postgresql

echo "Starting the database"

pg_ctl -D PREFIX/var/lib/postgresql start

echo "Similarly stop the database using"

pg_ctl -D PREFIX/var/lib/postgresql stop

echo "Create User"

createuser --superuser --pwprompt NateWeiler

echo "Create your database:"

createdb mydb

echo "Open your database"

psql mydb

echo "You will now see the promt"

mydb=#
