#!/usr/bin/python
import os
import sys


class FilterModule(object):

    def filters(self):
        return {
    #        'prefix': self.prefix,
            'env_vars': self.env_vars,
        }

    def env_vars(self, generic_password, generic_username):
        pw_value = os.getenv(generic_password)
        user_value = os.getenv(generic_username)
        return pw_value, user_value
    