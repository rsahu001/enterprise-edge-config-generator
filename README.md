# Enterprise Edge Config Generator

A compact, data-driven example for generating customer-edge BGP configuration from YAML inventory data and Jinja2 templates. It illustrates a repeatable configuration workflow that can be incorporated into a CI/CD or GitOps pipeline.

## How it works

```text
customers.yaml → Jinja2 template → per-site configuration files
```

- `customers.yaml` holds site-specific input data.
- `templates/enterprise-customer-edge.j2` defines the router configuration shape.
- `generate_customer_edge_config.py` renders one configuration per customer/site into `configs/`.

The included customer names, addresses, and ASNs are documentation examples; do not use them as production configuration.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install jinja2 pyyaml
python3 generate_customer_edge_config.py
```

Review the generated files in `configs/` before any deployment. A production implementation should validate schema and configuration policy, run a device-aware pre-deployment check, obtain change approval, and deploy through an audited pipeline.

## Why this pattern matters

Separating intent (YAML) from rendering (templates) makes changes reviewable, repeatable, and easier to test. It reduces drift and avoids hand-editing similar configurations across many sites.

## License

Copyright 2026 Raj Sahu. Licensed under the [Apache License 2.0](LICENSE).
