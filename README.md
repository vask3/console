# DIY Retro Console

so basically I made my own mini retro gaming handheld from scratch using the new **Raspberry Pi Pico 2** (RP2350) because buying one is boring B)

<img width="974" height="604" alt="Screenshot 2026-11-06 225834 (1)" src="https://github.com/user-attachments/assets/b19f379a-4e89-4d87-bdae-de83fb7a87e9" />

## what's inside
- **Brain:** Raspberry Pi Pico 2 (RP2350)
- **Screen:** 1.8" ST7735 SPI TFT LCD (super tiny but works)
- **Buttons:** 4-way D-Pad + A and B buttons (used internal pull-ups so I didn't have to add extra resistors lol)
- **Power:** straight through USB-C

## pinout (so I don't forget where everything goes)
- **Display:** `MOSI` -> GP19 | `SCK` -> GP18 | `CS` -> GP17 | `DC` -> GP16 | `RST` -> GP20
- **Buttons:** `UP` -> GP2 | `DOWN` -> GP3 | `LEFT` -> GP4 | `RIGHT` -> GP5 | `A` -> GP6 | `B` -> GP7

## status
next step is ordering the actual PCBs from JLCPCB and trying to code some custom C++ games without breaking anything
