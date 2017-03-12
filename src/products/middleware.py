class Middleware(object):
    def process_request(self, request):
        if 'cart_count' not in request.session:
        	request.session['cart_count'] = 0