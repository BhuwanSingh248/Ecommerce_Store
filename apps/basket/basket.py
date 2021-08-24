

class Basket():
    '''
        base basket class for default behaviour 
    ''' 

    def __init__(self, request) -> None:
        self.session = request.session
        basket = self.session.get('session_key')  # creating cookie with session key
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {}
        self.basket = basket

        
    def add(self, product, qty):
        product_id = product.id
        if product_id not in self.basket:
            self.basket[product_id] = {
                'price': float(product.price),
                'qty' : int(qty)
            }
        self.session.modified = True
        
    def __len__(self):
        '''
            get the basket data and item qty
            @ return 
            all item 
        '''
        return sum(item['qty'] for item in self.basket.values())

    