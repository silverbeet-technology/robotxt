# robotxt

<div align="center">
  <img src="img/robotxt-logo.png" alt="robotxt logo" width="200"/>
</div>

This project includes a Python script that generates a modern robots.txt file that'll help you block AI training bots, while (optionally) allowing AI crawling bots to index your your content so that it is still accessible to bots that power real-time AI search and answers. There are 3 levels of AI bot blocking included.

## Usage

* Install Python, if needed (howto: [macOS](https://docs.python.org/3/using/mac.html), [Windows](https://docs.python.org/3/using/windows.html), [Linux/Unix](https://docs.python.org/3/using/unix.html))
* Checkout code
```bash
git clone https://git.silverbeet.tech/phil/robotxt.git
```
* Run the script
```bash 
cd robotxt
python3 robotxt
```
* Answer the questions regarding the level of AI bot blocking you want implemented
  - Option 1: Allow all AI crawlers (maximum visibility)
  The simplest approach that lets every bot have full access to your content. If your goal is Generative Engine Optimization (GEO) visibility and you want to be cited everywhere, this is the starting point.
  - Option 2: Allow search-linked crawlers, block training-only crawlers
  This blocks bots that primarily collect training data while keeping your content accessible to bots that power real-time AI search and answers.
  > Note: The line between "training" and "retrieval" is blurring. GPTBot is used for both training and retrieval. Blocking GPTBot while allowing OAI-SearchBot is OpenAI's recommended split if you want to opt out of training but stay in ChatGPT search results
  - Option 3: Block all AI crawlers
    This blocks AI bots for training, and website indexing
  - Option 4: Block "all known" AI crawlers
    This blocks AI bots for training, and website indexing using a huge list of "all known" AI bots from the [ai-robots-txt/ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt) project
* Review output of new `robots.txt`
* Use the new `robots.txt` file in your environment [Where should I put my robots.txt file?](https://yoast.com/ultimate-guide-robots-txt/#where)

## Questions

- [What is robots.txt?](https://www.cloudflare.com/learning/bots/what-is-robots-txt/)
- [How does a Robots.txt file work?](https://www.cloudflare.com/learning/bots/what-is-robots-txt/#how-does-a-robotstxt-file-work)
- [How does robots.txt relate to bot management?](https://www.cloudflare.com/learning/bots/what-is-robots-txt/#how-does-robotstxt-relate-to-bot-management)

## Eratta

### License
* [MIT License](LICENSE)

### Logo
* The robot logo for this project was designed by [Magnific](https://www.magnific.com/) (src: [icon/robot_3685318](https://www.magnific.com/icon/robot_3685318))

### Other projects
Other projects I've found that are actively addressing the AI blocking issue that helped in the development of `robotxt`:

- [ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt) - an exhaustive list of AI agents and robots to block
  * they have a huge list of all known AI bots to block: [robots.txt](https://raw.githubusercontent.com/ai-robots-txt/ai.robots.txt/refs/heads/main/robots.txt) that I've included as option 4 in this project
- [Known Agents](https://knownagents.com/) - see how AI agents are crawling your site and using your tools
- [Generate Robotstxt](https://generaterobotstxt.com/) -  interactively generate a basic robots.txt file, which includes AI bot blocking options
- [The /llms.txt file](https://llmstxt.org/) - a proposed standard to use a llms.txt file to provide information to help LLMs use a website at inference time, following the ideals of the original robots.txt standard
- [Anubis](https://anubis.techaro.lol/) - an amazing open source project that, "<i>...uses a combination of heuristics to identify and block bots before they take your website down. You can customize the rules with your own policies.</i>", which gives you active and automated control over which bots can access your site and content
  * NOTE: I'm reviewing the [Traefik configuration for Anubis](https://anubis.techaro.lol/docs/admin/environments/traefik) to use on some of my sites

### Thanks
