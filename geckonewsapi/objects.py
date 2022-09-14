from dataclasses import dataclass

@dataclass
class Article:
    link: str
    title: str
    image: str
    time: str
    type: str

    source: str = None
    short: str = None

    def get_json(self):
        return {
            'image': self.image,
            'title': self.title,
            'url': self.link,
            'time': self.time,
            'type': self.type,
            'source': self.source,
            'short': self.short,
        }

    def __str__(self):
        string = 'Article(\n'
        string += f'\timage  = {self.image}\n'
        string += f'\ttitle  = {self.title}\n'
        string += f'\turl    = {self.link}\n'
        string += f'\ttime   = {self.time}\n'
        string += f'\ttype   = {self.type}\n'
        string += f'\tsource = {self.source}\n'
        string += f'\tshort  = {self.short}\n'
        string += ')'
        return string
