import random

def get_names():
    names = []
    print("Enter the names (type 'done' when finished):")
    while True:
        name = input("Enter name: ").strip()
        if name.lower() == 'done':
            break
        elif name:  # This ensures that empty inputs are not added to the list
            names.append(name)
    return names

def pick_random_name(names):
    if not names:
        print("No names were entered.")
        return None
    return random.choice(names)

def main():
    names = get_names()
    if names:
        random_name = pick_random_name(names)
        print(f"The randomly picked name is: {random_name}")

if __name__ == "__main__":
    main()
