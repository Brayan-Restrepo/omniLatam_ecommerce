import time
import threading
from django.utils.deprecation import MiddlewareMixin



_thread_locals = threading.local()

def current_request():
    '''Retorna el request'''
    
    return _thread_locals


class GlobalCurrentRequestMiddleware(MiddlewareMixin):
    '''Coloca el request en el hilo local'''
    
    def process_request(self, request):
        _thread_locals.current_request = request
        request.start_time = time.time()

 
    def process_response(self, request, response):
        """
        Se termina el procesamiento de la app.
        """

        return response