# Copyright 2015, Pinterest, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Defines example jobs."""

import datetime
import os

from pinball_ext.job.basic_jobs import PythonJob
from pinball_ext.job.basic_jobs import CommandLineJob
from pinball_ext.job_templates import CommandJobTemplate


JOB_IMPORT_DIRS = [os.path.dirname(os.path.realpath(__file__))]


class ExamplePythonJob(PythonJob):

    def _setup(self):
        print 'Do some setup in example python job!'

    def _execute(self):
        print 'Current time is {0!s}'.format(str(datetime.datetime.now()))


class ExampleCommandJob(CommandLineJob):

    def _setup(self):
        print 'Do not need to add args for this command!'
        self.arguments = ''

    def _get_command(self):
        return 'date'


# A template for a placeholder final job to add to the end of
# workflows.
FINAL_JOB = CommandJobTemplate('final', 'echo success')
