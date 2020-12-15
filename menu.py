class Menu():
    def __init__(self, prompt_text, choice_list):
        self.prompt_text = prompt_text
        self.choice_list = choice_list

    def get_choice(self):
        return self.get_user_choice(self.choice_list)

    def choices_to_string(self):
        choice_string = ""
        num = 1
        for choice in choice_list:
            choice_string += "%d: %s\n" % (num, choice)
            num += 1
        choice_string += self.prompt_text
        return choice_string

    def print_menu_error(self):
        print("That was not a valid choice. Try again.\n\n\n")

    def get_user_choice(self):
        choice = -1
        choice_string = self.choices_to_string(self.choice_list)
        while choice == -1:
            try:
                choice = int(input(choice_string))
                if choice <= 0 or choice > len(self.choice_list):
                    raise ValueError
            except ValueError:
                self.print_menu_error()
        return choice
