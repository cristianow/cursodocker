from bottle import route, run, request

@route('/', method='POST')
def send():
    assunto   = request.forms.get('assunto')
    mensangem = request.forms.get('mensangem')

    return 'Mensagem enfileirada ! Assunto: {} Mensagem: {}'.format(
            assunto, mensagem
        )


    if __name__ == '__main__':
        run(host='0.0.0.0', port=8080, debug=True)