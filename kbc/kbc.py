from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if answer == question["answer"] else False   

def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''

    import random
    count = 0
    while count <= 2:
        temp = random.randint(1,4)
        if ques["answer"] != temp:
            temp = "option" + str(temp)
            ques[temp] = ""
            count += 1
    return ques

def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks

    print("Welcome to KBC")
    prize = 0
    que_cnt = 0
    min_reward = 0
    life_line_used = False
    while que_cnt < 15:
        print(f'\tQuestion {que_cnt + 1}: {QUESTIONS[que_cnt]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[que_cnt]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[que_cnt]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[que_cnt]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[que_cnt]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        if ans.lower() == "quit":
            break

        if ans.lower() == "lifeline" and que_cnt != 14 and not life_line_used:
            life_line_used = True
            question = lifeLine(QUESTIONS[que_cnt])
            print(f'\tQuestion {que_cnt + 1}: {question["name"]}' )
            print(f'\t\tOptions:')
            print(f'\t\t\tOption 1: {question["option1"]}')
            print(f'\t\t\tOption 2: {question["option2"]}')
            print(f'\t\t\tOption 3: {question["option3"]}')
            print(f'\t\t\tOption 4: {question["option4"]}')
            ans = input('Your choice ( 1-4 ) : ')
        # check for the input validations
        try:
            int(ans)
        except:
            print("Invalid Input!!!")
            continue
        
        if isAnswerCorrect(QUESTIONS[que_cnt], int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            if que_cnt == 4:
                min_reward = 10000
            elif que_cnt == 10:
                min_reward = 320000
            prize += QUESTIONS[que_cnt]["money"]
            print('\nCorrect !')

        else:
            # end the game now.
            # also print the correct answer
            prize = min_reward
            print('\nIncorrect !')
            break
        que_cnt += 1
    # print the total money won in the end.
    print("Amount you win is ", prize)

kbc()