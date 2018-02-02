import json
import unittest

from ckan.plugins.toolkit import missing

from ckanext.repeating import validators


class TestRepeatingText(unittest.TestCase):
    def test_field_with_hyphenated_name_stored(self):
        key = (u'country-iso3',)
        data = {
            (u'country-iso3',): missing,
            ('__extras',): {
                'country-iso3-1': 'RWA',
                'country-iso3-2': u'TZA',
                'country-iso3-3': u'KEN',
                'country-iso3-4': u'',
            }
        }

        errors = {(u'country-iso3',): []}
        context = {}

        validators.repeating_text(key, data, errors, context)

        stored_value = json.loads(data[key])

        self.assertIn('RWA', stored_value)
        self.assertIn('TZA', stored_value)
        self.assertIn('KEN', stored_value)

        self.assertEqual(len(stored_value), 3)
