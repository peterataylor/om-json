# Observations & Measurements JSON encoding

This repository contains some provisional JSON schema for encoding observations & measurements in JSON. Work in progress. 

Main observation schema: [Observation](https://github.com/peterataylor/om-json/blob/master/Observation.json)
   * [Truth observation example](https://github.com/peterataylor/om-json/blob/master/observation-instance-example-boolean.json)
   * [Measurement observation example](https://github.com/peterataylor/om-json/blob/master/observation-instance-example-measure.json)
   * [Geometry (polygon) observation example](https://github.com/peterataylor/om-json/blob/master/observation-instance-example-geometry-polygon.json)

## Tools

  * Handy online validation of instances against schema: http://jsonschemalint.com/ (although lacks good errors for linked schemas)
  * Another online validator that is backed by Java; has slightly better error reporting: http://json-schema-validator.herokuapp.com/index.jsp. 
  * And another validator, also with better reporting: http://www.jsonschemavalidator.net/
  * [JSONLint](http://jsonlint.com)
  * Guide to authoring JSON schema: http://spacetelescope.github.io/understanding-json-schema/, specifically http://spacetelescope.github.io/understanding-json-schema/structuring.html#structuring

  There is a basic python validator in /tests that tests an instance against the specified schema. However, the various validators tend to handle specifics slightly differently. For example,
  some of them miss the regex tests for complex datet times. The best one so far seems to be http://www.jsonschemavalidator.net/. 

## TODOs

  * Investigate more strict validation from the Python library. 
  * Improve inheritence approach (currently just clones base type properties) 
  * Timseries support (i.e. timeseriesML)
  * ?replace role/relatedObservation with standard links rel/href?
  * Online validator 
