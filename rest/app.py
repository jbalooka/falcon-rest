import falcon
import falcon_jsonify
from .middleware.database import DatabaseRouter
from .middleware.falconjsoniopatch import JSONTranslator
from .middleware.falconjsoniopatch import RequireJSON
from .handlers.systems import TeamcenterSystemsHandler

def create():
    api = application = falcon.API(
        middleware=[
            RequireJSON(),
            JSONTranslator(),
            falcon_jsonify.Middleware(help_messages=True),
            DatabaseRouter(),
        ]
    )

    tc_systems_handler = TeamcenterSystemsHandler()
    api.add_route('/systems', tc_systems_handler)
    return api

if __name__ == "__main__":
    create()