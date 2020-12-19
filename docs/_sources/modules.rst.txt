REST API
========

**OAuth REST API** is a high-level interface designed for user authentication and security for `pOrgz <https://github.com/pOrgz/pOrgz-py>`_. Built using *flask*, which is a "micro web framework", and can be compiled with python 3.6+ (as it uses the *f-string conventions*).

This module follows a typical REST-API design, consisting of three *submodules*:

- **Controller**: which takes care of mapping request data to the defined request handler method [1],
- **Models**: which provides entities to represent interactions with REST resources [2], and
- **Resources**: which fetches data from the underline database.

.. toctree::
   :maxdepth: 4

   app

**References**
    [1] `Spring Resource Controller <https://www.journaldev.com/21536/spring-restcontroller>`_ - JournalDev

    [2] `REST Model <https://www.ibm.com/support/knowledgecenter/en/SSWLGF_8.5.5/com.ibm.sr.doc/rwsr_rest_model.html>`_ - - IBM Knowledge Center
