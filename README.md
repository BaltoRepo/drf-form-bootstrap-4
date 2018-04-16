# drf-form-bootstrap-4

Bootstrap 4 templates for Django Rest Framework `render_form` tag. 

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

Fields with `read_only=True` are included in the form but shown with read-only styling.

To display a field as text instead of as a field:

```
style={'class': 'form-control-plaintext'}
```

For inline checkboxes and radio buttons:

```
style={'inline': True}
```

TODO: ensure all field types and style options from DRF are supported.

## Differences from DRF

* Fields with `read_only=True` are included in the form.

## Development

```
make test
```

## License

MIT

&copy; 2018 Matt Fox
