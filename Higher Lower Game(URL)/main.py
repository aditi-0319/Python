from flask import Flask
import random
app = Flask(__name__)

random_num = random.randint(0, 9)
print(random_num)


@app.route('/')
def display():
    return '<h1 style="color:#BB2525">Guess a number between 0 and 9</h1>'


@app.route('/<int:num>')
def check(num):
    if num < random_num:
        return '<h1 style="color:#FF6969">Low, Try again!</h1>'\
               '<img src="https://i.giphy.com/media/jD4DwBtqPXRXa/giphy.webp" width=500px/>'
    elif num > random_num:
        return '<h1 style="color:#141E46">High, Try again!</h1>' \
               '<img src="https://i.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.webp" width=500px/>'
    elif num == random_num:
        return '<h1 style="color:#DFCCFB">Congratulations! You found the number!</h1>' \
               '<img src="https://i.giphy.com/media/4T7e4DmcrP9du/giphy.webp" width=500px/>'


if __name__ == "__main__":
    app.run(debug=True)