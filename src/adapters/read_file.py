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
    island: list[list[bool]] = []

    # with path.open("r") as f:
    #     for line in f:
    #         print(line)
    #         island_row =

    return island


def read_island_file_at_position(path: Path, x: int, y: int) -> bool:
    """
    Read a single value from the island file.

    :param path: path to file to read
    :param x: Which position in row should be the value taken from.
    :param y: Which row should be the value taken from.
    :return: True if island, False if water
    """
    # TODO: implement

    return False
