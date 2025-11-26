# Enterprise Edge Config Generator

Production-grade tool for generating BGP customer edge router configs using Jinja2 + YAML.

Used to provision 1000+ enterprise customer sites with zero-touch, repeatable configs.

Features:
- YAML-driven customer data
- Jinja2 templating
- Ready for CI/CD and GitOps
- BGP peering to Google (AS15169)

Usage:
```bash
pip install jinja2 pyyaml
python generate_customer_edge_config.py
