def print_even_odd():
    for num in range(10, 20):
        parity = "even" if num % 2 == 0 else "odd"
        print(f"{num} {parity}", end=' ')

def main():
    print_even_odd()

if __name__ == '__main__':
    main()
