ascii_art = """
"""

# Računa broj linija (visina) i maksimalnu širinu (broj karaktera u najdužoj liniji)
lines = ascii_art.strip().split('\n')
height = len(lines)
width = max(len(line) for line in lines)

print("Visina:", height)

print("Širina:", width)
