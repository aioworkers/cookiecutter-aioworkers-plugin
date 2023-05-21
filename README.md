# Cookiecutter for aioworkers plugin

Cookiecutter template to create aioworkers plugin.

## Update plugin
Plugin must be contained .scaraplate.conf with context params

Update plugin with template:
```bash
hatch run scaraplate rollup . ../aioworkers-sentry --no-input
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
