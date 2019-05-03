#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
import json
import sys
from org.slf4j import Logger
from org.slf4j import LoggerFactory
from xlrelease.HttpRequest import HttpRequest

class QuickBuild(object):
    def __init__(self, httpConnection, username=None, password=None):
        self.logger = LoggerFactory.getLogger("quickbuild")
        self.http_request = HttpRequest(httpConnection, username, password)

    @staticmethod
    def create_client(httpConnection, username=None, password=None):
        return QuickBuild(httpConnection, username, password)

    def get_version(self):
        api_url = '/rest/version'
        response = self.http_request.get(api_url)
        if response.isSuccessful():
            data = response.getResponse()

            return data
        else:
            self.logger.error('Get Version FAILED!!')
            sys.exit(1)

    def build(self, configurationId, respectBuildCondition, variables):
        api_url = '/rest/build_requests'
        response = self.http_request.get()
