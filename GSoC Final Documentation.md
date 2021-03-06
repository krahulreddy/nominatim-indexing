# GSoC Final Documentation

## All important links

### Code

* [Indexing repository link](https://github.com/krahulreddy/nominatim-indexing/)
* [Nominatim UI PR](https://github.com/osm-search/nominatim-ui/pull/32)
* [Nominatim UI branch](https://github.com/krahulreddy/nominatim-ui/tree/suggestions)
* [Proof of Concepts](https://github.com/krahulreddy/GSoc_POCs)
* [Elasticsearch and Solr comparison repo (Simple intro before starting the project)](https://github.com/krahulreddy/Search)

### Diary entries

* [Project introduction](https://www.openstreetmap.org/user/krahulreddy/diary/392958)
* [Community bonding](https://www.openstreetmap.org/user/krahulreddy/diary/393314)
* [Elasticsearch vs Solr](https://www.openstreetmap.org/user/krahulreddy/diary/393360)
* [Proof of concepts](https://www.openstreetmap.org/user/krahulreddy/diary/393458)
* [Phase 2 Update](https://www.openstreetmap.org/user/krahulreddy/diary/393800)

### Hosted Server

* [Server with Nominatim-UI (This will be offline after few days of completion of GSoC)](https://gsoc2020.nominatim.org/nominatim/ui/search.html)
* [API with suggestions (This will be offline after few days of completion of GSoC)](https://gsoc2020.nominatim.org/suggest/autocomplete?q=new%20york)

## About the project

This is a GSoC project, which has been developed over the Summer of 2020. This project is mentored by [Sarah Hoffmann (lonvia)](https://github.com/lonvia) and [Marc Tobias (mtmail)](https://github.com/mtmail).

### What are we doing: The problem statement

OSM’s main search engine Nominatim does not support search suggestions. A separate database, which should be derived from the Nominatim database, should be set up for search suggestions. This DB should support regular updates from Nominatim DB. This must handle various languages. It must be small enough to run alongside Nominatim.

This project aims at setting up such a search suggester by comparing various alternative implementations like Elasticsearch, Solr. These suggesters set up indexing to facilitate quick suggestions to the users. The finalized stack will be integrated with the Nominatim search API. Complete installation and setup documentation along with a test suite will be created as a part of this project.

### Why is it required?

Suggestions during search help a lot in terms of finding the right place. Adding suggestions to the Nominatim search will help the users of Nominatim and OpenStreetMap to easily find the right place without performing a Nominatim DB search.


### What are the approaches taken?

The following steps were taken to provide suggestions:

1. Selecting the search engine:
  Elasticsearch and Solr, which are based on the Lucene search engine help provide suggestions to text data. As a part of this project, a detailed comparison of features offered by Solr and elasticsearch was done. Even though both provided tools that are necessary for our project, we chose elasticsearch

2. Indexing the Nominatim DB into elasticsearch:
  The planet-wide DB was indexed on elasticsearch. This was made possible by the server provided by OpenCage for this project. We were able to index the addresses of all the places in multiple languages.

3. Hosting the suggestions as an API end-point
  The suggestions are hosted using a hug API.

4. Fetching the suggestions
  A branch of Nominatim-UI has been created to fetch and display the suggestions. This branch has code to fetch suggestions from your suggestions endpoint and display them as a list.

### What is the end product?

The complete instructions on how to set up the project are available at [nominatim-indexing](https://github.com/krahulreddy/nominatim-indexing).

The hosted server contains the end product of this project. These links might not be accessible after September 2020.

- [Server with Nominatim-UI](https://gsoc2020.nominatim.org/nominatim/ui/search.html)
- [API with suggestions](https://gsoc2020.nominatim.org/suggest/autocomplete?q=new%20york)

As an end product, we have:

* An Application that can setup elasticsearch an index for your extract of the OSM DB. This can be configured to index any set of name tags supported by Nominatim. 

* We also have `search.py`, which can be used to host these suggestions as an API. The API endpoints and the search queries are explained in [nominatim-indexing](https://github.com/krahulreddy/nominatim-indexing).

* The front-end changes needed to use these suggestions are available at [Nominatim UI](https://github.com/osm-search/nominatim-ui/pull/32)

All the three above can be used to set up Nominatim suggestions anywhere!

#### Special features

* Tokenization allows reordering of search terms.

![Imgur](https://i.imgur.com/zAeI3mi.png)

**Image:** autocomplete endpoint provides tokenization to allow reordering of search terms.

> **Note:** This tokenization might not be preferred by all users. We have prefix_match endpoint, which performs only prefix_match search and does not allow tokenization.

* The suggestions are sorted based on a formula to provide more important places first (Nominatim Importance score from wiki data is used for this)

formula = [wiki importance or {0.75 - record['rank_search'] / 40}] * factor + elasticsearch score

![Imgur](https://i.imgur.com/YM0ms25.png)

**Image:** autocomplete endpoint does not provide important places. This is because of the modified factor.

![Imgur](https://i.imgur.com/guLn5Ch.png)

**Image:** autocomplete endpoint provides important places first, with default formula.

* The API endpoints have features to modify the type of search performed.

![Imgur](https://i.imgur.com/8n9nITS.png)

**Image:** Fuzzy query type to allow typo tolerance.

* The suggestions are provided on each keystroke and are fast. (The suggestions provided are fast enough, so we did not implement debouncing)

![Imgur](https://i.imgur.com/3lnjEkM.png)

**Image:** Waterfall of network calls.

* Indexing time for planet-wide DB is less than 20 hours.
* The elasticsearch index takes up 10-13 GB of total space for planet-wide DB.

![Imgur](https://i.imgur.com/2QlbO6i.png)

**Image:** Shows the suggestion index size.

* Browser default language support - If the suggestions fetched are not from the browser default language, we provide the address in browser default language in parenthesis.

![Imgur](https://i.imgur.com/7dayNAH.png)

**Image:** Since the user typed in Kannada, and my browser default is English, `addr:en` has been shown in parenthesis.


* The suggestions also include icons to denote the category and type of the place.

![Imgur](https://i.imgur.com/WpVuLc0.png)

* Our setup can also be used over smaller extracts of Nominatim DB.

### What did I learn?

As a part of this project, I was able to learn

* elasticsearch indexing and querying
* more about how Nominatim works
* handling the planet DB
* Working and hosting on a server
* Commenting and Documenting Python application

### What next?
The following area few open ends of the project which can be improved and enhanced:

* The UI on the server can be improved.
* There are a lot of duplicate entries in the Nominatim DB. This effects the elasticsearch index size and the suggestions contains duplicates sometimes. Deduplication was attempted as part of this project but wasn't successful.
* Since results are sorted based on the importance score, we can try to incorporate this during the indexing time to decrease the search time even further.
* A test suite can be added for this project.
* The address formation can be improved.
* language support on the fetching part can be enhanced.

## Recap of the project

This section contains a brief overview of the work done over the last 5 months (Including the proposal writing)

### Proposal

The prerequisite for applying for GSoC for OpenStreetMap was to have mapped with OpenStreetMap. For `Nominatim` projects, there was an extra `Pull Request` requirement. I started working and pushed the following code:

* [First PR](https://github.com/osm-search/Nominatim/pull/1714) for issue [#886](https://github.com/osm-search/Nominatim/issues/886).
  I had to understand how Nominatim processed queries in order to work on this issue and send a PR. This is not merged intentionally. The mentors said that this satisfied the criteria for applying for GSoC.

After this, I went on to select the topic for GSoC. I chose `Search suggestions for osm.org`, which was featured in the OpenStreetMap [Ideas Page](https://wiki.openstreetmap.org/wiki/Google_Summer_of_Code/2020/Project_ideas). This project was labeled `Hard`. I was new to Nominatim and Elasticsearch(and other alternatives). I quickly started asking questions on the Mailing list and started gathering requirements and details regarding the project.

Sarah Hoffmann and Marc Tobias helped me out in the process and I was able to come up with a good proposal!

Proposal link: [Final proposal](https://docs.google.com/document/d/1vWBA-2SCWA0mgDrKlynmzn2aVUvovjwlTb_w8wlyitQ/edit)

#### Other contributions

* [Fixed few links while reading the codebase](https://github.com/osm-search/Nominatim/pull/1760)

* [Advanced installations for Nominatim](https://github.com/osm-search/Nominatim/pull/1758) - Enables setup and updates for multiple data extracts for Nominatim.

### Community bonding

During the community bonding period, I took up an issue in Nominatim - [setup-website option](https://github.com/osm-search/Nominatim/pull/1829). This is part of the [modern PHP initiative](https://github.com/osm-search/Nominatim/milestone/2). I hope to take this work forward by taking up more issues of this milestone after GSoC.

I was also provided a server. I set up Nominatim on this server and worked towards understanding the codebase better. I was also reading about elasticsearch and Solr during this phase. This helped us in a later stage when we had to decide on which search engine was to be finalized.

### Phase 1

This phase was meant for finalizing the tech stack and implementing Proof of Concepts. After a thorough comparison([diary entry](https://www.openstreetmap.org/user/krahulreddy/diary/393360)) of elasticsearch and Solr, we decided to go ahead with elasticsearch. The PoCs([diary entry](https://www.openstreetmap.org/user/krahulreddy/diary/393458)) covered almost all the technologies to be used in the final code.


### Phase 2

Due to other updates to the Nominatim repository, we decided to upgrade the server to Ubuntu 20.04. This was done by me as part of this phase.

At the end of this Phase, we had the server up and running with very simple prefix match suggestions. These were just based on the name of the place. Not with proper addresses, but the server was accessible and contained suggestions from elasticsearch. ([diary entry](https://www.openstreetmap.org/user/krahulreddy/diary/393800))

### Phase 3

As part of this phase, the following work was done:

* Made sure the address formation is right and indexed the planet-wide Database in most used languages.
* Made sure the indexing time was < 20 hours (This was regarded well within the limit, and approved.)
* Made sure the DB size was <13 GB for 10 languages. (This was also well within the expected range and approved.)
* Made sure the final code is clean and well commented.
* Finalized the queries to provide accurate suggestions:
  * Tokenization and completion are used together to provide accurate results.
  * The results are sorted according to the importance score of places. This makes sure the suggestions are of more important places.
* Complete Documentation for setup and API usage (Available [here](https://github.com/krahulreddy/nominatim-indexing))
* Updated the API based on suggestions from Sarah and Marc.
* UI of the suggestions was improved.
* Made sure results are returned based on browser default settings as well. (This helps for a suggestion with place names only in non-default languages)

### Challenges

More than the planned amount of work was done by the end of phase 1. I did another internship along with this GSoC project. That affected my work and communication with the mentors during Phase 2 of the project. This was covered a bit by the extra work done during phase 1. But still, without this other commitment, I could have taken up a few other tasks for this project. I still intend to work on this and improve the project beyond the scope of GSoC.

## Acknowledgements

My mentors [Sarah Hoffmann](https://github.com/lonvia) and [Marc Tobias](https://github.com/mtmail) helped me throughout the process. Our weekly calls helped a lot in keeping the work flowing in the right direction. They made sure I was equipped with the right set of knowledge and tools to carry on with this project.

I would like to thank my mentors and OpenStreetMap for this opportunity of working on this project. I would also like to thank OpenCage for providing the server used during the project. Hosting a live server with my project made the project experience much better.

I would also like to thank my college [National Institute of Technology Karnataka, Surathkal](https://www.nitk.ac.in/) for letting me do this GSoC project. I was introduced to the world of Open Source and GSoC by our professor [Mohit P. Tahiliani](https://github.com/mohittahiliani).
