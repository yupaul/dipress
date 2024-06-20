# dipress

This is a very basic Django REST Framework app. User can post a query, and the app will try to find a relevant Wikipedia article, generate mostly non-sensical text from it with [Dissociated press](https://en.wikipedia.org/wiki/Dissociated_press) algorithm, and save it.

## API Methods

* **/list/** - list IDs and queries of all saved texts
* **/read/\<id\>/** - read saved text by ID
* **/create/** - POST {"query":"user query"} - create and save new text

## Demo

* [/list/](https://dipress.os32.com/list/?format=json)
* [/read/](https://dipress.os32.com/read/9/?format=json)
* [/create/](https://dipress.os32.com/create/)

Demo is being hosted on a DigitalOcean Droplet.
