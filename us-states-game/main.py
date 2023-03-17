import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
state_names_list = data['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50",
                                    prompt="What's another state's name? ").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_names_list if state not in guessed_states]
        # for state in state_names_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn')
        break

    # If answer state is one of the states in all 50 states
    if answer_state in state_names_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f"{answer_state}")







