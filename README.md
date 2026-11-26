# DIY Retro Console

This is my own mini retro gaming handheld from scratch using the new **Raspberry Pi Pico 2** 

<img width="974" height="604" alt="Screenshot 2026-11-06 225834 (1)" src="https://github.com/user-attachments/assets/b19f379a-4e89-4d87-bdae-de83fb7a87e9" />

## what's inside
- **Brain:** Raspberry Pi Pico 2
- **Screen:** 1.8" ST7735 SPI TFT LCD
- **Buttons:** 4-way D-Pad + A and B buttons
- **Power:** USB-C

<img width="769" height="428" alt="image" src="https://github.com/user-attachments/assets/15bf45f0-5cbd-4cfe-a1d9-f500ce4753c0" />
<img width="647" height="320" alt="image" src="https://github.com/user-attachments/assets/0e54b47c-0b63-462d-8e78-3fab589c8ac9" />


## pinout (so I don't forget where everything goes)
- **Display:** `MOSI` -> GP19 | `SCK` -> GP18 | `CS` -> GP17 | `DC` -> GP16 | `RST` -> GP20
- **Buttons:** `UP` -> GP2 | `DOWN` -> GP3 | `LEFT` -> GP4 | `RIGHT` -> GP5 | `A` -> GP6 | `B` -> GP7

## status
next step is ordering the actual PCBs from JLCPCB and trying to code some custom C++ games without breaking anything
