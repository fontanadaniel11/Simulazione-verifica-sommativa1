from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name='customers')

@app.route('/')
def home():
    return render_template('home.html')




@app.route('/es1')
def esercizio1():
    return render_template('es1.html')


@app.route('/calcolo1', methods=['POST'])
def calcolo1():
    nome=request.form["nm"]
    cognome=request.form["sn"]
    dataframe = df[(df['first_name'] == nome) & (df['last_name'] == cognome)].to_html()
    return render_template('risultati.html', table = dataframe)





@app.route('/es2')
def esercizio2():
    return render_template('es2.html')


@app.route('/calcolo2', methods=['POST'])
def calcolo2():
    citta=request.form["citta"]
    dataframe = df[df['city'] == citta].to_html()
    return render_template('risultati.html', table = dataframe)





@app.route('/es3') 
def esercizio3():
    clienti = df.groupby('state').count()[['customer_id']].reset_index().to_html()
    return render_template('es3.html', table = clienti)



@app.route('/es4') 
def esercizio4():
    dataframe = clienti[clienti['customer_id'] == clienti['customer_id'].max()].to_html()
    return render_template('es4.html', table = dataframe)
















if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)