from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app=Flask(__name__)

#secret key for csrf security
app.config['SECRET_KEY'] = 'mysecretkey' #we create it as env_variable

class InfoForm(FlaskForm):
    breed = StringField('what breed are you?')
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    breed = False
    form= InfoForm()

    if form.validate_on_submit():
        breed= form.breed.data
        form.breed.data=''
    return render_template('index.html',form=form,breed=breed)

if __name__=='__main__':
    app.run(debug=True)
