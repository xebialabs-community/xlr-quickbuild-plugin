#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
import sys
import time
import com.xhaus.jyson.JysonCodec as json
from xlrelease.HttpRequest import HttpRequest
from quickbuild.QuickBuild import QuickBuild
from org.slf4j import Logger
from org.slf4j import LoggerFactory
logger = LoggerFactory.getLogger("quickbuild")

logger.error("===============================================================")
qb = QuickBuild.create_client( qbServer )
logger.warn(">> configurationId       = %s " % configurationId)
logger.warn(">> respectBuildCondition = %s " % respectBuildCondition)
for prop in variables.keys():
    logger.warn(">> %s  =  %s " % (prop, variables[prop]))

#qb = QuickBuild.create_client( params )

logger.error("===============================================================")
if len(variables) > 0 :
    buildVariables="\n<variables>"
    for prop in variables.keys():
        buildVariables = "%s\n<entry>\n<string>%s</string>\n<string>%s</string>\n</entry>" % (buildVariables, prop, variables[prop])
    buildVariables = "%s\n</variablers>" % buildVariables
else:
    buildVariables = ""

myXML = """<com.pmease.quickbuild.BuildRequest>
  <configurationId>%s</configurationId>
  <respectBuildCondition>%s</respectBuildCondition>%s
 </com.pmease.quickbuild.BuildRequest>""" % (configurationId, respectBuildCondition, buildVariables)

logger.error(myXML)

http_request = HttpRequest(qbServer)
api_url = '/rest/build_requests'
response = http_request.post(api_url, myXML, contentType='application/xml')
task.setStatusLine("Build queued")
logger.error(response.getResponse())
time.sleep(10)
task.schedule("quickbuild/Build.wait-for-build.py")

logger.error("===============================================================")
