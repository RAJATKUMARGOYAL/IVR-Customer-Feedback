from flask import Flask, url_for, request
from tiniyo.voice_response import VoiceResponse
from xmlhelp import tiniyoml
from config import *

app = Flask(__name__)


@app.route('/ivrfeedback/tiniyo', methods=['GET', 'POST'])
def lan():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('menu1', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say(message="Hello, We are representing from Tiniyo." +
                      "Please update your language." +
                      "Press 1 for English." +
                      "Press 2 for French." +
                      "Press 3 for Spanish."
                      "To repeat Press 0.", loop=3)
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu', methods=['POST'])
def menu1():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_lan_eng",
                      '2': "_lan_french",
                      '3': "_lan_spanish",
                      '0': "_repeat0"}

    if int(selected_options) == 1:
        response = feedback()
        return response
    elif int(selected_options) == 2:
        response = feedback_2()
        return response
    elif int(selected_options) == 3:
        response = feedback_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat0()
        return response
    else:
        return _redirect_welcome()


def _repeat0():
    response = VoiceResponse()
    response.redirect(url_for('lan', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu1/welcome', methods=['GET', 'POST'])
def feedback():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('menu1_1', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say(message="Hello, We are representing from Tiniyo." +
                      "Would you be happy to take part in quick survey?" +
                      "Press 1 for Give us your valuable feedback." +
                      "Press any key for Call Hangup.", loop=3, voice=male, language=uk)
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu1/feed_menu', methods=['POST'])
def menu1_1():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "cus_feed",
                      '0': "hangup"}

    if int(selected_options) == 1:
        response = cus_feed()
        return response
    else:
        return _redirect_welcome()


def _redirect_welcome():
    response = VoiceResponse()
    response.say(message="Thank you for give us your valuable time." +
                         "Your Feedback is important to us.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr-feedback/lan_menu1/feed_menu1/option1', methods=['GET', 'POST'])
def cus_feed():
    response = VoiceResponse()
    with response.gather(
            num_digits=2, action=url_for('menu1_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say(message="Excellent, Now you are on customer satisfaction survey." +
                      "On Scale of 1 to 10, Where 1 is poor, 5 is Average and 10 is Excellent." +
                      "How satisfied are you with our executive?", loop=3, voice=male, language=uk)
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu1/option1/option1', methods=['POST'])
def menu1_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1-10': "feedback_1",
                      'else': "repeat"}

    if int(selected_options) == 1:
        response = feed_1()
        return response
    elif int(selected_options) == 2:
        response = feed_1()
        return response
    elif int(selected_options) == 3:
        response = feed_1()
        return response
    elif int(selected_options) == 4:
        response = feed_1()
        return response
    elif int(selected_options) == 5:
        response = feed_1()
        return response
    elif int(selected_options) == 6:
        response = feed_1()
        return response
    elif int(selected_options) == 7:
        response = feed_1()
        return response
    elif int(selected_options) == 8:
        response = feed_1()
        return response
    elif int(selected_options) == 9:
        response = feed_1()
        return response
    elif int(selected_options) == 10:
        response = feed_1()
        return response
    else:
        return _redirect_feed_1()


def _redirect_feed_1():
    response = VoiceResponse()
    response.say(message="You enter incorrect key." +
                         "Please try again." +
                         "Your Feedback is important to us.", voice=female, language=uk)
    response.redirect(url_for('cus_feed', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu1/feed_menu1/option2', methods=['GET', 'POST'])
def feed_1():
    response = VoiceResponse()
    with response.gather(
            num_digits=2, action=url_for('menu1_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say(message="Thank you!" +
                      "We have got your input." +
                      "Is your problem solved?" +
                      "If yes, press 1." +
                      "If No, Press 2.", loop=3, voice=male, language=uk)
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu1/option1/option2', methods=['POST'])
def menu1_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "yes",
                      '2': "no"}

    if int(selected_options) == 1:
        response = feed_2()
        return response
    elif int(selected_options) == 2:
        response = feed_2()
        return response
    else:
        return _redirect_feed_2()


def _redirect_feed_2():
    response = VoiceResponse()
    response.say("You enter incorrect key." +
                 "Please try again." +
                 "Your Feedback is important to us.", voice=female, language=uk)
    response.redirect(url_for('feed_1', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu1/feed_menu1/option3', methods=['GET', 'POST'])
def feed_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=2, action=url_for('menu1_4', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say(message="Thank you!" +
                      "We have got your input." +
                      "How satisfied are you with our application?" +
                      "On Scale of 1 to 5, Where 1 is low rating and 5 is high rating.",
              loop=3, voice=male, language=uk)
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu1/option1/option3', methods=['POST'])
def menu1_4():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "low",
                      '5': "high"}

    if int(selected_options) == 1:
        response = feed_3()
        return response
    elif int(selected_options) == 2:
        response = feed_3()
        return response
    elif int(selected_options) == 3:
        response = feed_3()
        return response
    elif int(selected_options) == 4:
        response = feed_3()
        return response
    elif int(selected_options) == 5:
        response = feed_3()
        return response
    else:
        return _redirect_feed_3()


def _redirect_feed_3():
    response = VoiceResponse()
    response.say(message="You enter incorrect key." +
                         "Please try again." +
                         "Your Feedback is important to us.", voice=female, language=uk)
    response.redirect(url_for('feed_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu1/feed_menu1/option4', methods=['GET', 'POST'])
def feed_3():
    response = VoiceResponse()
    response.say(message="Thank you!" +
                         "We have got your input." +
                         "Thank you for give us your valuable time and feedback.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu2/welcome', methods=['GET', 'POST'])
def feedback_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('menu1_1_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say(message="Bonjour, Nous repr??sentons de Tiniyo." +
                      "Seriez-vous heureux de r??pondre ?? un sondage rapide?" +
                      "Appuyez sur 1 pour nous faire part de vos pr??cieux commentaires." +
                      "Appuyez sur n'importe quelle touche pour Raccrocher.", loop=3, voice=male, language=france)
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu2/feed_menu', methods=['POST'])
def menu1_1_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "cus_feed",
                      '0': "hangup"}

    if int(selected_options) == 1:
        response = cus_feed_2()
        return response
    else:
        return _redirect_welcome_2()


def _redirect_welcome_2():
    response = VoiceResponse()
    response.say(message="Merci de nous donner votre temps pr??cieux." +
                         "Votre avis est important pour nous.", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu2/feed_menu1/option1', methods=['GET', 'POST'])
def cus_feed_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=2, action=url_for('menu1_2_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say(message="Excellent, vous participez maintenant ?? l'enqu??te de satisfaction client." +
                      "Sur une ??chelle de 1 ?? 10, o?? 1 est m??diocre, 5 est moyen et 10 est excellent." +
                      "??tes-vous satisfait de notre ex??cutif?", loop=3, voice=male, language=france)
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu2/option1/option1', methods=['POST'])
def menu1_2_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1-10': "feedback_1",
                      'else': "repeat"}

    if int(selected_options) == 1:
        response = feed_1_2()
        return response
    elif int(selected_options) == 2:
        response = feed_1_2()
        return response
    elif int(selected_options) == 3:
        response = feed_1_2()
        return response
    elif int(selected_options) == 4:
        response = feed_1_2()
        return response
    elif int(selected_options) == 5:
        response = feed_1_2()
        return response
    elif int(selected_options) == 6:
        response = feed_1_2()
        return response
    elif int(selected_options) == 7:
        response = feed_1_2()
        return response
    elif int(selected_options) == 8:
        response = feed_1_2()
        return response
    elif int(selected_options) == 9:
        response = feed_1_2()
        return response
    elif int(selected_options) == 10:
        response = feed_1_2()
        return response
    else:
        return _redirect_feed_1_2()


def _redirect_feed_1_2():
    response = VoiceResponse()
    response.say(message="Vous entrez une cl?? incorrecte." +
                         "Veuillez r??essayer." +
                         "Votre avis est important pour nous.", voice=female, language=france)
    response.redirect(url_for('cus_feed_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu2/feed_menu1/option2', methods=['GET', 'POST'])
def feed_1_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=2, action=url_for('menu1_3_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say(message="Merci!" +
                      "Nous avons votre avis." +
                      "Votre probl??me est-il r??solu ?" +
                      "Si oui, appuyez sur 1." +
                      "Si non, appuyez sur 2.", loop=3, voice=male, language=france)
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu2/option1/option2', methods=['POST'])
def menu1_3_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "yes",
                      '2': "no"}

    if int(selected_options) == 1:
        response = feed_2_2()
        return response
    elif int(selected_options) == 2:
        response = feed_2_2()
        return response
    else:
        return _redirect_feed_2_2()


def _redirect_feed_2_2():
    response = VoiceResponse()
    response.say(message="Vous entrez une cl?? incorrecte." +
                         "Veuillez r??essayer." +
                         "Votre avis est important pour nous.", voice=female, language=france)
    response.redirect(url_for('feed_1_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu2/feed_menu1/option3', methods=['GET', 'POST'])
def feed_2_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=2, action=url_for('menu1_4_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say(message="Merci!" +
                      "Nous avons votre avis." +
                      "??tes-vous satisfait de votre candidature?" +
                      "Sur une ??chelle de 1 ?? 5, o?? 1 correspond ?? une note faible et 5 ?? une note ??lev??e.",
              loop=3, voice=male, language=france)
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu2/option1/option3', methods=['POST'])
def menu1_4_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "low",
                      '5': "high"}

    if int(selected_options) == 1:
        response = feed_3_2()
        return response
    elif int(selected_options) == 2:
        response = feed_3_2()
        return response
    elif int(selected_options) == 3:
        response = feed_3_2()
        return response
    elif int(selected_options) == 4:
        response = feed_3_2()
        return response
    elif int(selected_options) == 5:
        response = feed_3_2()
        return response
    else:
        return _redirect_feed_3_2()


def _redirect_feed_3_2():
    response = VoiceResponse()
    response.say(message="Vous entrez une cl?? incorrecte." +
                         "Veuillez r??essayer." +
                         "Votre avis est important pour nous.", voice=female, language=france)
    response.redirect(url_for('feed_2_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu2/feed_menu1/option4', methods=['GET', 'POST'])
def feed_3_2():
    response = VoiceResponse()
    response.say(message="Merci!" +
                         "Nous avons votre avis." +
                         "Merci de nous avoir accord?? votre temps pr??cieux et vos commentaires.",
                 voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu3/welcome', methods=['GET', 'POST'])
def feedback_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('menu1_1_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say(message="Hola, somos representantes de Tiniyo." +
                      "??Estar??a encantada de hacer una encuesta r??pida?" +
                      "Presione 1 para darnos sus valiosos comentarios." +
                      "Presione cualquier tecla para colgar la llamada.", loop=3, voice=male, language=spaines)
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu3/feed_menu', methods=['POST'])
def menu1_1_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "cus_feed",
                      '0': "hangup"}

    if int(selected_options) == 1:
        response = cus_feed_3()
        return response
    else:
        return _redirect_welcome_3()


def _redirect_welcome_3():
    response = VoiceResponse()
    response.say(message="Gracias por brindarnos su valioso tiempo." +
                         "Tu opini??n es importante para nosotros.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu3/feed_menu1/option1', methods=['GET', 'POST'])
def cus_feed_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=2, action=url_for('menu1_2_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say(message="Excelente, ahora est?? en la encuesta de satisfacci??n del cliente." +
                      "En la escala del 1 al 10, donde 1 es pobre, 5 es promedio y 10 es excelente." +
                      "??Qu?? tan satisfecha est??s con nuestra ejecutiva?", loop=3, voice=male, language=spaines)
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu3/option1/option1', methods=['POST'])
def menu1_2_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1-10': "feedback_1",
                      'else': "repeat"}

    if int(selected_options) == 1:
        response = feed_1_3()
        return response
    elif int(selected_options) == 2:
        response = feed_1_3()
        return response
    elif int(selected_options) == 3:
        response = feed_1_3()
        return response
    elif int(selected_options) == 4:
        response = feed_1_3()
        return response
    elif int(selected_options) == 5:
        response = feed_1_3()
        return response
    elif int(selected_options) == 6:
        response = feed_1_3()
        return response
    elif int(selected_options) == 7:
        response = feed_1_3()
        return response
    elif int(selected_options) == 8:
        response = feed_1_3()
        return response
    elif int(selected_options) == 9:
        response = feed_1_3()
        return response
    elif int(selected_options) == 10:
        response = feed_1_3()
        return response
    else:
        return _redirect_feed_1_3()


def _redirect_feed_1_3():
    response = VoiceResponse()
    response.say(message="Ingresa una clave incorrecta." +
                         "Int??ntalo de nuevo." +
                         "Tu opini??n es importante para nosotros.", voice=female, language=spaines)
    response.redirect(url_for('cus_feed_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu3/feed_menu1/option2', methods=['GET', 'POST'])
def feed_1_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=2, action=url_for('menu1_3_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say(message="??Gracias!" +
                      "Tenemos su opini??n." +
                      "??Tu problema est?? resuelto?" +
                      "Si es as??, presione 1." +
                      "Si la respuesta es No, presione 2.", loop=3, voice=male, language=spaines)
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu3/option1/option2', methods=['POST'])
def menu1_3_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "yes",
                      '2': "no"}

    if int(selected_options) == 1:
        response = feed_2_3()
        return response
    elif int(selected_options) == 2:
        response = feed_2_3()
        return response
    else:
        return _redirect_feed_2_3()


def _redirect_feed_2_3():
    response = VoiceResponse()
    response.say(message="Ingresa una clave incorrecta." +
                         "Int??ntalo de nuevo." +
                         "Tu opini??n es importante para nosotros.", voice=female, language=spaines)
    response.redirect(url_for('feed_1_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu3/feed_menu1/option3', methods=['GET', 'POST'])
def feed_2_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=2, action=url_for('menu1_4_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say(message="??Gracias!" +
                      "Tenemos su opini??n." +
                      "??Qu?? tan satisfecho est?? con nuestra aplicaci??n?" +
                      "En la escala del 1 al 5, donde 1 es calificaci??n baja y 5 es calificaci??n alta.",
              loop=3, voice=male, language=spaines)
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu3/option1/option3', methods=['POST'])
def menu1_4_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "low",
                      '5': "high"}

    if int(selected_options) == 1:
        response = feed_3_3()
        return response
    elif int(selected_options) == 2:
        response = feed_3_3()
        return response
    elif int(selected_options) == 3:
        response = feed_3_3()
        return response
    elif int(selected_options) == 4:
        response = feed_3_3()
        return response
    elif int(selected_options) == 5:
        response = feed_3_3()
        return response
    else:
        return _redirect_feed_3_3()


def _redirect_feed_3_3():
    response = VoiceResponse()
    response.say(message="Ingresa una clave incorrecta." +
                         "Int??ntalo de nuevo." +
                         "Tu opini??n es importante para nosotros.", voice=female, language=spaines)
    response.redirect(url_for('feed_2_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivrfeedback/lan_menu3/feed_menu1/option4', methods=['GET', 'POST'])
def feed_3_3():
    response = VoiceResponse()
    response.say(message="??Gracias!" +
                         "Tenemos su opini??n." +
                         "Gracias por brindarnos su valioso tiempo y comentarios.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


if __name__ == '__main__':
    app.run()
