import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def recomend(books, target_score, english_level, math = None, english = None):
        target_score = int(target_score)
        selected_books = {}
        selected_books['req'] = []
        selected_books['rec'] = []

        def remove(book):
          if book in selected_books['req']:
               selected_books['req'].remove(book)
          elif book in selected_books['rec']:
               selected_books['rec'].remove(book)

        def recommend(book):
          if book in selected_books['req']:
               selected_books['rec'].append(book)
               selected_books['req'].remove(book)

        def require(book):
          if book in selected_books['rec']:
               selected_books['req'].append(book)
               selected_books['rec'].remove(book)

        if target_score >= 800 and target_score < 1100:
             selected_books['rec'].append(books["vocab"]["camvocab"])
             selected_books['rec'].append(books["vocab"]["400words"])
             selected_books['rec'].append(books["gram"]["blue"])
             selected_books['rec'].append(books['math']['kaplan'])
             selected_books['req'].append(books["R&W"]["PR"])
             selected_books['req'].append(books['tests']['full8'])
        elif target_score >= 1100 and target_score < 1250:
             selected_books['rec'].append(books["vocab"]["camvocab"])
             selected_books['req'].append(books["vocab"]["400words"])   
             selected_books['req'].append(books["vocab"]["504words"])   
             selected_books['req'].append(books["gram"]["blue"])
             selected_books['rec'].append(books['math']['kaplan'])
             selected_books['req'].append(books['math']['Mworkout'])
             selected_books['rec'].append(books['math']['barronsM'])
             selected_books['req'].append(books["R&W"]["PR"])
             selected_books['rec'].append(books["R&W"]["RWW"])
             selected_books['req'].append(books['tests']['full8'])
        elif target_score >= 1250 and target_score < 1350:
             selected_books['rec'].append(books["vocab"]["camvocab"])
             selected_books['req'].append(books["vocab"]["400words"])   
             selected_books['req'].append(books["vocab"]["504words"])   
             selected_books['req'].append(books["vocab"]["1100words"])   
             selected_books['req'].append(books["gram"]["blue"])
             selected_books['rec'].append(books['math']['kaplan'])
             selected_books['req'].append(books['math']['Mworkout'])
             selected_books['req'].append(books['math']['barronsM'])
             temp = books["R&W"]["PR"]
             temp.category = "(Do Only Full Tests)" 
             selected_books['req'].append(temp)
             selected_books['rec'].append(books["R&W"]["RWW"])
             selected_books['req'].append(books["R&W"]["barronsR"])
             selected_books['req'].append(books["R&W"]["pandaW"])
             selected_books['req'].append(books["gram"]["meltzerG"])
             selected_books['req'].append(books['tests']['full8'])
        elif target_score >= 1350 and target_score < 1450:
             selected_books['rec'].append(books["vocab"]["camvocab"])
             selected_books['req'].append(books["vocab"]["400words"])   
             selected_books['req'].append(books["vocab"]["504words"])   
             selected_books['req'].append(books["vocab"]["1100words"])   
             selected_books['req'].append(books["vocab"]["powervocab"])   
             selected_books['req'].append(books["gram"]["blue"])
             selected_books['rec'].append(books["gram"]["peng"])
             selected_books['rec'].append(books['math']['kaplan'])
             selected_books['rec'].append(books['math']['Mworkout'])
             selected_books['req'].append(books['math']['barronsM'])
             selected_books['req'].append(books['math']['pandaM'])
             selected_books['rec'].append(books['math']['pandaM10'])
             temp = books["R&W"]["PR"]
             temp.category = "(Do Only Full Tests)" 
             selected_books['req'].append(temp)
             selected_books['rec'].append(books["R&W"]["RWW"])
             selected_books['req'].append(books["R&W"]["meltzerR"])
             selected_books['req'].append(books["R&W"]["barronsR"])
             selected_books['req'].append(books["R&W"]["pandaW"])
             selected_books['req'].append(books["gram"]["meltzerG"])
             selected_books['req'].append(books['tests']['full8'])
             selected_books['rec'].append(books['tests']['ivy4'])
        elif target_score >= 1450 and target_score < 1500: 
             selected_books['rec'].append(books["vocab"]["camvocab"])
             selected_books['req'].append(books["vocab"]["400words"])   
             selected_books['req'].append(books["vocab"]["504words"])   
             selected_books['req'].append(books["vocab"]["1100words"])   
             selected_books['rec'].append(books["vocab"]["601words"])   
             selected_books['req'].append(books["vocab"]["powervocab"])   
             selected_books['req'].append(books["gram"]["blue"])
             selected_books['rec'].append(books["gram"]["peng"])
             selected_books['rec'].append(books['math']['kaplan'])
             selected_books['rec'].append(books['math']['Mworkout'])
             selected_books['req'].append(books['math']['barronsM'])
             selected_books['req'].append(books['math']['pandaM'])
             selected_books['req'].append(books['math']['pandaM10'])
             temp = books["R&W"]["PR"]
             temp.category = "(Do Only Full Tests)" 
             selected_books['req'].append(temp)
             selected_books['rec'].append(books["R&W"]["RWW"])
             selected_books['req'].append(books["R&W"]["meltzerR"])
             selected_books['req'].append(books["R&W"]["barronsR"])
             selected_books['req'].append(books["R&W"]["pandaW"])
             selected_books['req'].append(books["R&W"]["iesR"])
             selected_books['req'].append(books["gram"]["meltzerG"])
             selected_books['req'].append(books['tests']['full8'])
             selected_books['rec'].append(books['tests']['iesF'])
             selected_books['rec'].append(books['tests']['ivy4'])
            
        elif target_score >= 1500:
             selected_books['rec'].append(books["vocab"]["camvocab"])
             selected_books['req'].append(books["vocab"]["400words"])   
             selected_books['req'].append(books["vocab"]["504words"])   
             selected_books['req'].append(books["vocab"]["1100words"])   
             selected_books['req'].append(books["vocab"]["601words"])   
             selected_books['req'].append(books["vocab"]["powervocab"])   
             selected_books['req'].append(books["gram"]["blue"])
             selected_books['rec'].append(books["gram"]["peng"])
             selected_books['rec'].append(books["gram"]["dest"]) 
             selected_books['rec'].append(books['math']['kaplan'])
             selected_books['rec'].append(books['math']['Mworkout'])
             selected_books['req'].append(books['math']['barronsM'])
             selected_books['req'].append(books['math']['pandaM'])
             selected_books['req'].append(books['math']['pandaM10'])
             temp = books["R&W"]["PR"]
             temp.category = "(Do Only Full Tests)" 
             selected_books['req'].append(temp)
             selected_books['rec'].append(books["R&W"]["RWW"])
             selected_books['req'].append(books["R&W"]["meltzerR"])
             selected_books['req'].append(books["R&W"]["barronsR"])
             selected_books['req'].append(books["R&W"]["pandaW"])
             selected_books['req'].append(books["R&W"]["iesR"])
             selected_books['req'].append(books["gram"]["meltzerG"])
             selected_books['req'].append(books['tests']['full8'])
             selected_books['req'].append(books['tests']['iesF'])
             selected_books['rec'].append(books['tests']['ivy4'])

        if english_level == "B2":
          remove(books["vocab"]["camvocab"])
        elif english_level == "B2+":
           remove(books["vocab"]["camvocab"])
           remove(books["vocab"]["504words"])
        elif english_level == "C1":
           remove(books["vocab"]["camvocab"])
           remove(books["vocab"]["504words"])
           recommend(books["vocab"]["1100words"]) 
           recommend(books["gram"]["blue"])
           recommend(books["vocab"]["400words"])
           recommend(books["vocab"]["601words"]) 
        elif english_level == "C1+" or english_level == "C2":
           remove(books["vocab"]["camvocab"])
           remove(books["vocab"]["504words"])
           remove(books["vocab"]["400words"])
           recommend(books["vocab"]["1100words"])
           recommend(books["vocab"]["601words"])
           recommend(books["gram"]["blue"])

        if math:
          if math >= 500 and math < 600:
               remove(books['math']['kaplan'])
          elif math >= 600 and math < 700:
               remove(books['math']['kaplan'])
               remove(books['math']['barronsM'])
          elif math >= 700 and math < 750:
               remove(books['math']['kaplan'])
               remove(books['math']['barronsM'])
               remove(books['math']['Mworkout'])
          elif math >= 750 and math < 790:
               remove(books['math']['kaplan'])
               remove(books['math']['barronsM'])
               remove(books['math']['Mworkout'])       
               remove(books['math']['pandaM'])
               recomend(books['math']['pandaM10'])
          elif math >= 790:
               remove(books['math']['kaplan'])
               remove(books['math']['barronsM'])
               remove(books['math']['Mworkout'])       
               remove(books['math']['pandaM'])
               remove(books['math']['pandaM10'])


        if english:
          if english >= 200 and english < 400:
               require(books["R&W"]["RWW"])
          elif english >= 400 and english < 500:
               pass
          elif english >= 500 and english < 600:
               temp = books["R&W"]["PR"]
               temp.category = "(Do Only Full Tests)" 
               remove(temp)
               recommend(temp)
               recommend(books["R&W"]["barronsR"])
          elif english >= 600 and english < 700:
               recommend(books["R&W"]["barronsR"])
               remove(books["R&W"]["RWW"])
          elif english >= 700 and english < 750:
               temp = books["R&W"]["PR"]
               temp.category = "(Do Only Full Tests)" 
               remove(temp)
               remove(books["R&W"]["RWW"])
               remove(books["R&W"]["barronsR"])
               recommend(books["gram"]["meltzerG"])
          elif english >= 750:
               temp = books["R&W"]["PR"]
               temp.category = "(Do Only Full Tests)" 
               remove(temp)
               remove(books["R&W"]["RWW"])
               recommend(books["R&W"]["meltzerR"])
               remove(books["R&W"]["barronsR"])
               require(books["R&W"]["pandaW"])
               remove(books["gram"]["meltzerG"])

          
          if english >= 700 and (english_level == "C1+" or english_level == "C2"):
               recommend(books["vocab"]["powervocab"]) 


     
        return selected_books

     
"""
English

200-400

           require(books["R&W"]["RWW"])
           require(books["R&W"]["pract500"]) 

400-500

           Nothing to delete or change

500-600

             recommend(books["R&W"]["PR"])
             recommend(books["R&W"]["barronsR"])
             
600-700
             selected_books['rec'].append(books["R&W"]["RWW"])
             recommend(books["R&W"]["barronsR"])
            





700-750
             selected_books['req'].append(books["R&W"]["PR"])
             selected_books['rec'].append(books["R&W"]["RWW"])
             selected_books['req'].append(books["R&W"]["barronsR"])
             recommend(books["gram"]["meltzerG"])
             selected_books['rec'].append(books["R&W"]["pract500"])



750-800

             selected_books['req'].append(books["R&W"]["PR"])
             selected_books['rec'].append(books["R&W"]["RWW"])
             recommend(books["R&W"]["meltzerR"])
             selected_books['req'].append(books["R&W"]["barronsR"])
             require(books["R&W"]["pandaW"])
             selected_books['req'].append(books["gram"]["meltzerG"])
             selected_books['rec'].append(books["R&W"]["pract500"])


Math Score

200-500 - nothing to delete


500-600 

selected_books['rec'].append(books['math']['kaplan'])
             
600-700
 selected_books['rec'].append(books['math']['kaplan'])
  selected_books['rec'].append(books['math']['barronsM'])
           
700-750 
  selected_books['rec'].append(books['math']['kaplan'])
             selected_books['rec'].append(books['math']['Mworkout'])
             selected_books['req'].append(books['math']['barronsM'])

750-800
selected_books['rec'].append(books['math']['kaplan'])
             selected_books['rec'].append(books['math']['Mworkout'])
             selected_books['req'].append(books['math']['barronsM'])
             selected_books['req'].append(books['math']['pandaM'])


           C1 rec books["vocab"]["1100words"] 
              rec books["gram"]["blue"]
              rec books["vocab"]["400words"] 
           C1  selected_books['req'].remove(books["vocab"]["camvocab"])
               selected_books['req'].remove(books["vocab"]["504words"])

          C1+/C2 rec books["vocab"]["1100words"]
                 rec books["gram"]["blue"] 

          C1+/C2 selected_books['req'].remove(books["vocab"]["camvocab"])
               selected_books['req'].remove(books["vocab"]["504words"])
               selected_books['req'].remove(books["vocab"]["400words"])
        
        if level == "B2":
           selected_books['req'].remove(books["vocab"]["camvocab"])
        elif level == "B2+":
           selected_books['req'].remove(books["vocab"]["camvocab"])
           selected_books['req'].remove(books["vocab"]["504words"])
        elif level == "C1":
           selected_books['req'].remove(books["vocab"]["camvocab"])
           selected_books['req'].remove(books["vocab"]["504words"])
           selected_books['req'].remove(books["vocab"]["504words"])
          """


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function




