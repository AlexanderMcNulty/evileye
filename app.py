from waitress import serve
from pyramid.view import view_config
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.renderers import render_to_response


@view_config(route_name='order')
def order(request):
    url = request.url
    name =  request.params.get('name', 'No Name Provided')
    body = 'URL %s with name: %s' % (url, name)
    return Response(
        content_type="text/html",
        body=body
    )

@view_config(route_name='index', renderer='index.jinja2')
def index_page(request):
    name =  request.params.get('name', 'No Name Provided')
    print('Incoming request')
    return {}




if __name__ == '__main__':
    with Configurator() as config:
        config.add_static_view('static', 'static', cache_max_age=3600)
        config.add_route('index', '/')
        config.add_route('order', '/order/')
        config.include('pyramid_jinja2')
        config.scan()
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=3002)
