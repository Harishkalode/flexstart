import os
import secrets
from flask import Flask,render_template, redirect, url_for, send_file
from flask_wtf import FlaskForm
from PIL import Image
from flask_wtf.file import FileField, FileAllowed
from wtforms import IntegerField, SubmitField,SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kjsdchksuhfkhhjdgdfgwufjldcnvsuyfhoiwofcjkjszhudyqwt67edroikepowkmdasnjdvtyqrw5yr8ojknds'

def save_picture(from_picture,width,height):
    rendom_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(from_picture.filename)
    picture_fn = rendom_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images',picture_fn)
    output_size = (width,height)

    i = Image.open(from_picture)
    img = i.resize(output_size)
    img.save(picture_path)

    return picture_fn

#form section


class CustomizationField(FlaskForm):
    image = FileField('Select Image', validators=[DataRequired(), FileAllowed(['jpg','jpeg','png'])])
    height = IntegerField('Height',validators=[DataRequired()])
    width = IntegerField('Width',validators=[DataRequired()])
    submit = SubmitField('Resize Image')


class PredefinedExamField(FlaskForm):
    image = FileField('Select Image', validators=[DataRequired(), FileAllowed(['jpg','jpeg','png'])])
    exam = SelectField('Select Exam',choices=[('upsc','UPSC civil examination'),('sbi po','SBI Po'),('sbi clerk','SBI Clerk'),
                                          ('ibps po','IBPS Po'),('ibps so','IBPS SO'),('ibps rrb','IBPS RRB'),('ssc cgl','SSC CGL'),('ssc cpo','SSC CPO'),('ssc je','SSC JE'),('ssc chsl','SSC CHSL'),
                                          ('rrb je','RRB JE'),('rrb alp','RRB ALP'),('lic aao','LIC AAO'),('rbi grade b','RBI GRADE B'),('cds exam','CDS EXAM'),
                                              ('neet','NEET'),('jee','JEE'),('gate','GATE')],
                       validators=[DataRequired()])
    submit = SubmitField('Resize Image')


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')


@app.route('/custom', methods=['GET','POST'])
def custom():
    form = CustomizationField()
    if form.validate_on_submit():
        if form.image.data:
            picture = save_picture(form.image.data,form.width.data,form.height.data)
            return redirect(url_for('thank_you',file = f"{picture}"))
    return render_template('custom.html', form=form,title='Customization')

@app.route('/predefined',methods = ['GET','POST'])
def predefined():
    form = PredefinedExamField()
    h = 0
    w = 0
    if form.exam.data == 'upsc':
        h = 350
        w = 350
    elif form.exam.data == 'sbi po':
        h = 230
        w = 200
    elif form.exam.data == 'sbi clerk':
        h = 230
        w = 200
    elif form.exam.data == 'ibps po':
        h = 230
        w = 200
    elif form.exam.data == 'ibps so':
        h = 230
        w = 200
    elif form.exam.data == 'ibps rrb':
        h = 230
        w = 200
    elif form.exam.data == 'ssc cgl':
        h = 200
        w = 300
    elif form.exam.data == 'ssc cpo':
        h = 120
        w = 100
    elif form.exam.data == 'ssc je':
        h = 200
        w = 300
    elif form.exam.data == 'ssc chsl':
        h = 120
        w = 100
    elif form.exam.data == 'rrb alp':
        h = 200
        w = 300
    elif form.exam.data == 'rrb je':
        h = 200
        w = 300
    elif form.exam.data == 'rbi grade b':
        h = 200
        w = 230
    elif form.exam.data == 'lic aao':
        h = 200
        w = 300
    elif form.exam.data == 'cd exam':
        h = 350
        w = 350
    elif form.exam.data == 'jee':
        h = 230
        w = 200
    elif form.exam.data == "neet":
        h = 230
        w = 200
    elif form.exam.data == 'gate':
        h = 320
        w = 240
    
    if form.validate_on_submit():
        if form.image.data:
            picture = save_picture(form.image.data, w , h)
            return redirect(url_for('thank_you', file=f"{picture}"))
    return render_template('predefined.html',tilte='Predefined Exam',form=form)


@app.route('/thank-you/<string:file>')
def thank_you(file):
    return render_template('thank you.html',tilte='Thank You', file=file)


@app.route('/download/<string:file>')
def download(file):
    p = f'static/images/{file}'
    return send_file(p,as_attachment=True)


if __name__ == "__main__":
    app.run(port=1001,debug=True)
