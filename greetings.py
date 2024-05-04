def greetings(name: str) -> str:
    name = name.strip().title()

    return f'Hello {name}'

def main() -> None:
    name: str = "Jordan"

    ax = greetings(name)
    print(ax)

if __name__ == "__main__":
    main()

