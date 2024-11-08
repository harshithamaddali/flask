from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user,current_user

app = Flask(_name_)
app.config['SECRET_KEY'] = 'your_secret_key'

#Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#Mock database of users (for demonstartion)
users = {'user1': {'password': 'password123'}}

#User class that inherits from UserMixin to handle user
class User(UserMixin):
    def _init_(self, id):
        self.id = id
@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id in users else None

@app.route('/')
@login_required
def home():
    return render_template('home.html', name=current_user.id)

@app.rote('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.from.get('password')

        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if _name_ == '_main_':
    app.run(debug=True)