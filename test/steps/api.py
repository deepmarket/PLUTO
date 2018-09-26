from src.api import Api

from behave import use_step_matcher, given, when, then, step
use_step_matcher("parse")


@given(r'the api is running')
def api_is_up(context):
    domain = Api().domain
    port = Api().port

    from requests import get
    status_request = str(get(f"http://{domain}:{port}/api/v1/").text.encode('utf-8')).lower()

    assert all([bool(txt) for txt in ['api', 'is', 'online'] if txt in str(status_request)])


@when(u'we send a "{request_type}" request to "{endpoint}"')
@when(u'we send a "{request_type}" request to "{endpoint}" with "{payload}"')
def step_impl(context, request_type, endpoint, payload=None):  # -- NOTE: number is converted into integer
    with Api(endpoint) as api:
        # request_type = request_type.uppper()
        if request_type == 'GET':
            api.get()
        elif request_type == "POST":
            api.post(payload)
        elif request_type == "PUT":
            api.put(payload)
        elif request_type == "DELETE":
            api.delete()


@then(u'a "{request_type}" request to "{endpoint}" should reply with a status of {status:d}')
@then(u'a "{request_type}" request to "{endpoint}" should reply with a status of {status:w}')
def step_impl(context, request_type, endpoint, status):
    with Api(endpoint) as api:
        # request_type = request_type.uppper()
        if request_type == 'GET':
            res, api_status = api.get()
        # elif request_type == "POST":
        #     api.post(payload)
        # elif request_type == "PUT":
        #     api.put(payload)
        # elif request_type == "DELETE":
        #     api.delete()

            assert api_status == status, f"{api_status} != {status}"
