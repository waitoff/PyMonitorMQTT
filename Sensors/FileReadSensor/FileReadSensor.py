import psutil
from Entity import Entity
import os
from consts import *

# Tip: customize topic because with more than one file, you must have different topics
TOPIC = 'file/file'


class FileReadSensor(Entity):
    def Initialize(self):
        self.AddTopic(TOPIC)
        self.filename = self.GetOption([CONTENTS_OPTION_KEY,FILE_READ_SENSOR_FILENAME_CONTENTS_OPTION])

    def Update(self):
        if not self.FileExists():
            raise Exception("File must exist (and can't be a directory) !")
        with open(self.filename,"r") as f:
            self.SetTopicValue(TOPIC,f.read())

    def FileExists(self):
        return os.path.exists(self.filename) and os.path.isfile(self.filename)