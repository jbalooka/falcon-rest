import falcon
from falconjsonio.middleware import JSONTranslator
from falconjsonio.middleware import RequireJSON
from .middleware.database import DatabaseRouter
from .persistence.models import create_db_tables
from .handlers.systems import TeamcenterSystemsHandler

def create():
    api = application = falcon.API(
        middleware = get_middleware_components()
    )
    create_db_tables()

    tc_systems_handler = TeamcenterSystemsHandler()
    api.add_route('/systems', tc_systems_handler)
    return api


def get_middleware_components():
    middleware = [
        RequireJSON(),
        JSONTranslator(),
        DatabaseRouter()
    ]

    return middleware

if __name__ == "__main__":
    create()