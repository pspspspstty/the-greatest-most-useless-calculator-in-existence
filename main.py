import menu

def main():
    try:
        print("Welcome!")
        m = menu.Menu()

        # Get the operation and inputs from the user
        operation = m.get_operation()
        op = m.select_operation(int(operation))

        # calls abstract method to output the respective answers
        op.calculate()
    except KeyboardInterrupt:
        print("\033[0m\nExiting...")

if __name__ == "__main__":
    main()
