# square_administration

> 📌 versioning: see [CHANGELOG.md](./CHANGELOG.md).

## about

administration business layer for my personal server.

## goals

- administration-specific logic
- api grouped by usecase
- integration with square_*
- simple and sufficient

## installation

```shell
pip install square_administration
```

## usage

### configuration

update the settings in `config.ini` and `config.testing.ini` to match your environment (urls, logging, etc.).

### running the service

```shell
python square_common_bl/main.py
```

## env

- python>=3.12.0

> feedback is appreciated. thank you!