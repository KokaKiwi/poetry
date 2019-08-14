import shutil
from poetry.utils.env import Env
from ..command import Command


class VenvClearCommand(Command):
    '''
    Clear VirtualEnv if any

    venv:clear
    '''

    def handle(self):
        env = Env.get(self.poetry.file.parent)

        if env.is_venv():
            shutil.rmtree(env.path)
