from pathlib import Path


def read_island_file(path: Path) -> list[list[bool]]:
    """
    Read file which consists of 0's, 1's and \n's.

    1 stands for the land, 0 for the water.
    All rows must have equal length.
    If the file does not fill the required form, an exception will be raised.

    :param path: path to file to read
    :return: island's representation with False standing for the water and True for the land.
    """
    file_content: list[list[bool]] = []

    with path.open("r") as f:
        for line in f:
            island_row = [c == '1' for c in line.rstrip()]
            file_content.append(island_row)

    return file_content


def read_island_file_at_position(path: Path, x: int, y: int) -> bool | None:
    """
    Read a single value from the island file.

    Unfortunately, this approach requires us to read the content of the file MULTIPLE times and will be very slow.
    An improvement over this approach would be to read batches of the files content, for example lines.

    :param path: path to file to read
    :param x: which position in row should be the value taken from.
    :param y: which row should be the value taken from.
    :return: True if land, False if water
    """
    with path.open("r") as f:
        first_line = f.readline()
        line_length = len(first_line)
        offset = line_length * y + x
        f.seek(offset)
        return f.read(1) == '1'


    # with path.open("r") as f:
    #     if y != 0:
    #         rows_to_skip = y
    #         for _ in range(rows_to_skip):
    #             next(f)
    #
    #     if x != 0:
    #         characters_to_skip = x
    #         f.read(characters_to_skip)
    #     character = f.read(1)
    #     return None if character == "" else character == '1'
