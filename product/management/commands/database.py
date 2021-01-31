#! /usr/bin/env python3
# coding: utf-8
""" """
from django.core.management.base import BaseCommand

from product.offapi.api_requests import ApiRequests

from product.offapi.insertdb import insertdb


class Command(BaseCommand):
    def databasefill(self):
        """ """
        print("Loading...")

        Api_data = ApiRequests().api_get_data()
        Insert = insertdb(Api_data)

    def handle(self, *args, **options):
        self.databasefill()
