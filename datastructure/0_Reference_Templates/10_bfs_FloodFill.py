def flood_fill(r: int, c:int, replacement:int,
               image: list[list[int]]
               )-> list[list[int]]:
    num_rows, num_cols = len(image), len(image[0])

    def get_neighbors(coord, color):
        row, col = coord
