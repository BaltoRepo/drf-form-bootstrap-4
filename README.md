# drf-form-bootstrap-4

Bootstrap 4 templates for Django Rest Framework `render_form` tag. 

TODO:
* error states
* ensure all field types in vertical have been updated
* ensure all field types and style options from DRF are supported.
* update horizontal, inline
* add basic docs
* upload to pypi, add 'make upload'
* make PR to DRF docs

## Requirements

TODO Django, DRF, Python versions

## Installation

From source:

```
todo git clone
cd ...
pip install --upgrade .
```

## Usage

TODO

To display a field as text instead of as a field:

```
style={'class': 'form-control-plaintext'}
```

For inline checkboxes and radio buttons:

```
style={'inline': True}
```

prepend/append text for inputs:

```
style={
    'prepend': 'prepend',
    'append': 'append',
}
```

## Development

Demo page showing variety of form fields and layouts is available with:

```
make runserver
```

Run tests:

```
make test
```

Make a GitHub pull request.

## License

MIT

&copy; 2018 Matt Fox
