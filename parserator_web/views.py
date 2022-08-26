import usaddress
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import ParseError


class Home(TemplateView):
    template_name = 'parserator_web/index.html'


class AddressParse(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        # TODO: Flesh out this method to parse an address string using the
        # parse() method and return the parsed components to the frontend.
        address_request = request.query_params.get('address')
        parsed_request = AddressParse.parse(self, address_request)

        # Implement error handling for bad address string!

        return Response({'requested_address': address_request,
                         'address_parts': parsed_request[0], 'address_type': parsed_request[1]})

    def parse(self, address):
        # TODO: Implement this method to return the parsed components of a
        # given address using usaddress: https://github.com/datamade/usaddress
        parsed_address = usaddress.tag(address)
        address_components = parsed_address[0]
        address_type = parsed_address[1]
        return address_components, address_type
