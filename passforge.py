#!/usr/bin/env python3
"""PassForge - A secure password generator with customizable options."""

import argparse
import secrets
import string
import sys


def generate_password(
    length: int = 16,
    uppercase: bool = True,
    lowercase: bool = True,
    digits: bool = True,
    symbols: bool = True,
    exclude_chars: str = "",
    count: int = 1,
) -> list[str]:
    """Generate cryptographically secure passwords."""
    pool = ""
    required = []

    if uppercase:
        pool += string.ascii_uppercase
        required.append(secrets.choice(string.ascii_uppercase))
    if lowercase:
        pool += string.ascii_lowercase
        required.append(secrets.choice(string.ascii_lowercase))
    if digits:
        pool += string.digits
        required.append(secrets.choice(string.digits))
    if symbols:
        pool += "!@#$%^&*()-_=+[]{}|;:,.<>?"
        required.append(secrets.choice("!@#$%^&*()-_=+[]{}|;:,.<>?"))

    if exclude_chars:
        pool = "".join(c for c in pool if c not in exclude_chars)

    if not pool:
        print("Error: No character types selected.", file=sys.stderr)
        sys.exit(1)

    if length < len(required):
        print(
            f"Error: Length too short. Minimum length is {len(required)}.",
            file=sys.stderr,
        )
        sys.exit(1)

    passwords = []
    for _ in range(count):
        remaining = length - len(required)
        password_chars = required + [secrets.choice(pool) for _ in range(remaining)]
        secrets.SystemRandom().shuffle(password_chars)
        passwords.append("".join(password_chars))

    return passwords


def generate_passphrase(
    word_count: int = 6,
    separator: str = "-",
    capitalize: bool = False,
    exclude_words: str = "",
) -> str:
    """Generate a secure passphrase using random words."""
    words = [
        "abandon", "ability", "able", "about", "above", "accept",
        "accident", "account", "achieve", "across", "act", "action",
        "activity", "actually", "add", "address", "administration",
        "admit", "adult", "affect", "after", "again", "against",
        "age", "agency", "agent", "agree", "ahead", "air",
        "all", "allow", "almost", "alone", "along", "alter",
        "among", "anger", "angle", "angry", "apart", "apple",
        "apply", "arena", "argue", "arise", "array", "aside",
        "asset", "attack", "attempt", "attend", "attention", "attorney",
        "audience", "author", "available", "avoid", "award", "aware",
        "away", "baby", "back", "bad", "bag", "balance",
        "ball", "band", "bank", "bar", "base", "beautiful",
        "decide", "deep", "defender", "degree", "describe",
        "deserve", "design", "desperate", "detail", "determine",
        "develop", "devote", "dictate", "dictate", "does",
        "damage", "damaged", "damn", "dare", "darling", "date",
        "daughter", "day", "dead", "deal", "dean", "dear",
        "debate", "decent", "describe", "expect", "express",
        "extra", "faint", "fail", "fall", "familiar", "family",
        "famous", "far", "fast", "father", "fear", "feed",
        "feel", "feet", "file", "film", "final", "finally",
        "financial", "find", "fine", "finger", "finish", "fire",
        "firm", "fish", "five", "floor", "fly", "focus",
        "force", "foreign", "forget", "form", "fortune", "four",
        "free", "from", "fresh", "friend", "frighten", "game",
        "garden", "gary", "gasp", "general", "generation", "get",
        "girl", "give", "glass", "go", "goal", "god",
        "good", "governor", "grace", "grain", "grand", "grant",
        "grass", "great", "green", "grey", "ground", "group",
        "grow", "guard", "guess", "guest", "guide", "gun",
        "habit", "hair", "half", "hall", "hand", "handle",
        "hang", "happy", "hard", "hate", "have", "he",
        "head", "health", "hear", "heart", "heat", "heavy",
        "hell", "help", "her", "here", "hero", "herself",
        "hide", "high", "him", "himself", "his", "historic",
        "historical", "hit", "hold", "home", "hope", "horrible",
        "horse", "hospital", "hot", "hotel", "hour", "house",
        "human", "hundred", "husband", "idea", "identify",
        "image", "imagine", "important", "improve", "in",
        "include", "including", "increase", "indeed", "individual",
        "industrial", "information", "inside", "instead", "institution",
        "influence", "inside", "insist", "instance", "instead", "institutional",
        "into", "investment", "involve", "issue", "it", "item",
        "jobs", "join", "john", "join", "joke", "journal",
        "joy", "judge", "jump", "jungle", "just", "keep",
        "key", "kid", "kill", "kind", "king", "kitchen",
        "knew", "knowledge", "labor", "lady", "land", "language",
        "large", "last", "late", "later", "laugh", "law",
        "lawyer", "lay", "lead", "leader", "learn", "lease",
        "least", "leave", "legal", "level", "life", "lift",
        "like", "likely", "limit", "little", "live", "local",
        "lock", "long", "look", "lose", "loss", "lot",
        "love", "low", "luck", "lying", "machine", "magazine",
        "mail", "main", "maintain", "major", "maker", "march",
        "marry", "marvel", "master", "matter", "maybe", "may",
        "meal", "mean", "measure", "media", "medicine", "meet",
        "meeting", "member", "memory", "mention", "message", "method",
        "middle", "might", "mile", "milk", "mind", "mine",
        "minister", "miss", "mission", "mistake", "mixed", "model",
        "modern", "moment", "money", "month", "moral", "more",
        "morning", "most", "mother", "mouth", "move", "movie",
        "much", "must", "name", "nation", "national", "natural",
        "nature", "near", "nearly", "necessary", "need", "negative",
        "neither", "never", "new", "news", "newspaper", "next",
        "nice", "night", "nine", "no", "non", "none",
        "nor", "north", "note", "nothing", "notice", "novel",
        "now", "number", "occur", "of", "off", "often",
        "oh", "oil", "okay", "old", "on", "once",
        "one", "only", "onto", "open", "operation", "opinion",
        "opportunity", "opposite", "option", "or", "order", "organize",
        "other", "others", "otherwise", "ought", "our", "out",
        "outer", "over", "owner", "pack", "page", "pain",
        "paint", "pair", "palace", "panel", "paper", "party",
        "peace", "people", "per", "perhaps", "period", "person",
        "personal", "phone", "physical", "pick", "picture", "piece",
        "place", "plan", "plane", "plant", "play", "player",
        "pleased", "please", "pleasure", "plug", "plenty", "poor",
        "popular", "population", "port", "portion", "portrait",
        "portray", "pose", "position", "positive", "possible",
        "power", "practice", "prepare", "present", "pretty", "prevent",
        "price", "private", "problem", "process", "produce",
        "product", "production", "professional", "professor", "program",
        "project", "promise", "promote", "proof", "proper", "property",
        "protect", "provide", "public", "pull", "purpose", "push",
        "put", "quality", "quite", "race", "radio", "raise",
        "range", "rapid", "rare", "rate", "rather", "reach",
        "read", "ready", "real", "reality", "realize", "really",
        "reason", "receive", "recent", "recently", "recognize",
        "record", "reduce", "refer", "regard", "region", "relate",
        "relationship", "religious", "remain", "remarkable", "remember",
        "remove", "report", "represent", "request", "require",
        "research", "resource", "respect", "respond", "rest", "result",
        "return", "reveal", "rich", "right", "rise", "risk",
        "river", "road", "rock", "role", "roman", "roof",
        "room", "rule", "run", "sad", "safe", "same",
        "save", "say", "scene", "school", "science", "scientist",
        "score", "sense", "separate", "series", "serious", "serve",
        "service", "seven", "several", "sexual", "sexual", "shake",
        "share", "she", "shoot", "show", "side", "sign",
        "significant", "similar", "simple", "simply", "since",
        "sing", "sister", "sit", "site", "situation", "six",
        "size", "skill", "skin", "small", "smile", "so",
        "social", "society", "soldier", "some", "something", "sometimes",
        "song", "soon", "sound", "source", "south", "space",
        "speak", "special", "specific", "speech", "spend", "sport",
        "spot", "spring", "staff", "stage", "stand", "standard",
        "star", "start", "state", "station", "stay", "steel",
        "step", "stick", "still", "stock", "stop", "store",
        "storm", "story", "straight", "strange", "street", "stress",
        "strong", "structure", "struggle", "student", "study", "stuff",
        "stupid", "style", "subject", "success", "successful", "such",
        "suddenly", "suffer", "suggest", "summer", "support", "sure",
        "surface", "surprise", "switch", "symbol", "system", "table",
        "take", "talk", "task", "teach", "technology", "television",
        "thank", "that", "the", "their", "them", "then",
        "theory", "there", "these", "they", "thing", "think",
        "third", "thirty", "this", "those", "though", "thought",
        "thousand", "threat", "threaten", "three", "through", "throughout",
        "throw", "thus", "time", "to", "today", "together",
        "tonight", "too", "tool", "top", "total", "tough",
        "toward", "town", "trade", "traditional", "traffic", "train",
        "training", "travel", "treat", "treatment", "tree", "trial",
        "try", "turn", "tv", "two", "type", "under",
        "understand", "unit", "until", "up", "upon", "us",
        "use", "usually", "value", "various", "very", "victim",
        "view", "voice", "wage", "wait", "walk", "wall",
        "want", "war", "watch", "water", "way", "we",
        "weapon", "wear", "weary", "week", "weekend", "weigh",
        "welcome", "well", "west", "western", "what", "whatever",
        "when", "where", "which", "while", "white", "who",
        "whole", "whose", "woman", "wonder", "wood", "word",
        "work", "worker", "world", "worry", "would", "wound",
        "wrap", "write", "writer", "wrong", "yard", "yeah",
        "year", "yes", "yet", "you", "young", "youth",
        "zero", "zombie"
    ]

    # Filter out excluded words
    if exclude_words:
        words = [w for w in words if w not in exclude_words.split()]

    selected_words = [secrets.choice(words) for _ in range(word_count)]

    if capitalize:
        selected_words = [w.capitalize() for w in selected_words]

    return separator.join(selected_words)


def main():
    parser = argparse.ArgumentParser(
        description="PassForge - Generate secure passwords and passphrases",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
examples:
  passforge                    # 16-char password with all char types
  passforge -l 32 -c 5         # Five 32-character passwords
  passforge --no-symbols -l 20 # 20-char, no symbols
  passforge --exclude "O0Il1"  # Exclude ambiguous characters
  passforge -p 6               # Generate 6-word passphrase
  passforge -p 8 -s _ -c 3    # Three 8-word passphrases with underscores
  passforge -p 4 -C            # Four capitalized words
  passforge -p 8 "common dribble fatal matrix grammar"  # Exclude words""",
    )
    parser.add_argument(
        "-l", "--length", type=int, default=16, help="Password length (default: 16)"
    )
    parser.add_argument(
        "-c", "--count", type=int, default=1, help="Number of passwords (default: 1)"
    )
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument(
        "--exclude", type=str, default="", help="Exclude specific characters"
    )
    parser.add_argument(
        "-p", "--passphrase", type=int, default=0, help="Generate passphrase with specified number of words (0 for standard passwords)"
    )
    parser.add_argument(
        "-s", "--separator", type=str, default="-", help="Separator for passphrase words (default: '-')"
    )
    parser.add_argument(
        "-C", "--capitalize", action="store_true", help="Capitalize passphrase words"
    )
    parser.add_argument(
        "--exclude-words", type=str, default="", help="Space-separated words to exclude from passphrase"
    )

    args = parser.parse_args()

    if args.passphrase > 0:
        passphrase = generate_passphrase(
            word_count=args.passphrase,
            separator=args.separator,
            capitalize=args.capitalize,
            exclude_words=args.exclude_words,
        )
        if args.count > 1:
            for i in range(args.count):
                print(passphrase)
        else:
            print(passphrase)
    else:
        passwords = generate_password(
            length=args.length,
            uppercase=not args.no_upper,
            lowercase=not args.no_lower,
            digits=not args.no_digits,
            symbols=not args.no_symbols,
            exclude_chars=args.exclude,
            count=args.count,
        )

        for i, pwd in enumerate(passwords, 1):
            if args.count > 1:
                print(f"{i}. {pwd}")
            else:
                print(pwd)


if __name__ == "__main__":
    main()
