# FAIR Health Data
Personal health data for Stuart J. Chalk made available using the 
[FAIR principles](https://www.force11.org/group/fairgroup/fairprinciples).
## What is this data?
As an example of creating FAIR (Findable, Accessible, Interoperable, Reusable) 
data for a seminar I presented on April 23<sup>rd</sup>, 2021, I decided to 
collect and publish my health data, starting January 1, 2021.  The data consists of:
- body weight
- body temperature (with room temperature as a 'control')
- resting heart rate
- data from my daily runs including
    - VO<sub>2</sub> max
    - calories burned
    - distance
    - average pace
    - a link to the activity (only one is open access due to privacy concerns)
    
The data is collected in an MS Excel spreadsheet exported to a .csv text file
and then processed through a [Python](https://www.python.org/) script run in 
a [Juypter notebook]().

The generated JSON-LD ([JSON for Linked Data](https://www.w3.org/TR/json-ld])) 
files are uploaded every month, and a new tagged version of the data is generated. Using 
[Zenodo](https://zenodo.org/), each release of this repository gets an 
automatically assigned [Digital Object Identifier](https://www.doi.org/) (DOI).

The .csv data file, Juypter notebook, and python scripts are available as part 
of the dataset.

### For Findability
The repository will be registered with Google datasets
### For Accessibility
The data is made available for free via this GitHub repository
### For Interoperability
The data is made available in JSON-LD format, a text-based human-readable 
encoding of RDF, easily ingested via any scripting language.
### For Reusabililty
The data is made available under the Creative Commons 
CC-BY-NC-SA 4.0 International License.
