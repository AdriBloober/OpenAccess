---
description: How to configure the OpenAccess server.
---

# Configuration

The OpenAccess config file named _config.yml_ configures the database connection, authentication configuration, and HTTP configuration.

{% hint style="info" %}
If the file does not exist, run the **run.py** and break up the process. The config.yml will be generated.
{% endhint %}

```text
AUTHENTICATION:
  HASHING_MODE: sha256 # the hash mode for the user password.
  SALT_GENERATING_CONFIG: # every user password would be salted with a individual salt.
    CHARSET: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
    LENGTH: 30
  TOKEN_GENERATING_CONFIG: # generating config for password link tokens and session tokens.
    CHARSET: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
    LENGTH: 35 # LENGTH * 2 is the length for the password link.
DEPLOYING_VERSION: '0.1'
HTTP:
  DATABASE:
    ADDITIONAL_URI: '' # if you need to additional something to the uri e.g a charset: https://docs.sqlalchemy.org/en/13/core/engines.html
    DB: access # the name of the database
    HOST: localhost # the host of the database
    PASSWORD: access # the password for the database user
    PORT: 3306 # the port of the database
    TYPE: mysql+pymysql # Look here for all database types: https://docs.sqlalchemy.org/en/13/core/engines.html
    USER: access # the user of the database
  DEBUG: false # leave it false
  ERROR_INCLUDE_MESSAGE: false # if you need a empty "message" variable in error json output
  FLASK_ENVIRONMENT: production # use production or development
  PROPAGATE_EXCEPTIONS: false 
  SQLALCHEMY_TRACK_MODIFICATIONS: true
  TESTING: false

```

You can also set up the config with environment variables: The name of the environment variable is the path to the variable joined with '\_'. For example the database port: HTTP\_DATABASE\_PORT or the token generating length: AUTHENTICATION\_TOKEN\_GENERATING\_CONFIG\_LENGTH.

