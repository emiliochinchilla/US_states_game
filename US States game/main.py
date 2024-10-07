from turtle import Turtle, Screen
import pandas

screen = Screen()
mapa = Turtle()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
mapa.shape(image)


data = pandas.read_csv("50_states.csv")
list_states = data.state.to_list()


correct_guesses = []
while len(correct_guesses) < 50:

    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in list_states if state not in correct_guesses]
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in list_states:
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]#ir al row del estado que se adivino
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        correct_guesses.append(answer_state)




