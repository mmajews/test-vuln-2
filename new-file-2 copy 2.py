from flask import request
print 'test-test-test'
print 'new-test'
print 'test'
print 'test-2'

@app.route('/')
def index0():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\

@app.route('/')
def index():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\
    
@app.route('/')
def index2():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\
    
@app.route('/')
def index3():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\


@app.route('/')
def index4():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\

@app.route('/')
def index5():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\

@app.route('/')
def index6():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\

@app.route('/')
def index7():
    module = request.args.get("module")
    exec("import urllib%s as urllib" % module) # Noncompliant\

@app.route('/')
def index8():
    from OpenSSL import SSL
    SSL.Context(SSL.SSLv3_METHOD)  # Noncompliant   