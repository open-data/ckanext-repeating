import ckan.plugins as p
from ckan.plugins.toolkit import add_template_directory

from ckanext.repeating import validators



class RepeatingPlugin(p.SingletonPlugin):
    p.implements(p.IValidators)
    p.implements(p.IConfigurer)

    def update_config(self, config):
        """
        We have some form snippets that support ckanext-scheming
        """
        add_template_directory(config, 'templates')

    def get_validators(self):
        return {
            'repeating_text': validators.repeating_text,
            'repeating_text_output':
                validators.repeating_text_output,
            }
