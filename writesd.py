"""python scidata JSON-LD writer"""
from scidatalib.scidata import SciData
from datetime import datetime
import json
import csv


def createsd(data):
    """function to create a scidata JSON-LD from incoming dictionary"""

    # variables
    daynum = data[0]
    actdate = data[1]
    weight = data[2]
    vo2 = data[3]
    itemp = data[4]
    btemp = data[5]
    resthr = data[6]
    miles = data[7]
    tm = datetime.strptime(data[8], '%H:%M:%S')
    time = (60*tm.hour) + tm.minute + round(tm.second/60, 2)
    cal = data[10]
    url = data[11]

    uid = 'dataset' + str(daynum)
    tm = datetime.strptime(actdate, '%m/%d/%y')
    dstr1 = tm.strftime('%m%d%y')
    dstr2 = tm.strftime('%B %d, %Y')
    dstr3 = tm.strftime('%m/%d/%Y')
    base = 'https://github.com/stuchalk/fair-health-data/data/sjc' + dstr1 + '/'
    nss = {
        "w3i": "https://w3id.org/skgo/modsci#",
        "qudt": "http://qudt.org/vocab/unit/",
        "loinc": "https://loinc.org/",
        "ss": "http://semanticscience.org/resource/",
        "obo": "http://purl.obolibrary.org/obo/",
        "dc": "http://purl.org/dc/terms/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "afp": "http://purl.allotrope.org/ontologies/process#"
    }
    cx1 = "https://stuchalk.github.io/scidata/contexts/scidata_activity.jsonld"
    cx2 = "https://stuchalk.github.io/scidata/contexts/scidata_subject.jsonld"

    # initialize
    sd = SciData('scidata:fair:sjc' + dstr1)
    sd.context([cx1, cx2])
    sd.namespaces(nss)
    sd.base(base)

    # file metadata
    sd.docid(uid)
    sd.version('1')

    # graph metadata
    sd.graph_id(base)
    sjc = {'name': 'Stuart J. Chalk',
           'email': 'stuartjchalk@gmail.com',
           'orcid': '0000-0002-0703-7776'}
    sd.author([sjc])
    sd.title('Health data for Stuart J. Chalk from ' + dstr2)
    sd.description('Record of body temperature, weight, resting heart rate, '
                   'VO2 max and physical activity on ' + dstr3)
    sd.publisher('Stuart J. Chalk')
    sd.permalink(base + '.jsonld')
    sd.keywords(['body temperature', 'body weight', 'resting heartrate',
                 'VO2 max', 'exercise'])
    ids = "loinc:18688-2"
    sd.ids(ids)

    # scidata
    sd.discipline('w3i:Health')

    # methodology
    sd.evaluation('experimental')
    mmnts = [{
            '@id': 'measurement',
            'scope': ['resource/1/', 'procedure/1/'],
            'technique': 'thermometry',
            'techniqueref': 'obo:OMIT_0028052'
        },
        {
            "@id": "measurement",
            "scope": "resource/2/",
            "technique": "weighing",
            "techniqueref": "afp:AFP_0000503"
        },
        {
            "@id": "measurement",
            "scope": ["resource/3/", "activity/1/"],
            "technique": "optical heart rate monitoring",
        },
        {
            "@id": "measurement",
            "scope": ["resource/3/", "activity/1/"],
            "technique": "geolocation mapping"
        },
        {
            "@id": "measurement",
            "scope": ["resource/3/", "activity/1/"],
            "technique": "timing",
            "techniqueref": "ss:SIO_000391"
        }
    ]
    rsrcs = [{
            "@id": "resource",
            "type": "digital infrared thermometer",
            "name": "iProven DMT-489",
            "vendor": "iProven"
        },
        {
            "@id": "resource",
            "type": "digital scale",
            "name": "Body Cardio",
            "vendor": "Withings"
        },
        {
            "@id": "resource",
            "name": "Forerunner 245",
            "type": "digital running watch",
            "vendor": "Garmin",
            "software": "Version 5.50",
            "accessory": "Garmin Running Dynamics Pod"
        }
    ]
    procs = [{
            "@id": "procedure",
            "description": "Measurement of body temperature was made "
                           "by turning on the infrared thermomemter, "
                           "verifying there were no errors, and taking a "
                           "measurement as follows. First, the 'head' "
                           "button was depressed and held down while moving "
                           "the device across the forehead from left to right "
                           "at a distance of ~1 cm away. The 'head' button "
                           "was then released.  The reading on the display "
                           "was recorded in the Notes app on an iPhone."
            }]
    acts = [{
        "@id": "activity",
        "@type": "obo:NCIT_C43431",
        "exercise": "road running",
        "exerciseref": "obo:NCIT_C94737",
        "url": url
    }]
    sd.aspects(mmnts + rsrcs + procs + acts)

    # system
    spmn = {
            "@id": "subject",
            "species": "homo sapien",
            "speciesref": "obo:NCBITaxon_9606",
            "gender": "male",
            "ethnicity": "caucasian",
            "nationality": "english"
            }
    cond = {
            "@id": "condition",
            "quantity": "temperature",
            "property": "room temperature",
            "propertyref": "loinc:60832-3",
            "value": {
                "@id": "numericvalue",
                "number": itemp,
                "unit": "qudt:DEG_F"
                }
            }
    sd.facets([spmn, cond])

    # dataset
    sd.scope('specimen/1/')
    pt1 = {
        "@id": "datapoint",
        "source": "measurement/1/",
        "property": "body temperature",
        "propertyref": "loinc:18688-2",
        "conditions": "condition/1/",
        "value": {
            "@id": "numericvalue",
            "number": btemp,
            "unit": "qudt:DEG_F"
        }
    }
    pt2 = {
        "@id": "datapoint",
        "source": "measurement/2/",
        "property": "body weight",
        "propertyref": "loinc:18690-8",
        "textstring": {
            "@id": "numericvalue",
            "number": weight,
            "unit": "qudt:LB"
        }
    }
    pt3 = {
        "@id": "datapoint",
        "source": "measurement/3/",
        "property": "resting heart rate",
        "propertyref": "loinc:40443-4",
        "number": {
            "@id": "numericvalue",
            "value": resthr,
            "unit": "qudt:BEAT-PER-MIN"
        }
    }
    pt4 = {
        "@id": "datapoint",
        "source": ["measurement/2/", "measurement/3/", "measurement/4/"],
        "property": "VO2 max",
        "propertyref": "loinc:94122-9",
        "activity": "activity/1/",
        "textstring": {
            "@id": "numericvalue",
            "value": vo2,
            "unit": "qudt:MilliL-PER-KiloGM-MIN"
        }
    }
    pt5 = {
        "@id": "datapoint",
        "source": ["measurement/3/", "measurement/4/"],
        "property": "calories burned",
        "propertyref": "loinc:93825-8",
        "value": {
            "@id": "numericvalue",
            "number": cal,
            "unit": "qudt:KiloCAL"
        }
    }
    pt6 = {
        "@id": "datapoint",
        "source": "measurement/4/",
        "property": "running distance",
        "propertyref": "loinc:93817-5",
        "value": {
            "@id": "numericvalue",
            "number": miles,
            "unit": "qudt:MI_US"
        }
    }
    pt7 = {
        "@id": "datapoint",
        "source": "measurement/5/",
        "property": "exercise duration",
        "propertyref": "loinc:55411-3",
        "value": {
            "@id": "numericvalue",
            "number": time,
            "unit": "qudt:MIN"
        }
    }
    grp = {
        "@id": "datagroup",
        "description": "running metrics",
        "source": ["resource/3/", "event/1/"],
        "datapoints": [pt4, pt5, pt6, pt7]
    }
    sd.datagroup([grp])
    sd.datapoint([pt1, pt2, pt3])

    # source
    sd.sources([{'citation': 'Chalk Health Study 2021',
                'url': 'https://github.com/stuchalk/fair-health-data'}])

    # rights
    sd.rights('Stuart J. Chalk',
              'https://creativecommons.org/licenses/by-nc-nd/4.0/')

    # generate the JSON-LD file
    output = sd.output
    del sd
    return output


# fields = ['Day', 'Date', 'Weight', 'VO2 Max', 'Indoor Temp', 'Body Temp',
#           'Resting HR', 'Miles', 'Time', 'Pace', 'Calories', 'GarminURL',
#           'Comment']
#
# example = [1, '1/1/21', 184.1, 48, 70, 97.1, 44, 3.26, '0:26:31', '8:07', 390,
#            'https://connect.garmin.com/modern/activity/6035525608']
#
# out = createsd(example)
# print(json.dumps(out, indent=4))


# Import your CSV data file
# flist = []
# filename = 'healthdata.csv'
# with open(filename, 'r') as dataset:
#     for line in csv.reader(dataset):
#         flist.append(line)
#
# for i, day in enumerate(flist):
#     if i == 0:
#         continue
#     print(day)
#     jsonld = createsd(day)
#     t = datetime.strptime(day[1], '%m/%d/%y')
#     date = t.strftime('%m%d%y')
#     f = open("data/sjc" + date + ".jsonld", "w")
#     f.write(json.dumps(jsonld))
#     f.close()
