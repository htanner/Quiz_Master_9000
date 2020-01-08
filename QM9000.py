import PySimpleGUI as sg
import time


def pre_quiz():
    layout = [[sg.Text('Set up audio equipment.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Start playlist.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Get prizes from staff')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Set up playlists for Rounds 2 and 7.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Prep Round 5 sheets.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Open score sheet.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Give 15 minute warning.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Give 5 minute warning.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout)
    window.read()
    window.close()


def quiz_intro():
    layout = [[sg.Text('Introduce yourself.')],
              [sg.Button('Done')]]
    window = sg.Window('Quiz Introduction', layout)
    window.read()
    window.close()
    layout = [[sg.Text(f'#1. Don\'t shout out the answers.'
                       f'\n#2. Don\'t mess with the Quizmaster.'
                       f'\n#3. The quiz is fixed. The questions are the questions and the answers are the answers.'
                       f'\n#4. No look-up devices.'
                       f'\n#5. No more than 6 people per team.')],
              [sg.Button('Done')]]
    window = sg.Window('The Rules', layout)
    window.read()
    window.close()


def round_1():
    layout = [[sg.Text('Read round instructions.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Read question 1.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 2.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 3.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 4.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 5.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 6.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 7.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 8.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Ask for repeats.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Read bonus question.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Announce bonus winner and give prize.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout)
    window.read()
    window.close()


def round_2():
    layout = [[sg.Text('Read round instructions.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 2', layout)
    window.read()
    window.close()


def round_3():
    layout = [[sg.Text('Read round instructions.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 3', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Read question 1.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 3', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 2.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 3', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 3.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 3', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 4.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 3', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 5.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 3', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 6.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 3', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 7.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 3', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 8.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 3', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Ask for repeats.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 3', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Read bonus question.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 3', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Announce bonus winner and give prize.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 3', layout)
    window.read()
    window.close()


def round_4():
    layout = [[sg.Text('Read round instructions.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 4', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Read question 1.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 4', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 2.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 4', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 3.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 4', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 4.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 4', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 5.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 4', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Remind teams that Round 5 answers are due at end of round.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 4', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Read question 6.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 4', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 7.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 4', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 8.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 4', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Ask for repeats.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 4', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Read bonus question.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 4', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Announce bonus winner and give prize.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 4', layout)
    window.read()
    window.close()


def round_5():
    pass


def round_6():
    layout = [[sg.Text('Read round instructions.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 6', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Read question 1.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 6', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 2.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 6', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 3.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 6', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 4.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 6', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 5.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 6', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 6.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 6', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 7.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 6', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 8.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 6', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Ask for repeats.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 6', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Read bonus question.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 6', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Announce bonus winner and give prize.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 6', layout)
    window.read()
    window.close()


def round_7():
    layout = [[sg.Text('Read round instructions.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 7', layout)
    window.read()
    window.close()


def round_8():
    layout = [[sg.Text('Read round instructions.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 8', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Read question 1.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 8', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 2.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 8', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 3.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 8', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 4.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 8', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 5.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 8', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 6.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 8', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 7.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 8', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 8.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 8', layout)
    window.read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Ask for repeats.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 8', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Read bonus question.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 8', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Announce bonus winner and give prize.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 8', layout)
    window.read()
    window.close()


def scoring_break(break_num):
    if break_num == 1:
        layout = [[sg.Text('Announce scoring break. Mention that Round 5 will be handed in after Round 4.')],
                  [sg.Input()],
                  [sg.Button('Done')]]
        window = sg.Window('Scoring Break', layout)
        window.read()
        window.close()
        layout = [[sg.Text('Read answers from Rounds 1, 2, and 3.')],
                  [sg.Input()],
                  [sg.Button('Done')]]
        window = sg.Window('Scoring Break', layout)
        window.read()
        window.close()
        layout = [[sg.Text('Read out current team standings.')],
                  [sg.Input()],
                  [sg.Button('Done')]]
        window = sg.Window('Scoring Break', layout)
        window.read()
        window.close()
    elif break_num == 2:
        layout = [[sg.Text('Announce scoring break. Take team pictures.')],
                  [sg.Input()],
                  [sg.Button('Done')]]
        window = sg.Window('Scoring Break', layout)
        window.read()
        window.close()
        layout = [[sg.Text('Read answers from Rounds 4 and 5.')],
                  [sg.Input()],
                  [sg.Button('Done')]]
        window = sg.Window('Scoring Break', layout)
        window.read()
        window.close()
        layout = [[sg.Text('Read out current team standings.')],
                  [sg.Input()],
                  [sg.Button('Done')]]
        window = sg.Window('Scoring Break', layout)
        window.read()
        window.close()
    else:
        layout = [[sg.Text('Announce scoring break.')],
                  [sg.Input()],
                  [sg.Button('Done')]]
        window = sg.Window('Scoring Break', layout)
        window.read()
        window.close()
        layout = [[sg.Text('Read answers from Rounds 6 and 7.')],
                  [sg.Input()],
                  [sg.Button('Done')]]
        window = sg.Window('Scoring Break', layout)
        window.read()
        window.close()
        layout = [[sg.Text('Read out current team standings.')],
                  [sg.Input()],
                  [sg.Button('Done')]]
        window = sg.Window('Scoring Break', layout)
        window.read()
        window.close()


def results_announcement():
    layout = [[sg.Text('Announce final scoring break.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Final Results', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Read answers from Round 8.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Final Results', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Read out final team standings.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Final Results', layout)
    window.read()
    window.close()
    layout = [[sg.Text('Hand out prizes.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Final Results', layout)
    window.read()
    window.close()


if __name__ == "__main__":
    sg.theme("Dark Purple 1")
    # layout = [[sg.Text('Skip pre-show prompts?')],
    #           [sg.Button('Yes'), sg.Button('No')]]
    # window = sg.Window('Running Late?', layout)
    # windowwindow.read()
    # window.close()

    pre_quiz()

    quiz_intro()

    round_1()
    round_2()
    round_3()

    scoring_break(1)

    round_4()
    round_5()

    scoring_break(2)

    round_6()
    round_7()

    scoring_break(3)

    round_8()

    results_announcement()
