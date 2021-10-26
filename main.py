from Tests.tests_crud import test_crud
from UserInterface.console import run_ui


def main():
    rezervari = []
    run_ui(rezervari)


if __name__ == '__main__':
    test_crud()
    main()
