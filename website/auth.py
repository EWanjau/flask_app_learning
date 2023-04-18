from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email Must be greater than 4 characters', category='error')
        elif len(firstName) < 2:
            flash('First name Must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('PAsswords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at-least 7 characters', category='error')
        else:
            #add user to database
            flash('Account Created Successfully', category='success')
    return render_template("sign_up.html")
