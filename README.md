# robotxt

<div align="center">
  <img src="img/robotxt-logo.png" alt="robotxt logo" width="200"/>
</div>

This project includes a Python script that generates a modern robots.txt file that'll help you block AI training bots, while (optionally) allowing AI crawling bots to index your website or content.

## Usage

* Install Python, if needed 
  - [macOS](https://docs.python.org/3/using/mac.html)
  - [Windows](https://docs.python.org/3/using/windows.html)
  - [Linux/Unix](https://docs.python.org/3/using/unix.html)
* Checkout code
* Run the script
* Answer questions
  - Option 1: Allow all AI crawlers (maximum visibility)
    This is the simplest approach. Every bot gets full access. If your goal is Generative Engine Optimization (GEO) visibility and you want to be cited everywhere, this is the starting point.
  
  - Option 2: Allow search-linked crawlers, block training-only crawlers
    This blocks bots that primarily collect training data while keeping your content accessible to bots that power real-time AI search and answers.
    Note: The line between "training" and "retrieval" is blurring. GPTBot is used for both training and retrieval. Blocking GPTBot while allowing OAI-SearchBot is OpenAI's recommended split if you want to opt out of training but stay in ChatGPT search results.
  
  - Option 3: Block all AI crawlers
    This blocks AI bots while keeping traditional search crawlers (Googlebot, Bingbot) allowed under the wildcard rule.
* Review output of new `robots.txt`
* Use the new `robots.txt` file in your environment

## Questions

- What is a robots.txt file, why would I want to use one on my site, and how do I use it? I would be repeating myself, so instead I'll link to the [moz.com robots.txt post](https://moz.com/learn/seo/robotstxt)

## Eratta

* Robot logo Designed by [Magnific](https://www.magnific.com/) (src: [icon/robot_3685318](https://www.magnific.com/icon/robot_3685318))
  
## More

More options that are actively addressing this issue

- [ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt)
  * including a huge list of all known AI bots to block: [robots.txt](https://raw.githubusercontent.com/ai-robots-txt/ai.robots.txt/refs/heads/main/robots.txt)
- [Known Agents](https://knownagents.com/)
