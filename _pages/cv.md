---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D in Electrical Engineering, Hunan University, 2022
* B.S. in Electrical Engineering and Automation, Hunan University, 2017

Work experience
======
* 2023-Present: Part-time Lecturer of EEE, NTU 
  * EE6506 Semiconductor Based Converter in Renewable Energy Systems
  * EE6514 Special Topics in Clean Energy System Design
  * EE6501 Power Electronic Converters

* 2022-Present: Research Fellow (supervised by Associate Professor Yi Tang, Cluster Director of ERI@N, Deputy Director of EEE, NTU)
  * Advanced Energy Management and Data Fusion for Smart Homes and Smart Grids (NTU-LiteON Collaboration Programme), Singapore

  
Project and Research Experience:
======
* 2021-2025：Advanced Energy Management and Data Fusion for Smart Homes and Smart Grids (NTU-LiteON Collaboration Programme), Singapore
* 2022-2024：Major Special Projects of Hunan Province (2020GK1010), China
* 2019-2021：Natural Science Foundation of China under Grant (51807057), China
* 2019-2021：Hunan Province Youth Fund Project (2019JJ50038), China
* 2018-2023：Project of Megmeet (University-Industry Collaboration Programme), China
* 2018-2020：Hunan Science and Technology Innovation Plan Project (2017XK2104), China

Publications
======
  <ul>{% for post in site.publications reversed %}
  {% if post.collection == "publications" and post.category == "manuscripts" %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Currently signed in to 43 different slack teams
