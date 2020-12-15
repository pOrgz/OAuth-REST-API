<div align = "center">

<img src = "./assets/logo.png" height = "128" width = "128" />
<h1 align = "center">OAuth REST API</h1><br>

<a href="https://github.com/pOrgz/OAuth-REST-API/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/pOrgz/OAuth-REST-API?style=plastic"></a>
<a href="https://github.com/pOrgz/OAuth-REST-API/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/pOrgz/OAuth-REST-API?style=plastic"></a>

</div>

<p align = "justify"><b>REST API</b> built on <i>Python 3.6</i> for managing user informations and sessions for the <b>pOrgz</b> main applictation. This REST-API design exposes login session information via an internal (localhost) session on a desired PORT. <b>TODO Documentations -- gist</b>. This API is taken from <i>template</i> (available at <a href="https://github.com/dPramanik7/rest-api-template">GitHub</a>).</p>

## Setup

<p align = "justify"><b>pOrgz</b> application is built using <i>flask</i> which is a <q>micro web framework</q>. By <b>default</b>, the application runs at <code>PORT = 5000</code>, and for this application specific task it is running on <code>localhost</code>. To change the default desitnation, you will need to set the <code>PORT</code> and <code>HOST</code>.</p>

## API Return JSON

<p align = "justify">All type of Authentication API will follow a general structure, which is summarized as below. For other API (if required), like getting list of all users, session information, they will be build and modified as required.</p>

```json
{
    "status" : {
        "type"    : "<str>  JSON Message Type : Generally a String Representing the APIs [`login` or `signup`]",
        "message" : "<str>  Message Body",
        "code"    : 200,
        "error"   : "<bool> `True` : Compilation or Programming Error Message, if Received; else `False`"
    },
    "data" : {
        "status" : "<str> Main Message - which is either `success` or `failed`, representing login/signup",
        "user"   : {
            "user-id"  : "<str> User ID Associated (a new ID on registration or an existing ID on login)",
            "username" : "<str> Username, as provided during Login",
            "email"    : "<str> Email Address - from DB (optional)",
            "fullname" : "<str> Full Name of the Login Person (as per Requirement)"
        },
        "remarks" : "<str> Reason if `status` = `failed` else `None`"
    },
    "time" : "<str> Time on which Login/Signup is Requested"
}
```
