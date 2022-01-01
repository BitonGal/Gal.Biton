from flask import Flask, render_template, session, request, redirect, Blueprint
import mysql
import mysql.connector



app = Flask(__name__)
app.secret_key = '111'


assignment10 = Blueprint('assignment10',
                         __name__,static_folder='static',
                         static_url_path='/assignment10',
                         template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='ex10_gal_biton')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)


    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

@assignment10.route('/showUsers', methods=['GET','POST'])
@assignment10.route('/assignment10', methods=['GET','POST'])
def showUsers():
    users = interact_db(query = "select * "
                                "from ex10_gal_biton.users", query_type='fetch')
    if session.get('ans') is  None:
        return render_template('assignment10.html', users=users)
    else:
        ans = session['ans']
        session.pop('ans')
        return render_template('assignment10.html', users=users, message=ans)

@assignment10.route('/delete', methods=['POST'])
def delete():
    email = request.form['email']
    query = "SELECT email " \
            "FROM ex10_gal_biton.users WHERE email='%s';" % email
    if len(interact_db(query=query, query_type='fetch')) == 0:
        session['ans'] = "not found"

    else:
        query = "delete from ex10_gal_biton.users " \
                "where email='%s';" % email
        interact_db(query=query, query_type='commit')
        session['ans'] = "deleted"
    return redirect('/showUsers')

@assignment10.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        firstName = request.form['fname']
        lastName = request.form['lname']
        UserName = request.form['UserName']
        email = request.form['email']
        query = " UPDATE ex10_gal_biton.users" \
                " SET UserName='%s',fname='%s' ,lname='%s' WHERE email='%s';"% (UserName, firstName, lastName, email)
        interact_db(query=query, query_type='commit')
        session['ans'] = 'updated'
        return redirect('/showUsers')
    return render_template('assignment10.html', req_method=request.method)


@assignment10.route('/insert', methods=['GET','POST'])
def insert():
    if request.method == 'POST':
        firstName = request.form['fname']
        lastName = request.form['lname']
        UserName = request.form['UserName']
        email = request.form['email']
        q = "SELECT email FROM " \
            "ex10_gal_biton.users WHERE email='%s';" % email
        if len(interact_db(query=q, query_type='fetch')) == 0:
            query = "insert into ex10_gal_biton.users " \
                    "values ('%s', '%s', '%s','%s');" % (UserName, firstName, lastName, email)
            interact_db(query=query, query_type='commit')
            session['ans'] = 'good job'
        else:
            session['ans'] ='email is occupied'
        return redirect('/showUsers')
    return render_template('assignment10.html', req_method=request.method)

