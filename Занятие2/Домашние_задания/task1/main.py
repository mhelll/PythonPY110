def count(start_number):
    while True:
        yield start_number
        start_number *= 2


if __name__ == "__main__":
    my_count = count(1)
    for _ in range(20):
        print(next(my_count))
