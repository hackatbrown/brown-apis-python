# Brown APIs in Python #
A Python package that makes using the various Brown APIs easier


## Example ##
    from client import Client

    brownAPIs = Client(<your-client-id>)
    print(brownAPIs.request('/wifi/count', location='ratty'))