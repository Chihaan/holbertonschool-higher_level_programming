#!/usr/bin/python3
"""Module for generating personalized invitation files from a template."""

import re


def generate_invitations(template, attendees):
    """Generate output_X.txt invitation files from a template and attendees."""
    if not isinstance(template, str):
        print("Template must be str type")
        return
    if (not isinstance(attendees, list)
            or not all(isinstance(a, dict) for a in attendees)):
        print("Attendees must be a list of dicts")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    fields = re.findall(r"\{(.+?)\}", template)

    for i, attendee in enumerate(attendees, start=1):
        tmp_template = template
        for field in fields:
            value = attendee.get(field, "N/A")
            if value is None:
                value = "N/A"
            tmp_template = tmp_template.replace("{" + field + "}", value)
        with open(f'output_{i}.txt', 'w') as f:
            f.write(tmp_template)
