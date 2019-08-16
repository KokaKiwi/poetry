from .command import Command


class DeployCommand(Command):
    """
    Deploy package (like using pip install with package)

    deploy
        { --user : Install in user local dir. }
        { --build : Build the package before deploying. }
        { --f|force : Force deploy package. }
        { pip-args?* : Additional arguments to pip. }
    """

    def handle(self):
        import subprocess

        # Building package first, if told
        if self.option("build"):
            self.comment('Building package...')
            self.call("build")

        self.info('Installing package...')
        cmd = ['pip', 'install', '--find-links=dist', '-U']
        if self.option('user'):
            cmd.append('--user')
        if self.option('force'):
            cmd.append('--force-reinstall')
        cmd.extend(self.argument('pip-args'))
        cmd.append(self.poetry.package.name)

        subprocess.run(cmd)
