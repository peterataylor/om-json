from jsonschema import validate, Draft4Validator
import json
import argparse

'''
Basic JSON instance validation script taking two
command line args: path to instance file and
path to schema file

e.g. python validate.py '../observation-instance-example-measure.json'
'../Observation.json'

requires jsonschema module

Peter T, CSIRO 2015
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run validation of instance \
            against schema')
    parser.add_argument("instance", help="instance file location")
    parser.add_argument("schema", help="schema file location")
    args = parser.parse_args()

    schema = open(args.schema).read()
    instance = open(args.instance).read()

    validate(json.loads(instance), json.loads(schema))
