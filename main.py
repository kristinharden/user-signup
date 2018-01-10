from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_form():
    return render_template("form.html",
       username_error = '',
       password_error = '',
       verify_password_error = '',
       email_error = '',
       username = '',
       password = '',
       verify_password = '',
       email = '' )

@app.route("/", methods=["POST"])
def sign_up():
    user = str(request.form["username"])
    pw = str(request.form["password"])
    validpw = str(request.form["verify_password"])
    em = str(request.form["email"])

    user_error = ""
    pw_error = ""
    vpw_error = ""
    em_error = ""

    if len(user) <3 or len(user) > 20 or " " in user:
        user_error = "Username must be between 3 and 20 characters long and may not contain spaces."
        user = ""

    if len(email)>0:
        if "@" not in em or "." not in em or " " in em or len(em) <3 or len(em) >20:
            em_error = "Not a valid email address."
            em = ""

    if len(pw) <3 or len(pw) > 20 or " " in pw:
        pw_error = "Password must be between 3 and 20 characters long and may not contain spaces."
        
    if pw != validpw:
        vpw_error = "Password entries do not match."

    if not user_error and not pw_error and not vpw_error and not em_error:
        return render_template("welcome.html", user=user)
    else:
        return render_template("form.html",
            user_error = user_error,
            pw_error = pw_error,
            vpw_error = vpw_error,
            em_error = em_error,
            user = user,
            pw = "",
            validpw = "",
            em = em,)

app.run()
