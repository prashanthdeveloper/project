from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class Student(db.Model):
    __tablename__="student"

    id=db.Column(db.Integer(), primary_key=True)
    # studentid=db.Column(db.Integer())
    sname=db.Column(db.String())
    sgroup=db.Column(db.String())
    srollno=db.Column(db.Integer())

    def __init__(self,sname,sgroup,srollno):
        # self.studentid=studentid
        self.sname=sname
        self.sgroup=sgroup
        self.srollno=srollno


    def __repr__(self):
        return " {} : {} ".format(self.sname,self.sgroup)

