# dipress

This is a very basic Django REST Framework app. User can post a query, and the app will use a relevant Wikipedia article to generate text with [Dissociated press](https://en.wikipedia.org/wiki/Dissociated_press) algorithm, and save it.

## API Methods

* **/list** - list IDs and queries of all saved texts
* **/read/\<id\>** - read saved text by ID
* **/create** - POST {"query":"user query"} - create and save new text

## Demo

* [/list](http://dipress.os32.com:8000/list)
* [/read](http://dipress.os32.com:8000/read)
* [/create](http://dipress.os32.com:8000/create)

It's being hosted on a DigitalOcean Droplet, and served with Django devserver (no SSL).
