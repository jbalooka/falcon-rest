import falcon
from falcon import testing
import pytest
import rest.app as server
import json


@pytest.fixture
def client():
    return testing.TestClient(server.create())


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_new_system_is_created(client):
    req_body = json.dumps(
            {
                "system_name": "TCAS030"
            }
    ).encode(encoding='utf_8')
    
    response = client.simulate_request(method = 'POST', path = '/systems', 
        headers = {
            "Content-Type" : "application/json",
            "Content-Length" : str(len(req_body)),
        },
        body = req_body
    )
    print(response.json)
    assert response.status == falcon.HTTP_OK