# Emulator Frontend for HTPC

The makings of an emulator frontend designed for an HTPC and a controller. Definitely a work in progress.

## Setup

1. Install SDL2, SDL2_ttf, SDL2_image
1. pyvenv env
1. source env/bin/activate
1. pip install -r requirements.txt
1. python main.py

## Notes

### Copy random roms

`for file in $(ssh root@192.168.100.2  "ls -a /mnt/Backup/roms/MAME/Roms/" | shuf | head -25); do scp root@192.168.100.2:/mnt/Backup/roms/MAME/Roms/$file .; done`
