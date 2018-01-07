import falcon
from falcon import testing
import pytest
import rest.app as server
import json


from rest.persistence.models import TeamcenterSystem

@pytest.fixture
def client():
    return testing.TestClient(server.create())


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_new_system_is_created(client):
    TeamcenterSystem.delete().where(TeamcenterSystem.system_name == 'TCAS030').execute()
    assert TeamcenterSystem.select().where(TeamcenterSystem.system_name == 'TCAS030').count() == 0
    
    response = client.simulate_request(method = 'POST', path = '/systems', 
        headers = {
            "Content-Type" : "application/json",
            "Charset" : "utf-8"
        },
        body = json.dumps(
            {
                "system_name" : "TCAS030"
            }).encode(encoding='utf_8')
    )

    assert response.status == falcon.HTTP_OK
    assert TeamcenterSystem.select().where(TeamcenterSystem.system_name == 'TCAS030').count() == 1