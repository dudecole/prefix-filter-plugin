#!/usr/bin/python
import os

class FilterModule(object):

    def filters(self):
        return {
            'prefix': self.prefix,
            #'varnames_create': self.varnames_create
        }

    def prefix(self, a_variable, a_prefix):
        a_new_variable = a_prefix + '_' + a_variable 
        some_dict = {a_new_variable: a_variable}

        return a_new_variable

    def varnames_create(self, variable_names, a_prefix):
        var_list = list(variable_names)

        for name in variable_names:
            os.getenv('*PASS')
            print("we found it...")
            
        a_new_variable = a_prefix + '_' + a_variable 
        some_dict = {a_new_variable: a_variable}

        return a_new_variable
#    def prefix_concat(self, pre_variable1, pre_variable2):
#        a_new_variable = pre_variable1 + '_' + pre_variable2
#        return a_new_variable
