# Neutrino API Utils

This Python utility provides a simple interface for interacting with various Neutrino API endpoints. It allows you to perform actions such as bad word filtering, email validation, phone number validation, and more.

## Prerequisites

- Python 3.x
- Required Python packages: `argparse`, `json`, `yaml`, `rich`

## Setup

1. Obtain Neutrino API credentials: [Neutrino API](https://www.neutrinoapi.com/)
2. Clone or download this repository to your local machine.

## Configuration

The utility uses a configuration file in YAML format (`config.yaml`) for Neutrino API credentials. Alternatively, you can provide credentials through command-line arguments.

Example `config.yaml`:

```yaml
user_id: YOUR_NEUTRINO_USER_ID
api_key: YOUR_NEUTRINO_API_KEY
```

## Usage

```
python neutrino_utils.py --config-file config.yaml --endpoint ENDPOINT_NAME --data DATA
```

1. config-file: Path to the YAML configuration file containing Neutrino API credentials.
1. user-id: Neutrino API user ID.
1. api-key: Neutrino API key.
1. endpoint: Name of the Neutrino API endpoint to use.
1. data: Data required for the selected endpoint.

For example:

```
python neutrino_utils.py --config-file config.yaml --endpoint bad-word-filter --data "This is a sample text."
```

## Neutrino API Endpoints

See [official api docs](https://www.neutrinoapi.com/api/api-basics/).


## License
This utility is licensed under the MIT License - see the LICENSE file for details.