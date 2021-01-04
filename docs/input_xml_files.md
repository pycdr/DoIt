# what is it about?

if you want to work with **DoIT**, you must know that how *the XML file* must be written. there are some elements that onluu these will be comprehended for **DoIt**:

### `data`
all of the elements must be placed in this tag (`<data>`); in this form:
```xml
<data>
	...
</data>
```
there can be each of `year`, `month` or `day`. anyway, we suggest to put only `year` elements.

### `<year>`
it defines a *year data part* and any data which are about a year (e.g. 2021, 1400, ...) must be all in one tag. we suggest to only use `month` element in it.

there are 3 defined arguments:

* **number**: number of the year (like: 1400)
* image: an image to show (like: *http://example.com/image.jpg*)
```xml
<year number="1753">
	...
</year>
```

### `<month>`
it defines a *month data part* and any data which are about a month (e.g. 1, 2, ...) must be all in one tag. you can only use `day` elements in it.

there are 3 defined arguments:

* **number**: number of the month from 1 until 12  (like: 8)
* **name**: name of the month (like: March)
* **count**: count of days in the month (like: 30)
* **weekfrom**: the week number of the first day (like: 2 [for Sunday])
* image: an image to show (like: *http://example.com/image.jpg*)
```xml
<month
	number="9"
	name="Azar"
	count="30"
	weekfrom="5"
	image="https://example.com/image.jpg"
>
	...
</month>
```
### `<day>`
it defines a *day data part* and any data which are about a day (e.g. 3, 21, 15, ...) must be all in one tag. you can only use `day` elements in it.

there are 3 defined arguments:

* number: number of the day (like: 12)
```xml
<day
	number="27"
>
	...
</day>
```
### `<time>`
this tag defines the proccesses of a day, and has these elements:
#### `<from>`
just a text, like `<from>12:30</from>`. it may be **HH**, **HH:MM** or **HH:MM:SS**.
#### `<to>`
like `<from>` element, but defines the end time.
#### `<title>`
defines the title of the proccess.
#### `<description>`
a short desctiption of the proccess.
#### `<text>`
full description of the proccess.

example:
```xml
<time>
	<from>12</from>
	<to>13:29:47</to>
	<title>Example</title>
	<description>this is an example.</description>
	<text>this is a long description of the proccess.</text>
</time>
```

## note
* all of arguments should be given as string, including number. like `<year number="2020">`
* **bold arguments** must be included in the argument when you are adding them.