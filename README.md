# PassForge

A secure password generator and passphrase creator using Python's `secrets` module for cryptographic randomness.

## Features

- **Password Generation**
  - Cryptographically secure generation (`secrets` module)
  - Customizable character types (upper, lower, digits, symbols)
  - Exclude ambiguous characters (`O`, `0`, `l`, `1`, `I`)
  - Batch generation support

- **Passphrase Generation**
  - Generate secure passphrases from a dictionary of common words (4000+ words)
  - Customizable word count (default: 6 words)
  - Choose custom separators (default: `-`)
  - Capitalize words in passphrase
  - Exclude specific words from passphrase generation

- **CLI Arguments**
  - Easy-to-use command-line interface with comprehensive options
  - Help documentation for all options

## Usage

### Password Examples

```bash
# Basic 16-character password
python passforge.py

# Generate five 32-character passwords
python passforge.py -l 32 -c 5

# 20-char, no symbols
python passforge.py --no-symbols -l 20

# Exclude ambiguous characters
python passforge.py --exclude "O0Il1"
```

### Passphrase Examples

```bash
# Generate 6-word passphrase (default)
python passforge.py -p 6

# Three 8-word passphrases with underscores
python passforge.py -p 8 -s _ -c 3

# Four capitalized words
python passforge.py -p 4 -C

# Exclude specific words
python passforge.py -p 5 --exclude-words "password login secret"
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
| `-p, --passphrase` | Generate passphrase with N words | 0 (off) |
| `-s, --separator` | Separator for passphrase words | `-` |
| `-C, --capitalize` | Capitalize passphrase words | off |
| `--exclude-words` | Space-separated words to exclude | none |

## Security

Uses `secrets` module which is suitable for managing secrets such as passwords, account authentication, security tokens, and related secrets.

## License

MIT


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
