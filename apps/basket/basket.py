

class Basket():
    '''
        base basket class for default behaviour 
    ''' 

    def __init__(self, request) -> None:
        self.session = request.session
        basket = self.session.get('session_key')  # creating cookie with session key
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {'number':120913137912}
        self.basket = basket

        