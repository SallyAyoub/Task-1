import json


def print_total_score(score, number_questions):
    print("Your Total Score is :" + " " + str(score) + "/" + str(number_questions) + "\n")


def read_option(option):
    total_score = 0
    if option == 'x':
        print(" Exiting the quiz \n")
        exit()
    else:
        option = int(option)
        category_of_option = list_of_categories[option - 1]
        option_dictionary = json_dictionary['quiz'].get(category_of_option, -1)
        if option_dictionary == -1:
            print(" This Option doesn't exist \n")
            exit()
        else:
            option_tuple = (option_dictionary.items())
            option_list = list(option_tuple)
            number_questions = 0
            for question in option_list:
                print(question[0])
                number_questions += 1
                print("The Question is :")
                print(question[1].get('question'))
                print("The Options are :")
                options = (question[1].get('options'))
                for j in range(0, len(options)):
                    print(options[j])
                print("                                                         ")
                guess = str(input("Please Enter your guessing: \n "))
                if guess.capitalize() == question[1].get('answer').capitalize():
                    total_score += 1
            print_total_score(total_score, number_questions)


with open('quiz.json', 'r') as json_file:
    json_dictionary = json.load(json_file)

categorise = list(json_dictionary['quiz'].keys())
index = 0
print(" This Quiz has questions for the categories: \n")
list_of_categories = []

for i in categorise:
    list_of_categories.insert(index, i)
    index += 1
    print(str(index) + "-" + " " + i + "\n")

while True:
    category = str(input("Please enter your Option:  \n"))
    read_option(category)
