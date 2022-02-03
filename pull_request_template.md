# Summary - *The What* #
**DO** - I've added a feature to the foobar pipeline which is responsible for filtering the signal of activity_raw. It includes data preparation and signal processing as well as tests. For more background, see details ticket or issue #api-123

**DONT** - Support for Tickets or Issues #api-123


# Purpose - *The Why* #
**DO** - These changes will reduce error and enable subsequent statistical model training. Without them, noise is to big to process the signal further.

**DONT** - Obviously necessary.


# Magic - *The How* (Optional)
**DO** - Before the filter is applied, data is synchronized and sorted by time. Thereafter, a genius bandpass filter applied to the raw signal with parameter x, y, z will do the job perfectly fine.

**DONT** - Filter applied.

# ToDo's - *Open Point List* #
**DO**
* The lower filter frequency still has to be validated
* The data preparation discards a lot of samples due to schema error xyz

**DONT**
There might be some additional changes necessary.

# Links #
* wiki
* JIRA
* Docs
* ...