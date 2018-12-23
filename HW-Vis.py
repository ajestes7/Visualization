# Import statements
import json
import tweepy
import unittest
import sqlite3
import twitter_info # still need this in the same directory, filled out
import matplotlib.pyplot as plt

## [PART 1]
# Finish writing the function getDayDict which takes a database cursor and returns a
# dictionary that has the days of the weeks as the keys (using "Sun", "Mon", "Tue",
# "Wed", "Thu", "Fri", "Sat") and the number of tweets on the named day as the values
#
# cur - the database cursor

def getDayDict(cur):
    cur.execute('SELECT time_posted from Tweets')
    dayDict = {'Sun': 0, 'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0}
    dayList = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

    for aTweet in cur:
        for day in dayList:
            if day in str(aTweet[0]):
                dayDict[day] += 1

    return dayDict

## [Part 2]
# Finish writing the function drawBarChart which takes the dictionary and draws a bar
# chart with the days of the week on the x axis and the number of tweets on the named day on
# the y axis.  The chart must have an x label, y label, and title.  Save the chart to
# "bar.png" and submit it on canvas.
#
# dayDict - a dictionary with the days of the week and the number of tweets per day

def drawBarChart(dayDict):
    dayList = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    dataList = []

    for day in dayList:
        dataList.append(dayDict[day])

    fig, ax = plt.subplots()

    ax.bar(range(0,7), dataList, 0.2, color = 'pink')
    ax.grid()
    ax.set_xticks(range(0,7))
    ax.set_xticklabels(tuple(dayList))
    ax.set(xLabel = 'Day of the Week', yLabel = '# of Tweets', title = '# of Tweets Per Day Per Week by AJ Estes')
    fig.savefig("bar.png")
    plt.show()

## [Part 3]
## Create unittests to test the function
# Finish writing the unittests.  Write the setUp function which will create the database connection
# to 'tweets.sqlite' and the cursor.  Write the tearDown function which closes the database connection.
# Write the test_getDayDict function to test getDayDict by comparing the returned dictionary to the
# expected value.  Also call drawBarChart in test_getDayDict.

class TestHW10(unittest.TestCase):

    def setUp(self):
        consumer_key = twitter_info.consumer_key
        consumer_secret = twitter_info.consumer_secret

        self.conn = sqlite3.connect('tweets.sqlite')
        self.cur = self.conn.cursor()

    def test_getDayDict(self):
        self.assertEqual(getDayDict(self.cur),{'Sun': 0, 'Mon': 69, 'Tue': 77, 'Wed': 90, 'Thu': 0, 'Fri': 0, 'Sat': 0})
        drawBarChart(getDayDict(self.cur))

if __name__ == "__main__":
    unittest.main(verbosity=2)
