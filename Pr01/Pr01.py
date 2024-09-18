class ArrayExample:
    def main(self):
        letters = ['f', 'r', 'e', 'd', ' ', 's', 'm', 'i', 't', 'h']
        name = "Hello, "
        a = [0] * 10

        for i in range(len(letters)):
            name += letters[i]
            print(f"{name}! Count to {i + 1}")

        self.send_message(name, len(letters))

    def send_message(self, name, msg):
        print(f"{name}! Count to {msg}")


example = ArrayExample()
example.main()

print("Hello")