[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<br>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->



### Built With
* [Fastapi](https://fastapi.tiangolo.com/)
* [Python](https://www.python.org/)


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.


### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python
  
  macOS
  ```sh
  brew install python@3.7
  ```
  for other systems check [python.org](https://www.python.org/downloads/)

* pip
  
  linux/macOS
  ```sh
  python -m pip --version
  ```

  windows
  ```sh
  py -m pip --version
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/dan-candeira/api_backend.git
   ```
2. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the main folder
   
4. Add a SECRET_KEY to the `.env` file:
   ```env
   SECRET_KEY = 'ENTER YOUR SECRET_KEY'
   ```
   
   examples of SECRET KEY at [randomkeygen](https://randomkeygen.com/)

5. Run command:
   ```sh
   uvicorn main:app --reload
   ```


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



Project Link: [https://github.com/dan-candeira/api_backend](https://github.com/dan-candeira/api_backend)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Dr. Fábio Henrique M. Oliveira](https://sites.google.com/view/oliveirafhm/home)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/dan-candeira/api_backend.svg?style=for-the-badge
[contributors-url]: https://github.com/dan-candeira/api_backend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dan-candeira/api_backend.svg?style=for-the-badge
[forks-url]: https://github.com/dan-candeira/api_backend/network/members
[stars-shield]: https://img.shields.io/github/stars/dan-candeira/api_backend.svg?style=for-the-badge
[stars-url]: https://github.com/dan-candeira/api_backend/stargazers
[issues-shield]: https://img.shields.io/github/issues/dan-candeira/api_backend.svg?style=for-the-badge
[issues-url]: https://github.com/dan-candeira/api_backend/issues
[license-shield]: https://img.shields.io/github/license/dan-candeira/api_backend.svg?style=for-the-badge
[license-url]: https://github.com/dan-candeira/api_backend/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: www.linkedin.com/in/daannybc