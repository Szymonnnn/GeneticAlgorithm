class HeadReader:
    def __init__(self) -> None:
        pass

    def read(tsp_file):
        name = tsp_file.readline()
        name = name.split(" ", 1)
        type = tsp_file.readline()
        type = type.split(" ", 1)
        comment = tsp_file.readline()
        comment = comment.split(" ", 1)
        dimension = tsp_file.readline()
        dimension = dimension.split(" ", 1)
        edge_weight_type = tsp_file.readline()
        edge_weight_type = edge_weight_type.split(" ", 1)
        section = tsp_file.readline()
        print("NAME: " + name[1], end="")

if __name__ == '__main__':
    print("It is not main file")