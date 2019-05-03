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
import re
import com.xhaus.jyson.JysonCodec as json
from xlrelease.HttpRequest import HttpRequest
from quickbuild.QuickBuild import QuickBuild
from org.slf4j import Logger
from org.slf4j import LoggerFactory
logger = LoggerFactory.getLogger("quickbuild")

def finishPolling(buildStatus):
    logger.warn("Finished: %s" % buildStatus)
    task.setStatusLine("[Build Done]")
    if buildStatus != 'SUCCESSFUL':
        logger.error("Build Status %s is not SUCCESSFUL" % buildStatus)
        sys.exit(1)


logger.error("===============================================================")
qb = QuickBuild.create_client( qbServer )
logger.warn(">> configurationId       = %s " % configurationId)
logger.warn(">> respectBuildCondition = %s " % respectBuildCondition)
logger.warn(">> Build It to Promte = %s " % buildIdIn)

#qb = QuickBuild.create_client( params )

logger.error("===============================================================")

http_request = HttpRequest(qbServer)
api_url = '/rest/latest_builds/%s' % configurationId

#try:
response = http_request.get(api_url)
logger.error(response.getResponse())
data = response.getResponse()
logger.error("Is Successful? %s" % response.isSuccessful() )
if response.isSuccessful():
    p = re.compile("<status>(.*)</status>")
    buildStatus = p.search(data).group(1)
    task.setStatusLine("[Build Status %s]" % buildStatus)
    p = re.compile('<id>(.*)</id>')
    buildId = p.search(data).group(1)
    logger.error("[Build ID %s]" % buildId)
    p = re.compile('<version>(.*)</version>')
    buildVersion = p.search(data).group(1)
    logger.error("[Build Status %s]" % buildStatus)
    if buildStatus != 'RUNNING':
        finishPolling(buildStatus)
        exit(0)
    else:
        task.schedule("quickbuild/Promote.wait-for-build.py")
else:
    logger.error("\nFailed to check the job status. Received an error from the Jenkins server: `%s`" % response.response)
    task.schedule("quickbuild/Promote.wait-for-build.py")

#except:
#    logger.error("\nFailed to check the job status due to connection problems. Will retry in the next polling run.")

task.schedule("quickbuild/Promote.wait-for-build.py")
