def t_e_s_t_root(test_object):
    test_object.testapp.get("/", status=200)
    test_object.testapp.get("/refresh", status=200)
    test_object.testapp.get("/login", status=200)
    test_object.testapp.get("/join", status=200)
    test_object.testapp.get("/recover", status=200)
    test_object.testapp.get("/not_found", status=404)
    test_object.testapp.get("/gravatar?name=Carlos", status=200)
