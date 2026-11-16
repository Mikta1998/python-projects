import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

state_data = pd.read_csv("50_states.csv")
states = state_data.state.to_list()

correct_guesses = []

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name? ")
score = 0

game_is_on = True

while game_is_on:
    if answer_state is None:
        game_is_on = False
        break
    else:
        answer_state = answer_state.title()
    if answer_state in states:
        if answer_state in correct_guesses:
            pass
        else:
            correct_guesses.append(answer_state)
            guessed_state = state_data[state_data.state == answer_state]
            x_coord = guessed_state.iloc[0]["x"]
            y_coord = guessed_state.iloc[0]["y"]
            writer.goto(x_coord, y_coord)
            writer.write(answer_state, font=("Arial", 8, "normal"))
            score += 1
    if len(correct_guesses) == len(states):
        break
    answer_state = screen.textinput(title=f"{score}/{len(states)} State's Correct", prompt="What's another state's name? ")

if game_is_on == False:
    screen.bye()
else:
    turtle.mainloop()