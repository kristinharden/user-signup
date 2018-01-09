from flask import Flask, request, redirect, render_template
import cgi
import os
# import jinja2

# template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
# (template_dir), autoescape=True)

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


# @app.route("/", methods=["POST"])
# def sign_up():
#     print("Try two")
#     user = str(request.form["username"])
#     pw = str(request.form["password"])
#     validpw = str(request.form["verify_password"])
#     em = str(request.form["email"])
#     print(user)
#     return render_template("form.html",
#        username_error = '',
#        password_error = '',
#        verify_password_error = '',
#        email_error = '',
#        username = '',
#        password = '',
#        verify_password = '',
#        email = '' )


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

    if len(user) <3 or len(user) > 20:
        user_error = "Username must be between 3 and 20 characters long."
    elif ' ' in user:
        user_error = "Username may not contain spaces."
    else:
        user = user

    if "@" or "." not in em and len(em) > 1 or " " in em or len(em) <3 or len(em) >20:
        em_error = "Not a valid email address."
        em = ""
    else:
        em = em

    if pw == "":
        pw_error = "Password required."
        pw = ""
        validpw = ""
    elif len(pw) <3 or len(pw) > 20:
        pw_error = "Password must be between 3 and 20 characters long."
        pw = ""
        validpw = ""
    elif ' ' in pw:
        pw_error = "Password may not contain spaces."
        pw = ""
        validpw = ""
    elif validpw == "":
        vpw_error = "Please validate password."
        pw = ""
        validpw = ""
    elif pw != validpw:
        vpw_error = "Password entries do not match."
        pw = ""
        validpw = ""
    else:
        pw = pw
        validpw = validpw

    if not user_error and not pw_error and not vpw_error and not em_error:
        # user = user
        return "Success"
        # return redirect("/welcome?user={0}".format(user))
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

# @app.route("/welcome", methods = ["GET"])
# def welcome():
#     user = request.args.get('user')
#     return render_template("welcome.html")

app.run()
