#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import random

def getRandomFortune():
    fortunes = ["lucky","not lucky","it's not your year","You will travel far","I see python in your future","random fortune","fortune faded"]
    return random.choice(fortunes)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = '<h1>Fortune Cookie</h1>'

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortune_sentence = "Your fortune: " + fortune
        random_fortune = "<p>" + fortune_sentence + "</p>"

        the_number = "<strong>" + str(random.randint(0,365)) + "</strong>"
        num_sentence = 'Your lucky number: ' + the_number
        num_paragraph = '<p>'+ num_sentence + '</p>'

        cookie_again_button = "<a href='.'><button>Another cookie please!</button></a>"

        content = header + random_fortune + num_paragraph + cookie_again_button

        self.response.write(content)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
