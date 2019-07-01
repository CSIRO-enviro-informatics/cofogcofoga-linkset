# COFOG / COFOG-A Linkset
This code repository contains a Linkset - a specialised Dataset linking objects in two other Datasets.

This Linkset contains [SKOS mapping properties](https://www.w3.org/TR/skos-reference/#mapping) between Concepts in the [COFOG](http://data.naa.gov.au/def/cofog) and Concepts in the [COFOG-A](http://data.naa.gov.au/def/cofog) vocabularies.

COFOG, "Classification of the Functions of Government", is a [United Nations Statistics Division](https://unstats.un.org/unsd/iiss/Classification-of-the-Functions-of-Government-COFOG.ashx)-issued vocabulary used to "...distinguish between the individual and collective services provided by general government and identifies consumption expenditures that benefit individual households...".

The COFOG-A is an Australian version of COFOG issued by the from the [Australian Bureau of Statistics](http://www.abs.gov.au) in the [Australian System of Government Finance Statistics: Concepts, Sources and Methods](http://www.ausstats.abs.gov.au/ausstats/subscriber.nsf/0/418BDDEBD088A012CA257F230019D433/$File/55140_2015.pdf) which is represented as a SKOS vocabulary online at <http://linked.data.gov.au/def/cofog-a>.


## Repository Contents
This repository contains the following files and folders:

* [README.md](README.md) - this file
* [imports/](imports/) - background information: the COFOG & COFOG-A vocabularies as RDF (turtle) files
* [data.ttl](data.ttl) - this Linkset's links as an RDF (turtle) file
* [header.ttl](header.ttl) - this Linkset’s data.ttl header information, stored separately for ease of access
* [example-data.ttl](example-data.ttl) - 5 Statements from the Linkset for ease of access, in RDF (turtle) format, as per the main data file but none of the whole-of-Linkset information
* [example-data-unreified.ttl](example-data-unreified.ttl) - 5 Statements from the Linkset but flattened, 'unreified', for even easier use
* [methods/](methods/) - a folder containing the notes, scripts (Python) and interim data used to create this Linkset


## Rights & License
The content of this repository is licensed for use under the [Creative Commons 4.0 License](https://creativecommons.org/licenses/by/4.0/). See the [license deed](LICENSE) all details.

Please note that the content of COFOG-A itself is derived from the [Australian Bureau of Statistics](http://www.abs.gov.au)' [Australian System of Government Finance Statistics: Concepts, Sources and Methods](http://www.ausstats.abs.gov.au/ausstats/subscriber.nsf/0/418BDDEBD088A012CA257F230019D433/$File/55140_2015.pdf).


## Contacts
*Technical contact:*  
**Nicholas Car**  
CSIRO Land & Water, Environmental Informatics Group  
<nicholas.car@csiro.au>  