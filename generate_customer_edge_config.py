#!/usr/bin/env python3
"""
Enterprise Customer Edge Config Generator
Used in production to provision 1000+ customer routers at scale
Author: Raj Sahu (rsahu001)
"""
from jinja2 import Environment, FileSystemLoader
import yaml
import os

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("enterprise-customer-edge.j2")

with open("customers.yaml") as f:
    customers = yaml.safe_load(f)

os.makedirs("configs", exist_ok=True)
for cust in customers:
    config = template.render(cust)
    filename = f"configs/{cust['customer_name']}-{cust['site_id']}.cfg"
    with open(filename, "w") as f:
        f.write(config)
    print(f"Generated → {filename}")
