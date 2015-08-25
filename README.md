# Observations & Measurements (O&M) JSON encoding

This repository contains JSON schema for encoding Observations & Measurements (O&M) in JSON. 

Main observation schema: [Observation](https://github.com/peterataylor/om-json/blob/master/Observation.json)
   * [Truth observation example](https://github.com/peterataylor/om-json/blob/master/observation-boolean-1.json)
   * [Measurement observation example](https://github.com/peterataylor/om-json/blob/master/observation-measure-1.json)
   * [Geometry (polygon) observation example](https://github.com/peterataylor/om-json/blob/master/observation-geometry-polygon-1.json)
   * [Geometry (linestring) observation example](https://github.com/peterataylor/om-json/blob/master/observation-geometry-linestring-1.json)
   * [Specimen example](https://github.com/peterataylor/om-json/blob/master/sample-specimen-1.json)

## Tools

There is a validator here: http://waterml2.csiro.au/om-json/. This is an altered version of JSON Schema Lint that uses Tiny Validator v4 and has O&M examples loaded. 

Other tools:
  * Handy online validation of instances against schema: http://jsonschemalint.com/ (although lacks good errors for linked schemas)
  * Another online validator that is backed by Java; has slightly better error reporting: http://json-schema-validator.herokuapp.com/index.jsp. 
  * And another validator, also with better reporting: http://www.jsonschemavalidator.net/
  * [JSONLint](http://jsonlint.com)
  * Guide to authoring JSON schema: http://spacetelescope.github.io/understanding-json-schema/, specifically http://spacetelescope.github.io/understanding-json-schema/structuring.html#structuring

  There is a basic python validator in /tests that tests an instance against the specified schema. However, the various validators tend to handle specifics slightly differently. 
  The best one so far seems to be http://www.jsonschemavalidator.net/. 

## TODOs

  * Investigate more strict validation from the Python library. 
  * Timeseries support (i.e. timeseriesML) - in progress. 
