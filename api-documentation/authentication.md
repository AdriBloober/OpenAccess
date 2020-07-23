# Authentication

{% api-method method="post" host="https://yourdomain.com/OpenAccess" path="/api/authentication/sessions" %}
{% api-method-summary %}
Login
{% endapi-method-summary %}

{% api-method-description %}
This endpoint allows you to get free cakes.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-body-parameters %}
{% api-method-parameter name="password" type="string" required=true %}
The password of the user.
{% endapi-method-parameter %}

{% api-method-parameter name="name" type="string" required=true %}
The name of the user.
{% endapi-method-parameter %}
{% endapi-method-body-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Login was successfully \(session will be returned\)
{% endapi-method-response-example-description %}

```
{
  "id": 0,
  "token": "string",
  "user": {
    "id": 0,
    "name": "string",
    "admin": false
  }
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=403 %}
{% api-method-response-example-description %}
InvalidCredentials
{% endapi-method-response-example-description %}

```
{
  "status": "error",
  "error": {
    "name": "invalid_credentials_error",
    "description": "The credentials to perform this authentication action are invalid."
  }
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% api-method method="get" host="https://yourdomain.com/OpenAccess" path="/api/authentication/sessions" %}
{% api-method-summary %}
Get a session
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="OpenAccessToken" type="string" required=true %}

{% endapi-method-parameter %}
{% endapi-method-headers %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
{
  "id": 0,
  "token": "string",
  "user": {
    "id": 0,
    "name": "string",
    "admin": false
  }
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=401 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
{
  "status": "error",
  "error": {
    "name": "invalid_session_error",
    "description": "The session is invalid or expired. You must reauthenticate you to perform this action with a new session."
  }
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}



{% api-method method="get" host="https://yourdomain.com/OpenAccess" path="/api/authentication/users" %}
{% api-method-summary %}
Get the user
{% endapi-method-summary %}

{% api-method-description %}

{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="OpenAccessToken" type="string" required=true %}

{% endapi-method-parameter %}
{% endapi-method-headers %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
{
    "id": 0,
    "name": "string",
    "admin": false
}
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=401 %}
{% api-method-response-example-description %}

{% endapi-method-response-example-description %}

```
{
  "status": "error",
  "error": {
    "name": "invalid_session_error",
    "description": "The session is invalid or expired. You must reauthenticate you to perform this action with a new session."
  }
}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

