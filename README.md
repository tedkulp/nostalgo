Copy random roms

`for file in $(ssh root@192.168.100.2  "ls -a /mnt/Backup/roms/MAME/Roms/" | shuf | head -25); do scp root@192.168.100.2:/mnt/Backup/roms/MAME/Roms/$file .; done`
