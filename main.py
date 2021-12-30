import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

correct_guess_list = []
list_of_states = data.state.to_list()
states_to_learn = []

while len(correct_guess_list) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess_list)}/50 states correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in list_of_states if state not in correct_guess_list]
        df_states_to_learn = pd.DataFrame(states_to_learn)
        df_states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in data.values:
        guess_row = data[data.state == answer_state]
        map_writer = turtle.Turtle()
        map_writer.hideturtle()
        map_writer.penup()
        map_writer.color("black")
        map_writer.goto(int(guess_row.x), int(guess_row.y))
        map_writer.write(answer_state, align="center", font={"Arial", 24, "normal"})
        correct_guess_list.append(answer_state)









screen.exitonclick()