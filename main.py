from dataclasses import dataclass
from pydoc import pager
from website import create_app

app = create_app()

if __name__ == '__main__':  # only if we run this file not just import does it run
    app.run(debug=True)



