"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, prompt:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

  


    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template
        """ answers is a list of key/value pairs with key = words passed in when create an instance of Story and values = inputs from form"""
        """text is the story wording 'template' that's passed in when create an instance of Story"""
        
        for (key, val) in answers.items():
            """ replace the {key} in the 'text' template with its value"""
            text = text.replace("{" + key + "}", val)
       
        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)




