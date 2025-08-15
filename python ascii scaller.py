def downscale_ascii_to_fit(ascii_art_lines, max_width_chars, max_height_lines):
    """
    Smanji ASCII umetnost da stane u max_width_chars x max_height_lines dimenzije.
    """
    original_height = len(ascii_art_lines)
    original_width = max(len(line) for line in ascii_art_lines)

    # Izračunaj skaliranje po x i y osama
    scale_x = max(1, original_width // max_width_chars)
    scale_y = max(1, original_height // max_height_lines)

    # Uzmi svaki scale_y red
    downscaled_lines = ascii_art_lines[::scale_y]

    # Za svaki red uzmi svaki scale_x karakter
    downscaled_lines = [''.join(line[i] for i in range(0, len(line), scale_x)) for line in downscaled_lines]

    return downscaled_lines


def main():
    # Učitaj ascii art iz fajla (ili možeš da zameniš sa stringom)
    input_file = 'ascii_art.txt'
    output_file = 'ascii_art_downscaled.txt'

    with open(input_file, 'r', encoding='utf-8') as f:
        ascii_art_lines = f.readlines()

    # Maksi dimenzije izračunate prema CSS-u i fontu
    max_width_chars = 22
    max_height_lines = 29

    downscaled = downscale_ascii_to_fit(ascii_art_lines, max_width_chars, max_height_lines)

    # Sačuvaj u fajl
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in downscaled:
            f.write(line.rstrip('\n') + '\n')

    print(f'Smanjena ASCII umetnost je sačuvana u: {output_file}')


if __name__ == '__main__':
    main()