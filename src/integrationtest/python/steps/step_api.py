from api import Api

from behave import use_step_matcher, given, when, then, step
use_step_matcher("parse")


@given(r'the api is up')
def api_is_up(context):

    api = Api()
    domain, port = api.host, api.port

    # domain = Api().domain
    # port = Api().port

    from requests import get

    try:
        status_request = str(get(f"http://{domain}:{port}/api/v1/").text.encode('utf-8')).lower()
    except (ConnectionError, ConnectionRefusedError):
        assert False, "The api is not online"
    else:
        # Quasi check for server status
        assert all([bool(txt) for txt in ['api', 'is', 'online'] if txt in str(status_request)]), f"The api is not up"


@when(u'I send a "{request_type}" request to "{endpoint}"')
@when(u'I send a "{request_type}" request to "{endpoint}" with "{payload}"')
def api_request_to(context, request_type, endpoint, payload=None):  # -- NOTE: number is converted into integer
    with Api(endpoint) as api:
        # request_type = request_type.uppper()
        if request_type == "GET":
            context.res, context.api_status = api.get()
        elif request_type == "POST":
            context.res, context.api_status = api.post(payload)
        elif request_type == "PUT":
            api.put(payload)
        elif request_type == "DELETE":
            context.res, context.api_status = api.delete()


@then(u'the request should reply with a status of {status:d}')
@then(u'the request should reply with a status of {status:w}')
def verify_api_request_to(context, status):

    status = status if type(status) == str and status is None else None

    assert context.api_status == status, f"{context.api_status} != {status}"


# @then(r'the request should reply with a status of (\d{3})')
# @then(r'the request should reply with a status of (\w+)')
# def verify_api_request_to(context, status):
#     pass
