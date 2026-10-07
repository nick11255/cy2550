# Part 6: Decoding

## Puzzle 1 (CyberChef)

**Plaintext:** I got a jar of dirt

**Operation chain:**
1. Vigenère — Decode — key: `dirt`
2. Substitute — Decode direction — Plaintext: `qwertyuiopasdfghjklzxcvbnm`, Ciphertext: `abcdefghijklmnopqrstuvwxyz`
3. Base64 — Decode (From Base64) — alphabet: `A-Za-z0-9+/=`
4. Binary — Decode (From Binary) — delimiter: Space, byte length: 8

## Puzzle 2 (dCode)

**Plaintext:** NOT ALL TREASURE IS SILVER AND GOLD MATE

**Operation chain:**
1. Monoalphabetic substitution — decode — key from the linked Crypto.jpeg table (CYBERISFUN ↔ 0123456789), letters to digits
2. Columnar transposition — decode — 5 columns, spaces preserved
3. Multi-tap phone code — decode
4. Atbash cipher — decode
