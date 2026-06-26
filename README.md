# PassForge

A secure password generator using Python's `secrets` module for cryptographic randomness.

## Features

- Cryptographically secure generation (`secrets` module)
- Customizable character types (upper, lower, digits, symbols)
- Exclude ambiguous characters (`O`, `0`, `l`, `1`, `I`)
- Batch generation support
- Minimal dependencies (stdlib only)

## Usage

```bash
# Basic 16-character password
python passforge.py

# Generate five 32-character passwords
python passforge.py -l 32 -c 5

# No symbols, 20 characters
python passforge.py --no-symbols -l 20

# Exclude ambiguous characters
python passforge.py --exclude "O0Il1"
```

## Options

| Flag | Description | Default |
|------|-------------|---------|
| `-l, --length` | Password length | 16 |
| `-c, --count` | Number of passwords | 1 |
| `--no-upper` | Exclude uppercase | off |
| `--no-lower` | Exclude lowercase | off |
| `--no-digits` | Exclude digits | off |
| `--no-symbols` | Exclude symbols | off |
| `--exclude` | Exclude specific chars | none |

## Security

Uses `secrets` module which is suitable for managing secrets such as passwords, account authentication, security tokens, and related secrets.

## License

MIT
