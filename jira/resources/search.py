from jira.resources.resource import Resource

__author__ = 'bspeakmon@atlassian.com'

class Search(Resource):

    def __init__(self, options, cookies=None):
        Resource.__init__(self, "search", options, cookies)
