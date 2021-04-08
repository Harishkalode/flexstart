import secrets
import os
from flask import Flask, render_template, url_for, redirect, send_file
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired, Length
from PIL import Image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'harish7634ydgwid78r3re48ryf78wrc7e8rcdc'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


class CustomImageFile(FlaskForm):
    file = FileField('Add Image', validators=[DataRequired(), FileAllowed(['jpg','png','jpeg'])])
    height = IntegerField('Height', validators=[DataRequired()])
    width = IntegerField('Width', validators=[DataRequired()])
    submit = SubmitField('Proceed to Continue')


def save_picture(from_picture,width,height):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(from_picture.filename)
    picture_fn = random_hex + '.jpg'
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (width,height)
    i = Image.open(from_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/custom", methods=['GET', 'POST'])
def custom():
    form = CustomImageFile()

    if form.validate_on_submit():
        if form.file.data:
            picture = save_picture(form.file.data, form.width.data, form.height.data)
            return redirect(url_for('thank',file = f'{picture}'))
    return render_template('custom.html', title='custom',form=form)


@app.route("/custom-made")
def custom_made():
    return render_template('custom-made.html', title='custom-made')


@app.route("/thank/<string:file>")
def thank(file):
    return render_template('thank-you.html', title='About',file=file)


@app.route("/download/<string:file>")
def download_file(file):
    p = f'static/profile_pics/{file}'
    return send_file(p,as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True,port=1100)