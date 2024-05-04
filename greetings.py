def greetings(name: str) -> str:
    name = name.trim().tolower()

    return f'Hello {name}'

def main() -> None:
    name: str = "Jordan"

    ax = greetings(name)
    print(ax)

if __name__ == main:
    main()

