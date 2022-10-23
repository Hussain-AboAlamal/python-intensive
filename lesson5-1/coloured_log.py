"""
Task # 1 
GitHub registration:
Register at https://github.com/
Create your own Private Repository `python-intensive`.
Add .gitignore with selecting "Python" as value
Clone that repo to your local machine
Configure `Collaborators` in your private repository and add trainers` github account


Task #2
Create git branch `lesson5-1`, and switch to it
Create virtual environment, install the package colorlog:
https://pypi.org/project/colorlog/
Configure the formatter so that, you have coloured message per each different log level

'DEBUG':    'blue',
'INFO':     'green',
'WARNING':  'yellow',
'ERROR':    'red',
'CRITICAL': 'violet',

Test your code inside the special section
Commit your changes to your local branch.
Push your changes to remote gitHub repository
Create a pull request with title 'lesson5-1'
Ask your trainer to review you hometask by requesting a Review in GitHub
"""
import logging
import colorlog

handler = colorlog.StreamHandler()

# configure logger format
formatter = colorlog.ColoredFormatter(
	"%(log_color)s%(message)s",
	datefmt=None,
	reset=True,
	log_colors={
		'DEBUG':    'cyan',
		'INFO':     'green',
		'WARNING':  'yellow',
		'ERROR':    'red',
		'CRITICAL': 'purple',
	},
	# secondary_log_colors={},
	# style='%'
)

handler.setFormatter(formatter)


class ColorLog:
    
    def __init__(self) -> None:
        self.logger = logging.getLogger('example')
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
    
    def debug(self, message: str) -> None:
        self.logger.debug(message)
        
    def info(self, message: str) -> None:
        self.logger.info(message)
        
    def warning(self, message: str) -> None:
        self.logger.warning(message)
        
    def error(self, message: str) -> None:
        self.logger.error(message)

    def critical(self, message: str) -> None:
        self.logger.critical(message)
        

if __name__ == "__main__":
    # test your code here
    colorLog = ColorLog()
    colorLog.debug('DEBUG')
    colorLog.info('INFO')
    colorLog.warning('WARNING')
    colorLog.error('ERROR')
    colorLog.critical('CRITICAL')
