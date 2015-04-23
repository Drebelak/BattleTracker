__author__ = 'Avi'
import wikipedia_utils
from json import dumps
from urllib import quote


def scrape_wiki(name):
    val = wikipedia_utils.GetWikipediaPage(name)
    res = wikipedia_utils.ParseTemplates(val["text"])

    infobox = dict(res["templates"]).get("Infobox person")

    if infobox is not None:
        years_active = infobox.get('years_active', "Not Provided")
        birth_place_raw = infobox.get('birth_place', "Not Provided")
        alma_mater = infobox.get('alma_mater', "Not Provided")
        occupation = infobox.get('occupation', "Not Provided")

        birth_place = birth_place_raw.replace('[','').replace(']','')
        alma_mater = alma_mater.replace('[','').replace(']','')
        occupation = occupation.replace('[','').replace(']','')

        data = {'name': name, 'years_active': years_active, 'birth_place': birth_place, 'alma_mater': alma_mater,
                'occupation': occupation}
    else:
        #for non-normal wiki formatting
        data = unrecognised_format(str(val), name)

    #return dumps(data, sort_keys=True, indent=4) #use this for visually testing output
    return data


def unrecognised_format(info, name):
    pos = info.find('birth_place')
    if pos != -1:
        b_pos = info.find(']', pos)
        birth_place = info[pos+11:b_pos].replace('[','').replace(']','').replace("=", "").strip()
    else:
        birth_place = "Not Provided"

    pos = info.find('years_active')
    if pos != -1:
        b_pos = info.find('\\n', pos)
        o_pos = info.find('<', pos)
        b_pos = min(b_pos, o_pos)
        years_active = info[pos+12:b_pos].replace('[','').replace(']','').replace("=", "").replace("\u2013", "-").strip()
    else:
        years_active = "Not Provided"

    pos = info.find('occupation')
    if pos != -1:
        b_pos = info.find('\\n', pos)
        o_pos = info.find('<', pos)
        b_pos = min(b_pos, o_pos)
        occupation = info[pos+11:b_pos].replace('[','').replace(']','').replace("=", "").strip()
    else:
        occupation = "Not Provided"

    pos = info.find('alma_mater')
    if pos != -1:
        b_pos = info.find(']', pos)
        alma_mater = info[pos+11:b_pos].replace('[','').replace(']','').replace("=", "").strip()
    else:
        alma_mater = "Not Provided"
    data = {'name': name, 'years_active': years_active, 'birth_place': birth_place, 'alma_mater': alma_mater,
            'occupation': occupation}
    return data