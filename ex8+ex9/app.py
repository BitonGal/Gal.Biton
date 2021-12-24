from flask import Flask, render_template ,request, session

app = Flask(__name__)
app.secret_key = '111'

users = {"user1": {"UserName": "galbi","First Name": "Gal","Last Name": "Biton", "Email": "galbi@post.bgu.ac.il"},
         "user2": {"UserName": "shiri","First Name": "Shiri", "Last Name": "mymon", "Email": "shiri@gmail.com"},
         "user3": {"UserName": "gadiz","First Name": "Gadi", "Last Name": "sukenik", "Email": "gadiz@gmail.com"},
         "user4": {"UserName": "segal3","First Name": "amit", "Last Name": "segal", "Email": "segal@gmail.com"},
         "user5": {"UserName": "guyp", "First Name": "guy", "Last Name": "peleg", "Email": "guyp@gmail.com"}
         }



@app.route('/home')
@app.route('/')
def main():
    return render_template('CV.html')


@app.route('/ex2')
def ex2():
    return render_template('exercise2.html')


@app.route('/forms')
def forms():
    return render_template('forms.html')


@app.route('/assignment8')
def assignment8():
    nyc = ("Museum of natural history", "Brooklyn Bridge", "9/11 memorial", "soho")
    return render_template('assignment8.html', nyc=nyc)

@app.route('/assignment9' , methods = ['GET','POST'])
def assignment9():
    current_method = request.method
    if current_method == 'GET':
        if 'user_name' in request.args:
            user_name = request.args['user_name']
            if user_name is '':
                return render_template('assignment9.html', search=True, users=users, finduser=True)
            user_dic = {}
            for user in users.values():
                if user['UserName'] == user_name:
                    user_dic[1] = user
            if len(user_dic) != 0:
                return render_template('assignment9.html', search=True, finduser=True, users=user_dic)
            else:
                return render_template('assignment9.html', finduser=False, search=True)
        return render_template('assignment9.html')
    elif current_method == 'POST':
        session['login'] = True
        users[request.form['email']] = {'First Name': request.form['firstName'],
                                            'Last Name': request.form['lastName'],
                                            'Email': request.form['email'],
                                            'User Name': request.form['userName']}
        session['userName'] = request.form['userName']
        return render_template('assignment9.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['login'] = False
    return render_template('CV.html')



if __name__ == '__main__':
    app.run()

