# cydav

Small Python controller for <a href="https://github.com/luv4bytes/cdav">cdav</a>.

Cydav provides a simple way to control cdav using the basic subprocess module.

Every operation cdav can be used for is accessible as a function of the cdav class.

## Example

```
def main():

	dav = cdav("path to cdav")
	options = cdav_options()
	
	options.user = "somedude"
	options.password = "verysecret"
	options.url = "https://test.com/dav/test.jpg"
	
	result = dav.GET(options, "./test.jpg")
```