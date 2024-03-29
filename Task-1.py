import json


def read_file() -> dict:
    """
    This function reads the contents of the json file and returns them in a dictionary
    Args:
        None

    Returns:
        dictionary that contains the json file data
    """
    with open('quiz.json', 'r') as json_file:
        json_dictionary_data = json.load(json_file)
    return json_dictionary_data


def read_option(option: int) -> None:
    """
    This function reads the category option the user entered and calls for the get_questions function
    Args:
        option (int): the numerical option of the category the user entered
    Returns:
        None
    Raises:
        IndexError: if the input option is out of bound
    """
    try:
        category_of_option = categorise[option]
        get_questions(category_of_option)
    except IndexError:
        print("The option you Entered isn't valid please try again")


def get_questions(selected_category: str) -> None:
    """
    This function loads the questions for the chosen category by the user to the terminal and for each question it calls
     the guess_answer function ,then it calls print_total_score function
    Args:
        selected_category (str): the category the user selected to take its quiz
    Returns:
        None
    """
    total_score = 0
    option_dictionary = json_dictionary['quiz'][selected_category]
    for questionKey, questions in option_dictionary.items():
        print(f"{questionKey}")
        for key, value in questions.items():
            if key == 'question':
                print(f"{key}:")
                print(f"{value}:")
            elif key == 'options':
                options_list = value
                for option in range(0, len(value)):
                    print(f"{option + 1}) {value[option]}")
            else:
                question_score = guess_answer(value, options_list)
                total_score += question_score
    print_total_score(total_score, len(option_dictionary))


def guess_answer(answer: str, options_list: list) -> int:
    """
    This function prompts the user to enter the guessing option and checks whether their guessing is right or not
    Args:
        answer (str): the question's correct answer
        options_list (list): the answers options
    Returns:
         score (int): the score the user got in the question
    Raises:
        ValueError: if the user enters a non numerical option
        IndexError: if the user option is out of bound
    """
    score = 0
    try:
        guess = int(input("Please Enter your guessing:"))
        if guess <= 0:
            print("The option you Entered isn't valid please try again")
            return score

    except ValueError:
        print("The option you Entered isn't valid please try again")
        return score
    try:
        if answer == options_list[guess - 1]:
            score += 1
    except IndexError:
        print("The option you Entered isn't valid please try again")
    return score


def print_total_score(score: int, number_questions: int) -> None:
    """
    This function prints the total score of the quiz by dividing the questions score by their number
    Args:
        score (int): the number of questions the user answered right
        number_questions (int): the total number of questions

    Returns:
        None
    """
    print(f"your total score is {score} / {number_questions}")


if __name__ == '__main__':
    json_dictionary = read_file()
    categorise = list(json_dictionary['quiz'].keys())

    while True:
        index = 0
        print("This Quiz has questions for the categories: ")
        for i in range(0, len(categorise)):
            print(f"{str(i + 1)}- {categorise[i]}")
        category = int(input("Please enter your Option : \n"))
        read_option(category - 1)
