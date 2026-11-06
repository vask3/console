# Pico2-Handheld: My DIY Retro Console 🚀
Yo! I built an ultra-minimalist retro gaming handheld powered by the new **Raspberry Pi Pico 2** (RP2350). Designed from scratch in EasyEDA Pro in under 45 minutes! 
I stripped out all unnecessary junk to make soldering super fast. No buzzers or clocks—just raw performance, 6 tactile buttons, and a crisp 1.8" screen.

<img width="974" height="604" alt="Screenshot 2026-11-06 225834 (1)" src="https://github.com/user-attachments/assets/b19f379a-4e89-4d87-bdae-de83fb7a87e9" />

## 🛠️ Hardware Specs
* **Brain:** Raspberry Pi Pico 2 (RP2350)
* **Screen:** 1.8" ST7735 SPI TFT LCD
* **Controls:** 4-way D-Pad + A/B Action buttons (using internal pull-ups)
* **Power:** Directly via USB-C

## 🔌 Pinout Layout
* **Display:** `MOSI` -> GP19 | `SCK` -> GP18 | `CS` -> GP17 | `DC` -> GP16 | `RST` -> GP20
* **Buttons:** `UP` -> GP2 | `DOWN` -> GP3 | `LEFT` -> GP4 | `RIGHT` -> GP5 | `A` -> GP6 | `B` -> GP7

Next up: ordering PCBs from JLCPCB and coding some custom C++ games!
