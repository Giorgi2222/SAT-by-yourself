from flask import Flask, redirect, render_template, request, session
from flask_session import Session

from helpers import apology, recomend

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = False

app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


class Book:
    def __init__(self, name, author, edition, category, url):
        self.name = name
        self.author = author
        self.edition = edition
        self.url = url
        self.category = category
    
books = {}
books['vocab'] = {}
books['gram'] = {}
books['R&W'] = {}
books['math'] = {}
books['tests'] = {}

books["vocab"]["400words"] = Book("400 Must-Have Words for the TOEFL", "Lawrence J Zwier", "Doesn't Matter","Vocabulary", "/400words")
books["vocab"]["504words"] = Book("504 Absolutely Essential Words", "Murray Bromberg", "5th or 6th Edition","Vocabulary", "/504words")
books["vocab"]["1100words"] = Book("1100 Words You Need to Know", "Murray Bromberg", "6th or 7th Edition","Vocabulary","/1100words")
books["vocab"]["powervocab"] = Book("SAT Power Vocab", "The Princeton Review Staff", "2nd Edition", "Vocabulary","/powervocab")
books["vocab"]["601words"] = Book("601 Words You Need to Know to Pass Your Exam", "Murray Bromberg", "Doesn't Matter","Vocabulary", "/601words")
books["vocab"]["camvocab"] = Book("English Vocabulary in Use - Upper-Intermediate", "Michael McCarthy and Felicity O'Dell", "Latest You Find","Vocabulary", "/camvocab")

books["gram"]["dest"] = Book("Destination C1 & C2: Grammar & Vocabulary", "Malcolm Mann and Steve Taylor-Knowles", "Doesn't Matter","Grammar", "/dest")
books["gram"]["blue"] = Book("The Blue Book of Grammar and Punctuation", "Jane Straus and Lester Kaufman", "Doesn't Matter","Grammar","/blue")
books["gram"]["peng"] = Book("The Penguin Guide to Punctuation", "Larry Trask", "Doesn't Matter", "Grammar","/peng")
books["gram"]["meltzerG"] = Book("The Ultimate Guide to SAT Grammar", "Erica L. Meltzer", "4th or 5th Edition", "Grammar","/meltzerG")

books["R&W"]["meltzerR"] = Book("The Critical Reader: The Complete Guide to SAT Reading","Erica L. Meltzer","3rd or 4th Edition","Reading and Writing", "/meltzerR")
books["R&W"]["pandaW"] = Book("The College Panda's SAT Writing: Advanced Guide and Workbook by The College Panda", "Nielson Phu", "Doesn't Matter", "Reading and Writing","/pandaW")
books["R&W"]["PR"] = Book("Princeton Review SAT Premium Prep","The Princeton Review Staff","Latest You Find", "Math, Reading and Writing","/PR")
books["R&W"]["barronsR"] = Book("Reading Workbook for the NEW SAT","Brian Stewart","Doesn't Matter","Reading and Writing", "/barronsR")
books["R&W"]["RWW"] = Book("Reading and Writing Workout for the SAT","The Princeton Review Staff","3rd or 4th Edition", "Reading and Writing","/RWW")
books["R&W"]["iesR"] = Book("IES New SAT Reading Practice Book","Khalid Khashoggi","Latest You Find","Reading and Writing", "/iesR")

books['math']['kaplan'] = Book("Kaplan's SAT Math Prep","The Kaplan Test Prep","7th or 8th Edition","Math","/kaplan")
books['math']['barronsM'] = Book("Barron's Math Workbook for the New SAT","Lawrence S. Leff","6th Edition","Math","/barronsM")
books['math']['pandaM'] = Book("The College Panda's SAT Math: Advanced Guide and Workbook for the New SAT","Nielson Phu","2nd Edition","Math","/pandaM")
books['math']['Mworkout'] = Book("Math Workout for the SAT","The Princeton Review Staff","5th Edition","Math","/Mworkout")
books['math']['pandaM10'] = Book("The College Panda's 10 Practice Tests for the SAT Math","Nielson Phu","Latest You Find","Math","/pandaM10")

books['tests']['ivy4'] = Book("Ivy Global's New SAT 4 Practice Tests","The Ivy Global","Latest You Find","Full Tests","/ivy4")
books['tests']['iesF'] = Book("IES New SAT Practice Tests","Khalid Khashoggi and Ariana Astuni","Latest You Find","Full Tests","/iesF")
books['tests']['full8'] = Book("Official SAT Downloadable Full-Length Practice Tests","Collegeboard","Latest You Find","Full Tests","/full8")



@app.route("/", methods=["GET", "POST"])
def collect_info():
    """Register user"""
    if request.method == "POST":
        target_score = request.form.get("target_score")
        english_level = request.form.get("english_level")
        english = request.form.get("english")
        math = request.form.get("math")

        try:
            target_score = int(target_score)
            target_score = round(target_score/100)*100
            if target_score == None or target_score < 800 or  target_score > 1600:
                return apology("Enter target score between 800 and 1600")
        except:
            return apology("Enter target score between 800 and 1600")
        
        if english and math:
            english = int(english)
            english = round(english/100)*100
            math = int(math)
            math = round(math/100)*100
            if english < 200 or  english > 800:
                return apology("math and english section scores should be numbers between 200 and 800")
            if  math < 200 or  math > 800:
                return apology("math and english section scores should be numbers between 200 and 800")



        session['target_score'] = target_score
        session['english_level'] = english_level

        if math and english:
            selected_books = recomend(books, target_score, english_level, math, english)
            session['english'] = english
            session['math']= math
        elif not math and not english:
            selected_books = recomend(books, target_score, english_level)
        else:
            return apology("Enter both or none of math and english section scores")
        
        return render_template("books.html", books=selected_books)
    else:
          if not session.get("target_score"):
            return render_template("index.html")
          else:
            if session.get("math") and session.get("english"):
                selected_books = recomend(books, session['target_score'], session['english_level'], session['math'], session['english'])
                return render_template("books.html", books=selected_books)
            else:
                selected_books = recomend(books, session['target_score'], session['english_level'])
                return render_template("books.html", books=selected_books)


@app.route("/allbooks")
def allbooks():

    return render_template("allbooks.html", books=books)



@app.route("/400words")
def words400():
    return render_template("400words.html")

@app.route("/504words")
def words504():
    return render_template("504words.html")

@app.route("/1100words")
def words1100():
    return render_template("1100words.html")

@app.route("/601words")
def words601():
    return render_template("601words.html")

@app.route("/camvocab")
def camvocab():
    return render_template("camvocab.html")

@app.route("/powervocab")
def powervocab():
    return render_template("powervocab.html")

@app.route("/dest")                                       
def dest():
    return render_template("dest.html")
#here
@app.route("/blue")
def blue():
    return render_template("blue.html")

@app.route("/peng")
def peng():
    return render_template("peng.html")

@app.route("/meltzerG")
def meltzerG():
    return render_template("meltzerG.html")

@app.route("/meltzerR")
def meltzerR():
    return render_template("meltzerR.html")

@app.route("/pandaW")
def pandaW():
    return render_template("pandaW.html")

@app.route("/PR")
def PR():
    return render_template("PR.html")

@app.route("/barronsR")
def barronsR():
    return render_template("barronsR.html")

@app.route("/RWW")
def RWW():
    return render_template("RWW.html")

@app.route("/iesR")
def iesR():
    return render_template("iesR.html")

@app.route("/kaplan")
def kaplan():
    return render_template("kaplan.html")

@app.route("/barronsM")
def barronsM():
    return render_template("barronsM.html")

@app.route("/pandaM")
def pandaM():
    return render_template("pandaM.html")

@app.route("/Mworkout")
def Mworkout():
    return render_template("Mworkout.html")

@app.route("/pandaM10")
def pandaM10():
    return render_template("pandaM10.html")

@app.route("/ivy4")
def ivy4():
    return render_template("ivy4.html")

@app.route("/iesF")
def iesF():
    return render_template("iesF.html")

@app.route("/full8")
def full8():
    return render_template("full8.html")



@app.route("/new")
def new():
    session['target_score'] = None
    session['english_level'] = None
    try:
        session['english'] = None
        session['math'] = None
    except:
        pass
    return redirect("/")



