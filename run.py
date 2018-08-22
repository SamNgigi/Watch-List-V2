#!/usr/bin/env python
from app import app

if __name__ == '__main__':
    """ 
    app.run(debug=True)

    We can now remove the debug=True from our app.run() because we
    have added the debug setting to the DevConfig settings of our
    app. 
    """
    app.run()
