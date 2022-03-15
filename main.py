from flask import Flask,render_template,request,redirect
from models import db,Student


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def home():
    return 'Hi'

@app.route('/data/create', methods=["GET",'POST'])
def create():
    if request.method == 'GET':
        return render_template('home.html')

    if request.method == 'POST':
        # studentid=request.form.get('student_id')
        studentname=request.form.get('student_name')
        studentgroup=request.form.get('student_group')
        studentrollno=request.form.get('student_rollno')
        students=Student(sname=studentname,sgroup=studentgroup,srollno=studentrollno)
        db.session.add(students)
        db.session.commit()
        return redirect('/data')

@app.route('/data')
def retrivelist():
    students=Student.query.all()
    #print(students)
    #print(len(students))
    return render_template('datalist.html',student=students)

@app.route('/data/<int:id>')
def retrivestudent(id):
    students=Student.query.filter_by(id=id).first()
    if students:
        return render_template('data.html',student=students)
    return "student with {} No data info".format(id)

@app.route('/data/<int:id>/update',methods=["GET","POST"])
def update(id):
    student=Student.query.filter_by(id=id).first()
    if request.method=='POST':
        if student:
            studentname=request.form.get('student_name')
            studentgroup=request.form.get('student_group')
            studentrollno=request.form.get('student_rollno')
            student.sname = studentname
            student.sgroup = studentgroup
            student.srollno = studentrollno
            # db.session.add(students)
            db.session.commit()
            return redirect('/data/'+str(id))
        return "student with {} No data info".format(id)
    return render_template('update.html',student=student)

if __name__=="__main__":
    app.run(debug=True,port=8888)