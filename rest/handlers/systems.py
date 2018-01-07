import falcon
from falconjsonio.schema import request_schema, response_schema
from ..persistence.models import TeamcenterSystem


system_post_request_schema = {
    'type':       'object',
    'properties': {
        'system_name':  {'type': 'string'}
    },
    'required': ['system_name']
}

class TeamcenterSystemsHandler(object):
    @request_schema(system_post_request_schema)
    def on_post(self, req, resp):
        TeamcenterSystem.create(**req.context['doc'])
        resp.status = falcon.HTTP_OK
