# Cookiecutter for aioworkers plugin

Cookiecutter template to create aioworkers plugin.

## Convert plugin

To use template for plugin:
```bash
hatch run init ../aioworkers-sentry
```

## Update plugin
Plugin must be contained .scaraplate.conf with context params

Update plugin with template:
```bash
hatch run update ../aioworkers-sentry
```

## Testing

Run tests:

```bash
hatch run pytest
```

Run lint:

```bash
hatch run lint:all
```

Run format:

```bash
hatch run lint:fmt
```
