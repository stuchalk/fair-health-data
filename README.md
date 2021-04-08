# FAIR Health Data
Personal health data for Stuart J. Chalk during the COVID pandemic
## What is this data?
As an example of creating FAIR (Findable, Accessible, Interoperable, Reusable ) data for a seminar I am going to give,
I decided to collect health data about myself from January 1, 2021.  The data consists of:
- weight
- body temperature (with room temperature as a 'control')
- resting heart rate
- data from my daily runs including
    - VO<sub>2</sub> max
    - calories burned
    - distance
    - pace
    - a link to the activity (only one open access)
    
The data is collected in an MS Excel spreadsheet exported to a .csv file
and then processed through a Python script run in Juypter notebook.

The generated JSON-LD ([JSON for Linked Data](https://www.w3.org/TR/json-ld])) are then
uploaded every month, and a new tagged version of the data is generated.  Using Zenodo, 
each version of the package gets a DOI assigned automatically.

The .csv file, Juypter notebook, and python scripts are available as part of the dataset.

### For Findability
The repository will be registered with Google datasets
### For Accessibility
The data is made available for free via this GitHub repository
### For Interoperability
The data is made available in JSON-LD format, a text-based encoding of RDF, easily ingested via
any scripting language, and readable by humans.
### For Reusabililty
The data is made available under the Creative Commons CC-BY-NC-SA 4.0 International License.
