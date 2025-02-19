import wtforms

from wtforms import validators


class ExampleForm(wtforms.Form):
    field = wtforms.TextField(
        "field",
        [
            validators.InputRequired(),
        ],
    )
