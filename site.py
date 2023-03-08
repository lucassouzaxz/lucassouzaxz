from flask import Flask

app = Flask(__name__)

# route -> página inicial do seu site
# função -> exibição da página

@app.route("/")
def homepage():
    return ("oi amor feliz dia das mulheres vc é a melhor namorada do mundo eu te amo muito muito infinito meu pinguinho de gente")


@app.route("/lembranças")
def lembranças():
    return "Vim por meio desta falar que eu te amo. Eu te amo porque você é uma pessoa espetacular e o melhor presente que o destino poderia me dar, eu te amo porque diariamente você me dá mil e um motivos para continuar, eu te amo por me fazer uma pessoa mais feliz só de saber que você tá por perto. Coloquei esse ponto só pro texto ficar mais bonito, sei que você gosta de textos bem escritos, sei disso porque te amo. Não existe uma quantidade de palavras para representar o quanto eu te amo, apesar de sempre resumir nessas 3 todo santo dia, eu quero sempre demonstrar meu amor de todas as formas possíveis para pessoa que me ama, assim como eu te amo. Por mais que nós passemos por momentos confusos ou atípicos, eu nunca vou deixar de te amar não importa o que aconteça. Eu insisto em dizer que eu te amo o máximo de vezes que posso nesse texto lotado de repetições e nada apropriado, para demonstrar que não são 15 vezes a mais ou a menos que determinam algo, e sim nossas atitudes na nossa relação, então repetindo novamente - pleonasmo -, eu te amo. Me conhece tão bem que já sabe que nesse ponto do texto eu já fiquei sem ideias do que escrever além de dizer eu te amo, a propósito, eu te amo. Ademais, quero que você fique pra sempre na minha vida, assim como eu desejo ficar na sua, para poder escrever mais textos como esse, para ter mais tempo e para demonstrar quanto amor tenho por você, ᴇᴜ ᴛᴇ ᴀᴍᴏ. Já não faço ideia do que escrever e estou com muita, muita saudade mesmo de conversar com você, já foram mais de 10 minutos escrevendo esse texto, lotados de eu te amo, que ainda não consegue demonstrar o tanto de amor que tenho, só falta um né? A partir daqui é tudo novo, eu escrevi isso em 2021 e queria dizer que nada mudou para mim. Sempre pensei e continuarei pensando desse jeito, o nosso amor é de outras vidas, é algo reservado para ser especial não importa o que aconteça."

if __name__ == "__main__":
   app.run(debug=True)
