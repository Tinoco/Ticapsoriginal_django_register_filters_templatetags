# Ticapsoriginal Django Register Filters Templatetags
Ticapsoriginal Useful Django Register Filters Template tags Extras File

## Filers:

* json serialization filter
* type casting filter
* acess dictionary filter
* None or null data filter
* drop string filter
* replace string filter
* safe mode output on template from data

# how to use filters :

* start your django project 
* create your core app 
* make directory templatetags inside your coreapp folder like this :

![](https://ticapsoriginal.com/static/register1.png)

* in your template file input extra load and use django filter register like this :

![](https://ticapsoriginal.com/static/register2.png)

## sintax : 

* {% load search_extras %}{{ search.forceUrl|rephttps }}
* {% load your_extra_file_name %}{{ data_input|register_filter_name }}


## quality:
* [`100% pycodestyle coverage`](https://pypi.org/project/pycodestyle/)

* [`0% code plagiarism detected`](https://github.com/blingenf/copydetect)

## about:
* code and resource used in [`Ticapsoriginal`](https://ticapsoriginal.com)
