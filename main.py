from Tests.testAll import runAllTests
from UserInterface.command_line_console import command_line_console
from UserInterface.console import runmenu


def main():
    runAllTests()
    lista = []
    while True:
        ui = input("Introduceti ui pentru console si cil pentru command in line: ")
        if ui == "ui":
            runmenu(lista)
            break
        elif ui == "cil":
            command_line_console(lista)
            break
        else:
            print('Optiune inexistenta')


if __name__ == "__main__":
    main()

