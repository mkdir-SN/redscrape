import scrape
import sys

def main():
    n = len(sys.argv) - 1

    if (n < 1):
        print("No meaningful args passed")
        return

    scrape.get()

if __name__ == "__main__":
    main()
