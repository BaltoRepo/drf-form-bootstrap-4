# drf-form-bootstrap-4

Bootstrap 4 templates for [Django Rest Framework `render_form` tag](http://www.django-rest-framework.org/topics/html-and-forms/).

TODO:
* form errors
* add basic docs
* upload to pypi, add 'make upload'
* make PR to DRF docs

## Requirements

Tested with Django 2.0 and Python 3.6. Probably works in earlier versions.

## Installation

From PyPI:

```
todo
```

Add 'TODO' to your `INSTALLED_APPS` setting.

```
INSTALLED_APPS = (
    ...
    'todo',
)
```

## Usage

Like the template packs in Django Rest Framework, this supports three layouts:

##### Vertical

    <form method="POST" novalidate>
      {% csrf_token %}
      {% render_form serializer template_pack='drfformbootstrap4/vertical' %}
      <div class="row">
        <div class="col text-right">
          <input class="btn btn-primary" type="submit" value="Submit">
        </div>
      </div>
    </form>


##### Horizontal


    <form method="POST" novalidate>
      {% csrf_token %}
      {% render_form serializer template_pack='drfformbootstrap4/horizontal' %}
      <div class="row">
        <div class="col text-right">
          <input class="btn btn-primary" type="submit" value="Submit">
        </div>
      </div>
    </form>



##### Inline

Note that `inline` is less well-tested than the others, and at the moment the error states don't  render properly. If this is a problem for you, submit an issue (or even better, a pull request).

    <form method="POST" novalidate class="form-inline">
      {% csrf_token %}
      {% render_form serializer template_pack='drfformbootstrap4/inline' %}
      <div class="row">
        <div class="col text-right">
          <input class="btn btn-primary" type="submit" value="Submit">
        </div>
      </div>
    </form>

### Additional options

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

Pretty standard: for this repo, make changes, and make a GitHub pull request.

There are demo pages showing variety of form fields and layouts. Use it for development by running:

```
make runserver
```

## License

MIT

&copy; 2018 Matthew Fox
