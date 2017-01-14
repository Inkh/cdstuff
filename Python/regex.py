import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

    return [word for word in words if re.search(regex, word)]

print get_matching_words('v')
print get_matching_words('s{2}')
print get_matching_words('[e]$')
print get_matching_words('(b)\D(b)')
print get_matching_words('(b)\D+(b)')
print get_matching_words('(b)\w+(b)')
print get_matching_words('a[^aeiou]*e[^aeiou]*i[^aeiou]*o[^aeiou]*u[^aeiou]')
print get_matching_words(r'(\w)\1')
# print get_matching_words(r'(^[regular expression]+$)')
print get_matching_words(r'([regular expression]+)')
