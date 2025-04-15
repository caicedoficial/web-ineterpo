#!/bin/bash
/opt/vercel/python3/bin/python3 -m pip install --upgrade pip
/opt/vercel/python3/bin/pip3 install -r requirements.txt
/opt/vercel/python3/bin/python3 manage.py collectstatic --noinput