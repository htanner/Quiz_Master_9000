import PySimpleGUI as sg
import time


def pre_quiz():
    layout = [[sg.Text('Set up audio equipment.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout).read()
    window.close()
    layout = [[sg.Text('Start playlist.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout).read()
    window.close()
    layout = [[sg.Text('Get prizes from staff')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout).read()
    window.close()
    layout = [[sg.Text('Set up playlists for Rounds 2 and 7.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout).read()
    window.close()
    layout = [[sg.Text('Prep Round 5 sheets.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout).read()
    window.close()
    layout = [[sg.Text('Open score sheet.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout).read()
    window.close()
    layout = [[sg.Text('Give 15 minute warning.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout).read()
    window.close()
    layout = [[sg.Text('Give 5 minute warning.')],
              [sg.Button('Done')]]
    window = sg.Window('Pre-Quiz', layout).read()
    window.close()


def quiz_intro():
    layout = [[sg.Text('Introduce yourself.')],
              [sg.Button('Done')]]
    window = sg.Window('Quiz Introduction', layout).read()
    window.close()
    layout = [[sg.Text(f'#1. Don\'t shout out the answers.'
                       f'\n#2. Don\'t mess with the Quizmaster.'
                       f'\n#3. The quiz is fixed. The questions are the questions and the answers are the answers.'
                       f'\n#4. No look-up devices.'
                       f'\n#5. No more than 6 people per team.')],
              [sg.Button('Done')]]
    window = sg.Window('The Rules', layout).read()
    window.close()


def round_1():
    layout = [[sg.Text('Read round instructions.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout).read()
    window.close()
    layout = [[sg.Text('Read question 1.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout).read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 2.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout).read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 3.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout).read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 4.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout).read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 5.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout).read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 6.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout).read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 7.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout).read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Read question 8.')],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout).read()
    window.close()
    time.sleep(20)
    layout = [[sg.Text('Ask for repeats.')],
              [sg.Input()],
              [sg.Button('Done')]]
    window = sg.Window('Round 1', layout).read()
    window.close()


def round_2():
    pass


def round_3():
    pass


def round_4():
    pass


def round_5():
    pass


def round_6():
    pass


def round_7():
    pass


def round_8():
    pass


def scoring_break():
    pass


def results_announcement():
    pass


if __name__ == "__main__":
    sg.theme("Dark Purple 1")
    # layout = [[sg.Text('Skip pre-show prompts?')],
    #           [sg.Button('Yes'), sg.Button('No')]]
    # window = sg.Window('Running Late?', layout)
    # window.read()
    # window.close()

    pre_quiz()

    quiz_intro()

    round_1()
    round_2()
    round_3()

    scoring_break()

    round_4()
    round_5()
    round_6()

    scoring_break()

    round_7()
    round_8()

    results_announcement()
