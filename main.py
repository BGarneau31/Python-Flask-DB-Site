from dataclasses import dataclass
from pydoc import pager
from website import create_app

app = create_app()

if __name__ == '__main__':  # only if we run this file not just import does it run
    app.run(debug=True)


# TODO add new column to workout class -- DATE, just like notes, it stores times to database and can use that for future calender

# TODO: figure out how to save last inputs after 'add exercise' button is pressed, so you can just press that button 3 times to log 3 sets

# TODO: figure out how to save last inputs after 'add exercise' button is pressed, so you can just press that button 3 times to log 3 sets
    # option 1 = add new pages for each date and have way to access previous dates data
    # option 2 = add multiple workouts per page -- prob gets too long and hard to navigate after 1 week but could be used to create workout templates and do sepecifc days on another page
    # option 3 = create tables to add full workouts/exercise multisets somehow and do something like that

    # with option 1: create routes that take code to go to specific day with that days data (day data found in workout class)

# TODO: figure out dumb pyton variable in JS onclick in html home/workout files
