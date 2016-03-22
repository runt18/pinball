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

import datetime

from pinball_ext.job.basic_jobs import PythonJob


class ExamplePythonJob(PythonJob):

    def _setup(self):
        print 'Do some setup in example python job!'

    def _execute(self):
        print 'Current time is {0!s}'.format(str(datetime.datetime.now()))


class ExamplePinballMagicPythonJob(PythonJob):
    def _setup(self):
        print 'Do some setup in example python job!'

    def _execute(self):
        # a_python_key=a_python_value pair will be passed to
        # the downstream job as event attribute.
        print 'PINBALL:EVENT_ATTR:a_python_key=a_python_value'
