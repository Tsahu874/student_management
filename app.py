from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



# Connecting the flask app with sqlite database
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'



# Object of SQLalchemy class
database = SQLAlchemy(app)

# Python class used to insert data into table
class StuList(database.Model):
    S_no = database.Column(database.Integer, primary_key= True)
    Name = database.Column(database.String(50),nullable = False)
    ID = database.Column(database.String(50), nullable=False,unique= True)
    PhoneNo = database.Column(database.Integer, nullable = False)
    Email = database.Column(database.String(80))






#First route
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        stuName = request.form.get("name")
        stu_id = request.form.get("id")
        stuPhone = request.form.get("phone")
        stuEmail = request.form.get("email")
        print(stuName,stu_id,stuPhone,stuEmail)

        # add it to database
        student = StuList(Name=stuName, ID= stu_id , PhoneNo = stuPhone,Email = stuEmail)
        database.session.add(student)
        database.session.commit()
    #     return redirect('/')
    
    # else:
    #     # fetch all the request is a get request
    #     allStudents = StuList.query.all()


    return render_template('index.html')

#second route
@app.route('/StuList')
def list():
    allStudents = StuList.query.all()
    return render_template('Stu_list.html', allStudents=allStudents)

#third route
@app.route('/detail', methods=["GET", "POST"])
def detail():
    student = None
    if request.method == "POST":
        student_id = request.form.get("studentID")
        student = StuList.query.filter_by(ID=student_id).first()
    return render_template('detail.html', student=student)

# Fourth route : delete student detail
@app.route('/delete')
def delete():
    Stu_ID = request.args.get('student_id')
   
    student = StuList.query.filter_by(ID=Stu_ID).first()

    #deleting the details
    database.session.delete(student)
    database.session.commit()


    # print(student)
    return redirect('/StuList')


# Fifth route : update the details
@app.route('/update', methods= ["GET","POST"])
def update():

    Stu_ID = request.args.get('student_id')
    # print(f"updating the detail of {Stu_ID}")

    # Fetching the details to check its existing  values
    student = StuList.query.filter_by(ID = Stu_ID).first()

    if request.method == "POST":
        updatedName = request.form.get('name')
        updatedId = request.form.get('id')
        updatedPh = request.form.get('phone')
        updatedEmail = request.form.get('email')

        # changing the value of details
        student.Name =  updatedName
        student.Id = updatedId
        student.PhoneNo = updatedPh 
        student.Email = updatedEmail
        database.session.add(student)
        database.session.commit()

        return redirect('/StuList')


    else:
        return render_template('update.html', student = student)





# if __name__ == "__main__":
app.run(debug=True)

