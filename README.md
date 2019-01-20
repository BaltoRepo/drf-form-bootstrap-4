# drf-form-bootstrap-4

[![PyPI version](https://badge.fury.io/py/drf-form-bootstrap-4.svg)](https://badge.fury.io/py/drf-form-bootstrap-4) [![Build Status](https://travis-ci.org/mattfox/drf-form-bootstrap-4.svg?branch=master)](https://travis-ci.org/mattfox/drf-form-bootstrap-4)

Bootstrap 4 templates for [Django REST Framework `render_form` tag](http://www.django-rest-framework.org/topics/html-and-forms/).

## Requirements

Tested with Django 2.0, DRF 3.8, Python 3.6. Almost certainly works in earlier versions.

## Installation

From PyPI:

```
pip install drf-form-bootstrap-4
```

Add `drfformbootstrap4` to your `INSTALLED_APPS` setting.

```
INSTALLED_APPS = (
    ...
    'drfformbootstrap4',
)
```

## Usage

Like the template packs in Django REST Framework, this supports three layouts:

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

Note that `inline` is less well-tested than the others, and at the moment the error states don't  render properly. If this is a problem for you, [add a comment to this issue](https://github.com/mattfox/drf-form-bootstrap-4/issues/2).

    <form method="POST" novalidate class="form-inline">
      {% csrf_token %}
      {% render_form serializer template_pack='drfformbootstrap4/inline' %}
      <div class="row">
        <div class="col text-right">
          <input class="btn btn-primary" type="submit" value="Submit">
        </div>
      </div>
    </form>

### Additional Options

Use the `style` field on your serializer to change the appearance of a field.

To display a field as text instead of as a field:

```
style={'class': 'form-control-plaintext'}
```

For inline checkboxes and radio buttons:

```
style={'inline': True}
```

Prepend/append text for inputs:

```
style={
    'prepend': 'text to prepend',
    'append': 'text to append',
}
```

## Development

Pretty standard: fork this repo, make changes, make a GitHub pull request.

There are demo pages showing a variety of form fields and layouts. To use it, first install its dependencies:

```
pip install -r requirements.txt
```

Then run the server:

```
make runserver
```

When using this `runserver`, you don't need to install `drfformbootstrap4` into your virtualenv before seeing changes. However if you want to see your changes reflected in a different application using the same virtualenv, install it with:

```
make install
```

Builds are here: https://travis-ci.org/mattfox/drf-form-bootstrap-4

## License

&copy; 2018 Matthew Fox

[MIT](https://github.com/mattfox/drf-form-bootstrap-4/blob/master/LICENSE)