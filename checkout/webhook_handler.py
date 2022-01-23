from django.http import HttpResponse

class stripeWH_Handler:
    """ Handle Stripe webhooks """

    def __innit__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """ Handle a generic, unknown, unexpected webhook event """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)