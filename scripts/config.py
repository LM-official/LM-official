# =============================================================================
# CREDENTIALS
# =============================================================================
USERNAME = "LM-official"


# =============================================================================
# SKIPS
# =============================================================================
# Matched case-insensitively (write here in lowercase)

# Repos that should never appear in the table, on top of the profile repo, always skipped
SKIP_REPO = set()

# Languages that should never appear in a stack, however much of a repo they fill
# Braces, not set("scss"): that one reads the string as an iterable and skips the letters "s" and "c"
SKIP_LANG = {"scss"}


# =============================================================================
# TABLE
# =============================================================================
MAX_DESCRIPTION = 220   # Max length of the description
MAX_STACK       = 6     # Max number of languages per project
MIN_SHARE       = 0.05  # Ignore languages below this % of the repository


# =============================================================================
# BADGES
# =============================================================================
SATURATION = (0.85, 1.00)  # Near-full, so every hue reads as a colour and not a grey
LIGHTNESS  = (0.34, 0.50)  # Kept wide so same-hue languages still differ in depth

# Mixed into the hash before the colour is derived, so it re-rolls every badge at once while staying identical from run to run
# A hash spreads names uniformly, so a few languages can always land on neighbouring hues by chance and read as the same colour
# Bump this to any other number to draw the whole palette again
COLOR_SALT = 148

# The ceiling badge colours are darkened to contrast against white text
# Is (1 + 0.05) / (L + 0.05), so 0.25 is 3.5:1, enough for the bold, shadowed uppercase shields renders
MAX_LUMINANCE = 0.25