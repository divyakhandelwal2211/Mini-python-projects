from flask  import Flask , render_template, request
# render template : A function to render HTML template
# request : is used to handle http request

import pickle
import numpy as np
# # pickle : is used to load the saved model

model = pickle.load(open('spamclassifier_mnb.pkl','rb'))
vectorizer = pickle.load(open('vectorizer.pkl','rb'))

app = Flask(__name__)

@app.route("/",methods = ['GET','POST'])     
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    try:
        if request.method == 'POST':
            messg = str(request.form['mesg'])
            transformed = vectorizer.transform([messg])
            transformed_data = transformed.toarray() # type: ignore
            pred = model.predict(transformed_data)
            output = str(pred[0])
            return render_template('result.html',prediction=f"{output}")
    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)