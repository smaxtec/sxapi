# Summary - *The What* #
**DO** - I've added a feature to the foobar pipeline which is responsible for filtering the signal of activity_raw. It includes data preparation and signal processing as well as tests. For more background, see details ticket #JIRA-123.

**DONT** - Support for #JIRA-123


# Purpose - *The Why* #
**DO** - These changes will reduce error and enable subsequent statistical model training. Without them, noise is to big to process the signal further

**DONT** - Obviously necessary. See #JIRA-123


# Magic - *The How* (Optional)
**DO** - Before the filter is applied, data is synchronized and sorted by time. Thereafter, a genius bandpass filter applied to the raw signal with parameter x, y, z will do the job perfectly fine.

**DONT** - Filter applied.

# ToDo's - *Open Point List* #
**DO**
* The lower filter frequency still has to be validated
* The data preparation discards a lot of samples due to schema error xyz

**DONT**
There might be some additional changes necessary.

# Reviewers - *The Who* #

* Review Owners (Watch in detail - Approval mendatory): @<smaxies> (see [wiki](https://wiki.smaxtec.com/pages/viewpage.action?pageId=73302356))
* Review Members (Watch briefly - Approval is optional): @<smaxies>. Focus: [link to focus files]
* Review Guests (Informative - Approval is optional): @<smaxies>

# Links #
* wiki
* JIRA
* ...