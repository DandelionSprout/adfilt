This folder is a passion project of Adfilt team member [iam-py-test](https://github.com/iam-py-test), based on [ClearURL's extension rules](https://gitlab.com/anti-tracking/ClearURLs/rules/-/raw/master/data.min.json).
<br>Before using this list, be aware:
- it only contains the ClearURLs rules for cleaning query parameters (the stuff after the ? in URLs, so the tracker=evil in https://example.com?tracker=evil). For security reasons, it is not possible to change any other part of the URL in uBlock Origin (not sure about AdGuard) <br>
For example, ClearURLs for uBo _can not_ remove ref_ from https://amazon.com/something/ref_=bla. Only the ClearURLs extension can do this.
- this list is known to cause break websites and even prevent some rules in other similar filterlists from working. Use with caution.
