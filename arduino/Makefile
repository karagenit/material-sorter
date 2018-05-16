main:
	rm -rf ./build/*
	arduino --verify --preserve-temp-files --pref build.path="./build" sorter/sorter.ino
	sudo avrdude -p atmega328p -C +avrdude.conf -c pi_gpio -v -U flash:w:build/sorter.ino.with_bootloader.hex:i
