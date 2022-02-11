from random import choices
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateField,IntegerField,SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    user_name = StringField('User Name')
    age = IntegerField('Age')
    gender = SelectField('Gender selection', choices = [('male','MALE'),('female','FEMALE')])
    race = SelectField('Race selection', choices = [('human','HUMAN'),('high elf','HIGH ELF'),('orc','ORC'),('khajiit','KHAJIIT')])
    class_selection = SelectField('Class Selection', choices=[('warrior','WARRIOR'),('mage','MAGE'),('Assassin','ASSASSIN'),('paladin','PALADIN'),('necromancer','NECROMANCER'),('bezerker','BEZERKER')])
    submit = SubmitField('Ready')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        user_name = form.user_name.data
        age = form.age.data
        gender = form.gender.data
        race = form.race.data
        class_selection = form.class_selection.data
        

        if len(user_name) == 0:
            message = "Please supply user name"
        else:
            message = f'Welcome to your adventure, {user_name}! and you\'re {age} years old ?! \n I see your race is {race} and your class is {class_selection}.\n The world is yours to shape!' 

    return render_template('home.html', form=form, message=message)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')