#Even processing
#Events (map of fields ie: {“foo”: 42, “bar”: “baz"}), 
#patterns, 
#rules (ie foo > 41) 


#Input list patterns -> each pattern has at least one rule
#The output: all of the patterns that matched
# when we analyze a pattern, we can store some rules that have passed in a set


# the easiest way: go through each rule in each pattern

class EventProcessing:

    def __init__(self, events, patterns):
        self.events = events
        self.patterns = patterns

    def checkRule(self, rule):
        #returns True or False
        pass

    def checkPattern(self, pattern):
        for _rule in pattern:
            if not self.checkRule(_rule):
                return False
        return True

    def processPatterns(self):
        output = []
        for pattern in self.patterns:
            if self.checkPattern(pattern):
                output.append(pattern)
        
        return output

EventProcessingInstance = EventProcessing(events, pattern)
print(EventProcessingInstance.processPatterns())

    


    









