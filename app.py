import requests
from flask import*

api_key="SUA CHAVE DE ACESSO AQUI"
endpoint="https://api.openai.com/v1/completions"



app = Flask(__name__,template_folder="template")

@app.route("/home", methods=['GET', 'POST'])
def pesquisa():

    if request.method =='POST':
        busca = request.form['busca']

        
        model = "text-davinci-003"

        data={
            "prompt": busca,
            "model":model,
            "max_tokens":1000
        }

        response= requests.post(endpoint, json=data, headers={
            "Content-Type":"application/json",
            "Authorization":f"Bearer {api_key}"
        })

        res = response.json()
        texto = res['choices'][0]['text']

        print(texto)

        return render_template("home.html", busca = busca, texto=texto)


    return render_template("home.html")
    

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")
