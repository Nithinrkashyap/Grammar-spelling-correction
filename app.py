from flask import Flask,request,render_template
from Model import SpellCheckerModule

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

# print("hello")
spell_checker_module=SpellCheckerModule()



@app.route('/grammar_spell_text',methods=['GET','POST'])
def spell():
    if request.method=='POST':
        text=request.form['text']
        print("text: ",text)
        input_text=text
        correct_spell=spell_checker_module.correct_spell(text)
        print("correct_spelling in /spell:",correct_spell)
        #& it returns a tuple
        incorrect_words,incorrect_words_count,correct_text=spell_checker_module.correct_grammar(text)
    return render_template('index.html', input_text=input_text  ,incorrect_words=incorrect_words,incorrect_words_count=incorrect_words_count,correct_text=correct_text,correct_spell=correct_spell);

@app.route('/grammar_spell_file',methods=['GET','POST'])
def grammar():
    if request.method=="POST":
        file=request.files['file']
        readable_file = file.read().decode('utf-8',errors='ignore')
        input_file=readable_file
        corrected_file_spell = spell_checker_module.correct_spell(readable_file)
        incorrect_words_file,incorrect_words_count_file,correct_text_file = spell_checker_module.correct_grammar(readable_file)
    return render_template('index.html',input_file=input_file,incorrect_words_file=incorrect_words_file,incorrect_words_count_file=incorrect_words_count_file,correct_text_file=correct_text_file,corrected_file_spell=corrected_file_spell);


if __name__ == "__main__":
    app.run(debug=True,port=5001)