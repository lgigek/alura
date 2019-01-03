from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'test'


class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


class User:
    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.password = password


user1 = User('test-1', 'Test1', '1')
user2 = User('test-2', 'Test2', '2')
users = {user1.username: user1,
         user2.username: user2}

game1 = Game('Super Mario', 'Action', 'SNES')
game2 = Game('Pokemon Gold', 'RPG', 'GBA')
game3 = Game('Moral Kombat', 'Fight', 'SNES')
games = [game1, game2, game3]


@app.route('/')
def index():
    return render_template('list.html', title='Playhouse', games=games)


@app.route('/new')
def new():
    if 'logged_user' not in session or session['logged_user'] is None:
        return redirect(url_for('login', next=url_for('new')))
    return render_template('new.html', title="New game")


@app.route('/create', methods=['POST'])
def create():
    games.append(Game(request.form['name'], request.form['category'], request.form['console']))
    return redirect(url_for('index'))


@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)


@app.route('/auth', methods=['POST'])
def auth():
    username = request.form['username']
    if username in users:
        user = users[username]
        if user.password == request.form['password']:
            session['logged_user'] = request.form['username']
            flash(f"{user.name} logged successfully!")
            next_page = request.form['next']
            return redirect(next_page)

    flash('Wrong user or password')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Logged out successfully!')
    return redirect(url_for('index'))


app.run(debug=True)
