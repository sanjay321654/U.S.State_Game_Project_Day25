from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
all_states_data = data.state.to_list()
list_states = []
while len(list_states) < 50:
    guessed_state = screen.textinput(title=f"{len(list_states)}/50 States Correct",
                                     prompt="What's the another state").title()

    if guessed_state == "Exit":
        missing_states = []
        for state in all_states_data:
            if state not in list_states:
                missing_states.append(state)
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("states_to_learn.csv")
        break

    if guessed_state in all_states_data:
        list_states.append(guessed_state)
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == guessed_state]
        tim.goto(x=int(state_data.x), y=int(state_data.y))
        tim.write(guessed_state)

