# -*- coding: utf-8 -*-
"""
This module is a scratchpad for general development, testing & debugging.
"""

from django.core.management.base import NoArgsCommand
from django.db import connection

from pexp.models import *


def reset_queries():
    connection.queries = []


class Command(NoArgsCommand):
    help = ""

    def handle_noargs(self, **options):
        Project.objects.all().delete()

        TestModelA.objects.create(field1='A1')
        TestModelB.objects.create(
            field1='B1',
            field2='B2'
        )
        TestModelC.objects.create(
            field1='C1',
            field2='C2',
            field3='C3'
        )
        print(TestModelA.objects.all())
        print()

        Project.objects.create(topic="John's gathering")
        ArtProject.objects.create(
            topic="Sculpting with Tim",
            artist="T. Turner"
        )
        ResearchProject.objects.create(
            topic="Swallow Aerodynamics",
            supervisor="Dr. Winter"
        )
        print(Project.objects.all())
        print()

        TestModelA.objects.all().delete()
        TestModelA.objects.create(field1='A1')
        TestModelB.objects.create(
            field1='B1',
            field2='B2'
        )
        TestModelC.objects.create(
            field1='C1',
            field2='C2',
            field3='C3'
        )
        print(TestModelA.objects.all())
        print()
